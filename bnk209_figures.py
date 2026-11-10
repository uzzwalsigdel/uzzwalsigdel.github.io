from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing, Rect, String, Line, Circle

def fig_risk_classification():
    d = Drawing(500, 145)
    d.add(Rect(0, 0, 500, 145, fillColor=colors.HexColor('#F7FAFC'), strokeColor=colors.HexColor('#CBD5E0')))
    d.add(String(120, 130, "FIGURE 1.1: CLASSIFICATION OF RISK & LOSS EXPOSURES IN RISK MANAGEMENT", fontName="Helvetica-Bold", fontSize=8.5, fillColor=colors.HexColor('#1A365D')))
    # Top Node
    d.add(Rect(175, 98, 150, 24, fillColor=colors.HexColor('#1A365D'), strokeColor=colors.black))
    d.add(String(192, 107, "TOTAL RISK EXPOSURES", fontName="Helvetica-Bold", fontSize=8, fillColor=colors.white))
    # 4 Main Branches
    branches = [
        (10, "1. Pure vs. Speculative", "Pure: Loss/No Loss (Insurable)\nSpeculative: Loss/Gain (Hedging)"),
        (132, "2. Diversifiable vs. Non-Div", "Diversifiable: Individual/Poolable\nNon-Div: Macro/Systemic"),
        (254, "3. Personal Risks", "Premature Death, Old Age,\nPoor Health, Unemployment"),
        (376, "4. Commercial / Enterprise", "Property, Liability, Business\nInterruption, Cyber, Strategic")
    ]
    for x, title, sub in branches:
        d.add(Line(250, 98, x + 57, 74, strokeColor=colors.HexColor('#2B6CB0'), strokeWidth=1.2))
        d.add(Rect(x, 48, 114, 26, fillColor=colors.HexColor('#2B6CB0'), strokeColor=colors.black))
        d.add(String(x + 5, 58, title, fontName="Helvetica-Bold", fontSize=7, fillColor=colors.white))
        d.add(Line(x + 57, 48, x + 57, 38, strokeColor=colors.black, strokeWidth=1))
        d.add(Rect(x, 8, 114, 30, fillColor=colors.white, strokeColor=colors.HexColor('#CBD5E0')))
        lns = sub.split('\n')
        d.add(String(x + 4, 24, lns[0], fontName="Helvetica", fontSize=6.3, fillColor=colors.HexColor('#1A202C')))
        d.add(String(x + 4, 13, lns[1], fontName="Helvetica", fontSize=6.3, fillColor=colors.HexColor('#2D3748')))
    return d

def fig_rm_process_and_matrix():
    d = Drawing(500, 150)
    d.add(Rect(0, 0, 500, 150, fillColor=colors.HexColor('#F7FAFC'), strokeColor=colors.HexColor('#CBD5E0')))
    d.add(String(14, 136, "FIG 2.1: 6-STEP RISK MANAGEMENT PROCESS", fontName="Helvetica-Bold", fontSize=8, fillColor=colors.HexColor('#1A365D')))
    steps = [
        "1. Set Pre-Loss & Post-Loss Objectives",
        "2. Identify All Loss Exposures",
        "3. Measure Frequency & Severity (Forecasting)",
        "4. Select Risk Control & Financing Tools",
        "5. Implement the Risk Management Program",
        "6. Monitor, Audit & Review via RMIS"
    ]
    for i, st in enumerate(steps):
        y = 114 - i * 19
        d.add(Rect(14, y, 185, 16, fillColor=colors.HexColor('#1A365D') if i%2==0 else colors.HexColor('#2B6CB0'), strokeColor=colors.white))
        d.add(String(20, y + 4.5, st, fontName="Helvetica-Bold", fontSize=6.8, fillColor=colors.white))

    # Right: 2x2 Risk Treatment Matrix
    d.add(String(225, 136, "FIG 2.2: FREQUENCY vs. SEVERITY RISK MATRIX (4 QUADRANTS)", fontName="Helvetica-Bold", fontSize=8, fillColor=colors.HexColor('#1A365D')))
    d.add(Rect(225, 72, 130, 55, fillColor=colors.HexColor('#EBF8FF'), strokeColor=colors.black))
    d.add(String(231, 112, "Q1: LOW Freq + LOW Sev", fontName="Helvetica-Bold", fontSize=7.2, fillColor=colors.HexColor('#2B6CB0')))
    d.add(String(231, 96, "Action: RETENTION", fontName="Helvetica-Bold", fontSize=7.2))
    d.add(String(231, 82, "(Self-insure / Absorb)", fontName="Helvetica", fontSize=6.5))

    d.add(Rect(355, 72, 135, 55, fillColor=colors.HexColor('#FEFCBF'), strokeColor=colors.black))
    d.add(String(361, 112, "Q2: HIGH Freq + LOW Sev", fontName="Helvetica-Bold", fontSize=7.2, fillColor=colors.HexColor('#744210')))
    d.add(String(361, 96, "Action: LOSS PREVENTION", fontName="Helvetica-Bold", fontSize=7.2))
    d.add(String(361, 82, "+ Retention / Deductible", fontName="Helvetica", fontSize=6.5))

    d.add(Rect(225, 15, 130, 57, fillColor=colors.HexColor('#C6F6D5'), strokeColor=colors.black))
    d.add(String(231, 56, "Q3: LOW Freq + HIGH Sev", fontName="Helvetica-Bold", fontSize=7.2, fillColor=colors.HexColor('#22543D')))
    d.add(String(231, 40, "Action: COMMERCIAL", fontName="Helvetica-Bold", fontSize=7.2))
    d.add(String(231, 26, "INSURANCE (Transfer!)", fontName="Helvetica-Bold", fontSize=7))

    d.add(Rect(355, 15, 135, 57, fillColor=colors.HexColor('#FED7D7'), strokeColor=colors.black))
    d.add(String(361, 56, "Q4: HIGH Freq + HIGH Sev", fontName="Helvetica-Bold", fontSize=7.2, fillColor=colors.HexColor('#822727')))
    d.add(String(361, 40, "Action: AVOIDANCE", fontName="Helvetica-Bold", fontSize=7.2))
    d.add(String(361, 26, "(Abandon Activity!)", fontName="Helvetica", fontSize=6.5))
    return d

def fig_legal_principles():
    d = Drawing(500, 125)
    d.add(Rect(0, 0, 500, 125, fillColor=colors.HexColor('#F7FAFC'), strokeColor=colors.HexColor('#CBD5E0')))
    d.add(String(115, 110, "FIGURE 4.1: THE SIX FUNDAMENTAL LEGAL PRINCIPLES OF INSURANCE CONTRACTS", fontName="Helvetica-Bold", fontSize=8.5, fillColor=colors.HexColor('#1A365D')))
    principles = [
        (10, "1. Utmost Good Faith", "Uberrimae Fidei:\n• Representations\n• Concealment\n• Warranties"),
        (90, "2. Insurable Interest", "Pecuniary stake:\n• Life: At Inception\n• Property: At Loss\n• Stops Gambling"),
        (170, "3. Indemnity", "Restore pre-loss\nposition only:\n• ACV = RC - Dep.\n• No profit on loss"),
        (250, "4. Subrogation", "Insurer steps into\ninsured's shoes to\nsue negligent 3rd\nparty after paying"),
        (330, "5. Contribution", "Double insurance\npro-rata sharing:\nPolicy / Total\nLimits x Loss"),
        (410, "6. Proximate Cause", "Causa Proxima:\nActive, dominant\nefficient cause must\nbe insured peril")
    ]
    for x, title, body in principles:
        d.add(Rect(x, 76, 77, 24, fillColor=colors.HexColor('#1A365D'), strokeColor=colors.white))
        d.add(String(x + 4, 85, title, fontName="Helvetica-Bold", fontSize=6.7, fillColor=colors.HexColor('#FEFCBF')))
        d.add(Rect(x, 12, 77, 64, fillColor=colors.white, strokeColor=colors.HexColor('#2B6CB0')))
        for idx, ln in enumerate(body.split('\n')):
            d.add(String(x + 4, 62 - idx * 13, ln, fontName="Helvetica", fontSize=6.3, fillColor=colors.HexColor('#2D3748')))
    return d

def fig_life_insurance_types():
    d = Drawing(500, 125)
    d.add(Rect(0, 0, 500, 125, fillColor=colors.HexColor('#F7FAFC'), strokeColor=colors.HexColor('#CBD5E0')))
    d.add(String(120, 110, "FIGURE 5.1: TAXONOMY OF LIFE INSURANCE POLICIES & ACTUARIAL RATE MAKING", fontName="Helvetica-Bold", fontSize=8.5, fillColor=colors.HexColor('#1A365D')))
    # Left: Term vs Cash Value
    d.add(Rect(12, 72, 225, 28, fillColor=colors.HexColor('#2B6CB0'), strokeColor=colors.black))
    d.add(String(20, 83, "1. TERM LIFE INSURANCE (Pure Protection, No Savings)", fontName="Helvetica-Bold", fontSize=7.2, fillColor=colors.white))
    d.add(Rect(12, 12, 225, 60, fillColor=colors.white, strokeColor=colors.HexColor('#CBD5E0')))
    d.add(String(18, 56, "• Yearly Renewable, 5/10/20/25-Yr Level Term, Decreasing Term", fontName="Helvetica", fontSize=6.6))
    d.add(String(18, 43, "• Lowest premium per Rs 1,000 coverage; Zero Cash Value", fontName="Helvetica", fontSize=6.6))
    d.add(String(18, 30, "• Ideal for young families with mortgages & CA investors", fontName="Helvetica", fontSize=6.6))
    d.add(String(18, 17, "• Add Riders: Critical Illness (CI), PTD/AD&D, Waiver of Prem.", fontName="Helvetica-Bold", fontSize=6.6, fillColor=colors.HexColor('#22543D')))

    # Right: Cash Value Life Insurance
    d.add(Rect(255, 72, 233, 28, fillColor=colors.HexColor('#2F855A'), strokeColor=colors.black))
    d.add(String(262, 83, "2. CASH-VALUE LIFE INSURANCE (Protection + Savings)", fontName="Helvetica-Bold", fontSize=7.2, fillColor=colors.white))
    d.add(Rect(255, 12, 233, 60, fillColor=colors.white, strokeColor=colors.HexColor('#CBD5E0')))
    d.add(String(261, 56, "• Whole Life (Ordinary, Limited-Pay), Endowment, Child Plan", fontName="Helvetica", fontSize=6.6))
    d.add(String(261, 43, "• Universal Life, Variable Life, Money-Back Endowment", fontName="Helvetica", fontSize=6.6))
    d.add(String(261, 30, "• Builds guaranteed Cash Surrender Value + Vested Bonus", fontName="Helvetica", fontSize=6.6))
    d.add(String(261, 17, "• Policy Loan (80–90% of CSV) & Nonforfeiture Options", fontName="Helvetica-Bold", fontSize=6.6, fillColor=colors.HexColor('#1A365D')))
    return d
