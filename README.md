📘 Intelligent Enterprise Assistant — SIH1706
🧠 AIM

To develop an AI-powered Intelligent Enterprise Assistant capable of handling HR, IT, and organizational queries, document summarization, and secure authentication using NLP and document processing.

💡 PROBLEM STATEMENT

Problem ID: SIH1706
Title: Intelligent Enterprise Assistant — Enhancing Organizational Efficiency through AI-Driven Chatbot Integration

The system should:

Handle HR, IT, and organizational questions.

Process uploaded enterprise documents (summarize, extract keywords).

Use email-based OTP for 2-Factor Authentication.

Filter bad language using a system-maintained dictionary.

Respond within 5 seconds for any query.

Support a minimum of 5 parallel users.

⚙️ IMPLEMENTATION STEPS
🔹 Backend (FastAPI)

Built using FastAPI framework.

Endpoints implemented:

/auth/send-otp — Email OTP generation

/auth/verify-otp — OTP verification

/upload/document — Uploads and processes documents

/query — NLP-based query handling

Includes SMTP OTP (prints OTP to console if SMTP not configured).

Handles PDF/DOCX summarization using TF-IDF.

Filters profanity from user queries.

🔹 Frontend (Streamlit)

Simple web UI for:

Authentication

Document Upload

Query Interaction

Uses FastAPI backend via requests API calls.

Displays assistant responses in an interactive chat view.

🔹 Security

2FA with Email OTP

Session token for each verified user

In-memory user sessions (demo mode)

🔹 Scalability

FastAPI’s async architecture allows parallel processing

Each request processed under 5 seconds

🧩 MAIN BACKEND CODE — main.py



🎨 FRONTEND CODE — frontend.py



🧾 OUTPUT 




🧾 RESULT 

