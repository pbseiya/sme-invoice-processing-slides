#!/usr/bin/env python3
"""
สร้างตัวอย่าง Invoice หลายแบบสำหรับสอน SME
- Invoice ภาษาอังกฤษ
- Invoice ภาษาไทย (มี VAT)
"""

from fpdf import FPDF
from datetime import datetime
import os

class InvoicePDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=False)
        
        # เพิ่ม Thai font
        thai_font = '/usr/share/fonts/truetype/noto/NotoSansThai-Regular.ttf'
        if os.path.exists(thai_font):
            self.add_font('Thai', '', thai_font)
            self.thai_font = 'Thai'
        else:
            self.thai_font = None
            
    def header_en(self, invoice_no, date, company_name):
        # Company info
        self.set_font('Helvetica', 'B', 20)
        self.cell(0, 10, company_name, 0, 1, 'L')
        self.set_font('Helvetica', '', 10)
        self.cell(0, 5, '123 Business Street, Bangkok 10110', 0, 1, 'L')
        self.cell(0, 5, 'Tel: +66 2-123-4567 | Email: billing@company.com', 0, 1, 'L')
        self.cell(0, 5, 'Tax ID: 0123456789012', 0, 1, 'L')
        self.ln(5)
        
        # Invoice title
        self.set_font('Helvetica', 'B', 24)
        self.cell(0, 15, 'INVOICE', 0, 1, 'R')
        self.set_font('Helvetica', '', 11)
        self.cell(95, 6, '', 0, 0)
        self.cell(95, 6, f'Invoice No: {invoice_no}', 0, 1, 'R')
        self.cell(95, 6, '', 0, 0)
        self.cell(95, 6, f'Date: {date}', 0, 1, 'R')
        self.cell(95, 6, '', 0, 0)
        self.cell(95, 6, 'Due Date: Net 30', 0, 1, 'R')
        self.ln(5)
        
    def bill_to_en(self, customer_name, address, tax_id):
        self.set_font('Helvetica', 'B', 11)
        self.cell(0, 6, 'BILL TO:', 0, 1)
        self.set_font('Helvetica', '', 11)
        self.cell(0, 6, customer_name, 0, 1)
        self.multi_cell(0, 6, address)
        self.cell(0, 6, f'Tax ID: {tax_id}', 0, 1)
        self.ln(5)
        
    def items_table_en(self, items):
        # Table header
        self.set_fill_color(240, 240, 240)
        self.set_font('Helvetica', 'B', 10)
        self.cell(15, 8, 'No.', 1, 0, 'C', True)
        self.cell(90, 8, 'Description', 1, 0, 'C', True)
        self.cell(20, 8, 'Qty', 1, 0, 'C', True)
        self.cell(30, 8, 'Unit Price', 1, 0, 'C', True)
        self.cell(35, 8, 'Amount', 1, 1, 'C', True)
        
        # Table rows
        self.set_font('Helvetica', '', 10)
        total = 0
        for i, item in enumerate(items, 1):
            self.cell(15, 8, str(i), 1, 0, 'C')
            self.cell(90, 8, item['desc'], 1, 0, 'L')
            self.cell(20, 8, str(item['qty']), 1, 0, 'C')
            self.cell(30, 8, f"{item['price']:,.2f}", 1, 0, 'R')
            amount = item['qty'] * item['price']
            self.cell(35, 8, f"{amount:,.2f}", 1, 1, 'R')
            total += amount
            
        self.ln(5)
        return total
        
    def totals_en(self, subtotal, vat_rate=7):
        vat = subtotal * vat_rate / 100
        grand_total = subtotal + vat
        
        self.set_font('Helvetica', '', 11)
        self.cell(140, 7, '', 0, 0)
        self.cell(50, 7, f'Subtotal:', 0, 0, 'R')
        self.cell(0, 7, f'{subtotal:,.2f}', 0, 1, 'R')
        
        self.cell(140, 7, '', 0, 0)
        self.cell(50, 7, f'VAT ({vat_rate}%):', 0, 0, 'R')
        self.cell(0, 7, f'{vat:,.2f}', 0, 1, 'R')
        
        self.set_font('Helvetica', 'B', 12)
        self.cell(140, 8, '', 0, 0)
        self.cell(50, 8, 'Grand Total:', 0, 0, 'R')
        self.cell(0, 8, f'{grand_total:,.2f}', 0, 1, 'R')
        
        self.ln(10)
        self.set_font('Helvetica', '', 9)
        self.multi_cell(0, 5, 'Payment Terms: Net 30 days\nBank: Bangkok Bank | Account: 123-4-56789-0')
        
    def header_th(self, invoice_no, date, company_name):
        if self.thai_font:
            self.set_font(self.thai_font, '', 18)
            self.cell(0, 10, company_name, 0, 1, 'L')
            self.set_font(self.thai_font, '', 10)
            self.cell(0, 5, '123 ถนนธุรกิจ กรุงเทพฯ 10110', 0, 1, 'L')
            self.cell(0, 5, 'โทร: 02-123-4567 | อีเมล: billing@company.com', 0, 1, 'L')
            self.cell(0, 5, 'เลขประจำตัวผู้เสียภาษี: 0123456789012', 0, 1, 'L')
        else:
            self.set_font('Helvetica', 'B', 18)
            self.cell(0, 10, company_name, 0, 1, 'L')
            self.set_font('Helvetica', '', 10)
            self.cell(0, 5, '123 Thanon Thurakit, Krungthep 10110', 0, 1, 'L')
            self.cell(0, 5, 'Tel: 02-123-4567 | Email: billing@company.com', 0, 1, 'L')
            self.cell(0, 5, 'Tax ID: 0123456789012', 0, 1, 'L')
        self.ln(5)
        
        # Invoice title
        self.set_font('Helvetica', 'B', 22)
        self.cell(0, 15, 'TAX INVOICE', 0, 1, 'R')
        self.set_font('Helvetica', '', 11)
        self.cell(95, 6, '', 0, 0)
        self.cell(95, 6, f'No: {invoice_no}', 0, 1, 'R')
        self.cell(95, 6, '', 0, 0)
        self.cell(95, 6, f'Date: {date}', 0, 1, 'R')
        self.ln(5)
        
    def bill_to_th(self, customer_name, address, tax_id):
        if self.thai_font:
            self.set_font(self.thai_font, '', 11)
            self.cell(0, 6, 'ลูกค้า / BILL TO:', 0, 1)
            self.cell(0, 6, customer_name, 0, 1)
            self.multi_cell(0, 6, address)
            self.cell(0, 6, f'เลขประจำตัวผู้เสียภาษี: {tax_id}', 0, 1)
        else:
            self.set_font('Helvetica', 'B', 11)
            self.cell(0, 6, 'BILL TO:', 0, 1)
            self.set_font('Helvetica', '', 11)
            self.cell(0, 6, customer_name, 0, 1)
            self.multi_cell(0, 6, address)
            self.cell(0, 6, f'Tax ID: {tax_id}', 0, 1)
        self.ln(5)
        
    def items_table_th(self, items):
        # Table header
        self.set_fill_color(240, 240, 240)
        if self.thai_font:
            self.set_font(self.thai_font, '', 10)
            self.cell(15, 8, 'ลำดับ', 1, 0, 'C', True)
            self.cell(80, 8, 'รายละเอียด', 1, 0, 'C', True)
            self.cell(20, 8, 'จำนวน', 1, 0, 'C', True)
            self.cell(25, 8, 'ราคา/หน่วย', 1, 0, 'C', True)
            self.cell(25, 8, 'จำนวนเงิน', 1, 0, 'C', True)
            self.cell(25, 8, 'VAT', 1, 1, 'C', True)
        else:
            self.set_font('Helvetica', 'B', 10)
            self.cell(15, 8, 'No.', 1, 0, 'C', True)
            self.cell(80, 8, 'Description', 1, 0, 'C', True)
            self.cell(20, 8, 'Qty', 1, 0, 'C', True)
            self.cell(25, 8, 'Price', 1, 0, 'C', True)
            self.cell(25, 8, 'Amount', 1, 0, 'C', True)
            self.cell(25, 8, 'VAT', 1, 1, 'C', True)
        
        # Table rows
        if self.thai_font:
            self.set_font(self.thai_font, '', 10)
        else:
            self.set_font('Helvetica', '', 10)
        subtotal = 0
        total_vat = 0
        for i, item in enumerate(items, 1):
            self.cell(15, 8, str(i), 1, 0, 'C')
            self.cell(80, 8, item['desc'], 1, 0, 'L')
            self.cell(20, 8, str(item['qty']), 1, 0, 'C')
            self.cell(25, 8, f"{item['price']:,.2f}", 1, 0, 'R')
            amount = item['qty'] * item['price']
            self.cell(25, 8, f"{amount:,.2f}", 1, 0, 'R')
            vat = amount * 7 / 100
            self.cell(25, 8, f"{vat:,.2f}", 1, 1, 'R')
            subtotal += amount
            total_vat += vat
            
        self.ln(5)
        return subtotal, total_vat
        
    def totals_th(self, subtotal, vat):
        grand_total = subtotal + vat
        
        if self.thai_font:
            self.set_font(self.thai_font, '', 11)
            self.cell(140, 7, '', 0, 0)
            self.cell(50, 7, 'รวมเงิน:', 0, 0, 'R')
            self.cell(0, 7, f'{subtotal:,.2f}', 0, 1, 'R')
            
            self.cell(140, 7, '', 0, 0)
            self.cell(50, 7, 'ภาษีมูลค่าเพิ่ม 7%:', 0, 0, 'R')
            self.cell(0, 7, f'{vat:,.2f}', 0, 1, 'R')
            
            self.set_font(self.thai_font, '', 12)
            self.cell(140, 8, '', 0, 0)
            self.cell(50, 8, 'ยอดรวมทั้งหมด:', 0, 0, 'R')
            self.cell(0, 8, f'{grand_total:,.2f}', 0, 1, 'R')
            
            self.ln(10)
            self.set_font(self.thai_font, '', 9)
            self.multi_cell(0, 5, 'เงื่อนไขการชำระเงิน: 30 วัน\nธนาคาร: ธนาคารกรุงเทพ | เลขที่บัญชี: 123-4-56789-0')
        else:
            self.set_font('Helvetica', '', 11)
            self.cell(140, 7, '', 0, 0)
            self.cell(50, 7, 'Subtotal:', 0, 0, 'R')
            self.cell(0, 7, f'{subtotal:,.2f}', 0, 1, 'R')
            
            self.cell(140, 7, '', 0, 0)
            self.cell(50, 7, 'VAT 7%:', 0, 0, 'R')
            self.cell(0, 7, f'{vat:,.2f}', 0, 1, 'R')
            
            self.set_font('Helvetica', 'B', 12)
            self.cell(140, 8, '', 0, 0)
            self.cell(50, 8, 'Grand Total:', 0, 0, 'R')
            self.cell(0, 8, f'{grand_total:,.2f}', 0, 1, 'R')
            
            self.ln(10)
            self.set_font('Helvetica', '', 9)
            self.multi_cell(0, 5, 'Payment Terms: Net 30 days\nBank: Bangkok Bank | Account: 123-4-56789-0')


def create_invoice_1():
    """Invoice ภาษาอังกฤษ - IT Services"""
    pdf = InvoicePDF()
    pdf.add_page()
    
    date = datetime(2026, 9, 1)
    pdf.header_en('INV-2026-0901', date.strftime('%B %d, %Y'), 'Tech Solutions Co., Ltd.')
    
    pdf.bill_to_en(
        'ABC Manufacturing PCL',
        '456 Industrial Road, Chonburi 20130\nThailand',
        '0987654321098'
    )
    
    items = [
        {'desc': 'Website Development - E-commerce Platform', 'qty': 1, 'price': 85000},
        {'desc': 'Mobile App Development (iOS)', 'qty': 1, 'price': 120000},
        {'desc': 'Mobile App Development (Android)', 'qty': 1, 'price': 120000},
        {'desc': 'Monthly Maintenance (September)', 'qty': 1, 'price': 15000},
        {'desc': 'Cloud Hosting Setup (AWS)', 'qty': 1, 'price': 25000},
    ]
    
    subtotal = pdf.items_table_en(items)
    pdf.totals_en(subtotal)
    
    pdf.output('/home/seiya/projects/training_course/sme-demo/invoices/invoice_001_en.pdf')
    print('Created: invoice_001_en.pdf')


def create_invoice_2():
    """Invoice ภาษาไทย - Office Supplies"""
    pdf = InvoicePDF()
    pdf.add_page()
    
    date = datetime(2026, 9, 5)
    pdf.header_th('TX-2026-0905', date.strftime('%d/%m/%Y'), 'สำนักงานสมบุญ จำกัด')
    
    pdf.bill_to_th(
        'บริษัท เจริญกิจ จำกัด',
        '789 ถนนสุขุมวิท กรุงเทพฯ 10110',
        '0123456789012'
    )
    
    items = [
        {'desc': 'กระดาษ A4 (80 แกรม) 5 รีม', 'qty': 10, 'price': 450},
        {'desc': 'หมึกพิมพ์ LaserJet สีดำ', 'qty': 5, 'price': 1200},
        {'desc': 'หมึกพิมพ์ LaserJet สี', 'qty': 3, 'price': 1800},
        {'desc': 'แฟ้มเอกสาร A4', 'qty': 20, 'price': 85},
        {'desc': 'ปากกาลูกลื่น (กล่อง 12 ด้าม)', 'qty': 5, 'price': 180},
        {'desc': 'เครื่องคิดเลข Casio', 'qty': 2, 'price': 650},
    ]
    
    subtotal, vat = pdf.items_table_th(items)
    pdf.totals_th(subtotal, vat)
    
    pdf.output('/home/seiya/projects/training_course/sme-demo/invoices/invoice_002_th.pdf')
    print('Created: invoice_002_th.pdf')


def create_invoice_3():
    """Invoice ภาษาอังกฤษ - Consulting Services"""
    pdf = InvoicePDF()
    pdf.add_page()
    
    date = datetime(2026, 9, 10)
    pdf.header_en('INV-2026-0910', date.strftime('%B %d, %Y'), 'Professional Consulting Group')
    
    pdf.bill_to_en(
        'Global Trading Co., Ltd.',
        '321 Silom Road, Bangkok 10500\nThailand',
        '0567890123456'
    )
    
    items = [
        {'desc': 'Business Strategy Consulting (40 hrs)', 'qty': 40, 'price': 2500},
        {'desc': 'Market Research & Analysis', 'qty': 1, 'price': 45000},
        {'desc': 'Financial Modeling & Forecasting', 'qty': 1, 'price': 35000},
        {'desc': 'Presentation Preparation', 'qty': 1, 'price': 15000},
    ]
    
    subtotal = pdf.items_table_en(items)
    pdf.totals_en(subtotal)
    
    pdf.output('/home/seiya/projects/training_course/sme-demo/invoices/invoice_003_consulting.pdf')
    print('Created: invoice_003_consulting.pdf')


def create_invoice_4():
    """Invoice ภาษาไทย - Restaurant Supplies"""
    pdf = InvoicePDF()
    pdf.add_page()
    
    date = datetime(2026, 9, 12)
    pdf.header_th('TX-2026-0912', date.strftime('%d/%m/%Y'), 'ร้านอาหารอร่อย จำกัด')
    
    pdf.bill_to_th(
        'บริษัท อาหารดี จำกัด',
        '555 ถนนพระราม 9 กรุงเทพฯ 10400',
        '0345678901234'
    )
    
    items = [
        {'desc': 'เนื้อวัวนำเข้า (กก.)', 'qty': 50, 'price': 450},
        {'desc': 'เนื้อหมู (กก.)', 'qty': 80, 'price': 180},
        {'desc': 'ไก่สด (กก.)', 'qty': 60, 'price': 120},
        {'desc': 'ผักสดผสม (กก.)', 'qty': 30, 'price': 85},
        {'desc': 'เครื่องปรุงรส (ชุด)', 'qty': 10, 'price': 350},
        {'desc': 'ข้าวสาร (กก.)', 'qty': 100, 'price': 45},
        {'desc': 'น้ำมันพืช (ลิตร)', 'qty': 20, 'price': 65},
    ]
    
    subtotal, vat = pdf.items_table_th(items)
    pdf.totals_th(subtotal, vat)
    
    pdf.output('/home/seiya/projects/training_course/sme-demo/invoices/invoice_004_restaurant.pdf')
    print('Created: invoice_004_restaurant.pdf')


def create_invoice_5():
    """Invoice ภาษาอังกฤษ - Marketing Services"""
    pdf = InvoicePDF()
    pdf.add_page()
    
    date = datetime(2026, 9, 15)
    pdf.header_en('INV-2026-0915', date.strftime('%B %d, %Y'), 'Digital Marketing Agency')
    
    pdf.bill_to_en(
        'Fashion Retail Co., Ltd.',
        '888 Siam Square, Bangkok 10330\nThailand',
        '0789012345678'
    )
    
    items = [
        {'desc': 'Social Media Management (Facebook + IG)', 'qty': 1, 'price': 35000},
        {'desc': 'Content Creation (20 posts)', 'qty': 20, 'price': 800},
        {'desc': 'Google Ads Management', 'qty': 1, 'price': 25000},
        {'desc': 'Facebook Ads Budget', 'qty': 1, 'price': 50000},
        {'desc': 'Photography (Product Shots)', 'qty': 1, 'price': 18000},
        {'desc': 'Video Production (3 clips)', 'qty': 3, 'price': 12000},
    ]
    
    subtotal = pdf.items_table_en(items)
    pdf.totals_en(subtotal)
    
    pdf.output('/home/seiya/projects/training_course/sme-demo/invoices/invoice_005_marketing.pdf')
    print('Created: invoice_005_marketing.pdf')


if __name__ == '__main__':
    print('Creating sample invoices for SME training...')
    print()
    
    create_invoice_1()
    create_invoice_2()
    create_invoice_3()
    create_invoice_4()
    create_invoice_5()
    
    print()
    print('All invoices created successfully!')
    print('Location: ~/projects/training_course/sme-demo/invoices/')
