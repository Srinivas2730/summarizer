import streamlit as st
from dotenv import load_dotenv
import os
import io

from langchain_groq import ChatGroq
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import CharacterTextSplitter

# Load environment variables
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Set up Streamlit
st.set_page_config(page_title="Doc Summarizer with Groq")
st.title("Document Summarizer using Groq's LLaMA3")

# Upload file
uploaded_file = st.file_uploader("Upload a PDF or TXT file", type=["pdf", "txt"])

if uploaded_file:
    file_ext = uploaded_file.name.split(".")[-1]
    temp_path = f"temp.{file_ext}"

    # Save file temporarily
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success(f"{uploaded_file.name} uploaded successfully!")

    try:
        # Load content
        loader = PyPDFLoader(temp_path) if file_ext == "pdf" else TextLoader(temp_path, encoding="utf8")
        pages = loader.load_and_split()

        # Split text
        splitter = CharacterTextSplitter(chunk_size=3000, chunk_overlap=300)
        chunks = splitter.split_documents(pages)
        full_text = " ".join([chunk.page_content for chunk in chunks])

        # Create summary prompt
        prompt = f"Please provide a clear and concise summary of the following document:\n\n{full_text}"

        # LLM Call
        llm = ChatGroq(groq_api_key=groq_api_key, model_name="llama3-70b-8192")
        response = llm.invoke(prompt)
        summary_text = response.content

        # Display summary
        st.markdown("### Summary")
        st.write(summary_text)

        # Download button
        summary_bytes = summary_text.encode("utf-8")
        st.download_button(
            label=" Download Summary as TXT",
            data=io.BytesIO(summary_bytes),
            file_name="summary.txt",
            mime="text/plain"
        )

    finally:
        # Delete temporary file
        if os.path.exists(temp_path):
            os.remove(temp_path)

