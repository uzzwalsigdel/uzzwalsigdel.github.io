from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, HRFlowable, Spacer
from notes_base import title_style, subtitle_style, body_style, make_table, P, P_hdr
from bnk209_u1_to_u4 import build_bnk209_u1_to_u4
from bnk209_u5_to_u7 import build_bnk209_u5_to_u7
from bnk209_exam_bank import build_bnk209_exam_bank

output_filename = "BNK_209_Insurance_and_Risk_Management_Exam_Notes.pdf"

def add_page_number(canvas, doc):
    canvas.saveState()
    canvas.setFont('Helvetica', 8.5)
    canvas.setFillColor(colors.HexColor('#4A5568'))
    canvas.drawString(36, 18, "TU BBA 8th Semester — BNK 209: Insurance and Risk Management Comprehensive Exam Notes (Units 1–7)")
    canvas.drawRightString(A4[0] - 36, 18, f"Page {doc.page}")
    canvas.restoreState()

def main():
    doc = SimpleDocTemplate(
        output_filename, pagesize=A4, leftMargin=36, rightMargin=36, topMargin=36, bottomMargin=34,
        title="BNK 209: Insurance and Risk Management Comprehensive Exam Notes (BBA 8th Semester)", author="Hoplite"
    )
    story = []

    story.append(Paragraph("TRIBHUVAN UNIVERSITY — FACULTY OF MANAGEMENT", title_style))
    story.append(Paragraph(
        "BBA Eighth Semester — BNK 209: Insurance and Risk Management (48 LHs)<br/>"
        "COMPREHENSIVE EXAM REVISION NOTES, FIGURES, ACTUARIAL NUMERICALS &amp; QUESTION BANK",
        subtitle_style
    ))
    t_toc = make_table([
        [P_hdr("Unit / Section"), P_hdr("Official TU Syllabus Topics Covered in Full Detail"), P_hdr("Lecture Hours")],
        [P("Unit 1: Introduction to Risk", True), P("Meaning of risk vs. uncertainty; Objective vs. subjective risk; Peril vs. Hazard (Physical, Moral, Attitudinal/Morale, Legal); Classification of risk (Pure vs. Speculative, Diversifiable vs. Non-Diversifiable, Enterprise vs. Systemic [Figure 1.1 & table]); Personal risks; Commercial risks; Burden of risk on society."), P("5 LHs")],
        [P("Unit 2: Risk Management", True), P("Meaning; Pre-loss & Post-loss objectives; 6-Step Risk Management Process (Figure 2.1); 2x2 Frequency-Severity Matrix (Figure 2.2); Risk Control (Avoidance, Prevention, Reduction) vs. Risk Financing (Retention/Captives, Non-Insurance Transfer, Commercial Insurance); Loss Forecasting (Probability, Regression, Distributions); NPV analysis; RMIS, VaR, Risk Appetite vs. Tolerance, TRM vs. ERM."), P("6 LHs")],
        [P("Unit 3: The Insurance Device", True), P("Definition & 4 basic characteristics of insurance; 6 requirements of an ideally insurable risk (and why Catastrophic Losses challenge insurance); Law of Large Numbers in risk pooling; Adverse selection & 5 control tools; Insurance vs. Gambling & Hedging; Benefits and costs of insurance to society."), P("5 LHs")],
        [P("Unit 4: Legal Principles in Insurance", True), P("The 6 Fundamental Legal Principles (Figure 4.1: Utmost Good Faith [Representations, Concealment, Warranties], Insurable Interest, Indemnity [ACV & exceptions], Subrogation, Contribution, Proximate Cause); 4 legal contract requirements; 5 distinct legal characteristics; Law & the Insurance Agent; 4 basic policy parts (D-I-C-E); Endorsements vs. Riders; Deductibles; Coinsurance formula & worked examples."), P("5 LHs")],
        [P("Unit 5: Life Insurance", True), P("Meaning & importance; Premature death & 6 financial impacts; Amount of life insurance to own (Human Life Value [HLV] vs. Financial Needs Approach); Types of life insurance (Figure 5.1 & Term vs. Cash-Value table); Contractual provisions; Dividend, Nonforfeiture & Settlement options; Riders (CI, PTD/AD&D, Waiver); Nepal Income Tax Act rules; Actuarial life premium calculation."), P("10 LHs")],
        [P("Unit 6: Non-Life & Social Insurance", True), P("Life vs. Non-Life table; Commercial property & liability; Fire insurance ('Hostile Fire', policy types, rating factors & 4 rating methods: Judgment, Class, Schedule, Experience); Marine insurance (Hull, Cargo, General Average, LC role); Auto insurance & compulsory Third-Party Liability; Agriculture insurance in Nepal (80% subsidy); Social insurance (Nepal SSF 31% scheme)."), P("12 LHs")],
        [P("Unit 7: Government Regulation", True), P("5 reasons for insurance regulation; 3 methods of regulation; 7 areas of regulation; Insurance Act 2079 & role/functions of Nepal Insurance Authority (NIA / Beema Pradhikaran); Role of insurance in Nepal's financial development."), P("5 LHs")],
        [P("Section 8: Numericals, Q&As & Case Guide", True), P("Worked Actuarial Numericals (HLV, Needs Approach, 1-Yr Term NSP, Coinsurance, Contribution) + Top 25 Group A (2-Mark) Q&As + Group D (20-Mark) Case Study Playbook."), P("Exam Bonus")],
    ], col_widths=[110, 330, 60])
    story.append(t_toc)
    story.append(Spacer(1, 8))

    build_bnk209_u1_to_u4(story)
    build_bnk209_u5_to_u7(story)
    build_bnk209_exam_bank(story)

    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
    print("Built:", output_filename)

if __name__ == "__main__":
    main()
