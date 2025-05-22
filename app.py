import streamlit as st
import requests
import json

# JDoodle API credentials
CLIENT_ID = "8f58f27348655b54abb39b54453bf0ab"
CLIENT_SECRET = "47402aab70bc0f0247ae39d30a0c58370d86d69038d46f5e1b5d1991ae4d34bf"

def run_prolog_code(code):
    url = "https://api.jdoodle.com/v1/execute"
    headers = {"Content-Type": "application/json"}
    payload = {
        "clientId": CLIENT_ID,
        "clientSecret": CLIENT_SECRET,
        "script": code,
        "language": "prolog",
        "versionIndex": "0"
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    if response.status_code == 200:
        return response.json().get("output", "Няма резултат")
    else:
        return f"Грешка при заявка: {response.status_code} - {response.text}"

st.title("Prolog Executor with JDoodle API")

st.markdown("**1. Въведи Prolog дефиниции (правила и факти):**")
definitions = st.text_area("", height=150, value="my_member(X, [X|_]).\nmy_member(X, [_|T]) :- my_member(X, T).")

st.markdown("**2. Въведи Prolog заявка (query), например: `:- my_member(2, [1,2,3]).`**")
query = st.text_input("")

if st.button("Изпълни"):
    if not query.strip():
        st.warning("Моля, въведи заявка (query) за изпълнение.")
    else:
        full_code = definitions.strip() + "\n\n" + query.strip()
        output = run_prolog_code(full_code)
        st.markdown("### Резултат:")
        st.text(output)
