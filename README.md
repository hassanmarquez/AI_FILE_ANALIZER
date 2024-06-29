# AI_FILE_ANALIZER
This repository hosts an application currently in development that aims to analyze PDF files, extracting and presenting specific details tailored to users' requirements quicky and clearly.

# LET'S START
# The following dependencies have to be installed using the command "pip install -r requirements.txt", means it will take the requirements file to know the dependencies, the following is the list of libraries:
openai
streamlit
python-dotenv
PyPDF2
st-pages
chromadb
Matplotlib
plotly
azure-cognitiveservices-speech
google-generativeai

# The following are the useful commands to validate the status of the components and dependencies in the server

## Shows the location of python library for python and python3 version
which -a python python3

## Check Python version
python --version

## Create the virtual machine (Env)
python3 -m venv venv

## Start the environment
source venv/bin/activate

## Stop he virtual environment
deactivate

## Check the list of package installed
pip list
pip freeze

## Install the dependencies from a file
pip install -r fileName.txt

## Start the chroma DB
chroma run

## Start Streamlit 
streamlit run src/main.py