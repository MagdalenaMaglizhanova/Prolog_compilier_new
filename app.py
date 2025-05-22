import streamlit as st
import requests

# JDoodle API credentials
JD_CLIENT_ID = "8f58f27348655b54abb39b54453bf0ab"
JD_CLIENT_SECRET = "47402aab70bc0f0247ae39d30a0c58370d86d69038d46f5e1b5d1991ae4d34bf"

st.title("🧠 Prolog Executor with JDoodle API")

code = st.text_area("✍️ Въведи Prolog код:", "member(X, [1,2,3]).")

if st.button("🚀 Изпълни"):
    with st.spinner("Изпращане към JDoodle..."):
        payload = {
            "clientId": JD_CLIENT_ID,
            "clientSecret": JD_CLIENT_SECRET,
            "script": code,
            "language": "prolog",
            "versionIndex": "0"
        }

        response = requests.post("https://api.jdoodle.com/v1/execute", json=payload)

        if response.status_code == 200:
            result = response.json()
            st.subheader("🧾 Резултат:")
            st.code(result.get("output", "Няма изход..."))
        else:
            st.error("❌ Възникна грешка при изпращането към JDoodle.")
