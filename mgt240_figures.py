from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing, Rect, String, Line, Circle, PolyLine

def fig_sm_process():
    d = Drawing(500, 145)
    d.add(Rect(0, 0, 500, 145, fillColor=colors.HexColor('#F7FAFC'), strokeColor=colors.HexColor('#CBD5E0')))
    d.add(String(125, 130, "FIGURE 1.1: THE COMPREHENSIVE STRATEGIC MANAGEMENT PROCESS MODEL", fontName="Helvetica-Bold", fontSize=8.8, fillColor=colors.HexColor('#1A365D')))
    boxes = [
        (10, "1. Strategic Intent\nVision, Mission,\nGoals & Objectives"),
        (108, "2. Environmental Scan\nExternal (PESTEL/5F)\n& Internal (RBV/VCA)"),
        (206, "3. Strategy Formulation\nCorporate, Business &\nFunctional Choices"),
        (304, "4. Implementation\nStructure, Leadership,\nCulture & Resources"),
        (402, "5. Evaluation & Control\nPremise, Surveillance,\nAlert & Audit")
    ]
    for x, text in boxes:
        d.add(Rect(x, 55, 88, 60, fillColor=colors.HexColor('#1A365D'), strokeColor=colors.HexColor('#2B6CB0')))
        lines = text.split('\n')
        d.add(String(x + 5, 98, lines[0], fontName="Helvetica-Bold", fontSize=7.5, fillColor=colors.HexColor('#FEFCBF')))
        d.add(String(x + 5, 83, lines[1], fontName="Helvetica", fontSize=7, fillColor=colors.white))
        d.add(String(x + 5, 70, lines[2], fontName="Helvetica", fontSize=7, fillColor=colors.white))
    for x in [98, 196, 294, 392]:
        d.add(Line(x, 85, x + 10, 85, strokeColor=colors.HexColor('#C53030'), strokeWidth=2))
    # Feedback loop arrow at bottom
    d.add(Line(446, 55, 446, 22, strokeColor=colors.HexColor('#2B6CB0'), strokeWidth=1.5))
    d.add(Line(446, 22, 54, 22, strokeColor=colors.HexColor('#2B6CB0'), strokeWidth=1.5))
    d.add(Line(54, 22, 54, 55, strokeColor=colors.HexColor('#2B6CB0'), strokeWidth=1.5))
    d.add(String(145, 27, "<--- Continuous Strategic Feedback & Corrective Action Loop ---", fontName="Helvetica-Bold", fontSize=7.8, fillColor=colors.HexColor('#2B6CB0')))
    return d

def fig_levels_of_strategy():
    d = Drawing(500, 145)
    d.add(Rect(0, 0, 500, 145, fillColor=colors.HexColor('#F7FAFC'), strokeColor=colors.HexColor('#CBD5E0')))
    d.add(String(125, 130, "FIGURE 1.2: HIERARCHY / PYRAMID OF THREE LEVELS OF STRATEGY", fontName="Helvetica-Bold", fontSize=8.8, fillColor=colors.HexColor('#1A365D')))
    # Top Level: Corporate
    d.add(Rect(145, 92, 210, 30, fillColor=colors.HexColor('#1A365D'), strokeColor=colors.white))
    d.add(String(160, 108, "LEVEL 1: CORPORATE-LEVEL STRATEGY", fontName="Helvetica-Bold", fontSize=8, fillColor=colors.HexColor('#FEFCBF')))
    d.add(String(162, 97, "(CEO & Board: Stability, Growth, Retrenchment)", fontName="Helvetica", fontSize=7, fillColor=colors.white))
    # Middle Level: Business (SBUs)
    sbu_x = [40, 195, 350]
    for i, x in enumerate(sbu_x):
        d.add(Line(250, 92, x + 55, 78, strokeColor=colors.HexColor('#2D3748'), strokeWidth=1.2))
        d.add(Rect(x, 48, 110, 30, fillColor=colors.HexColor('#2B6CB0'), strokeColor=colors.white))
        d.add(String(x + 8, 64, f"LEVEL 2: SBU {i+1} STRATEGY", fontName="Helvetica-Bold", fontSize=7.5, fillColor=colors.white))
        d.add(String(x + 8, 53, "(Cost, Diff., Focus)", fontName="Helvetica", fontSize=6.8, fillColor=colors.HexColor('#EBF8FF')))
    # Bottom Level: Functional
    func_x = [15, 112, 209, 306, 403]
    funcs = ["Marketing", "Finance", "Operations", "HRM", "R&D / IT"]
    for x, fn in zip(func_x, funcs):
        d.add(Line(250, 48, x + 40, 34, strokeColor=colors.HexColor('#718096'), strokeWidth=0.9))
        d.add(Rect(x, 8, 82, 26, fillColor=colors.HexColor('#2F855A'), strokeColor=colors.white))
        d.add(String(x + 6, 22, f"LEVEL 3: {fn}", fontName="Helvetica-Bold", fontSize=7.2, fillColor=colors.white))
        d.add(String(x + 6, 12, "Functional Strategy", fontName="Helvetica", fontSize=6.5, fillColor=colors.HexColor('#F0FFF4')))
    return d

def fig_porters_five_forces():
    d = Drawing(500, 175)
    d.add(Rect(0, 0, 500, 175, fillColor=colors.HexColor('#F7FAFC'), strokeColor=colors.HexColor('#CBD5E0')))
    d.add(String(115, 160, "FIGURE 2.1: MICHAEL PORTER'S FIVE FORCES MODEL OF INDUSTRY ANALYSIS", fontName="Helvetica-Bold", fontSize=8.8, fillColor=colors.HexColor('#1A365D')))
    # Top: Potential Entrants
    d.add(Rect(160, 120, 180, 32, fillColor=colors.HexColor('#2B6CB0'), strokeColor=colors.HexColor('#1A365D')))
    d.add(String(172, 138, "1. THREAT OF NEW ENTRANTS", fontName="Helvetica-Bold", fontSize=7.8, fillColor=colors.white))
    d.add(String(172, 126, "(Entry Barriers: Scale, Capital, Brand, Law)", fontName="Helvetica", fontSize=6.8, fillColor=colors.HexColor('#EBF8FF')))
    # Center: Industry Rivalry
    d.add(Rect(155, 62, 190, 42, fillColor=colors.HexColor('#9B2C2C'), strokeColor=colors.HexColor('#1A365D')))
    d.add(String(165, 88, "5. INTENSITY OF RIVALRY AMONG", fontName="Helvetica-Bold", fontSize=8, fillColor=colors.white))
    d.add(String(175, 77, "EXISTING COMPETITORS", fontName="Helvetica-Bold", fontSize=8, fillColor=colors.white))
    d.add(String(163, 66, "(Number of Rivals, Growth, Fixed Cost, Exit)", fontName="Helvetica", fontSize=6.6, fillColor=colors.HexColor('#FED7D7')))
    # Bottom: Substitutes
    d.add(Rect(160, 10, 180, 32, fillColor=colors.HexColor('#2B6CB0'), strokeColor=colors.HexColor('#1A365D')))
    d.add(String(168, 28, "4. THREAT OF SUBSTITUTE PRODUCTS", fontName="Helvetica-Bold", fontSize=7.8, fillColor=colors.white))
    d.add(String(172, 16, "(Price-Performance Ceiling & Switching Cost)", fontName="Helvetica", fontSize=6.8, fillColor=colors.HexColor('#EBF8FF')))
    # Left: Suppliers
    d.add(Rect(10, 62, 125, 42, fillColor=colors.HexColor('#1A365D'), strokeColor=colors.HexColor('#2B6CB0')))
    d.add(String(16, 88, "3. BARGAINING POWER", fontName="Helvetica-Bold", fontSize=7.5, fillColor=colors.white))
    d.add(String(28, 77, "OF SUPPLIERS", fontName="Helvetica-Bold", fontSize=7.5, fillColor=colors.white))
    d.add(String(14, 66, "(Few Suppliers, Unique Input)", fontName="Helvetica", fontSize=6.5, fillColor=colors.HexColor('#BEE3F8')))
    # Right: Buyers
    d.add(Rect(365, 62, 125, 42, fillColor=colors.HexColor('#1A365D'), strokeColor=colors.HexColor('#2B6CB0')))
    d.add(String(371, 88, "2. BARGAINING POWER", fontName="Helvetica-Bold", fontSize=7.5, fillColor=colors.white))
    d.add(String(388, 77, "OF BUYERS", fontName="Helvetica-Bold", fontSize=7.5, fillColor=colors.white))
    d.add(String(370, 66, "(Bulk Volume, Low Switching)", fontName="Helvetica", fontSize=6.5, fillColor=colors.HexColor('#BEE3F8')))
    # Connecting Lines
    d.add(Line(250, 120, 250, 104, strokeColor=colors.HexColor('#C53030'), strokeWidth=2))
    d.add(Line(250, 42, 250, 62, strokeColor=colors.HexColor('#C53030'), strokeWidth=2))
    d.add(Line(135, 83, 155, 83, strokeColor=colors.HexColor('#C53030'), strokeWidth=2))
    d.add(Line(365, 83, 345, 83, strokeColor=colors.HexColor('#C53030'), strokeWidth=2))
    return d

def fig_value_chain():
    d = Drawing(500, 130)
    d.add(Rect(0, 0, 500, 130, fillColor=colors.HexColor('#F7FAFC'), strokeColor=colors.HexColor('#CBD5E0')))
    d.add(String(120, 116, "FIGURE 2.2: PORTER'S VALUE CHAIN MODEL (PRIMARY & SUPPORT ACTIVITIES)", fontName="Helvetica-Bold", fontSize=8.8, fillColor=colors.HexColor('#1A365D')))
    support_labels = [
        "Support 1: Firm Infrastructure (Corporate Planning, Finance, Accounting, Legal, Quality Management)",
        "Support 2: Human Resource Management (Recruitment, Hiring, Training, Development, Compensation)",
        "Support 3: Technology Development (R&D, Product Design, Process Automation, ERP/IT Systems)",
        "Support 4: Procurement (Purchasing Raw Materials, Machinery, Components, Vendor Management)"
    ]
    for i, lbl in enumerate(support_labels):
        y = 96 - i * 14
        d.add(Rect(10, y, 410, 13, fillColor=colors.HexColor('#EBF8FF'), strokeColor=colors.HexColor('#2B6CB0')))
        d.add(String(15, y + 3.5, lbl, fontName="Helvetica-Bold", fontSize=6.9, fillColor=colors.HexColor('#1A365D')))
    prim_labels = ["1. Inbound\nLogistics", "2. Operations\n(Mfg/Assy)", "3. Outbound\nLogistics", "4. Marketing\n& Sales", "5. After-Sales\nService"]
    for i, lbl in enumerate(prim_labels):
        x = 10 + i * 82
        d.add(Rect(x, 8, 81, 44, fillColor=colors.HexColor('#1A365D'), strokeColor=colors.white))
        lines = lbl.split('\n')
        d.add(String(x + 8, 30, lines[0], fontName="Helvetica-Bold", fontSize=7.5, fillColor=colors.white))
        d.add(String(x + 8, 18, lines[1], fontName="Helvetica", fontSize=7, fillColor=colors.HexColor('#BEE3F8')))
    d.add(Rect(422, 8, 68, 101, fillColor=colors.HexColor('#2F855A'), strokeColor=colors.HexColor('#1A365D')))
    d.add(String(434, 62, "PROFIT", fontName="Helvetica-Bold", fontSize=9.5, fillColor=colors.white))
    d.add(String(432, 48, "MARGIN", fontName="Helvetica-Bold", fontSize=9.5, fillColor=colors.white))
    return d

def fig_ansoff_and_clock():
    d = Drawing(500, 150)
    d.add(Rect(0, 0, 500, 150, fillColor=colors.HexColor('#F7FAFC'), strokeColor=colors.HexColor('#CBD5E0')))
    d.add(String(20, 135, "FIGURE 3.1: ANSOFF'S PRODUCT-MARKET MATRIX (2x2)", fontName="Helvetica-Bold", fontSize=8.2, fillColor=colors.HexColor('#1A365D')))
    # Ansoff 4 cells
    d.add(Rect(20, 75, 105, 50, fillColor=colors.HexColor('#C6F6D5'), strokeColor=colors.HexColor('#2D3748')))
    d.add(String(26, 108, "1. MARKET PENETRATION", fontName="Helvetica-Bold", fontSize=7.2, fillColor=colors.HexColor('#22543D')))
    d.add(String(26, 95, "(Existing Prod + Existing Mkt)", fontName="Helvetica", fontSize=6.5))
    d.add(String(26, 83, "Lowest Risk; Boost Share", fontName="Helvetica-Bold", fontSize=6.5))

    d.add(Rect(125, 75, 105, 50, fillColor=colors.HexColor('#FEFCBF'), strokeColor=colors.HexColor('#2D3748')))
    d.add(String(131, 108, "2. PRODUCT DEVELOPMENT", fontName="Helvetica-Bold", fontSize=7.2, fillColor=colors.HexColor('#744210')))
    d.add(String(131, 95, "(New Product + Existing Mkt)", fontName="Helvetica", fontSize=6.5))
    d.add(String(131, 83, "R&D, New Features/Models", fontName="Helvetica-Bold", fontSize=6.5))

    d.add(Rect(20, 20, 105, 55, fillColor=colors.HexColor('#EBF8FF'), strokeColor=colors.HexColor('#2D3748')))
    d.add(String(26, 56, "3. MARKET DEVELOPMENT", fontName="Helvetica-Bold", fontSize=7.2, fillColor=colors.HexColor('#2B6CB0')))
    d.add(String(26, 43, "(Existing Prod + New Market)", fontName="Helvetica", fontSize=6.5))
    d.add(String(26, 31, "New Provinces / Exports", fontName="Helvetica-Bold", fontSize=6.5))

    d.add(Rect(125, 20, 105, 55, fillColor=colors.HexColor('#FED7D7'), strokeColor=colors.HexColor('#2D3748')))
    d.add(String(135, 56, "4. DIVERSIFICATION", fontName="Helvetica-Bold", fontSize=7.5, fillColor=colors.HexColor('#822727')))
    d.add(String(131, 43, "(New Product + New Market)", fontName="Helvetica", fontSize=6.5))
    d.add(String(131, 31, "Related vs. Unrelated", fontName="Helvetica-Bold", fontSize=6.5))

    # Right: Bowman's Strategic Clock
    d.add(String(258, 135, "FIGURE 3.2: BOWMAN'S STRATEGIC CLOCK (8 POSITIONS)", fontName="Helvetica-Bold", fontSize=8.2, fillColor=colors.HexColor('#1A365D')))
    d.add(Circle(370, 72, 42, fillColor=colors.HexColor('#EDF2F7'), strokeColor=colors.HexColor('#2B6CB0'), strokeWidth=1.5))
    d.add(String(343, 75, "Perceived Value", fontName="Helvetica-Bold", fontSize=7, fillColor=colors.HexColor('#1A365D')))
    d.add(String(350, 64, "vs. Price", fontName="Helvetica-Bold", fontSize=7, fillColor=colors.HexColor('#1A365D')))
    clock_pts = [
        (345, 118, "Pos 3: Hybrid (Best Cost)"),
        (415, 102, "Pos 4: Differentiation"),
        (420, 72, "Pos 5: Focused Diff."),
        (405, 38, "Pos 6-8: Failure Zone!"),
        (252, 42, "Pos 1: No-Frills (Low P/Low V)"),
        (252, 92, "Pos 2: Low Price Leader")
    ]
    for cx, cy, lbl in clock_pts:
        d.add(String(cx, cy, lbl, fontName="Helvetica-Bold", fontSize=6.8, fillColor=colors.HexColor('#2D3748')))
    return d

def fig_bcg_ge_hofer():
    d = Drawing(500, 155)
    d.add(Rect(0, 0, 500, 155, fillColor=colors.HexColor('#F7FAFC'), strokeColor=colors.HexColor('#CBD5E0')))
    d.add(String(12, 140, "FIG 3.3: BCG MATRIX (2x2)", fontName="Helvetica-Bold", fontSize=8, fillColor=colors.HexColor('#1A365D')))
    # BCG
    d.add(Rect(12, 80, 65, 50, fillColor=colors.HexColor('#FEFCBF'), strokeColor=colors.black))
    d.add(String(24, 105, "STARS", fontName="Helvetica-Bold", fontSize=7.5))
    d.add(String(16, 90, "(Invest/Grow)", fontName="Helvetica", fontSize=6.2))
    d.add(Rect(77, 80, 65, 50, fillColor=colors.HexColor('#EBF8FF'), strokeColor=colors.black))
    d.add(String(82, 105, "QUESTION ?", fontName="Helvetica-Bold", fontSize=7.2))
    d.add(String(82, 90, "(Select/Divest)", fontName="Helvetica", fontSize=6.2))
    d.add(Rect(12, 25, 65, 55, fillColor=colors.HexColor('#C6F6D5'), strokeColor=colors.black))
    d.add(String(16, 52, "CASH COWS", fontName="Helvetica-Bold", fontSize=7.2))
    d.add(String(18, 37, "(Milk Cash)", fontName="Helvetica", fontSize=6.2))
    d.add(Rect(77, 25, 65, 55, fillColor=colors.HexColor('#FED7D7'), strokeColor=colors.black))
    d.add(String(95, 52, "DOGS", fontName="Helvetica-Bold", fontSize=7.5))
    d.add(String(85, 37, "(Divest/Liq.)", fontName="Helvetica", fontSize=6.2))

    # GE 9-cell
    d.add(String(158, 140, "FIG 3.4: GE 9-CELL SCREEN (3x3)", fontName="Helvetica-Bold", fontSize=8, fillColor=colors.HexColor('#1A365D')))
    ge_c = [
        [colors.HexColor('#C6F6D5'), colors.HexColor('#C6F6D5'), colors.HexColor('#FEFCBF')],
        [colors.HexColor('#C6F6D5'), colors.HexColor('#FEFCBF'), colors.HexColor('#FED7D7')],
        [colors.HexColor('#FEFCBF'), colors.HexColor('#FED7D7'), colors.HexColor('#FED7D7')]
    ]
    ge_t = [
        ["Grow/Build", "Grow/Build", "Hold/Select"],
        ["Grow/Build", "Hold/Select", "Harvest/Div"],
        ["Hold/Select", "Harvest/Div", "Harvest/Div"]
    ]
    for r in range(3):
        for c in range(3):
            x = 158 + c * 50
            y = 95 - r * 35
            d.add(Rect(x, y, 50, 35, fillColor=ge_c[r][c], strokeColor=colors.black))
            d.add(String(x + 4, y + 15, ge_t[r][c], fontName="Helvetica-Bold", fontSize=6.2))

    # Hofer 15-cell (5x3)
    d.add(String(325, 140, "FIG 3.5: HOFER'S 15-CELL EVOLUTION MATRIX (5x3)", fontName="Helvetica-Bold", fontSize=7.8, fillColor=colors.HexColor('#1A365D')))
    stages = ["1.Dev", "2.Growth", "3.Shake", "4.Mature", "5.Decline"]
    for r in range(5):
        y = 109 - r * 21
        d.add(String(322, y + 6, stages[r], fontName="Helvetica-Bold", fontSize=6.2))
        for c in range(3):
            x = 362 + c * 42
            d.add(Rect(x, y, 42, 21, fillColor=colors.white, strokeColor=colors.HexColor('#2B6CB0')))
            if (r, c) in [(0,0), (1,0), (2,1), (3,0), (4,2)]:
                d.add(Circle(x + 21, y + 10.5, 6, fillColor=colors.HexColor('#BEE3F8'), strokeColor=colors.HexColor('#1A365D')))
    d.add(String(366, 131, "Strong        Average        Weak", fontName="Helvetica-Bold", fontSize=6.5))
    return d

def fig_org_structures():
    d = Drawing(500, 145)
    d.add(Rect(0, 0, 500, 145, fillColor=colors.HexColor('#F7FAFC'), strokeColor=colors.HexColor('#CBD5E0')))
    d.add(String(15, 130, "FIG 4.1: SBU STRUCTURE (MULTI-BUSINESS)", fontName="Helvetica-Bold", fontSize=8, fillColor=colors.HexColor('#1A365D')))
    # Left: SBU Structure
    d.add(Rect(65, 98, 100, 22, fillColor=colors.HexColor('#1A365D'), strokeColor=colors.black))
    d.add(String(75, 106, "Corporate CEO / HQ", fontName="Helvetica-Bold", fontSize=7.2, fillColor=colors.white))
    for i, lbl in enumerate(["SBU A", "SBU B", "SBU C"]):
        x = 12 + i * 72
        d.add(Line(115, 98, x + 32, 72, strokeColor=colors.black, strokeWidth=1))
        d.add(Rect(x, 50, 64, 22, fillColor=colors.HexColor('#2B6CB0'), strokeColor=colors.black))
        d.add(String(x + 16, 58, lbl, fontName="Helvetica-Bold", fontSize=7.2, fillColor=colors.white))
        d.add(Line(x + 32, 50, x + 32, 34, strokeColor=colors.black, strokeWidth=1))
        d.add(Rect(x, 14, 64, 20, fillColor=colors.HexColor('#EDF2F7'), strokeColor=colors.black))
        d.add(String(x + 6, 21, "Prod|Mkt|Fin", fontName="Helvetica", fontSize=6.5))

    # Right: Matrix Structure (Dual Command)
    d.add(String(265, 130, "FIG 4.2: MATRIX STRUCTURE (DUAL COMMAND GRID)", fontName="Helvetica-Bold", fontSize=8, fillColor=colors.HexColor('#1A365D')))
    funcs = ["R&D", "Engg", "Mktg", "Fin"]
    for c, fn in enumerate(funcs):
        x = 325 + c * 40
        d.add(Rect(x, 100, 36, 20, fillColor=colors.HexColor('#1A365D'), strokeColor=colors.black))
        d.add(String(x + 7, 107, fn, fontName="Helvetica-Bold", fontSize=6.8, fillColor=colors.white))
        d.add(Line(x + 18, 100, x + 18, 18, strokeColor=colors.HexColor('#2B6CB0'), strokeWidth=1))
    projs = ["Proj 1", "Proj 2", "Proj 3"]
    for r, pr in enumerate(projs):
        y = 72 - r * 26
        d.add(Rect(265, y, 48, 18, fillColor=colors.HexColor('#2F855A'), strokeColor=colors.black))
        d.add(String(272, y + 6, pr, fontName="Helvetica-Bold", fontSize=6.8, fillColor=colors.white))
        d.add(Line(313, y + 9, 475, y + 9, strokeColor=colors.HexColor('#2F855A'), strokeWidth=1))
        for c in range(4):
            x = 325 + c * 40
            d.add(Circle(x + 18, y + 9, 4, fillColor=colors.HexColor('#FEFCBF'), strokeColor=colors.black))
    return d
