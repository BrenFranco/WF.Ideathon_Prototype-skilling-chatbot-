import streamlit as st

st.set_page_config(
    page_title="Wadhwani Foundation Dictionary",
    layout="centered"
)

# --- LOGO ---
st.image("assets/wf_color.png", width=280)

# --- TITLE ---
st.title("Wadhwani Foundation Dictionary")
st.caption("Interactive Prototype • Ideathon Demo")

# --- INTRO ---
st.markdown("""
This prototype demonstrates a **centralized dictionary and chatbot experience**
designed to align how **operating, reporting, and technical terms** are understood
across the **Wadhwani Foundation**.

The goal is to create a **single source of truth** for terminology used in:
- KPIs and scorecards  
- Impact and skilling reports  
- Dashboards and internal reviews  
""")

st.divider()

# --- CHAT INPUT ---
user_input = st.text_input("💬 Type anything to interact with the dictionary:")

# --- CONSTANT DEMO RESPONSE ---
if user_input and user_input.strip().lower() != "explain transformations":
    st.markdown("### 🤖 Dictionary Assistant")

    st.info("""
### 👋 Welcome!

This is the **Wadhwani Foundation Dictionary** prototype.

#### 🧠 Purpose of this project
- Create **consistent definitions** for terms used across the Foundation
- Reduce confusion in reporting, reviews, and dashboards
- Help teams, leaders, and new joiners **speak the same language**

#### ⚙️ How the full version will work
- Users ask about a term (e.g. *Enabled*, *Transformations*, *Placements*)
- The system searches **official Impact-owned documents**
- It returns a **clear, standardized explanation**
- Related terms and reporting context are shown

#### 📘 Current scope of information
The terminology demonstrated in this prototype is based on **Impact documentation**, including:
- Skilling Metrics & Data Collection Methodology (CY26)
- Skilling Month-End Report (March 2026)

✅ **This is a demonstration prototype.**  
✅ Any input currently returns this explanation intentionally.

---

### ⌨️ Demo instruction
To see a **sample term explanation**, please type exactly:

**Explain Transformations**
""")

# --- TRANSFORMATIONS EXPLANATION ---
if user_input.strip().lower() == "explain transformations":
    st.markdown("### 📘 Term Explanation: Transformations")

    st.success("""
### ✅ Transformations (Skilling – Impact Definition)

**Transformations** refer to learners who have completed the **full structured skilling journey**
and have demonstrated **minimum viable employability readiness**, based on defined quality and
assessment standards.

#### 🔍 How a learner is classified as Transformed
A learner is considered **Transformed** only when **all mandatory components** are completed
and passed:

1. **Pre/Post Video Assessment**
   - Minimum score of **3 out of 5**

2. **Collaborate Activities**
   - At least **70% of required reflections passed**

3. **Full Course MCQ Assessments**
   - Both **Formative (FA)** and **Summative (SA)** assessments
   - Minimum **70% score in each**

> Interview Preparation may become part of the criteria once fully integrated.

#### 🎯 What Transformations signal
- High-confidence employability readiness
- Completion of the **entire skilling pathway**
- Strongest quality indicator used by Impact

#### 📊 Reporting & ownership
- Transformations are tracked via **platform analytics**
- Criteria are **defined and frozen for CY26**
- Applicable only to **cohort-based, full-course learners**
- Used in downstream **placement and impact calculations**

#### 📘 Source
This definition is based on **Impact-owned documentation**, including:
- Skilling Metrics & Data Collection Methodology (CY26)
- Skilling Month-End Reporting (March 2026)

✅ *This explanation reflects the current information available from Impact documents.*
""")
