# summarizer
                    📝 GROQ Document Summarizer with LLaMA3 – Powered by Streamlit

📌 Project Overview

Welcome to my Document Summarizer Web App! 🚀

This tool allows you to upload PDF or TXT files and instantly get a clean, structured summary using 
Groq’s ultra-fast LLaMA3 model.

Built with Streamlit, this app provides a lightweight and responsive user interface for generating document summaries within seconds.

🚀 How I Built & Ran the App (Step-by-Step):

Here’s the exact process I followed to bring this project to life 👇

1️⃣ Create a new folder for the summarizer app.

2️⃣ Inside that folder, create a file named docsummarizer.py
🧠 This is the Streamlit script containing the summarization logic.

3️⃣ Add a .env file
🔐 Use this file to securely store your API key:
GROQ_API_KEY=your_actual_groq_api_key_here

4️⃣ Create a requirements.txt file and add the following dependencies:

streamlit

python-dotenv

langchain-groq

langchain-community

langchain-huggingface

5️⃣ Open the terminal inside your project directory.

6️⃣ Install the dependencies with:
pip install -r requirements.txt

7️⃣ Run the application using Streamlit:
streamlit run docsummarizer.py

8️⃣ Open the summarizer app in your browser:
🌍 http://localhost:8501

🔁 GitHub Upload Steps
(How I published my project to GitHub 💻)

1️⃣ Created a new repository on GitHub.

2️⃣ Opened terminal inside my local project folder.

3️⃣ Initialized Git locally:
git init

4️⃣ Added all project files:
git add .

5️⃣ Committed changes with a message:
git commit -m "Add Groq Document Summarizer Streamlit app"

6️⃣ Linked the local project to GitHub:
git remote add origin https://github.com/your-username/your-repo-name.git
📝 Replace your-username and your-repo-name with your actual GitHub info.

7️⃣ Pushed everything to GitHub:
git push -u origin main

📁 Project Folder Structure

📦 doc-summarizer-app

┣ 📄 docsummarizer.py → Main app logic for summarizing documents

┣ 📄 .env → Stores Groq API key securely

┣ 📄 requirements.txt → List of all required packages

┣ 📄 README.md → This full project guide

💡 What the App Can Do

✔ Upload any PDF or TXT file

✔ Summarize the entire document content in seconds

✔ Uses Groq’s blazing-fast LLaMA3 for accurate summaries

✔ Clean and formatted output display

✔ Download summary as a .txt file

✔ Interactive and minimal UI built with Streamlit

✨ Tech Stack Used

Streamlit – Interactive frontend

Groq API (LLaMA3) – For summarizing content

LangChain + HuggingFace Embeddings – For document chunking

Python-dotenv – For managing secrets securely

👩‍💻 Created By

Ushmitha Annapaneni

Feel free to ⭐ star or fork this repo if you found it helpful or interesting!

📄 License

MIT License – Free to use, modify, and share