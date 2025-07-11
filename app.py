import streamlit as st
from retriever import retrieve_top_k_chunks, get_document_stats
from generator import query  # now using OpenRouter Mistral

st.set_page_config(page_title="Legal Chatbot", layout="wide")
st.title("📄 Chatbot for your Legal Queries")

# Session-based chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Sidebar: info and reset
with st.sidebar:
    st.markdown("### ℹ️ Info")
    st.markdown("**Model:** Mistral-7B via OpenRouter")
    doc_count, chunk_count = get_document_stats()
    st.markdown(f"**Indexed Chunks:** {chunk_count}")
    st.markdown(f"**Document Count:** {doc_count}")

    if st.button("🔁 Reset Chat"):
        st.session_state.chat_history = []
        st.rerun()

# Show chat history
for user, bot, refs in st.session_state.chat_history:
    st.chat_message("user").write(user)
    st.chat_message("assistant").write(bot)
    with st.expander("📌 Sources Used", expanded=False):
        for i, ref in enumerate(refs):
            st.markdown(f"**[{i+1}]** {ref[:300]}...")

# Handle user input
user_input = st.chat_input("Ask your legal question...")

if user_input:
    st.chat_message("user").write(user_input)
    top_chunks = retrieve_top_k_chunks(user_input, k=4)

    # Format RAG prompt
    context = "\n\n".join(top_chunks)
    prompt = f"Use the following legal context to answer the question.\n\nContext:\n{context}\n\nQuestion: {user_input}"

    # Call OpenRouter model
    response_text = query(prompt)

    # Show assistant response
    st.chat_message("assistant").write(response_text)

    # Show the top sources used (chunks)
    with st.expander("📌 Sources Used", expanded=False):
        for i, ref in enumerate(top_chunks):
            st.markdown(f"**[{i+1}]** {ref[:300]}...")

    # Store in chat history
    st.session_state.chat_history.append((user_input, response_text, top_chunks))