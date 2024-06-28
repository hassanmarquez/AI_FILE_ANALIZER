from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain.document_loaders import PyPDFLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import RetrievalQA
from langchain.chains import create_retrieval_chain
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
# Bring in streamlit for UI dev
import streamlit as st
# Bring in watsonx interface
from langchain_openai import AzureOpenAI
import os
from langchain_openai import AzureChatOpenAI



#----------------------------------------------------
os.environ["AZURE_OPENAI_ENDPOINT"] = ""
os.environ["AZURE_OPENAI_API_KEY"] = ""

llm=AzureChatOpenAI(
    azure_deployment="gpt-35-turbo-0613",
    openai_api_version="2023-07-01-preview",
)
#----------------------------------------------------
# This function Loads a PDF of your chosing
@st.cache_resource
def load_pdf():
   #Update PDF name here to whatever you Like
    pdf_name = './PDF_File/generative ai.pdf'
    loaders = [PyPDFLoader (pdf_name) ]
    # Create index - aka vector database - aka chromadb
    index = VectorstoreIndexCreator(
        embedding = HuggingFaceEmbeddings(model_name='all-miniLM-L12-v2'),
        text_splitter=RecursiveCharacterTextSplitter (chunk_size=700, chunk_overlap=1)
    ).from_loaders(loaders)
    # Retun the vector database
    return index
# Load er on up
index = load_pdf()

# Create a Q&A chain
chain = RetrievalQA.from_chain_type(
    llm,
    chain_type='stuff',
    retriever=index.vectorstore.as_retriever(), 
    input_key='question'
    )

# Setup the app title
st.title('HADA ASSISTENT')

# Setup a session state message variable to hold all the old messages
if 'messages' not in st.session_state:
    st. session_state.messages =[]

# Display all the historical messages
for message in st.session_state.messages:
    st.chat_message(message['role']).markdown(message['content'])

# Build a prompt input template to display the prompts
prompt = st.chat_input( 'Pass Your Prompt here')
# If the user hits enter then
if prompt:
    # Display the prompt
    st.chat_message('user').markdown(prompt)
    # Store the user prompt in state
    st.session_state.messages.append({'role':'user','content':prompt})
    # Send the prompt to the LLm
    response = chain.run(prompt)
    # Show the Llm response
    st.chat_message('assistant').markdown(response)
    # Store the LLM Response in state
    st.session_state.messages.append (
        {'role':'assistant','content':'response'})