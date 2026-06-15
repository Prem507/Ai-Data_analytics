import streamlit as st
import pandas as pd

from utils.llm import get_analysis
from utils.analyzer import run_code

st.set_page_config(page_title="AI Data Analyst")

st.title("AI Data Analyst")

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.subheader("Columns")
    st.write(list(df.columns))

    question = st.text_input(
        "Ask a question about your data"
    )

    if st.button("Analyze"):

        with st.spinner("Analyzing..."):

            code = get_analysis(
                list(df.columns),
                question
            )

            st.subheader("Generated Code")
            st.code(code, language="python")

            result = run_code(df, code)

            st.subheader("Result")
            st.write(result)