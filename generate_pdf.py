import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, mm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.graphics.shapes import Drawing, Line, String, PolyLine, Rect

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    'DocTitle',
    parent=styles['Title'],
    fontName='Helvetica-Bold',
    fontSize=18,
    leading=22,
    textColor=colors.HexColor('#1A365D'),
    alignment=1,
    spaceAfter=6
)

subtitle_style = ParagraphStyle(
    'DocSubTitle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=12,
    leading=16,
    textColor=colors.HexColor('#2B6CB0'),
    alignment=1,
    spaceAfter=12
)

paper_header_style = ParagraphStyle(
    'PaperHeader',
    parent=styles['Heading1'],
    fontName='Helvetica-Bold',
    fontSize=15,
    leading=19,
    textColor=colors.white,
    backColor=colors.HexColor('#1A365D'),
    borderPadding=8,
    alignment=1,
    spaceBefore=10,
    spaceAfter=12
)

group_header_style = ParagraphStyle(
    'GroupHeader',
    parent=styles['Heading2'],
    fontName='Helvetica-Bold',
    fontSize=12,
    leading=15,
    textColor=colors.HexColor('#1A365D'),
    backColor=colors.HexColor('#E2E8F0'),
    borderPadding=5,
    spaceBefore=12,
    spaceAfter=8
)

q_style = ParagraphStyle(
    'QuestionStyle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=10,
    leading=14,
    textColor=colors.HexColor('#1A202C'),
    backColor=colors.HexColor('#F7FAFC'),
    borderPadding=6,
    spaceBefore=8,
    spaceAfter=4
)

a_style = ParagraphStyle(
    'AnswerStyle',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=9.5,
    leading=13.5,
    textColor=colors.HexColor('#2D3748'),
    spaceBefore=2,
    spaceAfter=4
)

bullet_style = ParagraphStyle(
    'BulletStyle',
    parent=a_style,
    leftIndent=14,
    firstLineIndent=-8,
    spaceBefore=1,
    spaceAfter=2
)

hint_style = ParagraphStyle(
    'HintStyle',
    parent=styles['Normal'],
    fontName='Helvetica-Oblique',
    fontSize=9,
    leading=13,
    textColor=colors.HexColor('#744210'),
    backColor=colors.HexColor('#FEFCBF'),
    borderPadding=6,
    spaceBefore=4,
    spaceAfter=8
)

def add_q(story, q_text):
    story.append(Paragraph(q_text, q_style))

def add_a(story, a_text):
    for p in a_text.strip().split('\n\n'):
        p_clean = p.strip()
        if not p_clean:
            continue
        if p_clean.startswith('•'):
            for line in p_clean.split('\n'):
                story.append(Paragraph(line.strip(), bullet_style))
        else:
            story.append(Paragraph(p_clean.replace('\n', '<br/>'), a_style))

def add_hint(story, hint_text):
    story.append(Paragraph(f"<b>EXAM HINT TO REMEMBER:</b> {hint_text}", hint_style))

def make_table(data, col_widths=None):
    t = Table(data, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2B6CB0')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8.5),
        ('LEADING', (0, 0), (-1, -1), 11),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#FFFFFF')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.HexColor('#FFFFFF'), colors.HexColor('#F7FAFC')]),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#CBD5E0')),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
    ]))
    return t

def P(text, bold=False):
    st = ParagraphStyle('Cell', parent=a_style, fontSize=8.5, leading=11, fontName='Helvetica-Bold' if bold else 'Helvetica')
    return Paragraph(text, st)

def P_hdr(text):
    st = ParagraphStyle('CellHdr', parent=a_style, fontSize=8.5, leading=11, fontName='Helvetica-Bold', textColor=colors.white)
    return Paragraph(text, st)

print("Helper definitions ready.")
