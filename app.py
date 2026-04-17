import streamlit as st
import time

st.set_page_config(
    page_title="Wadhwani Foundation Terminology Dictionary",
    layout="centered"
)

# Logo
st.image("assets/wf_color.png", width=300)

# Title
st.title("Wadhwani Foundation Terminology Dictionary")
st.caption("Interactive UX Prototype • Ideathon Demo")

st.markdown("""
This prototype demonstrates a **centralized terminology chatbot** designed to align how
operating, reporting, and technical terms are understood across the **Wadhwani Foundation**.
""")

st.divider()

# DEMO NOTICE (VERY CLEAR)
st.warning("""
⚠️ **Demonstration Prototype Only**

This is a **UX and concept demo**.
- Any question typed will return the **same explanatory response**
- The AI-powered logic is intentionally disabled for stability
- The purpose is to showcase **experience, value, and feasibility**
""")

# Chat input
user_input = st.text_input("💬 Ask anything about WF terms, KPIs, or reports:")

if user_input:
    with st.spinner("Responding..."):
        time.sleep(1)

    st.markdown("### 🤖 Assistant")

    st.success("""
### 👋 Welcome to the Wadhwani Foundation Terminology Dictionary

This tool is envisioned as a **single source of truth** for how key terms are defined,
used, and interpreted across the Foundation.

---

### 🎯 What this dictionary covers
- **Operating terms** used by program and delivery teams  
- **Reporting and KPI terminology** used in Impact reviews and dashboards  
- **Technical and metric definitions** used in analysis and Power BI  

---

### 📘 Current scope of information (Prototype)
The terminology framework demonstrated here is based on **Impact-owned documents**, including:
- Skilling Metrics & Data Collection Methodology (CY26)
- Skilling Month-End Reporting (March 2026)

These documents define terms such as:
- Learner classifications (e.g., Transformed, Enabled, Engaged)
- Input, Output, and Outcome metrics
- Placement and attribution concepts
- Reporting and methodology rules used by Impact teams

---

### 🚀 In the full AI-enabled version
- Users will receive **term-specific answers**
- Definitions will be pulled directly from **official WF documents**
- Related terms and usage context will be surfaced automatically
- Updates will reflect the **latest approved methodologies**

---

✅ *This response is intentionally the same for all inputs and is shown for demonstration purposes only.*
""")

    st.divider()

    st.markdown("#### 🔍 Example questions this tool will support:")
    st.markdown("""
- What does *Enabled* vs *Transformed* mean?  
- How are placements attributed?  
- Which metrics count as outputs vs outcomes?  
- How is this term used in Impact reporting?
""")
