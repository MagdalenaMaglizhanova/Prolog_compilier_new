import streamlit as st
import requests
import json

# Настройки за JDoodle API
JDoodle_CLIENT_ID = "8f58f27348655b54abb39b54453bf0ab"
JDoodle_CLIENT_SECRET = "47402aab70bc0f0247ae39d30a0c58370d86d69038d46f5e1b5d1991ae4d34bf"

# Streamlit UI
st.title("Prolog Executor with JDoodle API")

st.markdown("### 1. Въведи Prolog дефиниции (правила и факти):")
definitions = st.text_area("Пример: my_member(X, [X|_]).\nmy_member(X, [_|T]) :- my_member(X, T).", height=150)

st.markdown("### 2. Въведи Prolog заявка (query):")
query = st.text_input("Пример: my_member(2, [1,2,3]).")

if st.button("Изпълни"):
    # Автоматично изграждане на Prolog код с main
    full_code = f""":- initialization(main).
{definitions}

main :- {query}, write('true'); write('false')."""

    # Данни за заявката към JDoodle
    payload = {
        "clientId": JDoodle_CLIENT_ID,
        "clientSecret": JDoodle_CLIENT_SECRET,
        "script": full_code,
        "language": "prolog",
        "versionIndex": "0"
    }

    # Изпращане на заявката
    response = requests.post("https://api.jdoodle.com/v1/execute", json=payload)
    result = response.json()

    # Показване на резултата
    st.markdown("### 🧾 Резултат:")
    st.code(result.get("output", "Няма резултат"))
