
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

mockups_dir = '/home/seiya/projects/training_course/private-course/courses/sme-invoice-processing-demo/slides/mockups'

# 1. Web App Upload
fig, ax = plt.subplots(figsize=(16, 9))
ax.set_xlim(0, 16)
ax.set_ylim(0, 9)
ax.axis('off')
fig.patch.set_facecolor('#ecf0f1')

# Header
header = patches.Rectangle((0, 8), 16, 0.8, facecolor='#2c3e50', zorder=1)
ax.add_patch(header)
ax.text(8, 8.4, '🤖 Invoice Processing System', ha='center', va='center', fontsize=18, fontweight='bold', color='white', zorder=2)

# Upload area
upload_box = patches.Rectangle((3, 4), 10, 3.5, linewidth=2, edgecolor='#3498db', linestyle='--', 
                                facecolor='#ebf5fb', alpha=0.5, zorder=1)
ax.add_patch(upload_box)
ax.text(8, 6.5, '📤', fontsize=40, ha='center', va='center', zorder=2)
ax.text(8, 5.5, 'วางไฟล์ Invoice ที่นี่ หรือ คลิกเพื่ออัปโหลด', ha='center', va='center', 
        fontsize=14, color='#2c3e50', zorder=2)
ax.text(8, 4.8, 'รองรับ PDF, PNG, JPG (ไม่เกิน 10MB)', ha='center', va='center', 
        fontsize=10, color='#7f8c8d', zorder=2)

# Recent invoices
ax.text(8, 3.5, '📋 ประมวลผลล่าสุด', ha='center', va='center', fontsize=14, fontweight='bold', color='#2c3e50')

invoices = [
    ('INV-001', '2026-09-18', '฿15,000', '✅ สำเร็จ'),
    ('INV-002', '2026-09-17', '฿23,500', '✅ สำเร็จ'),
    ('INV-003', '2026-09-16', '฿8,200', '⏳ กำลังประมวลผล')
]

for i, (inv, date, amount, status) in enumerate(invoices):
    y = 3 - i * 0.5
    row = patches.Rectangle((2, y-0.2), 12, 0.4, facecolor='white', edgecolor='#bdc3c7', linewidth=0.5, zorder=1)
    ax.add_patch(row)
    ax.text(3, y, inv, fontsize=9, color='#2c3e50', zorder=2)
    ax.text(5.5, y, date, fontsize=9, color='#7f8c8d', zorder=2)
    ax.text(9, y, amount, fontsize=9, fontweight='bold', color='#2c3e50', ha='center', zorder=2)
    ax.text(12, y, status, fontsize=9, color='#27ae60' if 'สำเร็จ' in status else '#f39c12', ha='center', zorder=2)

plt.tight_layout()
plt.savefig(f'{mockups_dir}/mockup_web_app_upload.png', dpi=150, bbox_inches='tight', facecolor='#ecf0f1')
plt.close()
print("✓ Web App Upload mockup created")

# 2. Phone Camera
fig, ax = plt.subplots(figsize=(16, 9))
ax.set_xlim(0, 16)
ax.set_ylim(0, 9)
ax.axis('off')
fig.patch.set_facecolor('#f8f9fa')

# Desk surface
desk = patches.Rectangle((0, 0), 16, 3, facecolor='#d4a574', alpha=0.3, zorder=1)
ax.add_patch(desk)

# Invoice document
invoice_bg = patches.Rectangle((4, 1), 8, 6, facecolor='white', edgecolor='#bdc3c7', linewidth=2, zorder=2)
ax.add_patch(invoice_bg)
ax.text(8, 6.5, 'INVOICE', ha='center', va='center', fontsize=20, fontweight='bold', color='#2c3e50', zorder=3)
ax.text(8, 6, 'ใบแจ้งหนี้', ha='center', va='center', fontsize=12, color='#7f8c8d', zorder=3)

# Invoice details
details = [
    'เลขที่: INV-2026-001',
    'วันที่: 18 กันยายน 2569',
    'ลูกค้า: บริษัท ABC จำกัด',
    '',
    'รายการ:',
    '  1. ค่าบริการที่ปรึกษา    ฿50,000',
    '  2. ค่าออกแบบ            ฿30,000',
    '  3. ค่าพัฒนาระบบ         ฿120,000',
    '',
    'รวมทั้งหมด:              ฿200,000'
]

for i, text in enumerate(details):
    ax.text(4.5, 5.5 - i*0.4, text, fontsize=8, color='#2c3e50', family='monospace', zorder=3)

# Phone outline
phone = patches.FancyBboxPatch((10, 2), 4, 6, boxstyle="round,pad=0.2", facecolor='#34495e', 
                                edgecolor='#2c3e50', linewidth=3, zorder=4)
ax.add_patch(phone)

# Phone screen
screen = patches.Rectangle((10.3, 2.5), 3.4, 5, facecolor='#000000', zorder=5)
ax.add_patch(screen)

# Camera viewfinder
viewfinder = patches.Rectangle((10.5, 3), 3, 4, facecolor='#1a1a2e', edgecolor='#00ff00', 
                                linewidth=1, zorder=6)
ax.add_patch(viewfinder)

# Corner markers
corners = [(10.5, 6.8), (13.5, 6.8), (10.5, 3), (13.5, 3)]
for x, y in corners:
    ax.plot([x, x+0.3], [y, y], color='#00ff00', linewidth=2, zorder=7)
    ax.plot([x, x], [y, y+0.3], color='#00ff00', linewidth=2, zorder=7)

# Camera icon
ax.text(12, 5, '📷', fontsize=30, ha='center', va='center', zorder=7)

# Capture button
capture_btn = plt.Circle((12, 3.5), 0.3, facecolor='white', edgecolor='#00ff00', linewidth=2, zorder=7)
ax.add_patch(capture_btn)

# Text
ax.text(8, 8.5, '✅ ถ่ายรูป Invoice ให้ชัดและตรง', ha='center', va='center', 
        fontsize=18, fontweight='bold', color='#27ae60', zorder=8)
ax.text(8, 0.3, '💡 เคล็ดลับ: ใช้แสงสว่างเพียงพอ ถือกล้องให้ตรง ถ่ายทั้งใบให้ครบ', 
        ha='center', va='center', fontsize=11, color='#7f8c8d', zorder=8)

plt.tight_layout()
plt.savefig(f'{mockups_dir}/mockup_phone_camera.png', dpi=150, bbox_inches='tight', facecolor='#f8f9fa')
plt.close()
print("✓ Phone Camera mockup created")

# 3. Dashboard
fig, ax = plt.subplots(figsize=(16, 9))
ax.set_xlim(0, 16)
ax.set_ylim(0, 9)
ax.axis('off')
fig.patch.set_facecolor('#f8f9fa')

# Header
header = patches.Rectangle((0, 8), 16, 0.8, facecolor='#34495e', zorder=1)
ax.add_patch(header)
ax.text(8, 8.4, '📊 Dashboard สรุปยอด Invoice', ha='center', va='center', 
        fontsize=18, fontweight='bold', color='white', zorder=2)

# Stats cards
stats = [
    ('📄 ใบแจ้งหนี้ทั้งหมด', '147', '#3498db'),
    ('💰 ยอดรวมเดือนนี้', '฿245,000', '#2ecc71'),
    ('⏱️ เวลาประมวลผล', '2.3 วินาที', '#e74c3c'),
    ('✅ ความแม่นยำ', '95%+', '#f39c12')
]

for i, (label, value, color) in enumerate(stats):
    x = 1 + i * 3.8
    card = patches.Rectangle((x, 6.5), 3.3, 1.2, facecolor='white', edgecolor=color, 
                             linewidth=2, zorder=1)
    ax.add_patch(card)
    ax.text(x + 1.65, 7.3, label, ha='center', va='center', fontsize=9, color='#7f8c8d', zorder=2)
    ax.text(x + 1.65, 6.9, value, ha='center', va='center', fontsize=14, fontweight='bold', 
            color=color, zorder=2)

# Line chart
ax.text(4, 6, '📈 ยอด Invoice รายเดือน', ha='center', va='center', fontsize=11, 
        fontweight='bold', color='#2c3e50')
chart_bg = patches.Rectangle((0.5, 3.5), 7, 2.3, facecolor='white', edgecolor='#bdc3c7', 
                              linewidth=1, zorder=1)
ax.add_patch(chart_bg)

months = ['เม.ย.', 'พ.ค.', 'มิ.ย.', 'ก.ค.', 'ส.ค.', 'ก.ย.']
values = [120, 150, 180, 210, 230, 245]
for i in range(len(months)-1):
    x1 = 1 + i * 1.1
    x2 = 1 + (i+1) * 1.1
    y1 = 3.7 + values[i] / 245 * 1.8
    y2 = 3.7 + values[i+1] / 245 * 1.8
    ax.plot([x1, x2], [y1, y2], color='#3498db', linewidth=2, zorder=3)
    ax.plot(x1, y1, 'o', color='#3498db', markersize=5, zorder=4)
    ax.text(x1, 3.6, months[i], ha='center', va='center', fontsize=7, color='#7f8c8d', zorder=2)

# Pie chart
ax.text(12, 6, '🥧 สัดส่วนตามประเภท', ha='center', va='center', fontsize=11, 
        fontweight='bold', color='#2c3e50')

pie_bg = patches.Rectangle((8.5, 3.5), 7, 2.3, facecolor='white', edgecolor='#bdc3c7', 
                            linewidth=1, zorder=1)
ax.add_patch(pie_bg)

# Pie slices (simplified)
categories = [
    ('🍔 อาหาร', '45%', '#e74c3c', 0, 162),
    ('📦 อุปกรณ์', '30%', '#3498db', 162, 270),
    ('🔧 บริการ', '25%', '#2ecc71', 270, 360)
]

for label, pct, color, start, end in categories:
    ax.text(10 + (categories.index((label, pct, color, start, end)) * 2), 5.3, 
            f'{label} {pct}', fontsize=8, color=color, fontweight='bold', zorder=2)

# Recent invoices table
ax.text(8, 3, '📋 ใบแจ้งหนีล่าสุด', ha='center', va='center', fontsize=11, 
        fontweight='bold', color='#2c3e50')

table_bg = patches.Rectangle((0.5, 0.5), 15, 2.3, facecolor='white', edgecolor='#bdc3c7', 
                              linewidth=1, zorder=1)
ax.add_patch(table_bg)

# Table header
table_header = patches.Rectangle((0.5, 2.4), 15, 0.4, facecolor='#34495e', zorder=2)
ax.add_patch(table_header)
ax.text(1.5, 2.6, 'เลขที่', fontsize=9, fontweight='bold', color='white', zorder=3)
ax.text(4, 2.6, 'วันที่', fontsize=9, fontweight='bold', color='white', zorder=3)
ax.text(7, 2.6, 'ประเภท', fontsize=9, fontweight='bold', color='white', ha='center', zorder=3)
ax.text(10.5, 2.6, 'จำนวนเงิน', fontsize=9, fontweight='bold', color='white', ha='center', zorder=3)
ax.text(14, 2.6, 'สถานะ', fontsize=9, fontweight='bold', color='white', ha='center', zorder=3)

# Table rows
rows = [
    ('INV-001', '18 ก.ย.', 'อาหาร', '฿15,000', '✅'),
    ('INV-002', '17 ก.ย.', 'อุปกรณ์', '฿23,500', '✅'),
    ('INV-003', '16 ก.ย.', 'บริการ', '฿8,200', '⏳'),
    ('INV-004', '15 ก.ย.', 'อาหาร', '฿12,800', '✅')
]

for i, (inv, date, cat, amount, status) in enumerate(rows):
    y = 2.1 - i * 0.4
    ax.text(1.5, y, inv, fontsize=8, color='#2c3e50', zorder=2)
    ax.text(4, y, date, fontsize=8, color='#7f8c8d', zorder=2)
    ax.text(7, y, cat, fontsize=8, color='#2c3e50', ha='center', zorder=2)
    ax.text(10.5, y, amount, fontsize=8, fontweight='bold', color='#2c3e50', ha='center', zorder=2)
    ax.text(14, y, status, fontsize=8, ha='center', zorder=2)

plt.tight_layout()
plt.savefig(f'{mockups_dir}/mockup_dashboard.png', dpi=150, bbox_inches='tight', facecolor='#f8f9fa')
plt.close()
print("✓ Dashboard mockup created")

# 4. Cronjob Workflow
fig, ax = plt.subplots(figsize=(16, 9))
ax.set_xlim(0, 16)
ax.set_ylim(0, 9)
ax.axis('off')
fig.patch.set_facecolor('#f8f9fa')

# Title
ax.text(8, 8.5, '🔄 Automated Invoice Processing Workflow', ha='center', va='center', 
        fontsize=20, fontweight='bold', color='#2c3e50')

# Workflow steps
steps = [
    ('⏰', 'ทุกวันจันทร์\n9:00 AM', '#9b59b6'),
    ('📄', 'รวบรวม\nInvoice', '#3498db'),
    ('🤖', 'AI\nประมวลผล', '#e74c3c'),
    ('💾', 'บันทึก\nDatabase', '#2ecc71'),
    ('📊', 'สร้าง\nรายงาน', '#f39c12'),
    ('💬', 'ส่ง\nLINE', '#1abc9c')
]

for i, (icon, label, color) in enumerate(steps):
    x = 1.5 + i * 2.5
    
    # Circle
    circle = plt.Circle((x, 5), 0.8, facecolor=color, edgecolor='white', linewidth=3, zorder=2)
    ax.add_patch(circle)
    
    # Icon
    ax.text(x, 5, icon, ha='center', va='center', fontsize=30, zorder=3)
    
    # Label
    ax.text(x, 3.8, label, ha='center', va='center', fontsize=10, fontweight='bold', color='#2c3e50')
    
    # Arrow (except last)
    if i < len(steps) - 1:
        ax.annotate('', xy=(x + 1.2, 5), xytext=(x + 0.8, 5),
                   arrowprops=dict(arrowstyle='->', lw=2, color='#95a5a6'))

# Benefits section
ax.text(8, 2.8, '✨ ประโยชน์ที่ได้รับ', ha='center', va='center', 
        fontsize=14, fontweight='bold', color='#2c3e50')

benefits = [
    ('⏱️', 'ประหยัดเวลา', 'ไม่ต้องทำมือทุกสัปดาห์'),
    ('🎯', 'แม่นยำ', 'AI อ่านข้อมูลอัตโนมัติ'),
    ('📈', 'ติดตามได้', 'รายงานอัตโนมัติทุกสัปดาห์')
]

for i, (icon, title, desc) in enumerate(benefits):
    x = 2 + i * 5
    y = 1.8
    
    # Card
    card = patches.Rectangle((x-1.5, y-0.8), 3, 1.3, facecolor='white', edgecolor='#bdc3c7', 
                             linewidth=1, zorder=1)
    ax.add_patch(card)
    
    ax.text(x, y+0.2, icon, ha='center', va='center', fontsize=20, zorder=2)
    ax.text(x, y-0.1, title, ha='center', va='center', fontsize=10, fontweight='bold', color='#2c3e50', zorder=2)
    ax.text(x, y-0.4, desc, ha='center', va='center', fontsize=8, color='#7f8c8d', zorder=2)

plt.tight_layout()
plt.savefig(f'{mockups_dir}/mockup_cronjob_workflow.png', dpi=150, bbox_inches='tight', facecolor='#f8f9fa')
plt.close()
print("✓ Cronjob Workflow mockup created")

# 5. Hermes Logo
fig, ax = plt.subplots(figsize=(9, 9))
ax.set_xlim(0, 9)
ax.set_ylim(0, 9)
ax.axis('off')
fig.patch.set_facecolor('white')

# Background circle
bg_circle = plt.Circle((4.5, 4.5), 3.5, facecolor='#667eea', alpha=0.1, zorder=1)
ax.add_patch(bg_circle)

# Stylized "H" with circuit elements
# Left vertical bar
left_bar = patches.Rectangle((2.5, 2), 0.8, 5, facecolor='#667eea', zorder=2)
ax.add_patch(left_bar)

# Right vertical bar
right_bar = patches.Rectangle((5.7, 2), 0.8, 5, facecolor='#667eea', zorder=2)
ax.add_patch(right_bar)

# Horizontal connector
connector = patches.Rectangle((3.3, 4), 2.4, 0.8, facecolor='#764ba2', zorder=2)
ax.add_patch(connector)

# Circuit nodes
nodes = [(2.9, 7), (2.9, 2), (6.1, 7), (6.1, 2), (4.5, 4.4)]
for x, y in nodes:
    node = plt.Circle((x, y), 0.15, facecolor='#f39c12', edgecolor='white', linewidth=2, zorder=3)
    ax.add_patch(node)

# Connection lines
lines = [((2.9, 7), (4.5, 4.4)), ((6.1, 7), (4.5, 4.4)), ((2.9, 2), (4.5, 4.4)), ((6.1, 2), (4.5, 4.4))]
for (x1, y1), (x2, y2) in lines:
    ax.plot([x1, x2], [y1, y2], color='#f39c12', linewidth=1.5, alpha=0.6, zorder=2)

# Wing symbol (simplified)
wing_left = patches.Polygon([[1.5, 5], [2, 5.5], [2, 4.5]], closed=True, facecolor='#667eea', alpha=0.7, zorder=2)
ax.add_patch(wing_left)
wing_right = patches.Polygon([[7.5, 5], [7, 5.5], [7, 4.5]], closed=True, facecolor='#667eea', alpha=0.7, zorder=2)
ax.add_patch(wing_right)

# Text
ax.text(4.5, 1, 'Hermes Agent', ha='center', va='center', fontsize=16, fontweight='bold', color='#2c3e50')

plt.tight_layout()
plt.savefig(f'{mockups_dir}/mockup_hermes_logo.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("✓ Hermes Logo mockup created")

print("\n✅ All 5 mockups created successfully!")
