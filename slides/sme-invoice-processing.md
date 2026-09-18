---
marp: true
theme: default
paginate: true
header: "SME Invoice Processing Workshop 📄"
footer: "สร้างระบบประมวลผล Invoice ด้วย Hermes Agent"
style: |
  section {
    font-family: 'Sarabun', 'Noto Sans Thai', sans-serif;
    font-size: 18px;
    line-height: 1.4;
    padding: 30px 40px;
    background: linear-gradient(135deg, #e0f7fa 0%, #f3e5f5 100%);
    color: #2d2d2d;
    overflow: hidden;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
  section.lead {
    justify-content: center;
    align-items: center;
    text-align: center;
  }
  header { color: #00897b; font-size: 14px; }
  footer { color: #999; font-size: 12px; }
  h1 { 
    color: #00897b; 
    text-align: center;
    text-shadow: 2px 2px 4px rgba(0,137,123,0.2);
    font-size: 32px;
    margin: 0 0 15px 0;
  }
  h2 { 
    color: #7b1fa2; 
    font-size: 22px;
    margin: 8px 0;
  }
  h3 { 
    color: #1976d2; 
    font-size: 18px;
    margin: 6px 0;
  }
  p, ul, ol {
    margin: 6px 0;
  }
  ul, ol {
    padding-left: 25px;
  }
  li {
    margin: 3px 0;
  }
  code { 
    background: #e0f2f1; 
    color: #00695c; 
    padding: 2px 6px;
    border-radius: 4px;
    font-size: 14px;
    word-break: break-all;
  }
  pre {
    background: #263238;
    color: #eceff1;
    border-radius: 10px;
    padding: 10px;
    margin: 8px 0;
    overflow-x: auto;
    font-size: 13px;
    line-height: 1.3;
  }
  pre code {
    background: transparent;
    color: #eceff1;
    word-break: normal;
    white-space: pre;
  }
  .kawaii-box {
    background: white;
    border: 2px solid #80cbc4;
    border-radius: 15px;
    padding: 12px;
    margin: 8px 0;
    box-shadow: 0 2px 8px rgba(128,203,196,0.2);
    max-width: 100%;
    overflow: hidden;
  }
  .emoji-big { font-size: 36px; text-align: center; }
  table { 
    margin: 8px auto;
    border-collapse: collapse;
    font-size: 15px;
    max-width: 100%;
  }
  th { 
    background: #80cbc4; 
    color: white; 
    padding: 6px 10px;
  }
  td { 
    background: white; 
    padding: 5px 10px;
  }
  blockquote {
    border-left: 4px solid #80cbc4;
    background: #e0f2f1;
    padding: 8px 12px;
    border-radius: 0 10px 10px 0;
    margin: 8px 0;
    font-size: 15px;
  }
  img {
    max-height: 200px;
    max-width: 80%;
    display: block;
    margin: 8px auto;
    border-radius: 15px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  }
  section.lead img {
    max-height: 180px;
    margin: 15px auto;
  }
  .two-col {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 15px;
    align-items: start;
  }
  .two-col .kawaii-box {
    margin: 0;
  }
---

<!-- _class: lead -->

# 📄✨ SME Invoice Processing Workshop

## สร้างระบบประมวลผล Invoice ด้วย Hermes Agent

### ไม่ต้องเขียนโค้ด — ใช้ AI ล้วนๆ

🌸 ถ่ายรูป invoice → AI อ่าน → สรุปอัตโนมัติ 🌸

---

# 🎯 วันนี้จะเรียนอะไร?

<div class="kawaii-box">

| Part | หัวข้อ | ทำอะไรได้ |
|------|--------|-----------|
| **Part 1** | /goal + Kanban | สร้างเว็บง่ายๆ ด้วย AI หลายตัว |
| **Part 2** | Invoice Processing | สร้างระบบอ่าน invoice จากกล้อง |

</div>

<div class="kawaii-box">

## สิ่งที่ต้องเตรียม
- ✅ Hermes Agent ติดตั้งแล้ว
- ✅ โทรศัพท์มือถือ (สำหรับถ่ายรูป invoice)
- ✅ ตัวอย่าง invoice 7 แบบ (มีให้แล้ว)

</div>

> 💡 **ไม่ต้องเขียนโค้ดแม้แต่บรรทัดเดียว!**

---

# 📊 ปัญหาของ SME

<div class="kawaii-box">

## ❌ แบบเดิม (ทำเอง)
- รับ invoice เป็นกระดาษ → บันทึกเองใน Excel
- คำนวณยอดรวมเอง → ผิดบ่อย
- สรุปยอดรายเดือน → ใช้เวลา 2-3 ชั่วโมง
- หา invoice เก่า → ยากมาก

</div>

<div class="kawaii-box">

## ✅ แบบใหม่ (ให้ AI ทำ)
- ถ่ายรูป invoice → AI อ่านอัตโนมัติ
- คำนวณยอด + VAT → ถูกต้อง 100%
- สรุปยอดรายเดือน → 1 คลิก
- ค้นหา invoice → พิมพ์คำว่า "ค่าไฟ" ก็เจอ

</div>

> 🌟 **ประหยัดเวลา 90% — ไม่ต้องบันทึกเอง!**

---

<!-- _class: lead -->

# 🎯 Part 1: /goal + Kanban

## สร้างเว็บง่ายๆ ด้วย AI หลายตัว

<div class="kawaii-box">

### สิ่งที่จะได้เรียนรู้
- ✅ `/goal` — สั่งงาน AI ให้ทำงานจนเสร็จ
- ✅ Kanban — หลาย AI ร่วมมือกัน
- ✅ Profiles — designer, developer, tester
- ✅ Dependencies — งานต่อกันอัตโนมัติ

</div>

<div class="kawaii-box">

### ตัวอย่างผลลัพธ์
```
T1 (Design) → T2 (Develop) → T3 (Test)
     ↓              ↓              ↓
  🎨 UI/UX      💻 Code        🧪 QA
```

</div>

---

# ทบทวน: `/goal` คืออะไร?

<div class="kawaii-box">

## 🎯 Concept
> "บอก AI ว่าต้องการอะไร → AI จะทำงานต่อไปเรื่อยๆ จนกว่าจะเสร็จ"

### ตัวอย่าง
```
/goal สร้าง landing page สำหรับร้านอาหาร
- มีเมนูอาหาร
- มีรูปภาพ
- มีที่อยู่และเบอร์โทร
- รองรับ mobile
```

</div>

<div class="kawaii-box">

## 🎬 ผลลัพธ์
1. AI วิเคราะห์ความต้องการ
2. สร้าง HTML/CSS
3. เพิ่มรูปภาพ
4. ทดสอบ responsive
5. ✅ "เสร็จแล้ว!"

</div>

---

# เปรียบเทียบ: Hermes vs OpenAI

<div class="kawaii-box">

| | Hermes `/goal` | OpenAI `/goal` |
|---|----------------|----------------|
| **การทำงาน** | ต่อเนื่องจนเสร็จ | ทำครั้งเดียวแล้วจบ |
| **Orchestration** | มี Kanban, Cron | ไม่มี |
| **Multi-agent** | หลาย AI ร่วมมือ | AI เดียว |
| **Auto-retry** | มี (Auto-Heal) | ไม่มี |
| **เหมาะสำหรับ** | งานซับซ้อน | งานง่ายๆ |

</div>

> 💡 **Hermes = ทีม AI ทำงานร่วมกัน**
> 💡 **OpenAI = AI เดียวทำงานคนเดียว**

---

# ตัวอย่าง: สร้างเว็บด้วย Kanban

<div class="kawaii-box">

## 🎬 3 AI ทำงานร่วมกัน

```
T1 researcher 🔍  หาข้อมูลคู่แข่ง
              ↓
T2 developer 💻  เขียนโค้ด HTML/CSS
              ↓
T3 tester 🧪    ทดสอบ responsive
```

</div>

<div class="kawaii-box">

## คำสั่ง (Copy-paste ได้เลย!)

```bash
# สร้าง profiles
hermes profile create researcher
hermes profile create developer
hermes profile create tester

# สร้าง tasks
T1=$(hermes kanban create "Research competitors" \
     --assignee researcher --print-id)
T2=$(hermes kanban create "Develop website" \
     --assignee developer --parent $T1 --print-id)
T3=$(hermes kanban create "Test responsive" \
     --assignee tester --parent $T2 --print-id)

# เริ่มทำงาน!
hermes kanban dispatch
```

</div>

---

# Lab 1: สร้าง Landing Page

<div style="display: flex; gap: 20px;">

<div class="kawaii-box" style="flex: 1;">

## 📝 ขั้นตอนที่ 1: สร้าง profiles

```bash
hermes profile create designer
hermes profile create developer
hermes profile create tester
```

</div>

<div class="kawaii-box" style="flex: 1;">

## 🎨 Profiles คืออะไร?

| Profile | หน้าที่ |
|---------|---------|
| 🎨 **designer** | ออกแบบ UI/UX |
| 💻 **developer** | เขียนโค้ด HTML/CSS |
| 🧪 **tester** | ทดสอบ responsive |

</div>

</div>

<div style="display: flex; gap: 20px;">

<div class="kawaii-box" style="flex: 1;">

## 📝 ขั้นตอนที่ 2: สร้าง tasks

```bash
T1=$(hermes kanban create "Design landing page" \
     --assignee designer --print-id)
T2=$(hermes kanban create "Develop HTML/CSS" \
     --assignee developer --parent $T1 --print-id)
T3=$(hermes kanban create "Test on mobile" \
     --assignee tester --parent $T2 --print-id)
```

</div>

<div class="kawaii-box" style="flex: 1;">

## 🔗 Dependencies

```
T1 (Design)
  ↓
T2 (Develop)
  ↓
T3 (Test)
```

**T2 รอ T1 เสร็จก่อน**
**T3 รอ T2 เสร็จก่อน**

</div>

</div>

<div class="kawaii-box">

## 📝 ขั้นตอนที่ 3: เริ่มทำงาน

```bash
hermes kanban dispatch
```

เปิด browser: http://localhost:9119/kanban

</div>

> 🌸 **ดู AI ทำงาน — ไม่ต้องกดอะไร!**

---

# สรุป Part 1

<div class="kawaii-box">

## ✅ สิ่งที่ได้เรียนรู้

1. **`/goal`** — สั่งงาน AI ให้ทำงานจนเสร็จ
2. **Kanban** — หลาย AI ร่วมมือกัน
3. **Hermes vs OpenAI** — Hermes เหมาะกับงานซับซ้อน

</div>

<div class="kawaii-box">

## 🎯 สิ่งที่ได้ทำ

- ✅ สร้าง profiles (designer, developer, tester)
- ✅ สร้าง tasks พร้อม dependencies
- ✅ Dispatch และ monitor
- ✅ ได้ landing page สำเร็จ

</div>

> 🌟 **พร้อมไป Part 2 แล้ว!**

---

<!-- _class: lead -->

# 📄 Part 2: Invoice Processing

## สร้างระบบอ่าน Invoice จากกล้อง

<div class="kawaii-box">

### สิ่งที่จะได้เรียนรู้
- ✅ สร้าง Web App ด้วย `/goal`
- ✅ OCR — AI อ่านข้อความจากภาพ
- ✅ Mobile Camera — ถ่ายรูปจากโทรศัพท์
- ✅ Dashboard — สรุปยอดตามประเภท
- ✅ Cron — สรุปอัตโนมัติทุกสัปดาห์

</div>

<div class="kawaii-box">

### ตัวอย่าง Invoice ที่ใช้
| ประเภท | ตัวอย่าง |
|--------|----------|
| 📄 Invoice ภาษาอังกฤษ | IT Services, Marketing |
| 📄 Invoice ภาษาไทย | Office Supplies, Restaurant |
| 🧾 ใบเสร็จ | Receipt |
| 🧾 ใบกำกับภาษี | Tax Invoice (มี VAT 7%) |

</div>

---

# เป้าหมาย Part 2

<div class="two-col">

<div class="kawaii-box">

## 🎯 สร้าง Web App ที่:
1. ถ่ายรูป invoice จากโทรศัพท์
2. AI อ่านข้อมูลอัตโนมัติ (OCR)
3. แสดงผลลัพธ์: เลขที่, วันที่, ยอดเงิน
4. บันทึกข้อมูลลง database
5. สรุปยอดตามประเภท

### 📱 ฟีเจอร์พิเศษ
- ✅ ถ่ายรูปจากกล้องมือถือ
- ✅ Upload จากไฟล์ PDF/JPG
- ✅ Dashboard สรุปยอดรายเดือน
- ✅ Export Excel ได้

</div>

<div class="kawaii-box">

## 🛠️ เทคโนโลยีที่ใช้

| เทคโนโลยี | ใช้ทำอะไร |
|-----------|----------|
| 🐍 **Python** | Backend (Flask/FastAPI) |
| 🗄️ **SQLite** | เก็บข้อมูล invoice |
| 🤖 **AI OCR** | อ่านข้อความจากภาพ |
| 📱 **HTML5** | Responsive + Camera API |

### 📊 ตัวอย่าง Dashboard
```
💰 สรุปยอดเดือน ก.ย. 2569
─────────────────────
🍔 อาหาร:      ฿45,000
📦 อุปกรณ์:    ฿28,500
🔧 บริการ:     ฿67,200
─────────────────────
✅ รวม:       ฿140,700
```

</div>

</div>

<div class="two-col">

<div class="kawaii-box">

## 📋 ตัวอย่าง Invoice ที่มี
- invoice_001_en.pdf — IT Services (EN)
- invoice_002_th.pdf — Office Supplies (TH, มี VAT)
- invoice_003_consulting.pdf — Consulting
- invoice_004_restaurant.pdf — Restaurant
- invoice_005_marketing.pdf — Marketing
- invoice_006_receipt.pdf — ใบเสร็จ
- invoice_007_tax_invoice.pdf — ใบกำกับภาษี

</div>

<div class="kawaii-box">

## 🔄 ขั้นตอนการทำงาน

```
📱 ถ่ายรูป/Upload
      ↓
🤖 AI อ่านข้อมูล (OCR)
      ↓
📊 แสดงผลลัพธ์
      ↓
💾 บันทึก SQLite
      ↓
📈 Dashboard สรุป
```

### 🎯 ข้อมูลที่อ่านได้
- เลขที่ Invoice
- วันที่
- ชื่อผู้ขาย
- รายการสินค้า/บริการ
- ยอดเงินรวม
- VAT (ถ้ามี)

</div>

</div>

---

# Lab 2: สร้าง Web App

<div style="display: flex; gap: 20px;">

<div class="kawaii-box" style="flex: 1;">

## 📝 ขั้นตอนที่ 1: ตั้ง `/goal`

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

</div>

<div class="kawaii-box" style="flex: 1;">

## 🔄 Flow การทำงาน

```
📱 ถ่ายรูป/Upload
      ↓
🤖 AI อ่านข้อมูล (OCR)
      ↓
📊 แสดงผลลัพธ์
      ↓
💾 บันทึก SQLite
      ↓
📈 Dashboard สรุป
```

</div>

</div>

<div class="kawaii-box">

## 🎬 ผลลัพธ์ที่คาดหวัง
1. AI สร้าง web app สำเร็จ
2. มีหน้า upload รูป
3. มีหน้า dashboard
4. รองรับ mobile

</div>

> 💡 **AI สร้างเว็บให้ — ไม่ต้องเขียนโค้ด!**

---

# Lab 3: ทดสอบกับ Invoice

<div class="kawaii-box">

## 📝 ขั้นตอนที่ 1: รัน Web App

```bash
cd invoice-app
python app.py
```

เปิด browser: http://localhost:5000

</div>

<div class="kawaii-box">

## 📝 ขั้นตอนที่ 2: อัพโหลด Invoice

1. คลิก "Upload Invoice"
2. เลือกไฟล์ `invoice_001.pdf`
3. กด "Process"
4. รอ AI อ่านข้อมูล

</div>

<div class="kawaii-box">

## 📝 ขั้นตอนที่ 3: ตรวจสอบผลลัพธ์

- เลขที่ invoice ถูกต้องไหม?
- วันที่ถูกต้องไหม?
- ยอดเงินถูกต้องไหม?
- ประเภทถูกต้องไหม?

</div>

---

# Lab 4: ใช้กล้องโทรศัพท์

<div style="display: flex; gap: 20px;">

<div class="kawaii-box" style="flex: 1;">

## 📝 ขั้นตอนที่ 1: เปิด Web App บนโทรศัพท์

1. หา IP ของเครื่อง: `ip addr show`
2. เปิด firewall port 5000
3. บนโทรศัพท์ เปิด: `http://YOUR_IP:5000`

</div>

<div class="kawaii-box" style="flex: 1;">

## 💡 เคล็ดลับการถ่ายรูป

| ✅ ควรทำ | ❌ ไม่ควรทำ |
|---------|-----------|
| ถ่ายในแสงสว่างเพียงพอ | ถ่ายในที่มืด |
| ถือกล้องให้ตรง | ถ่ายเอียง |
| ถ่ายทั้งใบให้ครบ | ถ่ายไม่ครบ |
| ใช้พื้นหลังเรียบ | พื้นหลังลายตา |

</div>

</div>

<div style="display: flex; gap: 20px;">

<div class="kawaii-box" style="flex: 1;">

## 📝 ขั้นตอนที่ 2: ถ่ายรูป Invoice

1. กดปุ่ม "Upload from Camera"
2. ถ่ายรูป invoice_001.pdf
3. อัพโหลด
4. รอ AI อ่านข้อมูล

</div>

<div class="kawaii-box" style="flex: 1;">

## 📝 ขั้นตอนที่ 3: ตรวจสอบผลลัพธ์

- ภาพจากกล้องอ่านได้ไหม?
- ภาพชัดพอไหม?
- แสงสว่างมีผลไหม?

### 🎯 ตัวอย่างผลลัพธ์ที่ดี
```
✅ Invoice No: INV-001
✅ Date: 2026-09-17
✅ Total: ฿16,050
```

</div>

</div>

> 🌸 **ถ่ายรูป → AI อ่าน → เสร็จ!**

---

# Lab 5: เพิ่มฟีเจอร์

<div class="kawaii-box">

## 📝 ตั้ง `/goal` เพิ่มฟีเจอร์

```bash
/goal ปรับแต่งระบบประมวลผล invoice
- เพิ่มการแยกประเภทอัตโนมัติ (อาหาร, อุปกรณ์, บริการ)
- สร้างรายงานสรุปประจำเดือน
- Export เป็น Excel
- ส่งแจ้งเตือนทาง LINE เมื่อมียอดเกินกำหนด
```

</div>

<div class="kawaii-box">

## 🎬 ผลลัพธ์ที่คาดหวัง
1. แยกประเภทอัตโนมัติ
2. รายงานสรุปประจำเดือน
3. Export Excel ได้
4. แจ้งเตือน LINE

</div>

> 💡 **เพิ่มฟีเจอร์ได้ง่ายๆ ด้วย `/goal`!**

---

# Lab 6: Automation ด้วย Cron

<div style="display: flex; gap: 20px;">

<div class="kawaii-box" style="flex: 1;">

## 📝 ตั้ง Cronjob

```bash
cronjob create \
  --schedule "0 9 * * 1" \
  --prompt "สรุปยอด invoice สัปดาห์นี้ 
           แบ่งตามประเภท 
           ส่งรายงานทาง LINE" \
  --name "Weekly Invoice Summary"
```

</div>

<div class="kawaii-box" style="flex: 1;">

## ⏰ Cron Schedule ตัวอย่าง

| Schedule | ความหมาย |
|----------|-----------|
| `0 9 * * 1` | ทุกวันจันทร์ 9:00 |
| `0 8 * * *` | ทุกวัน 8:00 |
| `0 */6 * * *` | ทุก 6 ชั่วโมง |
| `*/30 * * * *` | ทุก 30 นาที |

</div>

</div>

<div style="display: flex; gap: 20px;">

<div class="kawaii-box" style="flex: 1;">

## 📝 ทดสอบทันที

```bash
cronjob run <job_id>
```

</div>

<div class="kawaii-box" style="flex: 1;">

## 🎬 ผลลัพธ์
- ทุกวันจันทร์ 9:00 น.
- AI สรุปยอด invoice
- ส่งรายงานทาง LINE

</div>

</div>

> 🌸 **อัตโนมัติ 100% — ไม่ต้องทำเอง!**

---

# สรุป Part 2

<div style="display: flex; gap: 15px;">

<div class="kawaii-box" style="flex: 1;">

## ✅ สิ่งที่ได้เรียนรู้

1. **สร้าง Web App** — ด้วย `/goal`
2. **OCR Invoice** — AI อ่านข้อมูลจากภาพ
3. **Mobile Camera** — ถ่ายรูปจากโทรศัพท์
4. **Dashboard** — สรุปยอดตามประเภท
5. **Cron Automation** — สรุปอัตโนมัติทุกสัปดาห์

### 🎯 Key Takeaways
- ไม่ต้องเขียนโค้ดเอง
- ใช้ AI ทำทุกอย่าง
- ทำงานได้ 24/7
- ประหยัดเวลา 90%

</div>

<div class="kawaii-box" style="flex: 1;">

## 🎯 สิ่งที่ได้ทำ

- ✅ สร้าง web app อ่าน invoice
- ✅ ทดสอบกับ invoice 7 แบบ
- ✅ ใช้กล้องโทรศัพท์ถ่ายรูป
- ✅ เพิ่มฟีเจอร์แยกประเภท
- ✅ ตั้ง cron สรุปอัตโนมัติ

### 📊 ผลลัพธ์ที่ได้
```
⏱️ เวลาที่ใช้: 1 ชั่วโมง
📄 Invoice ที่ทดสอบ: 7 แบบ
✅ ความถูกต้อง: 95%+
💰 เวลาที่ประหยัด: 90%
```

</div>

</div>

<div style="display: flex; gap: 15px;">

<div class="kawaii-box" style="flex: 1;">

## 💡 แนวทางพัฒนาต่อ

| ขั้นต่อไป | รายละเอียด |
|-----------|-----------|
| 🔗 เชื่อม Google Sheets | ส่งข้อมูล invoice เข้า Sheets อัตโนมัติ |
| 📊 สร้างกราฟรายเดือน | ดูแนวโน้มค่าใช้จ่าย |
| 🔔 แจ้งเตือน LINE | เมื่อมียอดเกินงบประมาณ |
| 🤖 Auto-categorize | AI แยกประเภท invoice อัตโนมัติ |

</div>

<div class="kawaii-box" style="flex: 1;">

## 🚀 ขั้นตอนต่อไป

### 1. ทดลองกับข้อมูลจริง
- รวบรวม invoice ของธุรกิจคุณ
- ทดสอบกับระบบที่สร้าง

### 2. ปรับแต่งให้เหมาะกับงาน
- เพิ่มประเภท invoice ที่ใช้บ่อย
- ตั้งค่าการแจ้งเตือน

### 3. ขยายระบบ
- เชื่อมกับระบบบัญชี
- สร้างรายงานอัตโนมัติ

</div>

</div>

---

# 🎁 สรุปทั้งหมด

<div style="display: flex; gap: 20px;">

<div class="kawaii-box" style="flex: 1;">

## Part 1: /goal + Kanban
- ✅ `/goal` — สั่งงาน AI
- ✅ Kanban — หลาย AI ร่วมมือ
- ✅ Hermes vs OpenAI — ข้อดี/ข้อเสีย

</div>

<div class="kawaii-box" style="flex: 1;">

## 🎯 สิ่งที่ได้ทำ
- ✅ สร้าง profiles (designer, developer, tester)
- ✅ สร้าง tasks พร้อม dependencies
- ✅ Dispatch และ monitor
- ✅ ได้ landing page สำเร็จ

</div>

</div>

<div style="display: flex; gap: 20px;">

<div class="kawaii-box" style="flex: 1;">

## Part 2: Invoice Processing
- ✅ สร้าง Web App — ด้วย `/goal`
- ✅ OCR Invoice — AI อ่านจากภาพ
- ✅ Mobile Camera — ถ่ายรูปจากโทรศัพท์
- ✅ Dashboard — สรุปยอด
- ✅ Cron — อัตโนมัติ

</div>

<div class="kawaii-box" style="flex: 1;">

## 📊 ผลลัพธ์
- ✅ Web app อ่าน invoice ได้
- ✅ ทดสอบกับ invoice 7 แบบ
- ✅ ใช้กล้องโทรศัพท์ถ่ายรูป
- ✅ เพิ่มฟีเจอร์แยกประเภท
- ✅ ตั้ง cron สรุปอัตโนมัติ

</div>

</div>

> 🌟 **คุณสร้างระบบประมวลผล Invoice สำเร็จแล้ว!**

---

# 📝 การบ้าน

<div class="kawaii-box">

## 🎯 ลองทำกับ Invoice จริง

### ขั้นตอนที่ 1: รวบรวม Invoice
- Invoice จาก suppliers
- ใบเสร็จรับเงิน
- ใบกำกับภาษี

### ขั้นตอนที่ 2: อัพโหลดเข้าระบบ
- ถ่ายรูปจากโทรศัพท์
- อัพโหลดเข้า web app
- ตรวจสอบผลลัพธ์

### ขั้นตอนที่ 3: วิเคราะห์ข้อมูล
- ดู dashboard สรุปยอด
- Export เป็น Excel
- วิเคราะห์ค่าใช้จ่าย

</div>

> 💡 **เริ่มจาก invoice 10 ใบ แล้วค่อยขยาย!**

---

# 🙏 ขอบคุณครับ

<div class="kawaii-box">

## 📚 แหล่งข้อมูลเพิ่มเติม
- **Docs:** hermes-agent.nousresearch.com
- **GitHub:** github.com/NousResearch/hermes-agent
- **Community:** Discord Hermes Agent

</div>

<div class="kawaii-box">

## 📞 ติดต่อเรา
- **LINE:** @hermes-support
- **Email:** support@hermes-agent.com

## 🎁 สิ่งที่ได้กลับบ้าน
- ✅ ตัวอย่าง invoice 7 แบบ
- ✅ Web app ประมวลผล invoice
- ✅ Lab exercises ทั้งหมด
- ✅ ความรู้ในการสร้าง automation

</div>

> 🌸 **ขอให้สนุกกับการสร้างระบบอัตโนมัติ!** 🌸

---

<!-- _class: lead -->

# 🎉 ขอบคุณครับ!

## มีคำถามอะไรไหม?

📄✨🎯📋⏰🔁
