# Advanced LLM-Powered News Research Tool 📰

This tool leverages advanced language models to facilitate efficient research on news articles. Users can input URLs of articles, ask questions related to the content, and obtain answers along with referenced sources. The tool utilizes Hugging Face's models for question answering and embedding generation, along with FAISS for efficient document retrieval. Additionally, Langchain is employed for document loading, text splitting, embeddings, and vector stores.

## Usage

### Input News Article URLs

Enter the URLs of news articles you want to analyze in the sidebar. You can input up to three URLs.

### Process the Content

Click the "Process the Content" button to initiate the analysis of the submitted URLs.

### Ask Questions

After processing the content, you can ask any question related to the domain of the articles using the input field provided.

### View Results

The tool will retrieve relevant information from the processed articles and display generated answers along with referenced sources.

## Sample Results 📝

![loading the artciles](https://github.com/prajwol148/-Advanced-LLM-Powered-News-Research-Tool-/assets/68413988/a3055035-8e0d-49c4-8d41-3e93eb5b4e96)
![loading data from articles](https://github.com/prajwol148/-Advanced-LLM-Powered-News-Research-Tool-/assets/68413988/ef698b31-7465-44f3-9e63-299f13e83a6a)
![urls processed and embeddings stored](https://github.com/prajwol148/-Advanced-LLM-Powered-News-Research-Tool-/assets/68413988/42ce5d1e-3573-46aa-bdab-7230f7db5c19)
![4](https://github.com/prajwol148/-Advanced-LLM-Powered-News-Research-Tool-/assets/68413988/3d0f5da8-78fb-4575-aedd-8b3fdc1c7b0e)
![5](https://github.com/prajwol148/-Advanced-LLM-Powered-News-Research-Tool-/assets/68413988/d8e5a014-c310-42fb-996f-adfd32a838a2)
![6](https://github.com/prajwol148/-Advanced-LLM-Powered-News-Research-Tool-/assets/68413988/a80622ab-9c58-47d0-85ee-345cc6daf466)
![7](https://github.com/prajwol148/-Advanced-LLM-Powered-News-Research-Tool-/assets/68413988/a6c1022d-7058-4447-a860-cfc28648075c)


## Requirements

Make sure you have the following libraries installed:

- Streamlit
- HuggingFace Transformers
- langchain

## Installation

You can install the required libraries using pip:

```bash
pip install -r requirements.txt


## How to Run
Run the following command to start the Streamlit app:
streamlit run app.py


## Credits
This project utilizes the following libraries and resources:

Streamlit
Hugging Face Transformers
langchain
