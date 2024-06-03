# Import necessary libraries
import os
import streamlit as st
import pickle
import time
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

from HuggingFaceQAPipeline import HuggingFaceQAPipeline

# Set page configuration and title
st.set_page_config(page_title="Advanced LLM-Powered News Research Tool", page_icon="📰")
st.title("Advanced LLM-Powered News Research Tool 📰")

# Sidebar section for user input
st.sidebar.header("Enter News Article URLs")

# Collect URLs from the user
article_urls = [st.sidebar.text_input(f"URL {i + 1}") for i in range(3)]

# Button to trigger article analysis
if st.sidebar.button("Process the Content"):
    st.session_state["urls_submitted"] = True

# File path for storing FAISS index
index_file = "news_faiss_index.pkl"

# Initialize HuggingFace Q&A pipeline
qa_pipeline = HuggingFaceQAPipeline(model_name="deepset/roberta-base-squad2")

# Check if URLs are submitted and process articles
if st.session_state.get("urls_submitted", False):
    with st.spinner("Fetching and processing articles..."):
        # Load articles from URLs
        loader = UnstructuredURLLoader(urls=article_urls)
        raw_data = loader.load()

    with st.spinner("Splitting articles into chunks..."):
        # Split articles into smaller chunks
        splitter = RecursiveCharacterTextSplitter(separators=['\n\n', '\n', '.', ','], chunk_size=1000)
        documents = splitter.split_documents(raw_data)

    with st.spinner("Creating embeddings and building FAISS index..."):
        # Generate embeddings and build FAISS index
        embeddings_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        faiss_index = FAISS.from_documents(documents, embeddings_model)
        with open(index_file, "wb") as f:
            pickle.dump(faiss_index, f)

    # Display success message
    st.success("Articles processed and FAISS index created!")
    st.session_state["urls_submitted"] = False

# Input field for user queries
user_query = st.text_input("Ask any question on this domain 🤗:")

# Process user query and display results
if user_query:
    if os.path.exists(index_file):
        with st.spinner("Retrieving relevant information..."):
            # Load stored FAISS index
            with open(index_file, "rb") as f:
                stored_index = pickle.load(f)
                retriever = stored_index.as_retriever()
                relevant_docs = retriever.get_relevant_documents(user_query)

        # Combine relevant document contexts
        combined_context = " ".join([doc.page_content for doc in relevant_docs])
        qa_result = qa_pipeline({"question": user_query, "context": combined_context})

        # Display generated answer
        st.header("Generated Answer")
        st.write(qa_result["answer"])

        # Display referenced sources
        st.subheader("Referenced Sources:")
        for doc in relevant_docs:
            st.write(doc.metadata.get("source", "Unknown"))
