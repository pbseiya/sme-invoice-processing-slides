
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.font_manager as fm
import numpy as np

mockups_dir = '/home/seiya/projects/training_course/private-course/courses/sme-invoice-processing-demo/slides/mockups'

plt.rcParams['font.family'] = 'DejaVu Sans'

# ===== 1. Web App Upload (Fixed) =====
fig, ax = plt.subplots(figsize=(16, 9))
ax.set_xlim(0, 16)
ax.set_ylim(0, 9)
ax.axis('off')
fig.patch.set_facecolor('#ecf0f1')

header = patches.Rectangle((0, 8), 16, 0.8, facecolor='#2c3e50', zorder=1)
ax.add_patch(header)
ax.text(8, 8.4, 'Invoice Processing System', ha='center', va='center', fontsize=18, fontweight='bold', color='white', zorder=2)

upload_box = patches.Rectangle((3, 4), 10, 3.5, linewidth=2, edgecolor='#3498db', linestyle='--', 
                                facecolor='#ebf5fb', alpha=0.5, zorder=1)
ax.add_patch(upload_box)
ax.text(8, 6.5, '[ UPLOAD ]', fontsize=36, ha='center', va='center', fontweight='bold', color='#3498db', zorder=2)
ax.text(8, 5.5, 'Drop invoice here or click to upload', ha='center', va='center', fontsize=14, color='#2c3e50', zorder=2)
ax.text(8, 4.8, 'PDF, PNG, JPG (max 10MB)', ha='center', va='center', fontsize=10, color='#7f8c8d', zorder=2)

ax.text(8, 3.5, 'Recent Processing', ha='center', va='center', fontsize=14, fontweight='bold', color='#2c3e50')

invoices = [
    ('INV-001', '2026-09-18', '15,000', 'SUCCESS'),
    ('INV-002', '2026-09-17', '23,500', 'SUCCESS'),
    ('INV-003', '2026-09-16', '8,200', 'PROCESSING')
]

for i, (inv, date, amount, status) in enumerate(invoices):
    y = 3 - i * 0.5
    row = patches.Rectangle((2, y-0.2), 12, 0.4, facecolor='white', edgecolor='#bdc3c7', linewidth=0.5, zorder=1)
    ax.add_patch(row)
    ax.text(3, y, inv, fontsize=9, color='#2c3e50', zorder=2)
    ax.text(5.5, y, date, fontsize=9, color='#7f8c8d', zorder=2)
    ax.text(9, y, amount, fontsize=9, fontweight='bold', color='#2c3e50', ha='center', zorder=2)
    status_color = '#27ae60' if status == 'SUCCESS' else '#f39c12'
    ax.text(12, y, status, fontsize=9, color=status_color, ha='center', zorder=2)

plt.tight_layout()
plt.savefig(f'{mockups_dir}/mockup_web_app_upload.png', dpi=150, bbox_inches='tight', facecolor='#ecf0f1')
plt.close()
print("Fixed Web App Upload mockup")

# ===== 2. Phone Camera (Fixed) =====
fig, ax = plt.subplots(figsize=(16, 9))
ax.set_xlim(0, 16)
ax.set_ylim(0, 9)
ax.axis('off')
fig.patch.set_facecolor('#f8f9fa')

desk = patches.Rectangle((0, 0), 16, 3, facecolor='#d4a574', alpha=0.3, zorder=1)
ax.add_patch(desk)

invoice_bg = patches.Rectangle((4, 1), 8, 6, facecolor='white', edgecolor='#bdc3c7', linewidth=2, zorder=2)
ax.add_patch(invoice_bg)
ax.text(8, 6.5, 'INVOICE', ha='center', va='center', fontsize=20, fontweight='bold', color='#2c3e50', zorder=3)

details = [
    'Invoice No: INV-2026-001',
    'Date: 18 September 2026',
    'Customer: ABC Co., Ltd.',
    '',
    'Items:',
    '  1. Consulting Service    50,000',
    '  2. Design Service        30,000',
    '  3. Development          120,000',
    '',
    'Total:                    200,000'
]

for i, text in enumerate(details):
    ax.text(4.5, 5.5 - i*0.4, text, fontsize=8, color='#2c3e50', family='monospace', zorder=3)

phone = patches.FancyBboxPatch((10, 2), 4, 6, boxstyle="round,pad=0.2", facecolor='#34495e', 
                                edgecolor='#2c3e50', linewidth=3, zorder=4)
ax.add_patch(phone)

screen = patches.Rectangle((10.3, 2.5), 3.4, 5, facecolor='#000000', zorder=5)
ax.add_patch(screen)

viewfinder = patches.Rectangle((10.5, 3), 3, 4, facecolor='#1a1a2e', edgecolor='#00ff00', 
                                linewidth=1, zorder=6)
ax.add_patch(viewfinder)

corners = [(10.5, 6.8), (13.5, 6.8), (10.5, 3), (13.5, 3)]
for x, y in corners:
    ax.plot([x, x+0.3], [y, y], color='#00ff00', linewidth=2, zorder=7)
    ax.plot([x, x], [y, y+0.3], color='#00ff00', linewidth=2, zorder=7)

ax.text(12, 5, '[CAM]', fontsize=16, ha='center', va='center', fontweight='bold', color='#00ff00', zorder=7)

capture_btn = plt.Circle((12, 3.5), 0.3, facecolor='white', edgecolor='#00ff00', linewidth=2, zorder=7)
ax.add_patch(capture_btn)

ax.text(8, 8.5, 'Capture Invoice Clearly & Straight', ha='center', va='center', 
        fontsize=16, fontweight='bold', color='#27ae60', zorder=8)
ax.text(8, 0.3, 'Tips: Good lighting, hold camera straight, capture full invoice', 
        ha='center', va='center', fontsize=11, color='#7f8c8d', zorder=8)

plt.tight_layout()
plt.savefig(f'{mockups_dir}/mockup_phone_camera.png', dpi=150, bbox_inches='tight', facecolor='#f8f9fa')
plt.close()
print("Fixed Phone Camera mockup")

# ===== 3. Cronjob Workflow (Fixed) =====
fig, ax = plt.subplots(figsize=(16, 9))
ax.set_xlim(0, 16)
ax.set_ylim(0, 9)
ax.axis('off')
fig.patch.set_facecolor('#f8f9fa')

ax.text(8, 8.5, 'Automated Invoice Processing Workflow', ha='center', va='center', 
        fontsize=20, fontweight='bold', color='#2c3e50')

steps = [
    ('MON\n9:00', '#9b59b6'),
    ('COLLECT\nInvoice', '#3498db'),
    ('AI\nProcess', '#e74c3c'),
    ('SAVE\nDatabase', '#2ecc71'),
    ('CREATE\nReport', '#f39c12'),
    ('SEND\nLINE', '#1abc9c')
]

for i, (label, color) in enumerate(steps):
    x = 1.5 + i * 2.5
    
    circle = plt.Circle((x, 5), 0.8, facecolor=color, edgecolor='white', linewidth=3, zorder=2)
    ax.add_patch(circle)
    
    ax.text(x, 5, f'[{i+1}]', ha='center', va='center', fontsize=12, fontweight='bold', color='white', zorder=3)
    
    ax.text(x, 3.8, label, ha='center', va='center', fontsize=10, fontweight='bold', color='#2c3e50')
    
    if i < len(steps) - 1:
        ax.annotate('', xy=(x + 1.2, 5), xytext=(x + 0.8, 5),
                   arrowprops=dict(arrowstyle='->', lw=2, color='#95a5a6'))

ax.text(8, 2.8, 'Benefits', ha='center', va='center', 
        fontsize=14, fontweight='bold', color='#2c3e50')

benefits = [
    ('Save Time', 'No manual weekly work'),
    ('Accurate', 'AI reads automatically'),
    ('Trackable', 'Weekly reports sent')
]

for i, (title, desc) in enumerate(benefits):
    x = 2.5 + i * 4
    y = 1.8
    
    card = patches.Rectangle((x-1.5, y-0.8), 3, 1.3, facecolor='white', edgecolor='#bdc3c7', 
                             linewidth=1, zorder=1)
    ax.add_patch(card)
    
    ax.text(x, y+0.2, f'[{i+1}]', ha='center', va='center', fontsize=20, fontweight='bold', color='#3498db', zorder=2)
    ax.text(x, y-0.1, title, ha='center', va='center', fontsize=10, fontweight='bold', color='#2c3e50', zorder=2)
    ax.text(x, y-0.4, desc, ha='center', va='center', fontsize=8, color='#7f8c8d', zorder=2)

plt.tight_layout()
plt.savefig(f'{mockups_dir}/mockup_cronjob_workflow.png', dpi=150, bbox_inches='tight', facecolor='#f8f9fa')
plt.close()
print("Fixed Cronjob Workflow mockup")

# ===== 4. Landing Page (Fixed) =====
fig, ax = plt.subplots(figsize=(16, 9))
ax.set_xlim(0, 16)
ax.set_ylim(0, 9)
ax.axis('off')
fig.patch.set_facecolor('#ffffff')

navbar = patches.Rectangle((0, 8.2), 16, 0.6, facecolor='#2c3e50', zorder=1)
ax.add_patch(navbar)
ax.text(8, 8.5, 'Restaurant Delicious', ha='center', va='center', fontsize=16, fontweight='bold', color='white', zorder=2)
ax.text(1, 8.5, 'HOME', fontsize=14, color='white', zorder=2)
ax.text(15, 8.5, 'MENU', fontsize=14, color='white', ha='right', zorder=2)

hero = patches.Rectangle((0, 5), 16, 3.2, facecolor='#ff6b6b', alpha=0.9, zorder=1)
ax.add_patch(hero)
ax.text(8, 7, 'Welcome to\nRestaurant Delicious', ha='center', va='center', fontsize=28, fontweight='bold', color='white', zorder=2)
ax.text(8, 5.5, 'Authentic Thai cuisine since 2007', ha='center', va='center', fontsize=14, color='white', zorder=2)

menu_btn = patches.FancyBboxPatch((6.5, 5.8), 3, 0.5, boxstyle="round,pad=0.1", facecolor='white', edgecolor='white', zorder=2)
ax.add_patch(menu_btn)
ax.text(8, 6.05, 'View Menu', ha='center', va='center', fontsize=12, fontweight='bold', color='#ff6b6b', zorder=3)

ax.text(8, 4.5, 'Popular Dishes', ha='center', va='center', fontsize=20, fontweight='bold', color='#2c3e50')

food_items = [
    ('Pad Thai', '120', '#ffa502'),
    ('Tom Yum', '280', '#ff6348'),
    ('Green Curry', '180', '#2ed573'),
    ('Crab Rice', '150', '#1e90ff')
]

for i, (name, price, color) in enumerate(food_items):
    x = 2 + i * 3.5
    card = patches.Rectangle((x-1.2, 2.5), 2.4, 1.5, facecolor='#f8f9fa', edgecolor='#dcdde1', linewidth=1, zorder=1)
    ax.add_patch(card)
    
    food_circle = plt.Circle((x, 3.5), 0.4, facecolor=color, alpha=0.7, zorder=2)
    ax.add_patch(food_circle)
    
    ax.text(x, 2.9, name, ha='center', va='center', fontsize=10, fontweight='bold', color='#2c3e50', zorder=2)
    ax.text(x, 2.7, price, ha='center', va='center', fontsize=9, color='#e74c3c', zorder=2)

contact = patches.Rectangle((0, 0), 16, 2.2, facecolor='#34495e', zorder=1)
ax.add_patch(contact)
ax.text(8, 1.5, '123 Sukhumvit Road, Bangkok 10110  |  Tel: 02-123-4567', ha='center', va='center', fontsize=11, color='white', zorder=2)
ax.text(8, 0.8, 'Open daily 10:00-22:00', ha='center', va='center', fontsize=10, color='#bdc3c7', zorder=2)

plt.tight_layout()
plt.savefig(f'{mockups_dir}/mockup_landing_page.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("Fixed Landing Page mockup")

print("\nAll mockups fixed!")
