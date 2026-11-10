from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, HRFlowable, Spacer
from notes_base import title_style, subtitle_style, body_style, make_table, P, P_hdr
from mgt240_u1_u2 import build_mgt240_u1_u2
from mgt240_u3_u4_u5 import build_mgt240_u3_u4_u5
from mgt240_exam_bank import build_mgt240_exam_bank

output_filename = "MGT_240_Strategic_Management_Exam_Notes.pdf"

def add_page_number(canvas, doc):
    canvas.saveState()
    canvas.setFont('Helvetica', 8.5)
    canvas.setFillColor(colors.HexColor('#4A5568'))
    canvas.drawString(36, 18, "TU BBA 8th Semester — MGT 240: Strategic Management Comprehensive Exam Notes (Units 1–5 + Question Bank)")
    canvas.drawRightString(A4[0] - 36, 18, f"Page {doc.page}")
    canvas.restoreState()

def main():
    doc = SimpleDocTemplate(
        output_filename, pagesize=A4, leftMargin=36, rightMargin=36, topMargin=36, bottomMargin=34,
        title="MGT 240: Strategic Management Comprehensive Exam Notes (BBA 8th Semester)", author="Hoplite"
    )
    story = []

    story.append(Paragraph("TRIBHUVAN UNIVERSITY — FACULTY OF MANAGEMENT", title_style))
    story.append(Paragraph(
        "BBA Eighth Semester — MGT 240: Strategic Management (48 LHs)<br/>"
        "COMPREHENSIVE EXAM REVISION NOTES, FIGURES, EXAMPLES &amp; QUESTION BANK",
        subtitle_style
    ))
    t_toc = make_table([
        [P_hdr("Unit / Section"), P_hdr("Official TU Syllabus Topics Covered in Full Detail"), P_hdr("Lecture Hours")],
        [P("Unit 1: Introduction", True), P("Concept, features & importance of strategy & strategic management; 4 phases of evolution; elements & 5-step process model (with Figure 1.1); need for strategy; 3 levels of strategy (with Figure 1.2 & table); strategic planning; Vision (Collins & Porras), Mission (Fred David's 9 components), SMART Objectives; role of information."), P("9 LHs")],
        [P("Unit 2: Environment & Strategy Analysis", True), P("Internal & external environment layers; PESTEL analysis table; Porter's Five Forces Model (with Figure 2.1); ETOP matrix example; Scenario planning; Competitor & Strategic Group analysis; Hyper-competition; RBV, Threshold vs. Strategic Resources & VRIO table; Porter's Value Chain Analysis (with Figure 2.2); Historical, Industry Norms & Benchmarking; SAP table; SWOT/TOWS matrix."), P("10 LHs")],
        [P("Unit 3: Strategy Formulation", True), P("Concept & importance; Corporate Grand Strategies (Stability, Ansoff's 4 Growth Directions [Figure 3.1], Vertical/Horizontal Integration, Related/Unrelated Diversification, Retrenchment [Turnaround, Divestment, Liquidation], Combination); Business-Level Strategies (Porter's Generic Strategies & Bowman's 8-Position Strategic Clock [Figure 3.2]); Functional Strategies (Marketing, Finance, Operations, HRM, R&D table); Methods (Internal, M&A, Alliances); Portfolio Matrices (BCG 2x2, GE 3x3, Hofer's 5x3 [Figures 3.3–3.5]); SFA Criteria."), P("12 LHs")],
        [P("Unit 4: Strategy Implementation", True), P("Concept & Formulation vs. Implementation table; 7 Organizational Structures (Simple, Functional, Multidivisional, SBU [Figure 4.1], Matrix [Figure 4.2], Holding Company, Project/Team/Network); process & requirements (structure, resources, management systems); Strategic Leadership roles & capabilities."), P("10 LHs")],
        [P("Unit 5: Strategic Evaluation & Control", True), P("Concept; Strategic vs. Operational Control table; 4 Types of Strategic Control (Premise, Surveillance, Special Alert, Implementation); 6-step process; Strategic Audit; Strategic Information System (SIS); guidelines for effective control."), P("7 LHs")],
        [P("Section 6: Exam Question Bank & Case Playbook", True), P("Top 25 Rapid-Fire Group A (2-Mark) Q&As + Group B/C Analytical Writing Structure + Step-by-Step Group D (20-Mark) Case Study Solving Playbook."), P("Exam Bonus")],
    ], col_widths=[110, 330, 60])
    story.append(t_toc)
    story.append(Spacer(1, 8))

    build_mgt240_u1_u2(story)
    build_mgt240_u3_u4_u5(story)
    build_mgt240_exam_bank(story)

    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
    print("Built:", output_filename)

if __name__ == "__main__":
    main()
