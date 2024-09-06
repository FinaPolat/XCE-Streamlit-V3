import json

from retry import retry
import streamlit as st

from langchain_huggingface import ChatHuggingFace


system_message = """Efficient Explainable Learning on Knowledge Graphs (ENEXA) is a European project developing human-centered explainable machine learning approaches for real world knowledge graphs.
You are ENEXA Explanation Chatbot that can answer questions about a given class expression learned by the ENEXA pipeline. ENEXA pipeline extracts triples from Wikipedia pages using an encoder-decoder model and converts the extracted triples into a Knowledge Graph. Then, the pipeline looks for the inconsustencies and errors in the Knowledge Graph and corrects them. Finally, the pipeline learns a class expression from the corrected Knowledge Graph using a neural class expression learner. 
In the context of knowledge graphs and ontology languages such as  RDF (Resource Description Framework) and OWL (Web Ontology Language), a class expression refers to a way of specifying a set of individuals or instances that share certain characteristics or properties. Classes represent sets of individuals, and class expressions provide a more detailed and expressive way of defining these sets. 
Class expressions can involve logical combinations of classes, restrictions on properties, and other constructs to precisely define the criteria for membership in a class.
The user would like to talk about the following class expression:
{class_expression}
Answer the user questions according to provided information and use short answers. If the users thanks you, you can say "You're welcome!" or "My pleasure! and stop".
"""

first_chatbot_message = """Welcome to ENEXA Explanations Module, it is great that you would like to talk about {class_expression_name}, one of the learned expressions! 

We are going to co-construct explanations about this class expression. Before we start, please verify that your API key is entered correctly on the left-hand side for ensuring seamless interaction. If everything is all set up, please tell me what you would like to know about it.
"""	

def read_json(file_path):
    try:
        with open(file_path, 'r') as file:
            json_data = json.load(file)
            return json_data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON in '{file_path}': {e}")
        return None
    

@st.cache_data
def load_class_expression(file_path="class_expression.json"):
    raw_content = read_json(file_path)
    class_expression = {
                "name": raw_content["learned_expression"],
                "content": json.dumps(raw_content, ensure_ascii=False),
            }
    return class_expression

class_expression = load_class_expression()

@retry(tries=3, delay=2, max_delay=10)
def _get_response(HF_llm, messages):
    hf_chatbot = ChatHuggingFace(llm=HF_llm, verbose=True)
    response = hf_chatbot.invoke(messages)
    return response.content


def generate_response(HF_llm, messages, prompt_input):
    messages.append({"role": "user", "content": prompt_input})
    #for m in messages:
        #print(m)
    return _get_response(HF_llm, messages)