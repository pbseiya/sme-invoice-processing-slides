#!/usr/bin/env python3
"""
สร้างตัวอย่าง Invoice ใหม่ด้วย WeasyPrint (ฉบับแก้ไข - พอดีหน้า A4)
- ใช้ HTML/CSS สำหรับ layout ที่ถูกต้อง
- รองรับ font ไทยหลายแบบ
- ปรับขนาดให้พอดีหน้า A4 (1 หน้า)
"""

from weasyprint import HTML
from pathlib import Path
from datetime import datetime
import os

# โฟลเดอร์ output
invoices_dir = Path('/home/seiya/projects/training_course/private-course/courses/sme-invoice-processing-demo/invoices')
invoices_dir.mkdir(exist_ok=True)

# CSS สำหรับ invoice (ปรับให้พอดี A4)
base_css = """
@page {
    size: A4;
    margin: 1.5cm;
}

body {
    font-family: 'Sarabun', 'Noto Sans Thai', sans-serif;
    font-size: 10pt;
    line-height: 1.4;
    color: #333;
}

.header {
    display: flex;
    justify-content: space-between;
    align-items: start;
    margin-bottom: 15px;
    border-bottom: 2px solid #2c5aa0;
    padding-bottom: 10px;
}

.company-info {
    flex: 1;
}

.company-name {
    font-size: 18pt;
    font-weight: bold;
    color: #2c5aa0;
    margin-bottom: 5px;
}

.company-info div {
    font-size: 9pt;
    margin: 2px 0;
}

.invoice-title {
    font-size: 22pt;
    font-weight: bold;
    text-align: right;
    color: #2c5aa0;
}

.invoice-meta {
    text-align: right;
    margin-top: 5px;
    font-size: 9pt;
}

.meta-row {
    margin: 3px 0;
}

.bill-to {
    background: #f5f5f5;
    padding: 10px 15px;
    border-radius: 5px;
    margin-bottom: 15px;
}

.bill-to-title {
    font-weight: bold;
    font-size: 10pt;
    margin-bottom: 5px;
    color: #2c5aa0;
}

.bill-to div {
    font-size: 9pt;
    margin: 2px 0;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 15px;
}

thead {
    background: #2c5aa0;
    color: white;
}

th {
    padding: 6px 8px;
    text-align: left;
    font-weight: bold;
    font-size: 9pt;
}

td {
    padding: 5px 8px;
    border-bottom: 1px solid #ddd;
    font-size: 9pt;
}

.text-right {
    text-align: right;
}

.text-center {
    text-align: center;
}

.totals {
    margin-left: auto;
    width: 250px;
    font-size: 9pt;
}

.total-row {
    display: flex;
    justify-content: space-between;
    padding: 4px 0;
}

.total-row.grand-total {
    font-size: 11pt;
    font-weight: bold;
    border-top: 2px solid #2c5aa0;
    margin-top: 5px;
    padding-top: 8px;
}

.payment-info {
    margin-top: 20px;
    padding: 10px 15px;
    background: #f9f9f9;
    border-radius: 5px;
    font-size: 8pt;
}

.payment-info strong {
    font-size: 9pt;
}

.footer {
    margin-top: 20px;
    text-align: center;
    font-size: 8pt;
    color: #666;
}
"""

def create_invoice_1():
    """Invoice ภาษาอังกฤษ - IT Services"""
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
        {base_css}
        </style>
    </head>
    <body>
        <div class="header">
            <div class="company-info">
                <div class="company-name">Tech Solutions Co., Ltd.</div>
                <div>123 Business Street, Bangkok 10110</div>
                <div>Tel: +66 2-123-4567 | Email: billing@techsolutions.com</div>
                <div>Tax ID: 0123456789012</div>
            </div>
            <div>
                <div class="invoice-title">INVOICE</div>
                <div class="invoice-meta">
                    <div class="meta-row"><strong>Invoice No:</strong> INV-2026-0901</div>
                    <div class="meta-row"><strong>Date:</strong> September 1, 2026</div>
                    <div class="meta-row"><strong>Due Date:</strong> Net 30</div>
                </div>
            </div>
        </div>
        
        <div class="bill-to">
            <div class="bill-to-title">BILL TO:</div>
            <div><strong>ABC Manufacturing PCL</strong></div>
            <div>456 Industrial Road, Chonburi 20130, Thailand</div>
            <div>Tax ID: 0987654321098</div>
        </div>
        
        <table>
            <thead>
                <tr>
                    <th style="width: 40px;">No.</th>
                    <th>Description</th>
                    <th style="width: 50px;" class="text-center">Qty</th>
                    <th style="width: 90px;" class="text-right">Unit Price</th>
                    <th style="width: 90px;" class="text-right">Amount</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td class="text-center">1</td>
                    <td>Website Development - E-commerce Platform</td>
                    <td class="text-center">1</td>
                    <td class="text-right">85,000.00</td>
                    <td class="text-right">85,000.00</td>
                </tr>
                <tr>
                    <td class="text-center">2</td>
                    <td>Mobile App Development (iOS)</td>
                    <td class="text-center">1</td>
                    <td class="text-right">120,000.00</td>
                    <td class="text-right">120,000.00</td>
                </tr>
                <tr>
                    <td class="text-center">3</td>
                    <td>Mobile App Development (Android)</td>
                    <td class="text-center">1</td>
                    <td class="text-right">120,000.00</td>
                    <td class="text-right">120,000.00</td>
                </tr>
                <tr>
                    <td class="text-center">4</td>
                    <td>Monthly Maintenance (September)</td>
                    <td class="text-center">1</td>
                    <td class="text-right">15,000.00</td>
                    <td class="text-right">15,000.00</td>
                </tr>
                <tr>
                    <td class="text-center">5</td>
                    <td>Cloud Hosting Setup (AWS)</td>
                    <td class="text-center">1</td>
                    <td class="text-right">25,000.00</td>
                    <td class="text-right">25,000.00</td>
                </tr>
            </tbody>
        </table>
        
        <div class="totals">
            <div class="total-row">
                <span>Subtotal:</span>
                <span>฿365,000.00</span>
            </div>
            <div class="total-row">
                <span>VAT (7%):</span>
                <span>฿25,550.00</span>
            </div>
            <div class="total-row grand-total">
                <span>Grand Total:</span>
                <span>฿390,550.00</span>
            </div>
        </div>
        
        <div class="payment-info">
            <strong>Payment Terms:</strong> Net 30 days<br>
            <strong>Bank:</strong> Bangkok Bank | <strong>Account:</strong> 123-4-56789-0<br>
            <strong>Account Name:</strong> Tech Solutions Co., Ltd.
        </div>
        
        <div class="footer">
            Thank you for your business!
        </div>
    </body>
    </html>
    """
    
    # สร้าง PDF
    pdf_path = invoices_dir / 'invoice_001_en.pdf'
    HTML(string=html_content).write_pdf(str(pdf_path))
    print(f'✅ Created: {pdf_path.name}')
    
    # สร้าง PNG จาก PDF
    from pdf2image import convert_from_path
    png_path = invoices_dir / 'invoice_001_en.png'
    images = convert_from_path(str(pdf_path), dpi=150)
    if images:
        images[0].save(str(png_path), 'PNG')
        print(f'✅ Created: {png_path.name}')


def create_invoice_2():
    """Invoice ภาษาไทย - Office Supplies"""
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
        {base_css}
        .company-name {{ color: #2d7a2d; }}
        .invoice-title {{ color: #2d7a2d; }}
        thead {{ background: #2d7a2d; }}
        .total-row.grand-total {{ border-top-color: #2d7a2d; }}
        .bill-to-title {{ color: #2d7a2d; }}
        .bill-to {{ background: #f0f8f0; }}
        </style>
    </head>
    <body>
        <div class="header">
            <div class="company-info">
                <div class="company-name">สำนักงานสมบุญ จำกัด</div>
                <div>123 ถนนธุรกิจ กรุงเทพฯ 10110</div>
                <div>โทร: 02-123-4567 | อีเมล: billing@somboon.com</div>
                <div>เลขประจำตัวผู้เสียภาษี: 0123456789012</div>
            </div>
            <div>
                <div class="invoice-title">ใบกำกับภาษี</div>
                <div class="invoice-meta">
                    <div class="meta-row"><strong>เลขที่:</strong> TX-2026-0905</div>
                    <div class="meta-row"><strong>วันที่:</strong> 5 กันยายน 2569</div>
                    <div class="meta-row"><strong>กำหนดชำระ:</strong> 30 วัน</div>
                </div>
            </div>
        </div>
        
        <div class="bill-to">
            <div class="bill-to-title">ลูกค้า / BILL TO:</div>
            <div><strong>บริษัท เจริญกิจ จำกัด</strong></div>
            <div>789 ถนนสุขุมวิท กรุงเทพฯ 10110</div>
            <div>เลขประจำตัวผู้เสียภาษี: 0123456789012</div>
        </div>
        
        <table>
            <thead>
                <tr>
                    <th style="width: 40px;">ลำดับ</th>
                    <th>รายละเอียด</th>
                    <th style="width: 50px;" class="text-center">จำนวน</th>
                    <th style="width: 80px;" class="text-right">ราคา/หน่วย</th>
                    <th style="width: 80px;" class="text-right">จำนวนเงิน</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td class="text-center">1</td>
                    <td>กระดาษ A4 (80 แกรม) 5 รีม</td>
                    <td class="text-center">10</td>
                    <td class="text-right">450.00</td>
                    <td class="text-right">4,500.00</td>
                </tr>
                <tr>
                    <td class="text-center">2</td>
                    <td>หมึกพิมพ์ LaserJet สีดำ</td>
                    <td class="text-center">5</td>
                    <td class="text-right">1,200.00</td>
                    <td class="text-right">6,000.00</td>
                </tr>
                <tr>
                    <td class="text-center">3</td>
                    <td>หมึกพิมพ์ LaserJet สี</td>
                    <td class="text-center">3</td>
                    <td class="text-right">1,800.00</td>
                    <td class="text-right">5,400.00</td>
                </tr>
                <tr>
                    <td class="text-center">4</td>
                    <td>แฟ้มเอกสาร A4</td>
                    <td class="text-center">20</td>
                    <td class="text-right">85.00</td>
                    <td class="text-right">1,700.00</td>
                </tr>
                <tr>
                    <td class="text-center">5</td>
                    <td>ปากกาลูกลื่น (กล่อง 12 ด้าม)</td>
                    <td class="text-center">5</td>
                    <td class="text-right">180.00</td>
                    <td class="text-right">900.00</td>
                </tr>
                <tr>
                    <td class="text-center">6</td>
                    <td>เครื่องคิดเลข Casio</td>
                    <td class="text-center">2</td>
                    <td class="text-right">650.00</td>
                    <td class="text-right">1,300.00</td>
                </tr>
            </tbody>
        </table>
        
        <div class="totals">
            <div class="total-row">
                <span>รวมเงิน:</span>
                <span>฿19,800.00</span>
            </div>
            <div class="total-row">
                <span>ภาษีมูลค่าเพิ่ม 7%:</span>
                <span>฿1,386.00</span>
            </div>
            <div class="total-row grand-total">
                <span>ยอดรวมทั้งหมด:</span>
                <span>฿21,186.00</span>
            </div>
        </div>
        
        <div class="payment-info">
            <strong>เงื่อนไขการชำระเงิน:</strong> 30 วัน<br>
            <strong>ธนาคาร:</strong> ธนาคารกรุงเทพ | <strong>เลขที่บัญชี:</strong> 123-4-56789-0<br>
            <strong>ชื่อบัญชี:</strong> สำนักงานสมบุญ จำกัด
        </div>
        
        <div class="footer">
            ขอบคุณที่ใช้บริการ
        </div>
    </body>
    </html>
    """
    
    pdf_path = invoices_dir / 'invoice_002_th.pdf'
    HTML(string=html_content).write_pdf(str(pdf_path))
    print(f'✅ Created: {pdf_path.name}')
    
    from pdf2image import convert_from_path
    png_path = invoices_dir / 'invoice_002_th.png'
    images = convert_from_path(str(pdf_path), dpi=150)
    if images:
        images[0].save(str(png_path), 'PNG')
        print(f'✅ Created: {png_path.name}')


def create_invoice_3():
    """Invoice ภาษาอังกฤษ - Consulting Services"""
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
        {base_css}
        .company-name {{ color: #1a3a52; }}
        .invoice-title {{ color: #1a3a52; }}
        thead {{ background: #1a3a52; }}
        .total-row.grand-total {{ border-top-color: #1a3a52; }}
        .bill-to-title {{ color: #1a3a52; }}
        </style>
    </head>
    <body>
        <div class="header">
            <div class="company-info">
                <div class="company-name">Professional Consulting Group</div>
                <div>321 Silom Road, Bangkok 10500</div>
                <div>Tel: +66 2-987-6543 | Email: info@consulting.com</div>
                <div>Tax ID: 0567890123456</div>
            </div>
            <div>
                <div class="invoice-title">INVOICE</div>
                <div class="invoice-meta">
                    <div class="meta-row"><strong>Invoice No:</strong> INV-2026-0910</div>
                    <div class="meta-row"><strong>Date:</strong> September 10, 2026</div>
                    <div class="meta-row"><strong>Due Date:</strong> Net 30</div>
                </div>
            </div>
        </div>
        
        <div class="bill-to">
            <div class="bill-to-title">BILL TO:</div>
            <div><strong>Global Trading Co., Ltd.</strong></div>
            <div>321 Silom Road, Bangkok 10500, Thailand</div>
            <div>Tax ID: 0567890123456</div>
        </div>
        
        <table>
            <thead>
                <tr>
                    <th style="width: 40px;">No.</th>
                    <th>Description</th>
                    <th style="width: 50px;" class="text-center">Hours</th>
                    <th style="width: 90px;" class="text-right">Rate/Hour</th>
                    <th style="width: 90px;" class="text-right">Amount</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td class="text-center">1</td>
                    <td>Business Strategy Consulting</td>
                    <td class="text-center">40</td>
                    <td class="text-right">2,500.00</td>
                    <td class="text-right">100,000.00</td>
                </tr>
                <tr>
                    <td class="text-center">2</td>
                    <td>Market Research & Analysis</td>
                    <td class="text-center">1</td>
                    <td class="text-right">45,000.00</td>
                    <td class="text-right">45,000.00</td>
                </tr>
                <tr>
                    <td class="text-center">3</td>
                    <td>Financial Modeling & Forecasting</td>
                    <td class="text-center">1</td>
                    <td class="text-right">35,000.00</td>
                    <td class="text-right">35,000.00</td>
                </tr>
                <tr>
                    <td class="text-center">4</td>
                    <td>Presentation Preparation</td>
                    <td class="text-center">1</td>
                    <td class="text-right">15,000.00</td>
                    <td class="text-right">15,000.00</td>
                </tr>
            </tbody>
        </table>
        
        <div class="totals">
            <div class="total-row">
                <span>Subtotal:</span>
                <span>฿195,000.00</span>
            </div>
            <div class="total-row">
                <span>VAT (7%):</span>
                <span>฿13,650.00</span>
            </div>
            <div class="total-row grand-total">
                <span>Grand Total:</span>
                <span>฿208,650.00</span>
            </div>
        </div>
        
        <div class="payment-info">
            <strong>Payment Terms:</strong> Net 30 days<br>
            <strong>Bank:</strong> Siam Commercial Bank | <strong>Account:</strong> 987-6-54321-0<br>
            <strong>Account Name:</strong> Professional Consulting Group
        </div>
        
        <div class="footer">
            Thank you for your business!
        </div>
    </body>
    </html>
    """
    
    pdf_path = invoices_dir / 'invoice_003_consulting.pdf'
    HTML(string=html_content).write_pdf(str(pdf_path))
    print(f'✅ Created: {pdf_path.name}')
    
    from pdf2image import convert_from_path
    png_path = invoices_dir / 'invoice_003_consulting.png'
    images = convert_from_path(str(pdf_path), dpi=150)
    if images:
        images[0].save(str(png_path), 'PNG')
        print(f'✅ Created: {png_path.name}')


def create_invoice_4():
    """Invoice ภาษาไทย - Restaurant Supplies"""
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
        {base_css}
        .company-name {{ color: #ff6b35; }}
        .invoice-title {{ color: #ff6b35; }}
        thead {{ background: #ff6b35; }}
        .total-row.grand-total {{ border-top-color: #ff6b35; }}
        .bill-to-title {{ color: #ff6b35; }}
        .bill-to {{ background: #fff5f0; }}
        </style>
    </head>
    <body>
        <div class="header">
            <div class="company-info">
                <div class="company-name">ร้านอาหารอร่อย จำกัด</div>
                <div>555 ถนนพระราม 9 กรุงเทพฯ 10400</div>
                <div>โทร: 02-555-6789 | อีเมล: order@aroi.com</div>
                <div>เลขประจำตัวผู้เสียภาษี: 0345678901234</div>
            </div>
            <div>
                <div class="invoice-title">ใบกำกับภาษี</div>
                <div class="invoice-meta">
                    <div class="meta-row"><strong>เลขที่:</strong> TX-2026-0912</div>
                    <div class="meta-row"><strong>วันที่:</strong> 12 กันยายน 2569</div>
                    <div class="meta-row"><strong>กำหนดชำระ:</strong> 30 วัน</div>
                </div>
            </div>
        </div>
        
        <div class="bill-to">
            <div class="bill-to-title">ลูกค้า / BILL TO:</div>
            <div><strong>บริษัท อาหารดี จำกัด</strong></div>
            <div>555 ถนนพระราม 9 กรุงเทพฯ 10400</div>
            <div>เลขประจำตัวผู้เสียภาษี: 0345678901234</div>
        </div>
        
        <table>
            <thead>
                <tr>
                    <th style="width: 40px;">ลำดับ</th>
                    <th>รายละเอียด</th>
                    <th style="width: 50px;" class="text-center">จำนวน</th>
                    <th style="width: 80px;" class="text-right">ราคา/หน่วย</th>
                    <th style="width: 80px;" class="text-right">จำนวนเงิน</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td class="text-center">1</td>
                    <td>เนื้อวัวนำเข้า (กก.)</td>
                    <td class="text-center">50</td>
                    <td class="text-right">450.00</td>
                    <td class="text-right">22,500.00</td>
                </tr>
                <tr>
                    <td class="text-center">2</td>
                    <td>เนื้อหมู (กก.)</td>
                    <td class="text-center">80</td>
                    <td class="text-right">180.00</td>
                    <td class="text-right">14,400.00</td>
                </tr>
                <tr>
                    <td class="text-center">3</td>
                    <td>ไก่สด (กก.)</td>
                    <td class="text-center">60</td>
                    <td class="text-right">120.00</td>
                    <td class="text-right">7,200.00</td>
                </tr>
                <tr>
                    <td class="text-center">4</td>
                    <td>ผักสดผสม (กก.)</td>
                    <td class="text-center">30</td>
                    <td class="text-right">85.00</td>
                    <td class="text-right">2,550.00</td>
                </tr>
                <tr>
                    <td class="text-center">5</td>
                    <td>เครื่องปรุงรส (ชุด)</td>
                    <td class="text-center">10</td>
                    <td class="text-right">350.00</td>
                    <td class="text-right">3,500.00</td>
                </tr>
                <tr>
                    <td class="text-center">6</td>
                    <td>ข้าวสาร (กก.)</td>
                    <td class="text-center">100</td>
                    <td class="text-right">45.00</td>
                    <td class="text-right">4,500.00</td>
                </tr>
                <tr>
                    <td class="text-center">7</td>
                    <td>น้ำมันพืช (ลิตร)</td>
                    <td class="text-center">20</td>
                    <td class="text-right">65.00</td>
                    <td class="text-right">1,300.00</td>
                </tr>
            </tbody>
        </table>
        
        <div class="totals">
            <div class="total-row">
                <span>รวมเงิน:</span>
                <span>฿55,950.00</span>
            </div>
            <div class="total-row">
                <span>ภาษีมูลค่าเพิ่ม 7%:</span>
                <span>฿3,916.50</span>
            </div>
            <div class="total-row grand-total">
                <span>ยอดรวมทั้งหมด:</span>
                <span>฿59,866.50</span>
            </div>
        </div>
        
        <div class="payment-info">
            <strong>เงื่อนไขการชำระเงิน:</strong> 30 วัน<br>
            <strong>ธนาคาร:</strong> ธนาคารกสิกรไทย | <strong>เลขที่บัญชี:</strong> 456-7-89012-3<br>
            <strong>ชื่อบัญชี:</strong> ร้านอาหารอร่อย จำกัด
        </div>
        
        <div class="footer">
            ขอบคุณที่ใช้บริการ
        </div>
    </body>
    </html>
    """
    
    pdf_path = invoices_dir / 'invoice_004_restaurant.pdf'
    HTML(string=html_content).write_pdf(str(pdf_path))
    print(f'✅ Created: {pdf_path.name}')
    
    from pdf2image import convert_from_path
    png_path = invoices_dir / 'invoice_004_restaurant.png'
    images = convert_from_path(str(pdf_path), dpi=150)
    if images:
        images[0].save(str(png_path), 'PNG')
        print(f'✅ Created: {png_path.name}')


def create_invoice_5():
    """Invoice ภาษาอังกฤษ - Marketing Services"""
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
        {base_css}
        .company-name {{ color: #8b5cf6; }}
        .invoice-title {{ color: #8b5cf6; }}
        thead {{ background: #8b5cf6; }}
        .total-row.grand-total {{ border-top-color: #8b5cf6; }}
        .bill-to-title {{ color: #8b5cf6; }}
        .bill-to {{ background: #f5f3ff; }}
        </style>
    </head>
    <body>
        <div class="header">
            <div class="company-info">
                <div class="company-name">Digital Marketing Agency</div>
                <div>888 Siam Square, Bangkok 10330</div>
                <div>Tel: +66 2-888-9999 | Email: hello@digitalmarketing.com</div>
                <div>Tax ID: 0789012345678</div>
            </div>
            <div>
                <div class="invoice-title">INVOICE</div>
                <div class="invoice-meta">
                    <div class="meta-row"><strong>Invoice No:</strong> INV-2026-0915</div>
                    <div class="meta-row"><strong>Date:</strong> September 15, 2026</div>
                    <div class="meta-row"><strong>Due Date:</strong> Net 30</div>
                </div>
            </div>
        </div>
        
        <div class="bill-to">
            <div class="bill-to-title">BILL TO:</div>
            <div><strong>Fashion Retail Co., Ltd.</strong></div>
            <div>888 Siam Square, Bangkok 10330, Thailand</div>
            <div>Tax ID: 0789012345678</div>
        </div>
        
        <table>
            <thead>
                <tr>
                    <th style="width: 40px;">No.</th>
                    <th>Description</th>
                    <th style="width: 50px;" class="text-center">Qty</th>
                    <th style="width: 90px;" class="text-right">Unit Price</th>
                    <th style="width: 90px;" class="text-right">Amount</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td class="text-center">1</td>
                    <td>Social Media Management (Facebook + IG)</td>
                    <td class="text-center">1</td>
                    <td class="text-right">35,000.00</td>
                    <td class="text-right">35,000.00</td>
                </tr>
                <tr>
                    <td class="text-center">2</td>
                    <td>Content Creation (20 posts)</td>
                    <td class="text-center">20</td>
                    <td class="text-right">800.00</td>
                    <td class="text-right">16,000.00</td>
                </tr>
                <tr>
                    <td class="text-center">3</td>
                    <td>Google Ads Management</td>
                    <td class="text-center">1</td>
                    <td class="text-right">25,000.00</td>
                    <td class="text-right">25,000.00</td>
                </tr>
                <tr>
                    <td class="text-center">4</td>
                    <td>Facebook Ads Budget</td>
                    <td class="text-center">1</td>
                    <td class="text-right">50,000.00</td>
                    <td class="text-right">50,000.00</td>
                </tr>
                <tr>
                    <td class="text-center">5</td>
                    <td>Photography (Product Shots)</td>
                    <td class="text-center">1</td>
                    <td class="text-right">18,000.00</td>
                    <td class="text-right">18,000.00</td>
                </tr>
                <tr>
                    <td class="text-center">6</td>
                    <td>Video Production (3 clips)</td>
                    <td class="text-center">3</td>
                    <td class="text-right">12,000.00</td>
                    <td class="text-right">36,000.00</td>
                </tr>
            </tbody>
        </table>
        
        <div class="totals">
            <div class="total-row">
                <span>Subtotal:</span>
                <span>฿180,000.00</span>
            </div>
            <div class="total-row">
                <span>VAT (7%):</span>
                <span>฿12,600.00</span>
            </div>
            <div class="total-row grand-total">
                <span>Grand Total:</span>
                <span>฿192,600.00</span>
            </div>
        </div>
        
        <div class="payment-info">
            <strong>Payment Terms:</strong> Net 30 days<br>
            <strong>Bank:</strong> Kasikorn Bank | <strong>Account:</strong> 789-0-12345-6<br>
            <strong>Account Name:</strong> Digital Marketing Agency
        </div>
        
        <div class="footer">
            Thank you for your business!
        </div>
    </body>
    </html>
    """
    
    pdf_path = invoices_dir / 'invoice_005_marketing.pdf'
    HTML(string=html_content).write_pdf(str(pdf_path))
    print(f'✅ Created: {pdf_path.name}')
    
    from pdf2image import convert_from_path
    png_path = invoices_dir / 'invoice_005_marketing.png'
    images = convert_from_path(str(pdf_path), dpi=150)
    if images:
        images[0].save(str(png_path), 'PNG')
        print(f'✅ Created: {png_path.name}')


def create_invoice_6():
    """ใบเสร็จรับเงิน (Receipt)"""
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
        {base_css}
        .company-name {{ color: #10b981; }}
        .invoice-title {{ color: #10b981; }}
        thead {{ background: #10b981; }}
        .total-row.grand-total {{ border-top-color: #10b981; }}
        .bill-to-title {{ color: #10b981; }}
        .bill-to {{ background: #f0fdf4; }}
        </style>
    </head>
    <body>
        <div class="header">
            <div class="company-info">
                <div class="company-name">บริษัท สมใจ จำกัด</div>
                <div>123 ถนนรัชดาภิเษก กรุงเทพฯ 10400</div>
                <div>โทร: 02-123-4567 | อีเมล: info@somjai.com</div>
                <div>เลขประจำตัวผู้เสียภาษี: 0987654321098</div>
            </div>
            <div>
                <div class="invoice-title">ใบเสร็จรับเงิน</div>
                <div class="invoice-meta">
                    <div class="meta-row"><strong>เลขที่:</strong> REC-2026-0920</div>
                    <div class="meta-row"><strong>วันที่:</strong> 20 กันยายน 2569</div>
                    <div class="meta-row"><strong>รับจาก:</strong> บริษัท เจริญกิจ จำกัด</div>
                </div>
            </div>
        </div>
        
        <div class="bill-to">
            <div class="bill-to-title">รับเงินจาก / RECEIVED FROM:</div>
            <div><strong>บริษัท เจริญกิจ จำกัด</strong></div>
            <div>789 ถนนสุขุมวิท กรุงเทพฯ 10110</div>
            <div>เลขประจำตัวผู้เสียภาษี: 0123456789012</div>
        </div>
        
        <table>
            <thead>
                <tr>
                    <th style="width: 40px;">ลำดับ</th>
                    <th>รายละเอียด</th>
                    <th style="width: 100px;" class="text-right">จำนวนเงิน</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td class="text-center">1</td>
                    <td>ค่าสินค้าตามใบกำกับภาษี TX-2026-0905</td>
                    <td class="text-right">21,186.00</td>
                </tr>
                <tr>
                    <td class="text-center">2</td>
                    <td>ค่าสินค้าตามใบกำกับภาษี TX-2026-0912</td>
                    <td class="text-right">59,866.50</td>
                </tr>
            </tbody>
        </table>
        
        <div class="totals">
            <div class="total-row grand-total">
                <span>รวมเงินที่รับ:</span>
                <span>฿81,052.50</span>
            </div>
        </div>
        
        <div class="payment-info">
            <strong>วิธีการชำระเงิน:</strong> โอนผ่านธนาคาร<br>
            <strong>ธนาคาร:</strong> ธนาคารกรุงเทพ | <strong>เลขที่บัญชี:</strong> 123-4-56789-0<br>
            <strong>วันที่โอน:</strong> 20 กันยายน 2569<br>
            <strong>ผู้รับเงิน:</strong> นางสาวสมใจ ดีงาม
        </div>
        
        <div class="footer">
            ขอบคุณที่ใช้บริการ
        </div>
    </body>
    </html>
    """
    
    pdf_path = invoices_dir / 'invoice_006_receipt.pdf'
    HTML(string=html_content).write_pdf(str(pdf_path))
    print(f'✅ Created: {pdf_path.name}')
    
    from pdf2image import convert_from_path
    png_path = invoices_dir / 'invoice_006_receipt.png'
    images = convert_from_path(str(pdf_path), dpi=150)
    if images:
        images[0].save(str(png_path), 'PNG')
        print(f'✅ Created: {png_path.name}')


def create_invoice_7():
    """ใบกำกับภาษีเต็มรูปแบบ (Tax Invoice)"""
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
        {base_css}
        .company-name {{ color: #dc2626; }}
        .invoice-title {{ color: #dc2626; }}
        thead {{ background: #dc2626; }}
        .total-row.grand-total {{ border-top-color: #dc2626; }}
        .bill-to-title {{ color: #dc2626; }}
        .bill-to {{ background: #fef2f2; }}
        </style>
    </head>
    <body>
        <div class="header">
            <div class="company-info">
                <div class="company-name">บริษัท ก่อสร้างไทย จำกัด</div>
                <div>999 ถนนพระราม 3 กรุงเทพฯ 10120</div>
                <div>โทร: 02-999-8888 | อีเมล: billing@thaiconstruction.com</div>
                <div>เลขประจำตัวผู้เสียภาษี: 0567890123456</div>
            </div>
            <div>
                <div class="invoice-title">ใบกำกับภาษี</div>
                <div class="invoice-meta">
                    <div class="meta-row"><strong>เลขที่:</strong> TAX-2026-0925</div>
                    <div class="meta-row"><strong>วันที่:</strong> 25 กันยายน 2569</div>
                    <div class="meta-row"><strong>กำหนดชำระ:</strong> 30 วัน</div>
                </div>
            </div>
        </div>
        
        <div class="bill-to">
            <div class="bill-to-title">ผู้ซื้อ / BUYER:</div>
            <div><strong>บริษัท อสังหาริมทรัพย์ จำกัด</strong></div>
            <div>999 ถนนพระราม 3 กรุงเทพฯ 10120</div>
            <div>เลขประจำตัวผู้เสียภาษี: 0567890123456</div>
        </div>
        
        <table>
            <thead>
                <tr>
                    <th style="width: 40px;">ลำดับ</th>
                    <th>รายละเอียด</th>
                    <th style="width: 50px;" class="text-center">จำนวน</th>
                    <th style="width: 80px;" class="text-right">ราคา/หน่วย</th>
                    <th style="width: 80px;" class="text-right">จำนวนเงิน</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td class="text-center">1</td>
                    <td>ค่าวัสดุก่อสร้าง (ปูนซีเมนต์ 500 กระสอบ)</td>
                    <td class="text-center">500</td>
                    <td class="text-right">180.00</td>
                    <td class="text-right">90,000.00</td>
                </tr>
                <tr>
                    <td class="text-center">2</td>
                    <td>ค่าเหล็กเส้น (เหล็กข้ออ้อย 12 มม.)</td>
                    <td class="text-center">200</td>
                    <td class="text-right">450.00</td>
                    <td class="text-right">90,000.00</td>
                </tr>
                <tr>
                    <td class="text-center">3</td>
                    <td>ค่าอิฐมวลเบา</td>
                    <td class="text-center">1000</td>
                    <td class="text-right">25.00</td>
                    <td class="text-right">25,000.00</td>
                </tr>
                <tr>
                    <td class="text-center">4</td>
                    <td>ค่ากระเบื้องมุงหลังคา</td>
                    <td class="text-center">500</td>
                    <td class="text-right">35.00</td>
                    <td class="text-right">17,500.00</td>
                </tr>
            </tbody>
        </table>
        
        <div class="totals">
            <div class="total-row">
                <span>รวมเงิน:</span>
                <span>฿222,500.00</span>
            </div>
            <div class="total-row">
                <span>ภาษีมูลค่าเพิ่ม 7%:</span>
                <span>฿15,575.00</span>
            </div>
            <div class="total-row grand-total">
                <span>ยอดรวมทั้งหมด:</span>
                <span>฿238,075.00</span>
            </div>
        </div>
        
        <div class="payment-info">
            <strong>เงื่อนไขการชำระเงิน:</strong> 30 วัน<br>
            <strong>ธนาคาร:</strong> ธนาคารไทยพาณิชย์ | <strong>เลขที่บัญชี:</strong> 567-8-90123-4<br>
            <strong>ชื่อบัญชี:</strong> บริษัท ก่อสร้างไทย จำกัด<br>
            <strong>หมายเหตุ:</strong> ใบกำกับภาษีนี้ออกตามประมวลรัษฎากร มาตรา 105
        </div>
        
        <div class="footer">
            ขอบคุณที่ใช้บริการ
        </div>
    </body>
    </html>
    """
    
    pdf_path = invoices_dir / 'invoice_007_tax_invoice.pdf'
    HTML(string=html_content).write_pdf(str(pdf_path))
    print(f'✅ Created: {pdf_path.name}')
    
    from pdf2image import convert_from_path
    png_path = invoices_dir / 'invoice_007_tax_invoice.png'
    images = convert_from_path(str(pdf_path), dpi=150)
    if images:
        images[0].save(str(png_path), 'PNG')
        print(f'✅ Created: {png_path.name}')


if __name__ == '__main__':
    print('Creating sample invoices v2 with WeasyPrint (A4 single page)...')
    print()
    
    create_invoice_1()
    print()
    create_invoice_2()
    print()
    create_invoice_3()
    print()
    create_invoice_4()
    print()
    create_invoice_5()
    print()
    create_invoice_6()
    print()
    create_invoice_7()
    
    print()
    print(f'✅ All invoices created in: {invoices_dir}')
