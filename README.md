# SME Invoice Processing Workshop

**คอร์สสอนสร้างระบบประมวลผล Invoice ด้วย Hermes Agent**

## 📋 ภาพรวม

คอร์สนี้สอนให้ SME สร้างระบบประมวลผล invoice แบบอัตโนมัติ โดยใช้ Hermes Agent ทั้งหมด ไม่ต้องเขียนโค้ดเอง

## 🎯 สิ่งที่จะได้เรียนรู้

### Part 1: /goal + Kanban (1 ชั่วโมง)
- ทบทวน `/goal` vs Kanban
- เปรียบเทียบ Hermes `/goal` vs OpenAI `/goal`
- ตัวอย่าง: สร้างเว็บง่ายๆ ด้วย Kanban
- Lab: ใช้ Kanban สร้าง landing page

### Part 2: Invoice Processing Web App (1 ชั่วโมง)
- สร้าง web app อ่าน invoice
- ใช้กล้องโทรศัพท์ถ่ายรูป invoice
- AI อ่านและสรุปข้อมูล
- บันทึกข้อมูล + สรุปยอดตามประเภท
- Lab: สร้างระบบบันทึก invoice ของตัวเอง

## 📁 โครงสร้างไฟล์

```
sme-invoice-processing-demo/
├── README.md                          # ไฟล์นี้
├── invoices/                          # ตัวอย่าง invoice
│   ├── invoice_001_en.pdf            # IT Services (EN)
│   ├── invoice_002_th.pdf            # Office Supplies (TH, มี VAT)
│   ├── invoice_003_consulting.pdf    # Consulting Services
│   ├── invoice_004_restaurant.pdf    # Restaurant Supplies
│   ├── invoice_005_marketing.pdf     # Marketing Services
│   ├── invoice_006_receipt.pdf       # ใบเสร็จรับเงิน
│   └── invoice_007_tax_invoice.pdf   # ใบกำกับภาษี
├── scripts/
│   └── create_sample_invoices.py     # Script สร้าง invoice
├── assets/                            # รูปภาพ, โลโก้
└── templates/                         # Template สำหรับ web app
```

## 🚀 การเตรียมตัว

### สิ่งที่ต้องมี
1. **Hermes Agent** ติดตั้งในเครื่อง
2. **Python 3.8+** (สำหรับรัน script สร้าง invoice)
3. **โทรศัพท์มือถือ** (สำหรับถ่ายรูป invoice ใน Part 2)

### ติดตั้ง dependencies
```bash
pip install fpdf2 pillow
```

## 📚 ตัวอย่าง Invoice ที่มี

### 1. invoice_001_en.pdf - IT Services
- ภาษาอังกฤษ
- บริการ IT (Web Design, App Development)
- ไม่มี VAT

### 2. invoice_002_th.pdf - Office Supplies
- ภาษาไทย
- อุปกรณ์สำนักงาน
- มี VAT 7%

### 3. invoice_003_consulting.pdf - Consulting
- ภาษาอังกฤษ
- บริการที่ปรึกษา
- มี VAT 7%

### 4. invoice_004_restaurant.pdf - Restaurant
- ภาษาไทย
- วัตถุดิบร้านอาหาร
- มี VAT 7%

### 5. invoice_005_marketing.pdf - Marketing
- ภาษาอังกฤษ
- บริการการตลาด
- มี VAT 7%

### 6. invoice_006_receipt.pdf - Receipt
- ใบเสร็จรับเงิน
- ภาษาไทย/อังกฤษ
- ไม่มี VAT

### 7. invoice_007_tax_invoice.pdf - Tax Invoice
- ใบกำกับภาษี
- ภาษาไทย/อังกฤษ
- มี VAT 7%

## 🎓 แผนการสอน

### Part 1: /goal + Kanban (60 นาที)

#### 0-10 นาที: ทบทวน /goal
- `/goal` คืออะไร
- ใช้เมื่อไหร่
- ตัวอย่างการใช้งาน

#### 10-20 นาที: เปรียบเทียบ Hermes vs OpenAI
- Hermes `/goal`: ทำงานต่อเนื่อง, มี Kanban, Cron
- OpenAI `/goal`: ทำครั้งเดียว, ไม่มี orchestration
- ข้อดี/ข้อเสียของแต่ละแบบ

#### 20-35 นาที: Kanban Multi-Profile
- สร้าง profiles: researcher, writer, reviewer
- สร้าง tasks พร้อม dependencies
- Dispatch และ monitor

#### 35-50 นาที: Lab - สร้าง Landing Page
```bash
# สร้าง profiles
hermes profile create researcher
hermes profile create writer
hermes profile create reviewer

# สร้าง tasks
hermes kanban create "Research competitors" --assignee researcher
hermes kanban create "Write landing page" --assignee writer --parent T1
hermes kanban create "Review and polish" --assignee reviewer --parent T2

# เริ่มทำงาน
hermes kanban dispatch
```

#### 50-60 นาที: สรุป Part 1
- สิ่งที่เรียนรู้
- คำถาม-คำตอบ

---

### Part 2: Invoice Processing Web App (60 นาที)

#### 0-10 นาที: แนะนำโปรเจกต์
- เป้าหมาย: สร้าง web app อ่าน invoice
- ใช้กล้องโทรศัพท์ถ่ายรูป
- AI อ่านและสรุปข้อมูล
- บันทึกข้อมูล + สรุปยอด

#### 10-25 นาที: สร้าง Web App ด้วย /goal
```bash
/goal สร้าง web app สำหรับประมวลผล invoice
- ใช้ Flask หรือ FastAPI
- มีหน้า upload รูป invoice
- ใช้ AI อ่านข้อมูลจาก invoice (OCR)
- แสดงผลลัพธ์: เลขที่ invoice, วันที่, ยอดเงิน, ประเภท
- บันทึกข้อมูลลง SQLite
- มีหน้า dashboard แสดงสรุปยอดตามประเภท
- รองรับ mobile (responsive design)
```

#### 25-40 นาที: ทดสอบกับตัวอย่าง invoice
- อัพโหลด invoice_001.pdf - invoice_007.pdf
- ตรวจสอบว่า AI อ่านข้อมูลถูกต้อง
- แก้ไขถ้ามีข้อผิดพลาด

#### 40-50 นาที: เพิ่มฟีเจอร์กล้องถ่ายรูป
- ใช้ HTML5 Camera API
- ถ่ายรูป invoice จากโทรศัพท์
- อัพโหลดและประมวลผลทันที
- แสดงผลลัพธ์แบบ real-time

#### 50-55 นาที: Lab - ปรับแต่งระบบ
```bash
/goal ปรับแต่งระบบประมวลผล invoice
- เพิ่มการแยกประเภทอัตโนมัติ (อาหาร, อุปกรณ์, บริการ)
- สร้างรายงานสรุปประจำเดือน
- Export เป็น Excel
- ส่งแจ้งเตือนทาง LINE เมื่อมียอดเกินกำหนด
```

#### 55-60 นาที: สรุป Part 2
- สิ่งที่เรียนรู้
- คำถาม-คำตอบ
- แนวทางพัฒนาต่อ

## 💡 เทคนิคการสอน

### ใช้ Hermes ล้วนๆ
- ไม่ต้องสอนเขียนโค้ด
- ใช้ `/goal` สั่งงาน
- ใช้ Kanban orchestrate
- ใช้ Cron สำหรับ automation

### ตัวอย่างจริง
- ใช้ invoice จริง 7 แบบ
- ทดสอบกับข้อมูลหลากหลาย
- แก้ปัญหาจริงที่เจอ

### Mobile-First
- ทดสอบบนโทรศัพท์
- ใช้กล้องถ่ายรูป
- Responsive design

## 🔧 Commands ที่ใช้บ่อย

### /goal
```bash
/goal สร้าง web app อ่าน invoice
/goal status
/goal pause
/goal resume
```

### Kanban
```bash
hermes kanban create "task name" --assignee profile
hermes kanban list
hermes kanban dispatch
hermes kanban reclaim <task_id>
```

### Cron
```bash
cronjob create --schedule "0 9 * * 1" --prompt "สรุปยอด invoice สัปดาห์นี้"
cronjob list
cronjob run <job_id>
```

## 📞 ติดต่อ

- **LINE:** @hermes-support
- **Docs:** hermes-agent.nousresearch.com/docs

---

**อัพเดทล่าสุด:** 2026-09-17
