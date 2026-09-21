---
marp: true
theme: default
paginate: true
header: "SME Invoice Processing Workshop 📄"
footer: "สร้างระบบประมวลผล Invoice ด้วย Hermes Agent"
style: |
  section {
    font-family: 'Sarabun', 'Noto Sans Thai', 'Noto Color Emoji', sans-serif;
    font-size: 16px;
    line-height: 1.35;
    padding: 25px 35px;
    background: linear-gradient(135deg, #e0f7fa 0%, #f3e5f5 100%);
    color: #2d2d2d;
    overflow: hidden;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
  
  section * {
    font-family: inherit;
  }
  
  section li,
  section p,
  section td,
  section th,
  section h1,
  section h2,
  section h3 {
    line-height: 1.6;
    overflow-wrap: break-word;
    white-space: normal;
  }
  
  /* Fix emoji to render inline with text */
  img.emoji, .emoji {
    display: inline !important;
    width: 1em !important;
    height: 1em !important;
    vertical-align: -0.1em !important;
    margin: 0 0.1em 0 0 !important;
  }
  
  img[data-marp-twemoji] {
    display: inline !important;
    width: 1.1em !important;
    height: 1.1em !important;
    vertical-align: -0.15em !important;
    margin: 0 0.1em 0 0 !important;
  }
  
  /* Invoice full grid layout */
  .invoice-full-grid {
    position: absolute !important;
    top: 80px !important;
    left: 30px !important;
    right: 30px !important;
    bottom: 50px !important;
    display: grid !important;
    grid-template-columns: 1fr 1fr 1fr !important;
    grid-template-rows: 1fr 1fr !important;
    gap: 10px !important;
  }
  
  .invoice-full-grid img {
    width: 100% !important;
    height: 100% !important;
    object-fit: contain !important;
    border: 2px solid #e0e0e0 !important;
    border-radius: 8px !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15) !important;
  }
  
  /* Prevent digit spacing issues */
  span.num, code {
    letter-spacing: 0 !important;
    word-spacing: 0 !important;
  }
  
  /* Global fix for number spacing */
  section {
    word-spacing: normal !important;
    text-justify: auto !important;
  }
  section.lead {
    justify-content: center;
    align-items: center;
    text-align: center;
  }
  header { color: #00897b; font-size: 13px; }
  footer { color: #999; font-size: 11px; }
  h1 {
    color: #00897b;
    text-align: center;
    text-shadow: 2px 2px 4px rgba(0,137,123,0.2);
    font-size: 28px;
    margin: 0 0 10px 0;
  }
  h2 {
    color: #7b1fa2;
    font-size: 20px;
    margin: 6px 0;
  }
  h3 {
    color: #1976d2;
    font-size: 16px;
    margin: 4px 0;
  }
  p, ul, ol { margin: 4px 0; }
  ul, ol { padding-left: 22px; }
  li { margin: 2px 0; }
  code {
    background: #e0f2f1;
    color: #004d40;
    padding: 1px 5px;
    border-radius: 4px;
    font-size: 13px;
    word-break: break-all;
  }
  pre {
    background: #1e1e1e;
    color: #d4d4d4;
    border-radius: 8px;
    padding: 8px;
    margin: 6px 0;
    overflow-x: auto;
    font-size: 12px;
    line-height: 1.25;
  }
  pre code {
    background: transparent;
    color: #d4d4d4 !important;
    word-break: normal;
    white-space: pre;
  }
  /* Override syntax highlighting for better contrast */
  pre .hljs-keyword,
  pre .hljs-selector-tag,
  pre .hljs-built_in,
  pre .hljs-name,
  pre .hljs-tag {
    color: #569cd6 !important;
  }
  pre .hljs-string,
  pre .hljs-title,
  pre .hljs-section,
  pre .hljs-attribute,
  pre .hljs-literal,
  pre .hljs-template-tag,
  pre .hljs-selector-id,
  pre .hljs-selector-class,
  pre .hljs-quote,
  pre .hljs-template-variable,
  pre .hljs-addition {
    color: #ce9178 !important;
  }
  pre .hljs-comment,
  pre .hljs-deletion,
  pre .hljs-number,
  pre .hljs-regexp {
    color: #b5cea8 !important;
  }
  .kawaii-box {
    background: white;
    border: 2px solid #80cbc4;
    border-radius: 12px;
    padding: 10px;
    margin: 6px 0;
    box-shadow: 0 2px 8px rgba(128,203,196,0.2);
    max-width: 100%;
    overflow: visible;
  }
  .emoji-big { font-size: 32px; text-align: center; }
  table {
    margin: 6px auto;
    border-collapse: collapse;
    font-size: 14px;
    max-width: 100%;
  }
  th {
    background: #80cbc4;
    color: white;
    padding: 5px 8px;
  }
  td {
    background: white;
    padding: 4px 8px;
  }
  blockquote {
    border-left: 4px solid #80cbc4;
    background: #e0f2f1;
    padding: 6px 10px;
    border-radius: 0 8px 8px 0;
    margin: 6px 0;
    font-size: 14px;
  }
  img {
    max-height: 180px;
    max-width: 80%;
    display: block;
    margin: 6px auto;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  }
  .invoice-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 8px;
    margin: 8px 0;
  }
  .invoice-grid img {
    max-height: 120px;
    width: 100%;
    object-fit: contain;
    margin: 0;
  }
  .invoice-grid-full {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-template-rows: repeat(2, 1fr);
    gap: 20px;
    width: 100%;
    height: calc(100% - 120px);
    margin: 20px auto;
    padding: 0 40px;
    box-sizing: border-box;
  }
  .invoice-grid-full img {
    max-height: 100%;
    max-width: 100%;
    width: auto;
    height: auto;
    object-fit: contain;
    border: 2px solid #e0e0e0;
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    justify-self: center;
    align-self: center;
  }
  .two-col {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    align-items: start;
  }
  .two-col .kawaii-box { margin: 0; }
  .compact pre { font-size: 11px; padding: 6px; margin: 4px 0; }
  .compact .kawaii-box { padding: 8px; margin: 4px 0; }
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

<div style="display: flex; justify-content: space-around; margin-top: 20px;">
  <img src="mockups/kawaii_part1_agents.png" style="width: 45%; max-height: 200px; object-fit: contain; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
  <img src="mockups/kawaii_part2_invoice.png" style="width: 45%; max-height: 200px; object-fit: contain; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
</div>

---

# 📊 ปัญหาของ SME

<div class="two-col">

<div class="kawaii-box">

## ❌ แบบเดิม (ทำเอง)
- รับ invoice กระดาษ → บันทึกเองใน Excel
- คำนวณยอดรวมเอง → ผิดบ่อย
- สรุปยอดรายเดือน → ใช้เวลา 2-3 ชม.
- หา invoice เก่า → ยากมาก

</div>

<div class="kawaii-box">

## ✅ แบบใหม่ (ให้ AI ทำ)
- ถ่ายรูป → AI อ่านอัตโนมัติ
- คำนวณยอด + VAT → ถูกต้อง `100%`
- สรุปยอดรายเดือน → 1 คลิก
- ค้นหา → พิมพ์คำว่า "ค่าไฟ" ก็เจอ

</div>

</div>

> 🌟 **ประหยัดเวลา `90%` — ไม่ต้องบันทึกเอง!**

---

# 🎯 Part 1: /goal + Kanban

## สร้างเว็บง่ายๆ ด้วย AI หลายตัว

<div class="two-col">

<div class="kawaii-box">

### สิ่งที่จะได้เรียนรู้
- ✅ `/goal` — สั่งงาน AI ให้ทำงานจนเสร็จ
- ✅ Kanban — หลาย AI ร่วมมือกัน
- ✅ Profiles — designer, developer, tester
- ✅ Dependencies — งานต่อกันอัตโนมัติ

</div>

<div>

![Multi-Agent Collaboration](mockups/kawaii_part1_agents.png)

</div>

</div>

---

# ทบทวน: `/goal` คืออะไร?

<div class="two-col">

<div class="kawaii-box">

## 🎯 Concept
> "บอก AI ว่าต้องการอะไร → AI ทำงานจนเสร็จ"

### ตัวอย่าง
```
/goal สร้าง landing page ร้านอาหาร
- มีเมนูอาหาร
- มีรูปภาพ
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

</div>

---

# เปรียบเทียบ: Hermes vs OpenAI

<div class="kawaii-box">

| | Hermes `/goal` | OpenAI `/goal` |
|---|---|---|
| **การทำงาน** | ต่อเนื่องจนเสร็จ | ทำครั้งเดียวแล้วจบ |
| **Orchestration** | มี Kanban, Cron | ไม่มี |
| **Multi-agent** | หลาย AI ร่วมมือ | AI เดียว |
| **Auto-retry** | มี (Auto-Heal) | ไม่มี |
| **เหมาะสำหรับ** | งานซับซ้อน | งานง่ายๆ |

</div>

> 💡 **Hermes = ทีม AI ทำงานร่วมกัน** | **OpenAI = AI เดียวทำงานคนเดียว**

---

# ตัวอย่าง: สร้างเว็บด้วย Kanban

<div class="two-col">

<div class="kawaii-box">

## 💬 แบบภาษามนุษย์ (ง่ายมาก!)

```
/goal สร้าง landing page สำหรับร้านอาหาร
โดยมีทีม AI 3 คน:
- researcher หาข้อมูลคู่แข่ง
- developer เขียนโค้ด HTML/CSS
- tester ทดสอบ responsive
```

**แค่นี้! AI จะจัดการทุกอย่างให้เอง**

</div>

<div class="kawaii-box compact">

## 🔧 แบบ Command (สำหรับสาย Tech)

```bash
hermes profile create researcher
hermes profile create developer
hermes profile create tester

T1=$(hermes kanban create "Research" \
     --assignee researcher --print-id)
T2=$(hermes kanban create "Develop" \
     --assignee developer --parent $T1 --print-id)
T3=$(hermes kanban create "Test" \
     --assignee tester --parent $T2 --print-id)

hermes kanban dispatch
```

</div>

</div>

![Kanban Board](mockups/mockup_kanban_board.png)

> 💡 **ทั้งสองแบบได้ผลลัพธ์เหมือนกัน — เลือกแบบที่ถนัด!**

---

# Lab 1: สร้าง Landing Page

<div class="two-col">

<div class="kawaii-box">

## 💬 แบบภาษามนุษย์

```
/goal สร้าง landing page สำหรับร้านอาหาร
- มีเมนูอาหารและรูปภาพ
- มีที่อยู่และเบอร์โทร
- รองรับมือถือ
- ให้ทีม AI 3 คนช่วยกัน:
  designer ออกแบบ, developer เขียนโค้ด, tester ทดสอบ
```

**แค่นี้! AI จะสร้าง profiles และ tasks ให้เอง**

</div>

<div class="kawaii-box compact">

## 🔧 แบบ Command (สำหรับสาย Tech)

```bash
hermes profile create designer
hermes profile create developer
hermes profile create tester

T1=$(hermes kanban create "Design" \
     --assignee designer --print-id)
T2=$(hermes kanban create "Develop" \
     --assignee developer --parent $T1 --print-id)
T3=$(hermes kanban create "Test" \
     --assignee tester --parent $T2 --print-id)

hermes kanban dispatch
```

</div>

</div>

> 🌸 **ทั้งสองแบบได้ผลลัพธ์เหมือนกัน — เลือกแบบที่ถนัด!**

![Landing Page Result](mockups/mockup_landing_page.png)

---

# สรุป Part 1

<div class="two-col">

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

</div>

> 🌟 **พร้อมไป Part 2 แล้ว!**

---

<!-- _class: lead -->

# 📄 Part 2: Invoice Processing

---

## ตัวอย่าง Invoice 6 ประเภท

<div class="invoice-full-grid">

<img src="invoices/invoice_001_en.png" />
<img src="invoices/invoice_002_th.png" />
<img src="invoices/invoice_003_consulting.png" />
<img src="invoices/invoice_004_restaurant.png" />
<img src="invoices/invoice_005_marketing.png" />
<img src="invoices/invoice_006_receipt.png" />

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

### 🛠️ เทคโนโลยี
- 🐍 Python (Flask/FastAPI)
- 🗄️ SQLite
- 🤖 AI OCR
- 📱 HTML5 Responsive

</div>

<div class="kawaii-box">

## 📋 ตัวอย่าง Invoice ที่มี

![Invoice EN](invoices/invoice_001_en.png)

### 🔄 ขั้นตอนการทำงาน
```
📱 ถ่ายรูป → 🤖 AI อ่าน → 💾 บันทึก → 📈 สรุป
```

</div>

</div>

---

# Lab 2: สร้าง Web App

<div class="two-col">

<div class="kawaii-box compact">

## 📝 ตั้ง `/goal`

```bash
/goal สร้าง web app ประมวลผล invoice
- ใช้ Flask หรือ FastAPI
- มีหน้า upload รูป invoice
- ใช้ AI อ่านข้อมูล (OCR)
- แสดง: เลขที่, วันที่, ยอดเงิน, ประเภท
- บันทึก SQLite
- Dashboard สรุปยอดตามประเภท
- รองรับ mobile
```

</div>

<div class="kawaii-box">

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

> 💡 **AI สร้างเว็บให้ — ไม่ต้องเขียนโค้ด!**

![Web App Interface](mockups/mockup_web_app_upload.png)

---

# Lab 3: ทดสอบกับ Invoice

<div class="two-col">

<div class="kawaii-box">

## 📝 ขั้นตอน

1. รัน Web App: `python app.py`
2. เปิด browser: `http://localhost:5000`
3. คลิก "Upload Invoice"
4. เลือกไฟล์ invoice
5. กด "Process"
6. รอ AI อ่านข้อมูล

</div>

<div class="kawaii-box">

## 📄 ตัวอย่าง Invoice ที่ใช้ทดสอบ

![Invoice TH](invoices/invoice_002_th.png)

### ✅ ตรวจสอบผลลัพธ์
- เลขที่ invoice ถูกต้องไหม?
- วันที่ถูกต้องไหม?
- ยอดเงินถูกต้องไหม?

</div>

</div>

---

# Lab 4: ใช้กล้องโทรศัพท์

<div class="two-col">

<div class="kawaii-box">

## 📝 เปิดบนโทรศัพท์

1. หา IP: `ip addr show`
2. เปิด port 5000
3. โทรศัพท์เปิด: `http://YOUR_IP:5000`
4. กด "Upload from Camera"
5. ถ่ายรูป invoice
6. รอ AI อ่าน

</div>

<div class="kawaii-box">

## 💡 เคล็ดลับการถ่ายรูป

| ✅ ควรทำ | ❌ ไม่ควรทำ |
|---------|-----------|
| แสงสว่างเพียงพอ | ที่มืด |
| ถือกล้องให้ตรง | ถ่ายเอียง |
| ถ่ายทั้งใบให้ครบ | ถ่ายไม่ครบ |
| พื้นหลังเรียบ | พื้นหลังลายตา |

</div>

</div>

> 🌸 **ถ่ายรูป → AI อ่าน → เสร็จ!**

![Phone Camera Tips](mockups/mockup_phone_camera.png)

---

# Lab 5: เพิ่มฟีเจอร์

<div class="two-col">

<div class="kawaii-box compact">

## 📝 ตั้ง `/goal` เพิ่มฟีเจอร์

```bash
/goal ปรับแต่งระบบประมวลผล invoice
- แยกประเภทอัตโนมัติ
  (อาหาร, อุปกรณ์, บริการ)
- รายงานสรุปประจำเดือน
- Export Excel
- แจ้งเตือน LINE เมื่อเกินงบ
```

</div>

<div class="kawaii-box">

## 🎬 ผลลัพธ์ที่คาดหวัง

1. ✅ แยกประเภทอัตโนมัติ
2. ✅ รายงานสรุปประจำเดือน
3. ✅ Export Excel ได้
4. ✅ แจ้งเตือน LINE

### 📊 ตัวอย่าง Dashboard
```
💰 สรุปยอดเดือน ก.ย. 2569
───────────────────
🍔 อาหาร:    ฿45,000
📦 อุปกรณ์:  ฿28,500
🔧 บริการ:   ฿67,200
───────────────────
✅ รวม:     ฿140,700
```

</div>

</div>

![Dashboard Preview](mockups/mockup_dashboard.png)

---

# Lab 6: Automation ด้วย Cron

<div class="two-col">

<div class="kawaii-box">

## 💬 แบบภาษามนุษย์

```
/cronjob ทุกวันจันทร์ 9 โมงเช้า
ให้สรุปยอด invoice สัปดาห์นี้
แบ่งตามประเภท
แล้วส่งรายงานทาง LINE
```

**แค่นี้! AI จะตั้ง cronjob ให้เอง**

</div>

<div class="kawaii-box compact">

## 🔧 แบบ Command (สำหรับสาย Tech)

```bash
cronjob create \
  --schedule "0 9 * * 1" \
  --prompt "สรุปยอด invoice
   สัปดาห์นี้ แบ่งตามประเภท
   ส่งรายงานทาง LINE" \
  --name "Weekly Summary"

# ทดสอบทันที
cronjob run <job_id>
```

</div>

</div>

> 💡 **ทั้งสองแบบได้ผลลัพธ์เหมือนกัน — เลือกแบบที่ถนัด!**

![Cron Workflow](mockups/mockup_cronjob_workflow.png)

---

# สรุป Part 2

<div class="two-col">

<div class="kawaii-box">

## ✅ สิ่งที่ได้เรียนรู้

1. **สร้าง Web App** — ด้วย `/goal`
2. **OCR Invoice** — AI อ่านจากภาพ
3. **Mobile Camera** — ถ่ายจากโทรศัพท์
4. **Dashboard** — สรุปยอดตามประเภท
5. **Cron** — อัตโนมัติทุกสัปดาห์

### 📊 ผลลัพธ์
- ⏱️ เวลา: 1 ชม. | ✅ ถูกต้อง: `95%+` | 💰 ประหยัด: `90%`

</div>

<div class="kawaii-box">

## 💡 แนวทางพัฒนาต่อ

| ขั้นต่อไป | รายละเอียด |
|-----------|-----------|
| 🔗 Google Sheets | ส่งข้อมูลอัตโนมัติ |
| 📊 กราฟรายเดือน | ดูแนวโน้ม |
| 🔔 แจ้งเตือน LINE | เมื่อเกินงบ |
| 🤖 Auto-categorize | AI แยกประเภท |

### 🚀 ขั้นตอนต่อไป
1. ทดลองกับข้อมูลจริง
2. ปรับแต่งให้เหมาะกับงาน
3. เชื่อมระบบบัญชี

</div>

</div>

---

# 🎁 สรุปทั้งหมด

<div class="two-col">

<div class="kawaii-box">

## Part 1: /goal + Kanban
- ✅ `/goal` — สั่งงาน AI
- ✅ Kanban — หลาย AI ร่วมมือ
- ✅ Hermes vs OpenAI
- ✅ สร้าง landing page สำเร็จ

</div>

<div class="kawaii-box">

## Part 2: Invoice Processing
- ✅ สร้าง Web App ด้วย `/goal`
- ✅ OCR Invoice จากภาพ
- ✅ กล้องโทรศัพท์
- ✅ Dashboard + Cron อัตโนมัติ

</div>

</div>

![Workshop Journey](mockups/kawaii_workshop_journey.png)

> 🌟 **คุณสร้างระบบประมวลผล Invoice สำเร็จแล้ว!**

---

# 📝 การบ้าน

<div class="kawaii-box">

## 🎯 ลองทำกับ Invoice จริง

### ขั้นตอนที่ 1: รวบรวม Invoice
- Invoice จาก suppliers / ใบเสร็จ / ใบกำกับภาษี

### ขั้นตอนที่ 2: อัพโหลดเข้าระบบ
- ถ่ายรูปจากโทรศัพท์ → อัพโหลด → ตรวจสอบ

### ขั้นตอนที่ 3: วิเคราะห์ข้อมูล
- ดู dashboard → Export Excel → วิเคราะห์ค่าใช้จ่าย

</div>

> 💡 **เริ่มจาก invoice 10 ใบ แล้วค่อยขยาย!**

---

# 🙏 ขอบคุณครับ

<div class="two-col">

<div class="kawaii-box">

## 📚 แหล่งข้อมูลเพิ่มเติม
- **Docs:** hermes-agent.nousresearch.com
- **GitHub:** github.com/NousResearch/hermes-agent
- **Community:** Discord Hermes Agent

</div>

<div class="kawaii-box">

## 🎁 สิ่งที่ได้กลับบ้าน
- ✅ ตัวอย่าง invoice 7 แบบ
- ✅ Web app ประมวลผล invoice
- ✅ Lab exercises ทั้งหมด
- ✅ ความรู้ในการสร้าง automation

</div>

</div>

> 🌸 **ขอให้สนุกกับการสร้างระบบอัตโนมัติ!** 🌸

---

<!-- _class: lead -->

# 🎉 ขอบคุณครับ!

## มีคำถามอะไรไหม?

📄✨🎯📋⏰🔁
