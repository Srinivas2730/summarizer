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
st.title(" Document Summarizer using Groq's LLaMA3")

# Upload file
uploaded_file = st.file_uploader("Upload a PDF or TXT file", type=["pdf", "txt"])

if uploaded_file:
    # Save uploaded file temporarily
    file_ext = uploaded_file.name.split(".")[-1]
    temp_path = f"temp.{file_ext}"
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success(f"{uploaded_file.name} uploaded successfully!")

    # Load content
    if file_ext == "pdf":
        loader = PyPDFLoader(temp_path)
    else:
        loader = TextLoader(temp_path, encoding="utf8")

    pages = loader.load_and_split()

    # Split into chunks
    splitter = CharacterTextSplitter(chunk_size=3000, chunk_overlap=300)
    chunks = splitter.split_documents(pages)
    full_text = " ".join([chunk.page_content for chunk in chunks])

    # Create prompt
    prompt = f"Please provide a clear and concise summary of the following document:\n\n{full_text}"

    # Call Groq API
    llm = ChatGroq(groq_api_key=groq_api_key, model_name="llama3-70b-8192")
    response = llm.invoke(prompt)

    # Extract the actual string
    summary_text = response.content

    # Display summary
    st.markdown("###Summary")
    st.write(summary_text)

    # Download as TXT
    summary_bytes = summary_text.encode("utf-8")
    st.download_button(
        label="Download Summary as TXT",
        data=io.BytesIO(summary_bytes),
        file_name="summary.txt",
        mime="text/plain"
    )

