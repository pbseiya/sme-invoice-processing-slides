
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.font_manager as fm
import numpy as np

# Set font to support Thai
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(16, 9))
ax.set_xlim(0, 16)
ax.set_ylim(0, 9)
ax.axis('off')
fig.patch.set_facecolor('#f8f9fa')

# Header
header = patches.Rectangle((0, 8), 16, 0.8, facecolor='#34495e', zorder=1)
ax.add_patch(header)
ax.text(8, 8.4, 'Invoice Dashboard', ha='center', va='center', 
        fontsize=18, fontweight='bold', color='white', zorder=2)

# Stats cards
stats = [
    ('Total Invoices', '147', '#3498db'),
    ('Monthly Total', '245,000', '#2ecc71'),
    ('Processing Time', '2.3 sec', '#e74c3c'),
    ('Accuracy', '95%+', '#f39c12')
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
ax.text(4, 6, 'Monthly Invoice Volume', ha='center', va='center', fontsize=11, 
        fontweight='bold', color='#2c3e50')
chart_bg = patches.Rectangle((0.5, 3.5), 7, 2.3, facecolor='white', edgecolor='#bdc3c7', 
                              linewidth=1, zorder=1)
ax.add_patch(chart_bg)

months = ['Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']
values = [120, 150, 180, 210, 230, 245]
for i in range(len(months)-1):
    x1 = 1 + i * 1.1
    x2 = 1 + (i+1) * 1.1
    y1 = 3.7 + values[i] / 245 * 1.8
    y2 = 3.7 + values[i+1] / 245 * 1.8
    ax.plot([x1, x2], [y1, y2], color='#3498db', linewidth=2, zorder=3)
    ax.plot(x1, y1, 'o', color='#3498db', markersize=5, zorder=4)
    ax.text(x1, 3.6, months[i], ha='center', va='center', fontsize=7, color='#7f8c8d', zorder=2)

# Pie chart (actual visualization)
ax.text(12, 6, 'Category Breakdown', ha='center', va='center', fontsize=11, 
        fontweight='bold', color='#2c3e50')

pie_bg = patches.Rectangle((8.5, 3.5), 7, 2.3, facecolor='white', edgecolor='#bdc3c7', 
                            linewidth=1, zorder=1)
ax.add_patch(pie_bg)

# Draw actual pie chart
pie_ax = fig.add_axes([0.65, 0.42, 0.2, 0.2])
categories = ['Food', 'Equipment', 'Services']
percentages = [45, 30, 25]
colors = ['#e74c3c', '#3498db', '#2ecc71']
wedges, texts, autotexts = pie_ax.pie(percentages, labels=categories, autopct='%1.0f%%',
                                       colors=colors, startangle=90, textprops={'fontsize': 8})
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')

# Recent invoices table
ax.text(8, 3, 'Recent Invoices', ha='center', va='center', fontsize=11, 
        fontweight='bold', color='#2c3e50')

table_bg = patches.Rectangle((0.5, 0.5), 15, 2.3, facecolor='white', edgecolor='#bdc3c7', 
                              linewidth=1, zorder=1)
ax.add_patch(table_bg)

# Table header
table_header = patches.Rectangle((0.5, 2.4), 15, 0.4, facecolor='#34495e', zorder=2)
ax.add_patch(table_header)
ax.text(1.5, 2.6, 'Invoice', fontsize=9, fontweight='bold', color='white', zorder=3)
ax.text(4, 2.6, 'Date', fontsize=9, fontweight='bold', color='white', zorder=3)
ax.text(7, 2.6, 'Category', fontsize=9, fontweight='bold', color='white', ha='center', zorder=3)
ax.text(10.5, 2.6, 'Amount', fontsize=9, fontweight='bold', color='white', ha='center', zorder=3)
ax.text(14, 2.6, 'Status', fontsize=9, fontweight='bold', color='white', ha='center', zorder=3)

# Table rows
rows = [
    ('INV-001', 'Sep 18', 'Food', '15,000', 'OK'),
    ('INV-002', 'Sep 17', 'Equipment', '23,500', 'OK'),
    ('INV-003', 'Sep 16', 'Services', '8,200', 'Pending'),
    ('INV-004', 'Sep 15', 'Food', '12,800', 'OK')
]

for i, (inv, date, cat, amount, status) in enumerate(rows):
    y = 2.1 - i * 0.4
    ax.text(1.5, y, inv, fontsize=8, color='#2c3e50', zorder=2)
    ax.text(4, y, date, fontsize=8, color='#7f8c8d', zorder=2)
    ax.text(7, y, cat, fontsize=8, color='#2c3e50', ha='center', zorder=2)
    ax.text(10.5, y, amount, fontsize=8, fontweight='bold', color='#2c3e50', ha='center', zorder=2)
    status_color = '#27ae60' if status == 'OK' else '#f39c12'
    ax.text(14, y, status, fontsize=8, ha='center', color=status_color, zorder=2)

plt.savefig('mockup_dashboard.png', dpi=150, bbox_inches='tight', facecolor='#f8f9fa')
plt.close()
print("Fixed Dashboard mockup created")
