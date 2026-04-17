import streamlit as st

st.set_page_config(
    page_title="Wadhwani Foundation Dictionary",
    layout="centered"
)

# --- LOGO ---
st.image("assets/wf_color.png", width=260)

# --- TITLE ---
st.title("Wadhwani Foundation Dictionary")
st.caption("Interactive Prototype • Ideathon Demo")

st.markdown("""
A centralized dictionary designed to align how **operating, reporting, and technical terms**
are defined and understood across the **Wadhwani Foundation**.
""")

# --- TABS ---
tab1, tab2 = st.tabs(["💬 Dictionary Demo", "📘 Terminology Summary"])

# =========================
# TAB 1 — CHAT DEMO
# =========================
with tab1:
    st.divider()

    st.markdown("""
    **How to use this demo**
    - Type *anything* to understand what this project does
    - For the guided demo, type one of the following **exactly**:
      - **Explain Transformations**
      - **Explain Enabled**
      - **Explain Engaged**
      - **Explain Placements**
    """)

    user_input = st.text_input("💬 Type here:")

    # ---------- CONSTANT DEMO RESPONSE ----------
    if user_input and user_input.strip().lower() not in [
        "explain transformations",
        "explain enabled",
        "explain engaged",
        "explain placements",
    ]:
        st.info("""
### 🤖 Dictionary Assistant (Demo Response)

Welcome to the **Wadhwani Foundation Dictionary**.

#### 🎯 Purpose
This initiative creates a **single source of truth** for terminology used across the Foundation,
reducing ambiguity in:
- KPIs and scorecards
- Impact and skilling reports
- Dashboards and leadership reviews

#### ⚙️ How the full version will work
- Users ask about a specific term
- The system retrieves definitions from **official Impact documents**
- Clear explanations, context, and related terms are returned

#### 📘 Current scope
The terminology demonstrated here is based on **Impact-owned Skilling documentation**, including:
- Skilling Metrics & Data Collection Methodology (CY26)
- Skilling Month-End Report (March 2026)

✅ **This is a prototype for demonstration purposes.**  
✅ All non-demo inputs intentionally return this explanation.
""")

    # ---------- TRANSFORMATIONS ----------
    if user_input.strip().lower() == "explain transformations":
        st.success("""
### 📌 Transformations

**Transformations** represent learners who have completed the **full structured skilling journey**
and met defined quality and assessment standards, indicating **high-confidence employability readiness**.

#### Criteria
All mandatory components must be completed and passed:
- Pre/Post Video: ≥ 3/5
- Collaborate reflections: ≥ 70% passed
- Full Course MCQs (FA & SA): ≥ 70% in each

#### What it signals
- Highest quality learning outcome
- Strongest indicator used by Impact
- Input to downstream placement and impact calculations

**Source:** Impact – Skilling Methodology (CY26), March 2026 Reporting
""")

    # ---------- ENABLED ----------
    if user_input.strip().lower() == "explain enabled":
        st.success("""
### 📌 Enabled

**Enabled learners** are those who demonstrate **meaningful capability building**
but have not completed full transformation requirements.

#### Criteria
- Score ≥ 50 points across defined learning components
- Does not require completion of the full transformation checklist

#### What it signals
- Strong engagement and skill exposure
- Primary pool for placement enablement and follow-on support

**Source:** Impact – Skilling Methodology (CY26)
""")

    # ---------- ENGAGED ----------
    if user_input.strip().lower() == "explain engaged":
        st.success("""
### 📌 Engaged

**Engaged learners** show active participation beyond registration but
have not yet reached enablement thresholds.

#### Criteria
- Score between 30–49 points across learning components

#### What it signals
- Early-stage engagement
- Key cohort for nudges and activation strategies

**Source:** Impact – Skilling Methodology (CY26)
""")

    # ---------- PLACEMENTS ----------
    if user_input.strip().lower() == "explain placements":
        st.success("""
### 📌 Placements

**Placements** refer to learners securing employment after skilling participation,
tracked across multiple pathways.

#### Key concepts
- Tracked after defined eligibility windows
- Includes total placements and attributable incremental placements
- Used to measure outcome-level impact

#### Reporting ownership
- Validated through surveys and attribution logic
- Governed by Impact-defined methodologies

**Source:** Impact – Skilling Month-End Report (March 2026)
""")

# =========================
# TAB 2 — TERMINOLOGY SUMMARY
# =========================
with tab2:
    st.divider()

    st.markdown("""
### 📘 Terminology Summary (Current Scope)

This dictionary currently covers **Impact-owned Skilling terminology**, including:

#### Learner Classifications
- **Transformations** – Full journey completion with high employability readiness  
- **Enabled** – Meaningful capability building without full transformation  
- **Engaged** – Active participation below enablement threshold  

#### Metric Types
- **Inputs** – Enrolments and participation signals  
- **Outputs** – Enabled and Transformed learners  
- **Outcomes** – Placements and incremental impact  

#### Governance
- Definitions are **centrally defined by Impact**
- Methodologies are **frozen for CY26**
- Reporting aligns to **monthly and YTD reviews**

✅ This prototype demonstrates how these terms can be accessed
through a **single, consistent interface**.

🚀 Future versions will expand coverage across programs and regions.
""")
``
