/**
 * Solo Builder Starter Kit Setup Script
 * CLI tự động hóa thiết lập cấu trúc Solo Builder cho bất kỳ dự án mới nào.
 * Không cần bất kỳ dependency bên ngoài nào (Zero-dependency).
 */

const fs = require('fs');
const path = require('path');
const readline = require('readline');

// ANSI Colors để trang trí Terminal chuyên nghiệp
const C = {
  reset: "\x1b[0m",
  bold: "\x1b[1m",
  green: "\x1b[32m",
  yellow: "\x1b[33m",
  blue: "\x1b[34m",
  magenta: "\x1b[35m",
  cyan: "\x1b[36m",
  red: "\x1b[31m",
  gray: "\x1b[90m"
};

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// Tiêu đề trang trí
console.log(`\n${C.bold}${C.cyan}===================================================`);
console.log(` 🛠️  SOLO BUILDER STARTER KIT - SETUP WIZARD 🛠️`);
console.log(`===================================================${C.reset}\n`);

// Thư mục chứa template nguồn (thư mục chứa script này)
const sourceDir = path.join(__dirname, 'templates');
// Thư mục đích (thường là Root của dự án mới - nơi người dùng thực thi command)
const destDir = process.cwd();

// Kiểm tra thư mục templates nguồn
if (!fs.existsSync(sourceDir)) {
  console.log(`${C.bold}${C.red}❌ Lỗi: Không tìm thấy thư mục templates nguồn tại: ${sourceDir}${C.reset}`);
  console.log(`Đảm bảo bạn đã sao chép đầy đủ thư mục solo-builder-kit cùng với thư mục 'templates' của nó.\n`);
  process.exit(1);
}

// Hàm hỏi người dùng dạng Promise
function askQuestion(query) {
  return new Promise(resolve => rl.question(query, resolve));
}

// Hàm đệ quy copy thư mục và thay thế biến
function copyFolderRecursiveSync(source, target, projectName, techStack) {
  let files = [];

  // Tạo thư mục đích nếu chưa có
  if (!fs.existsSync(target)) {
    fs.mkdirSync(target, { recursive: true });
  }

  // Đọc danh sách file/thư mục con
  if (fs.lstatSync(source).isDirectory()) {
    files = fs.readdirSync(source);
    files.forEach(function (file) {
      const curSource = path.join(source, file);
      const curTarget = path.join(target, file);

      if (fs.lstatSync(curSource).isDirectory()) {
        copyFolderRecursiveSync(curSource, curTarget, projectName, techStack);
      } else {
        copyAndInterpolateFileSync(curSource, curTarget, projectName, techStack);
      }
    });
  }
}

// Hàm copy từng file và điền template variables
function copyAndInterpolateFileSync(sourceFile, destFile, projectName, techStack) {
  try {
    let content = fs.readFileSync(sourceFile, 'utf8');

    // Thay thế các biến {{PROJECT_NAME}} và {{TECH_STACK}}
    content = content.replace(/\{\{PROJECT_NAME\}\}/g, projectName);
    content = content.replace(/\{\{TECH_STACK\}\}/g, techStack);

    // Ghi đè hoặc tạo file mới ở thư mục đích
    fs.writeFileSync(destFile, content, 'utf8');
    
    // Hiển thị tiến trình dạng tối giản, đẹp mắt
    const relativePath = path.relative(destDir, destFile);
    console.log(`  ${C.green}✔ Created:${C.reset} ${relativePath}`);
  } catch (error) {
    console.log(`  ${C.red}❌ Error writing file ${destFile}: ${error.message}${C.reset}`);
  }
}

async function run() {
  // Lấy tên thư mục hiện tại làm mặc định cho tên dự án
  const defaultProjectName = path.basename(destDir);
  
  console.log(`${C.bold}📁 Thư mục cài đặt hiện tại:${C.reset} ${C.gray}${destDir}${C.reset}\n`);

  // Bước 1: Hỏi Tên dự án
  const projectNameInput = await askQuestion(`${C.bold}1. Nhập tên dự án${C.reset} (Mặc định: ${C.yellow}${defaultProjectName}${C.reset}): `);
  const projectName = projectNameInput.trim() || defaultProjectName;

  // Bước 2: Hỏi Tech Stack của dự án
  console.log(`\n${C.bold}2. Định nghĩa Tech Stack cho dự án (Để hướng dẫn AI Agent)${C.reset}`);
  console.log(`   Nhập các công nghệ chính (ví dụ: React + Tailwind CSS hoặc Express + MongoDB).`);
  console.log(`   (Mỗi công nghệ cách nhau bằng dấu xuống dòng hoặc dùng ký hiệu đầu dòng '-')`);
  console.log(`   (Bấm Enter 2 lần hoặc gõ 'done' để hoàn thành nhập liệu)\n`);

  let techStackLines = [];
  let lineNum = 1;
  while (true) {
    const line = await askQuestion(`   - Tech ${lineNum}: `);
    if (line.trim().toLowerCase() === 'done' || line.trim() === '') {
      break;
    }
    techStackLines.push(`- ${line.trim()}`);
    lineNum++;
  }

  // Nếu không nhập gì, gán mặc định cho tech stack
  if (techStackLines.length === 0) {
    techStackLines = [
      "- Node.js / JavaScript / TypeScript",
      "- Frontend/Backend Framework bất kỳ",
      "- CSS / Styling tự chọn"
    ];
  }
  const techStack = techStackLines.join('\n');

  console.log(`\n${C.cyan}---------------------------------------------------${C.reset}`);
  console.log(`${C.bold}🚀 Bắt đầu cài đặt Solo Builder Starter Kit...${C.reset}\n`);

  // Thực thi copy và thiết lập
  copyFolderRecursiveSync(sourceDir, destDir, projectName, techStack);

  // Tạo các thư mục trống cần thiết nếu chưa có (như plans)
  const plansDir = path.join(destDir, 'docs', 'plans');
  if (!fs.existsSync(plansDir)) {
    fs.mkdirSync(plansDir, { recursive: true });
  }

  // Kết quả thành công mỹ mãn
  console.log(`\n${C.bold}${C.green}===================================================`);
  console.log(` 🎉 CÀI ĐẶT THÀNH CÔNG SOLO BUILDER STARTER KIT! 🎉`);
  console.log(`===================================================${C.reset}`);
  console.log(`\n${C.bold}Các bước tiếp theo của bạn:${C.reset}`);
  console.log(` 1. Hãy cấu hình tóm tắt yêu cầu dự án trong file:  ${C.bold}${C.yellow}docs/brief.md${C.reset}`);
  console.log(` 2. Định nghĩa chi tiết yêu cầu nghiệp vụ tại:      ${C.bold}${C.yellow}docs/BRD.md${C.reset}`);
  console.log(` 3. Cập nhật roadmap phát triển theo phase trong:    ${C.bold}${C.yellow}docs/plans/master-plan.md${C.reset}`);
  console.log(` 4. Bắt đầu làm việc với AI Agent (Antigravity)!`);
  console.log(`    Agent sẽ tự động đọc ${C.bold}AGENTS.md${C.reset} và thực thi quy trình cực kỳ kỷ luật.\n`);
  
  rl.close();
}

run().catch(err => {
  console.error(`${C.red}Lỗi bất ngờ xảy ra: ${err.message}${C.reset}`);
  rl.close();
});
