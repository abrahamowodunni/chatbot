from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings
from pinecone import Pinecone
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
from src.prompt import *
import os

app = Flask(__name__)

load_dotenv()


PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
pc = Pinecone(api_key= PINECONE_API_KEY)
index = pc.Index("fitnesschatbot")
print(index.describe_index_stats())

embeddings = download_hugging_face_embeddings()

#Initializing the Pinecone
index_name= "fitnesschatbot"

from langchain_pinecone import PineconeVectorStore
text_field = "text" 

#Loading the index
docsearch=PineconeVectorStore.from_existing_index(index_name= index_name, embedding=embeddings, text_key= text_field)

retriever = docsearch.as_retriever()

# docsearch.as_retriever()
# query = "best chest workout?"
# doc = docsearch.similarity_search(query)
# print(doc)

PROMPT=PromptTemplate(template=prompt_template, input_variables=["context", "question"])

chain_type_kwargs={"prompt": PROMPT}

llm=CTransformers(model="model/llama-2-7b-chat.ggmlv3.q4_0.bin",
                  model_type="llama",
                  config={'max_new_tokens':512,
                          'temperature':0.8})


qa=RetrievalQA.from_chain_type(
    llm=llm, 
    chain_type="stuff", 
    retriever=retriever, 
    chain_type_kwargs=chain_type_kwargs
    )




@app.route("/")
def index():
    return render_template('chat.html')



@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    result=qa({"query": input})
    print("Response : ", result["result"])
    return str(result["result"])



if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True)