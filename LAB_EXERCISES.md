# Lab Exercises - SME Invoice Processing Workshop

## Part 1: /goal + Kanban

### Lab 1.1: ทบทวน /goal

**วัตถุประสงค์:** เข้าใจการใช้งาน `/goal` พื้นฐาน

**ขั้นตอน:**
1. เปิด Hermes terminal
2. ตั้ง `/goal` สร้างรายงานยอดขายจากไฟล์ CSV

```bash
/goal อ่านไฟล์ sales.csv ในโฟลเดอร์ปัจจุบัน 
สร้างไฟล์ Excel สรุปยอดขายแยกตามเดือน 
พร้อมกราฟแท่งแสดงแนวโน้ม
บันทึกเป็น sales_report.xlsx
```

3. ดูสถานะ:
```bash
/goal status
```

4. ตรวจสอบผลลัพธ์: เปิดไฟล์ `sales_report.xlsx`

**คำถาม:**
- `/goal` ทำอะไรบ้าง?
- ใช้เวลานานเท่าไหร่?
- ผลลัพธ์ถูกต้องไหม?

---

### Lab 1.2: เปรียบเทียบ Hermes vs OpenAI

**วัตถุประสงค์:** เข้าใจความแตกต่างระหว่าง Hermes `/goal` และ OpenAI `/goal`

**ขั้นตอน:**

#### ทดสอบ Hermes `/goal`
```bash
/goal สร้าง landing page สำหรับร้านอาหาร
- มีเมนูอาหาร
- มีรูปภาพ
- มีที่อยู่และเบอร์โทร
- รองรับ mobile
```

สังเกต:
- Hermes ทำงานต่อเนื่องจนเสร็จ
- มี Kanban dashboard ให้ดู
- สามารถ pause/resume ได้

#### เปรียบเทียบ OpenAI `/goal`
(ถ้ามี OpenAI API)
```bash
# OpenAI ChatGPT
Create a landing page for a restaurant
```

สังเกต:
- OpenAI ทำครั้งเดียวแล้วจบ
- ไม่มี orchestration
- ต้องสั่งเองทุก step

**คำถาม:**
- อะไรคือข้อดีของ Hermes `/goal`?
- อะไรคือข้อดีของ OpenAI `/goal`?
- เมื่อไหร่ควรใช้แบบไหน?

---

### Lab 1.3: Kanban Multi-Profile

**วัตถุประสงค์:** ใช้ Kanban กับหลาย profiles

**ขั้นตอน:**

1. สร้าง profiles
```bash
hermes profile create researcher
hermes profile create writer
hermes profile create reviewer
```

2. สร้าง board
```bash
hermes kanban boards create content-pipeline
hermes kanban boards switch content-pipeline
```

3. สร้าง tasks
```bash
T1=$(hermes kanban create "Research restaurant trends" \
     --assignee researcher --print-id)

T2=$(hermes kanban create "Write blog post about trends" \
     --assignee writer --parent $T1 --print-id)

T3=$(hermes kanban create "Review and edit blog post" \
     --assignee reviewer --parent $T2 --print-id)
```

4. เริ่มทำงาน
```bash
hermes kanban dispatch
```

5. ดูความคืบหน้า
```bash
hermes kanban list
```

เปิด browser: http://localhost:9119/kanban

**คำถาม:**
- แต่ละ profile ทำอะไร?
- Tasks ทำงานต่อยังไง?
- ใช้เวลานานเท่าไหร่?

---

### Lab 1.4: สร้าง Landing Page ด้วย Kanban

**วัตถุประสงค์:** ใช้ Kanban สร้าง landing page จริง

**ขั้นตอน:**

1. สร้าง profiles
```bash
hermes profile create designer
hermes profile create developer
hermes profile create tester
```

2. สร้าง tasks
```bash
T1=$(hermes kanban create "Design landing page mockup" \
     --assignee designer --print-id)

T2=$(hermes kanban create "Develop HTML/CSS from mockup" \
     --assignee developer --parent $T1 --print-id)

T3=$(hermes kanban create "Test responsive design" \
     --assignee tester --parent $T2 --print-id)
```

3. เริ่มทำงาน
```bash
hermes kanban dispatch
```

4. ตรวจสอบผลลัพธ์
- เปิดไฟล์ HTML ที่สร้าง
- ทดสอบบนมือถือ

**คำถาม:**
- Landing page สวยไหม?
- รองรับ mobile ไหม?
- Kanban ช่วยอะไรบ้าง?

---

## Part 2: Invoice Processing Web App

### Lab 2.1: สร้าง Web App พื้นฐาน

**วัตถุประสงค์:** สร้าง web app อ่าน invoice ด้วย `/goal`

**ขั้นตอน:**

1. ตั้ง `/goal`
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

2. รอให้ทำงานเสร็จ (อาจใช้เวลา 10-15 นาที)

3. รัน web app
```bash
cd invoice-app
python app.py
```

4. เปิด browser: http://localhost:5000

**คำถาม:**
- Web app ทำงานไหม?
- Upload invoice ได้ไหม?
- AI อ่านข้อมูลถูกต้องไหม?

---

### Lab 2.2: ทดสอบกับตัวอย่าง Invoice

**วัตถุประสงค์:** ทดสอบ web app กับ invoice จริง

**ขั้นตอน:**

1. อัพโหลด invoice_001.pdf
- ตรวจสอบผลลัพธ์
- เลขที่ invoice ถูกต้องไหม?
- วันที่ถูกต้องไหม?
- ยอดเงินถูกต้องไหม?

2. อัพโหลด invoice_002.pdf (ภาษาไทย)
- ตรวจสอบผลลัพธ์
- AI อ่านภาษาไทยได้ไหม?

3. อัพโหลด invoice_006.pdf (receipt)
- ตรวจสอบผลลัพธ์
- แยกประเภทถูกต้องไหม?

4. อัพโหลด invoice_007.pdf (tax invoice)
- ตรวจสอบผลลัพธ์
- คำนวณ VAT ถูกต้องไหม?

**คำถาม:**
- Invoice ไหนอ่านยากที่สุด?
- AI ทำผิดพลาดตรงไหน?
- จะปรับปรุงยังไง?

---

### Lab 2.3: ใช้กล้องโทรศัพท์

**วัตถุประสงค์:** ถ่ายรูป invoice จากโทรศัพท์

**ขั้นตอน:**

1. เปิด web app บนโทรศัพท์
- เข้า http://YOUR_IP:5000
- (ต้องเปิด port firewall)

2. ถ่ายรูป invoice
- กดปุ่ม "Upload from Camera"
- ถ่ายรูป invoice_001.pdf
- อัพโหลด

3. ตรวจสอบผลลัพธ์
- AI อ่านข้อมูลจากภาพถ่ายได้ไหม?
- ภาพชัดพอไหม?

**คำถาม:**
- ภาพจากกล้องอ่านได้ไหม?
- ต้องปรับปรุงอะไรบ้าง?
- แสงสว่างมีผลไหม?

---

### Lab 2.4: เพิ่มฟีเจอร์ด้วย /goal

**วัตถุประสงค์:** ปรับแต่งระบบด้วย `/goal`

**ขั้นตอน:**

1. ตั้ง `/goal` เพิ่มฟีเจอร์
```bash
/goal ปรับแต่งระบบประมวลผล invoice
- เพิ่มการแยกประเภทอัตโนมัติ (อาหาร, อุปกรณ์, บริการ)
- สร้างรายงานสรุปประจำเดือน
- Export เป็น Excel
- ส่งแจ้งเตือนทาง LINE เมื่อมียอดเกินกำหนด
```

2. ทดสอบฟีเจอร์ใหม่
- แยกประเภทอัตโนมัติทำงานไหม?
- รายงานสรุปถูกต้องไหม?
- Export Excel ได้ไหม?

**คำถาม:**
- ฟีเจอร์ไหนมีประโยชน์ที่สุด?
- จะเพิ่มฟีเจอร์อะไรอีก?

---

### Lab 2.5: Automation ด้วย Cron

**วัตถุประสงค์:** ตั้งเวลาประมวลผล invoice อัตโนมัติ

**ขั้นตอน:**

1. ตั้ง cronjob
```bash
cronjob create \
  --schedule "0 9 * * 1" \
  --prompt "สรุปยอด invoice สัปดาห์นี้ 
           แบ่งตามประเภท 
           ส่งรายงานทาง LINE" \
  --name "Weekly Invoice Summary"
```

2. ทดสอบทันที
```bash
cronjob run <job_id>
```

3. ตรวจสอบผลลัพธ์
- รายงานสรุปถูกต้องไหม?
- ส่ง LINE ได้ไหม?

**คำถาม:**
- Cron ช่วยอะไรบ้าง?
- จะตั้ง schedule ยังไง?

---

## 🎯 เกณฑ์การประเมิน

### Part 1: /goal + Kanban
- [ ] ใช้ `/goal` สร้างรายงานได้
- [ ] ใช้ Kanban สร้าง landing page ได้
- [ ] เข้าใจความแตกต่าง Hermes vs OpenAI

### Part 2: Invoice Processing
- [ ] สร้าง web app ได้
- [ ] อ่าน invoice จากไฟล์ได้
- [ ] อ่าน invoice จากภาพถ่ายได้
- [ ] สรุปยอดตามประเภทได้
- [ ] ใช้ Cron automation ได้

---

## 📞 ต้องการความช่วยเหลือ?

- ถามใน Discord
- เปิด Issue ใน GitHub
- ติดต่อทีมงาน

**ขอให้สนุกกับการเรียนรู้!** 🌸
