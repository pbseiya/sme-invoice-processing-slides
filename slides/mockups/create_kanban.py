
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image, ImageDraw, ImageFont
import numpy as np

# Create figure
fig, ax = plt.subplots(figsize=(16, 9))
ax.set_xlim(0, 16)
ax.set_ylim(0, 9)
ax.axis('off')
fig.patch.set_facecolor('#f8f9fa')

# Title
ax.text(8, 8.5, 'Kanban Board', ha='center', va='top', fontsize=24, fontweight='bold', color='#2c3e50')

# Columns
columns = [
    ('To Do', '#e3f2fd', 2),
    ('In Progress', '#fff3e0', 8),
    ('Done', '#e8f5e9', 14)
]

for title, color, x in columns:
    # Column background
    rect = patches.Rectangle((x-2.5, 1), 5, 6.5, linewidth=2, edgecolor='#bdc3c7', 
                              facecolor=color, alpha=0.7, zorder=1)
    ax.add_patch(rect)
    
    # Column title
    ax.text(x, 7.2, title, ha='center', va='top', fontsize=16, fontweight='bold', color='#34495e', zorder=2)

# Cards in To Do
todo_cards = [
    'Research\nCompetitors',
    'Design\nWireframes',
    'Write\nDocumentation'
]
for i, card in enumerate(todo_cards):
    y = 6.5 - i * 1.8
    card_rect = patches.Rectangle((0.5, y-1), 3, 1.2, linewidth=1, edgecolor='#95a5a6', 
                                   facecolor='white', zorder=2)
    ax.add_patch(card_rect)
    ax.text(2, y-0.4, card, ha='center', va='center', fontsize=10, color='#2c3e50', zorder=3)

# Cards in In Progress
progress_cards = [
    'Frontend\nDevelopment',
    'API\nIntegration'
]
for i, card in enumerate(progress_cards):
    y = 6.5 - i * 1.8
    card_rect = patches.Rectangle((6.5, y-1), 3, 1.2, linewidth=1, edgecolor='#e67e22', 
                                   facecolor='white', zorder=2)
    ax.add_patch(card_rect)
    ax.text(8, y-0.4, card, ha='center', va='center', fontsize=10, color='#2c3e50', zorder=3)

# Cards in Done
done_cards = [
    'Project\nSetup ✓',
    'Database\nSchema ✓'
]
for i, card in enumerate(done_cards):
    y = 6.5 - i * 1.8
    card_rect = patches.Rectangle((12.5, y-1), 3, 1.2, linewidth=1, edgecolor='#27ae60', 
                                   facecolor='white', zorder=2)
    ax.add_patch(card_rect)
    ax.text(14, y-0.4, card, ha='center', va='center', fontsize=10, color='#2c3e50', zorder=3)

plt.tight_layout()
plt.savefig('mockup_kanban_board.png', dpi=150, bbox_inches='tight', facecolor='#f8f9fa')
print("Kanban board mockup created successfully")
