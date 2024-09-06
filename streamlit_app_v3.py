import os
import streamlit as st
from langchain_huggingface import HuggingFaceEndpoint


# App title
st.set_page_config(page_title="Explain A Class Expression", page_icon="static/enexa.ico")

# NOTE: Normally imports should all be at the top of the page,
# but st.set_page_config must be the first Streamlit command
# and there are other Streamlit commands in util.py
from utils_v3 import system_message, first_chatbot_message, class_expression, generate_response

# Hugging Face API Credentials
with st.sidebar:
    st.image("static/enexa_logo_v0.png")
    HF_api_key = os.getenv("HUGGINGFACEHUB_API_TOKEN")
    if HF_api_key:
        st.success("Hugging Face API token already provided!", icon="✅")
    else:
        HF_api_key = st.text_input("Enter Hugging Face API key:", type="password")
        if not HF_api_key:
            st.warning("Please enter your credentials!", icon="⚠️")
        else:
            st.success("Proceed to entering your prompt message!", icon="👉")

# Load class expressions
ce_name = class_expression["name"]
ce_content = class_expression["content"]
messages_4_LLM = [{"role": "system", "content": system_message.format(class_expression=ce_content) + "\n" + first_chatbot_message.format(class_expression_name=ce_name)}]

# Initialize Hugging Face endpoint
HF_llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3",
    task="text-generation",
    max_new_tokens=1024,
    repetition_penalty=1.2,
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant",
        "content": first_chatbot_message.format(class_expression_name=ce_name)}
        ]

# Display chat history so far
for i, message in enumerate(st.session_state.messages):
    #print(f"i: {i}")
    #print(f"message: {message}")
    if i == 0:
        with st.chat_message(message["role"], avatar="static/enexa.ico"):
            st.write(message["content"]) 
    else:
        with st.chat_message(message["role"]):
            st.write(message["content"])
        messages_4_LLM.append(message)
    

# User-provided prompt
if prompt := st.chat_input(disabled=not HF_api_key):
    st.session_state.messages.append({ "role": "user", "content": prompt })
    with st.chat_message("user"):
        st.write(prompt)

#print(f"Number of messages_4_LLM: {len(messages_4_LLM)}")
#for m in messages_4_LLM:
    #print(f"messages_4_LLM:\n{m}")
#print("##############################################")

if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner('"Thinking"...'):
                response = generate_response(HF_llm, messages_4_LLM, prompt)
                st.write(response) 
        st.session_state.messages.append({
            "role": "assistant",
            "content": response,
        })

