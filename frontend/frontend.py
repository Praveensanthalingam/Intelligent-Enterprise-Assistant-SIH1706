import streamlit as st, requests

BASE_URL = "http://127.0.0.1:8000"
st.title("🤖 Intelligent Enterprise Assistant")

page = st.sidebar.radio("Navigation", ["Authentication", "Document Upload", "Chat"])

if page == "Authentication":
    email = st.text_input("Enter email")
    if st.button("Send OTP"):
        r = requests.post(f"{BASE_URL}/auth/send-otp", json={"email": email})
        st.info(r.json()["message"])
    otp = st.text_input("Enter OTP")
    if st.button("Verify OTP"):
        r = requests.post(f"{BASE_URL}/auth/verify-otp", json={"email": email, "otp": otp})
        if r.status_code == 200:
            st.session_state["token"] = r.json()["token"]
            st.success("OTP Verified ✅")
        else:
            st.error(r.text)

elif page == "Document Upload":
    if "token" not in st.session_state: st.warning("Authenticate first.")
    else:
        file = st.file_uploader("Upload PDF")
        if st.button("Upload") and file:
            res = requests.post(f"{BASE_URL}/upload/document", files={"file": file}, data={"token": st.session_state["token"]})
            if res.status_code == 200:
                data = res.json()
                st.success("Uploaded successfully")
                st.write("### Summary:", data["summary"])
                st.write("### Keywords:", ", ".join(data["keywords"]))
            else: st.error(res.text)

elif page == "Chat":
    if "token" not in st.session_state: st.warning("Authenticate first.")
    else:
        q = st.text_area("Enter query")
        if st.button("Ask"):
            res = requests.post(f"{BASE_URL}/query", json={"token": st.session_state["token"], "query": q})
            st.write(res.json().get("answer", "No response"))
