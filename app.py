import streamlit as st
import time

st.set_page_config(
    page_title="Wadhwani Foundation Terminology Dictionary",
    layout="centered"
)

# Header
st.title("📘 Wadhwani Foundation Terminology Dictionary")
st.caption("Interactive prototype • Ideathon demo")

st.markdown("""
Welcome to the **Wadhwani Foundation Terminology Dictionary** —  
a centralized, AI‑enabled reference system designed to align how we define, report, and interpret key terms across the organization.
""")

st.divider()

# Chat input
user_input = st.text_input("💬 Ask anything about WF terms, metrics, or reports:")

if user_input:
    with st.spinner("Thinking..."):
        time.sleep(1)

    st.markdown("### 🤖 Assistant")

    st.success("""
### 👋 Welcome!

This is the **Wadhwani Foundation Terminology Dictionary**.

#### 🎯 What this tool does
- Explains **operating, reporting, and technical terms**
- Aligns definitions used in **KPIs, dashboards, and reports**
- Reduces confusion across **teams, regions, and programs**

#### 🧠 How it works (in the full version)
- You ask a question (e.g. *“What does Enabled learner mean?”*)
- The system searches **official WF documents**
- It returns a **clear, standardized explanation**
- It highlights **related terms** and **usage context**

#### 🚀 Why this matters
✅ Faster reporting  
✅ Fewer misinterpretations  
✅ One shared language across the Foundation  

*(This is an interactive UX prototype for the Ideathon.  
The production version will be AI‑powered and document‑grounded.)*
""")

    st.divider()

    st.markdown("#### 🔍 Example questions you could ask:")
    st.markdown("""
- What does *Enabled* vs *Transformed* mean?  
- How are placements calculated?  
- What is considered an input vs output metric?  
- How does this term appear in Power BI reports?
""")
