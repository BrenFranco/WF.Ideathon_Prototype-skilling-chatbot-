import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title="Skilling Metrics Assistant", layout="wide")

st.title("📊 Skilling Metrics & Reporting Assistant")
st.caption("Answers are strictly based on Skilling Methodology (CY26) and March 2026 Report")

with st.sidebar:
    st.header("About this prototype")
    st.write("""
    This chatbot explains Skilling metrics and reporting logic.
    It is grounded ONLY in:
    - Skilling Metrics & Methodology (CY26)
    - Skilling Month-End Report (March 2026)
    """)

@st.cache_resource
def load_data():
    docs = []
    paths = [
        "data/Skilling - Metrics and Data Collection Methodology CY26 - updated.pdf",
        "data/Skilling Month-End Report - March 2026.pdf"
    ]
    for path in paths:
        loader = PyPDFLoader(path)
        docs.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    chunks = splitter.split_documents(docs)

    embeddings = OpenAIEmbeddings()
    return FAISS.from_documents(chunks, embeddings)

vectorstore = load_data()

llm = ChatOpenAI(temperature=0)

retriever = vectorstore.as_retriever()

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a Skilling metrics assistant. Answer ONLY using the provided context. If the answer is not in the documents, say 'Not specified in source documents.'"),
    ("human", "{question}")
])

chain = (
    {"context": retriever, "question": lambda x: x}
    | prompt
    | llm
    | StrOutputParser()
)

query = st.text_input("Ask a question about Skilling metrics:")

if query:
    st.subheader("Answer")
    response = chain.invoke(query)
    st.write(response)
