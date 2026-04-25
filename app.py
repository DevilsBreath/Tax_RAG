import streamlit as st
import requests

API_URL = "http://localhost:8000/chat"

st.set_page_config(page_title="TaxGPT India", page_icon="🇮🇳", layout="wide")

st.title("TaxGPT India 🇮🇳")
st.markdown("Your Local AI Assistant for Indian Tax Laws, powered by Qwen 2.5 3B.")

with st.sidebar:
    st.header("💡 Example Queries")
    st.markdown("- What is the standard deduction under the new tax regime (Sec 115BAC)?")
    st.markdown("- What is the TDS rate for professional fees under Section 194J?")
    st.markdown("- Explain the provisions of Section 80C for tax-saving investments.")
    st.markdown("- How are long-term capital gains on equity shares taxed?")
    st.divider()
    st.info("Ensure the FastAPI backend is running on port 8000.")

if "messages" not in st.session_state:
    st.session_state.messages = []

def display_evidence(evidence):
    with st.expander("📚 View Legal Sources"):
        for idx, ev in enumerate(evidence):
            meta = ev.get("metadata", {})
            source_name = meta.get("source", "Unknown Document")
            page_num = meta.get("page", "?")
            st.markdown(f"**[Source {ev.get('rank', idx+1)}] {source_name} (Page {page_num})**")
            st.markdown(f"*Relevance Score: {ev['score']:.4f}*")
            st.info(ev["text"])

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "evidence" in message and message["evidence"]:
            display_evidence(message["evidence"])

# Chat input
if prompt := st.chat_input("Ask a tax or compliance question..."):
    # Add user message to state
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Call API
    with st.chat_message("assistant"):
        with st.spinner("Consulting the tax code..."):
            try:
                response = requests.post(API_URL, json={"question": prompt, "top_k": 4})
                response.raise_for_status()
                data = response.json()
                
                answer = data.get("answer", "No answer received.")
                evidence = data.get("evidence", [])
                
                st.markdown(answer)
                if evidence:
                    display_evidence(evidence)
                        
                st.session_state.messages.append({
                    "role": "assistant", 
                    "content": answer,
                    "evidence": evidence
                })
                
            except requests.exceptions.RequestException as e:
                st.error(f"Error connecting to API: {e}")
                st.markdown("Make sure the FastAPI backend is running on `http://localhost:8000`")
