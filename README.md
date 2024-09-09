﻿# XCE-Streamlit-V3

This app is an LLM-powered chatbot built using Streamlit and the LangChain-Huggingface API. It it is developed by Shubha Guha and Fina Polat under the supervision of Paul Groth for the ENEXA Explanations Module. 

The main purpose of the app is showcasing the idea of co-construction of explanations.

This is the third version of ENEXA Explainer. This version employs an open-source LLM: https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3 

Here are some technicalities:

The script requires two input variables: HUGGINGFACEHUB_API_TOKEN and EXPRESSION_FILE.

HUGGINGFACEHUB_API_TOKEN can be taken from environment variables or manually entered after runing the application.

EXPRESSION_FILE is the mounting point, we copy this file into the container. 
 

### Pull the image from Docker Hub:
`docker pull finapolat/xce-streamlit_v3:enexa`

### Set the variables
#### Linux
`export OPENAI_API_KEY=your_api_key`

`export EXPRESSION_FILE=/path/to/expression_file.json`

#### Windows
`setx OPENAI_API_KEY "your_api_key"`

`setx EXPRESSION_FILE "path_to_your_expression_file"`

### Run the docker:

#### Linux
`docker run -p 8501:8501 -e OPENAI_API_KEY -v $EXPRESSION_FILE:/app/class_expression.json finapolat/xce-streamlit_v3:enexa`

#### Windows
`docker run -p 8501:8501 -e OPENAI_API_KEY -v %EXPRESSION_FILE%:/app/class_expression.json finapolat/xce-streamlit_v3:enexa`

To view the app, please browse to http://localhost:8501
