import pandas as pd
import glob
import os
import re

files = glob.glob('c:/Users/hoang/Downloads/TOAN/goiHS/danh_sach_hoc_sinh_*.xls*')
primary_files = []
for f in files:
    m = re.search(r'hoc_sinh_([1-5])_', f)
    if m:
        primary_files.append(f)

with open('inspect_output3.txt', 'w', encoding='utf-8') as out:
    df = pd.read_excel(primary_files[0], header=None, dtype=str)
    out.write(df.head(20).to_string())
