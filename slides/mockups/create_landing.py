
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(16, 9))
ax.set_xlim(0, 16)
ax.set_ylim(0, 9)
ax.axis('off')
fig.patch.set_facecolor('#ffffff')

# Navbar
navbar = patches.Rectangle((0, 8.2), 16, 0.6, facecolor='#2c3e50', zorder=1)
ax.add_patch(navbar)
ax.text(8, 8.5, 'ร้านอาหารอร่อย', ha='center', va='center', fontsize=16, fontweight='bold', color='white', zorder=2)
ax.text(1, 8.5, '🏠', fontsize=14, color='white', zorder=2)
ax.text(15, 8.5, '☰', fontsize=14, color='white', ha='right', zorder=2)

# Hero section
hero = patches.Rectangle((0, 5), 16, 3.2, facecolor='#ff6b6b', alpha=0.9, zorder=1)
ax.add_patch(hero)
ax.text(8, 7, 'ยินดีต้อนรับสู่\nร้านอาหารอร่อย', ha='center', va='center', fontsize=28, fontweight='bold', color='white', zorder=2)
ax.text(8, 5.5, 'อาหารไทยแท้รสชาติดั้งเดิม ตั้งแต่ปี 2550', ha='center', va='center', fontsize=14, color='white', zorder=2)

# Menu button
menu_btn = patches.FancyBboxPatch((6.5, 5.8), 3, 0.5, boxstyle="round,pad=0.1", facecolor='white', edgecolor='white', zorder=2)
ax.add_patch(menu_btn)
ax.text(8, 6.05, 'ดูเมนู', ha='center', va='center', fontsize=12, fontweight='bold', color='#ff6b6b', zorder=3)

# Food items section
ax.text(8, 4.5, 'เมนูยอดนิยม', ha='center', va='center', fontsize=20, fontweight='bold', color='#2c3e50')

# Food cards
food_items = [
    ('ผัดไทย', '฿120', '#ffa502'),
    ('ต้มยำกุ้ง', '฿280', '#ff6348'),
    ('แกงเขียวหวาน', '฿180', '#2ed573'),
    ('ข้าวผัดปู', '฿150', '#1e90ff')
]

for i, (name, price, color) in enumerate(food_items):
    x = 2 + i * 3.5
    # Card background
    card = patches.Rectangle((x-1.2, 2.5), 2.4, 1.5, facecolor='#f8f9fa', edgecolor='#dcdde1', linewidth=1, zorder=1)
    ax.add_patch(card)
    
    # Food circle (representing image)
    food_circle = plt.Circle((x, 3.5), 0.4, facecolor=color, alpha=0.7, zorder=2)
    ax.add_patch(food_circle)
    
    # Food name
    ax.text(x, 2.9, name, ha='center', va='center', fontsize=10, fontweight='bold', color='#2c3e50', zorder=2)
    ax.text(x, 2.7, price, ha='center', va='center', fontsize=9, color='#e74c3c', zorder=2)

# Contact section
contact = patches.Rectangle((0, 0), 16, 2.2, facecolor='#34495e', zorder=1)
ax.add_patch(contact)
ax.text(8, 1.5, '📍 123 ถนนสุขุมวิท กรุงเทพฯ 10110  |  ☎ 02-123-4567', ha='center', va='center', fontsize=11, color='white', zorder=2)
ax.text(8, 0.8, 'เปิดทุกวัน 10:00-22:00 น.', ha='center', va='center', fontsize=10, color='#bdc3c7', zorder=2)

plt.tight_layout()
plt.savefig('mockup_landing_page.png', dpi=150, bbox_inches='tight', facecolor='white')
print("Landing page mockup created")
