from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable, KeepTogether
)
from reportlab.graphics.shapes import Drawing, Rect, String, Line, Circle, PolyLine

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    'DocTitle', parent=styles['Title'], fontName='Helvetica-Bold', fontSize=20,
    leading=25, textColor=colors.HexColor('#1A365D'), alignment=1, spaceAfter=8
)
subtitle_style = ParagraphStyle(
    'DocSubTitle', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=12.5,
    leading=17, textColor=colors.HexColor('#2B6CB0'), alignment=1, spaceAfter=12
)
unit_style = ParagraphStyle(
    'UnitHeader', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=14.5,
    leading=19, textColor=colors.white, backColor=colors.HexColor('#1A365D'),
    borderPadding=8, spaceBefore=10, spaceAfter=10
)
topic_style = ParagraphStyle(
    'TopicHeader', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=11.8,
    leading=15.5, textColor=colors.HexColor('#1A365D'), backColor=colors.HexColor('#E2E8F0'),
    borderPadding=5.5, spaceBefore=10, spaceAfter=5
)
subtopic_style = ParagraphStyle(
    'SubTopicHeader', parent=styles['Heading3'], fontName='Helvetica-Bold', fontSize=10.5,
    leading=14, textColor=colors.HexColor('#2B6CB0'), spaceBefore=7, spaceAfter=3
)
body_style = ParagraphStyle(
    'BodyStyle', parent=styles['Normal'], fontName='Helvetica', fontSize=10,
    leading=14.5, textColor=colors.HexColor('#2D3748'), spaceBefore=2.5, spaceAfter=4
)
bullet_style = ParagraphStyle(
    'BulletStyle', parent=body_style, leftIndent=16, firstLineIndent=-9, spaceBefore=1.5, spaceAfter=2.5
)
example_style = ParagraphStyle(
    'ExampleStyle', parent=styles['Normal'], fontName='Helvetica', fontSize=9.6,
    leading=14, textColor=colors.HexColor('#22543D'), backColor=colors.HexColor('#F0FFF4'),
    borderPadding=6, spaceBefore=4, spaceAfter=6
)
tip_style = ParagraphStyle(
    'TipStyle', parent=styles['Normal'], fontName='Helvetica-Oblique', fontSize=9.5,
    leading=13.8, textColor=colors.HexColor('#744210'), backColor=colors.HexColor('#FEFCBF'),
    borderPadding=6, spaceBefore=4, spaceAfter=8
)

def add_unit(story, text):
    story.append(Paragraph(text, unit_style))

def add_topic(story, text):
    story.append(Paragraph(text, topic_style))

def add_subtopic(story, text):
    story.append(Paragraph(text, subtopic_style))

def add_body(story, text):
    for p in text.strip().split('\n\n'):
        p_clean = p.strip()
        if not p_clean:
            continue
        if p_clean.startswith('•'):
            for line in p_clean.split('\n'):
                story.append(Paragraph(line.strip(), bullet_style))
        else:
            story.append(Paragraph(p_clean.replace('\n', '<br/>'), body_style))

def add_example(story, text):
    story.append(Paragraph(f"<b>PRACTICAL / NEPAL CORPORATE EXAMPLE:</b><br/>{text.replace(chr(10), '<br/>')}", example_style))

def add_tip(story, text):
    story.append(Paragraph(f"<b>EXAM MEMORY TIP / MNEMONIC:</b> {text}", tip_style))

def make_table(data, col_widths=None):
    t = Table(data, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2B6CB0')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('LEADING', (0, 0), (-1, -1), 12),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.HexColor('#FFFFFF'), colors.HexColor('#F7FAFC')]),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#CBD5E0')),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 4.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 5.5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5.5),
    ]))
    return t

def P(text, bold=False):
    st = ParagraphStyle('Cell', parent=body_style, fontSize=9, leading=12, fontName='Helvetica-Bold' if bold else 'Helvetica')
    return Paragraph(text, st)

def P_hdr(text):
    st = ParagraphStyle('CellHdr', parent=body_style, fontSize=9, leading=12, fontName='Helvetica-Bold', textColor=colors.white)
    return Paragraph(text, st)
