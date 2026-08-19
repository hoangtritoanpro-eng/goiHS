import pandas as pd
import glob
import os
import re
import requests
import time
import math

def clean_phone(p):
    if pd.isna(p) or str(p).strip() == '':
        return ""
    p = str(p).strip()
    # Remove everything except digits
    p = re.sub(r'\D', '', p)
    if not p:
        return ""
    # If the number in excel lost its leading 0 (e.g. 905123456)
    if len(p) >= 9 and not p.startswith('0'):
        p = '0' + p
    return p

files = glob.glob('c:/Users/hoang/Downloads/TOAN/goiHS/danh_sach_hoc_sinh_*.xls*')
primary_files = []
for f in files:
    m = re.search(r'hoc_sinh_([1-5])_', f)
    if m:
        primary_files.append(f)

print(f"Found {len(primary_files)} primary school files.")

all_students = {}
now = int(time.time() * 1000)
count = 0

for f in primary_files:
    print(f"Processing {os.path.basename(f)}...")
    # Find header row
    df_raw = pd.read_excel(f, header=None, dtype=str)
    header_row = -1
    for i in range(min(20, len(df_raw))):
        row_vals = [str(x).lower() for x in df_raw.iloc[i].values]
        if any('họ và tên' in v or 'họ tên' in v or 'tên học sinh' in v for v in row_vals):
            header_row = i
            break
            
    if header_row == -1:
        print(f"  -> Could not find header row in {os.path.basename(f)}. Skipping.")
        continue
        
    df = pd.read_excel(f, header=header_row, dtype=str)
    
    name_col = None
    phone_col = None
    class_col = None
    
    for c in df.columns:
        c_lower = str(c).lower()
        if 'họ và tên' in c_lower or 'họ tên' in c_lower or 'tên học sinh' in c_lower:
            name_col = c
        if 'điện thoại' in c_lower or 'sđt' in c_lower or 'sdt' in c_lower or 'phone' in c_lower or 'phụ huynh' in c_lower:
            phone_col = c
        if 'lớp' in c_lower or 'class' in c_lower:
            class_col = c

    # Extract class from filename or first few rows if missing
    default_class = ""
    for i in range(min(20, len(df_raw))):
        row_vals = [str(x).lower() for x in df_raw.iloc[i].values]
        for v in row_vals:
            if v.startswith('lớp:'):
                default_class = v.split('-')[0].replace('lớp:', '').replace('cs5', '').replace('_', '').replace('CS5', '').strip()
                break
        if default_class: break
        
    if not default_class:
        # try to get from filename like 1_3int
        m = re.search(r'hoc_sinh_(.*?)_cs5', os.path.basename(f))
        if m:
            default_class = m.group(1).replace('_', '/').upper()

    print(f"  -> Class: {default_class}, Name Col: {name_col}, Phone Col: {phone_col}")
    
    for idx, row in df.iterrows():
        if pd.isna(row[name_col]) or str(row[name_col]).strip() == '' or 'tổng số' in str(row[name_col]).lower():
            continue
            
        name = str(row[name_col]).strip()
        cls = default_class
        if class_col and not pd.isna(row[class_col]) and str(row[class_col]).strip():
            cls = str(row[class_col]).strip().replace('cs5', '').replace('_', '').replace('CS5', '').strip()
            
        phone = ""
        if phone_col:
            phone = clean_phone(row[phone_col])
            
        student_id = f"hs_{now}_{count}"
        count += 1
        
        student_data = {
            "name": name,
            "className": cls,
            "status": "waiting"
        }
        if phone:
            student_data["parentEmail"] = phone
            
        all_students[student_id] = student_data

print(f"\nTotal students parsed: {len(all_students)}")

firebase_url = "https://goihs-e3b26-default-rtdb.asia-southeast1.firebasedatabase.app/students.json"

print(f"Uploading {len(all_students)} students to Firebase...")
# We use PATCH to only add/update these students without deleting existing ones
response = requests.patch(firebase_url, json=all_students)
if response.status_code == 200:
    print("Successfully uploaded!")
else:
    print(f"Failed: {response.status_code} - {response.text}")

