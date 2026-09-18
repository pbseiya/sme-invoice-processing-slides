#!/usr/bin/env python3
"""
สร้างตัวอย่าง Invoice ใหม่ด้วย WeasyPrint
- ใช้ HTML/CSS สำหรับ layout ที่ถูกต้อง
- รองรับ font ไทยหลายแบบ
- สร้างภาพ invoice เป็น PNG
"""

from weasyprint import HTML, CSS
from pathlib import Path
from datetime import datetime
import os

# โฟลเดอร์ output
invoices_dir = Path('/home/seiya/projects/training_course/private-course/courses/sme-invoice-processing-demo/invoices')
invoices_dir.mkdir(exist_ok=True)

# CSS สำหรับ invoice
base_css = """
@page {
    size: A4;
    margin: 2cm;
}

body {
    font-family: 'Sarabun', 'Noto Sans Thai', sans-serif;
    font-size: 11pt;
    line-height: 1.6;
    color: #333;
}

.header {
    display: flex;
    justify-content: space-between;
    align-items: start;
    margin-bottom: 30px;
    border-bottom: 3px solid #2c5aa0;
    padding-bottom: 20px;
}

.company-info {
    flex: 1;
}

.company-name {
    font-size: 24pt;
    font-weight: bold;
    color: #2c5aa0;
    margin-bottom: 10px;
}

.invoice-title {
    font-size: 28pt;
    font-weight: bold;
    text-align: right;
    color: #2c5aa0;
}

.invoice-meta {
    text-align: right;
    margin-top: 10px;
}

.meta-row {
    margin: 5px 0;
}

.bill-to {
    background: #f5f5f5;
    padding: 20px;
    border-radius: 8px;
    margin-bottom: 30px;
}

.bill-to-title {
    font-weight: bold;
    font-size: 12pt;
    margin-bottom: 10px;
    color: #2c5aa0;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 30px;
}

thead {
    background: #2c5aa0;
    color: white;
}

th {
    padding: 12px;
    text-align: left;
    font-weight: bold;
}

td {
    padding: 12px;
    border-bottom: 1px solid #ddd;
}

.text-right {
    text-align: right;
}

.text-center {
    text-align: center;
}

.totals {
    margin-left: auto;
    width: 300px;
}

.total-row {
    display: flex;
    justify-content: space-between;
    padding: 8px 0;
}

.total-row.grand-total {
    font-size: 14pt;
    font-weight: bold;
    border-top: 2px solid #2c5aa0;
    margin-top: 10px;
    padding-top: 15px;
}

.payment-info {
    margin-top: 40px;
    padding: 20px;
    background: #f9f9f9;
    border-radius: 8px;
    font-size: 10pt;
}

.footer {
    margin-top: 50px;
    text-align: center;
    font-size: 9pt;
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
            <div>456 Industrial Road, Chonburi 20130</div>
            <div>Thailand</div>
            <div>Tax ID: 0987654321098</div>
        </div>
        
        <table>
            <thead>
                <tr>
                    <th style="width: 50px;">No.</th>
                    <th>Description</th>
                    <th style="width: 80px;" class="text-center">Qty</th>
                    <th style="width: 120px;" class="text-right">Unit Price</th>
                    <th style="width: 120px;" class="text-right">Amount</th>
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
    
    # สร้าง PNG จาก PDF (ใช้ pdf2image)
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
                    <th style="width: 50px;">ลำดับ</th>
                    <th>รายละเอียด</th>
                    <th style="width: 70px;" class="text-center">จำนวน</th>
                    <th style="width: 100px;" class="text-right">ราคา/หน่วย</th>
                    <th style="width: 100px;" class="text-right">จำนวนเงิน</th>
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
    
    # สร้าง PNG จาก PDF
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
            <div>321 Silom Road, Bangkok 10500</div>
            <div>Thailand</div>
            <div>Tax ID: 0567890123456</div>
        </div>
        
        <table>
            <thead>
                <tr>
                    <th style="width: 50px;">No.</th>
                    <th>Description</th>
                    <th style="width: 80px;" class="text-center">Hours</th>
                    <th style="width: 120px;" class="text-right">Rate/Hour</th>
                    <th style="width: 120px;" class="text-right">Amount</th>
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
    
    # สร้าง PNG จาก PDF
    from pdf2image import convert_from_path
    png_path = invoices_dir / 'invoice_003_consulting.png'
    images = convert_from_path(str(pdf_path), dpi=150)
    if images:
        images[0].save(str(png_path), 'PNG')
        print(f'✅ Created: {png_path.name}')


if __name__ == '__main__':
    print('Creating sample invoices v2 with WeasyPrint...')
    print()
    
    create_invoice_1()
    print()
    create_invoice_2()
    print()
    create_invoice_3()
    
    print()
    print(f'✅ All invoices created in: {invoices_dir}')
