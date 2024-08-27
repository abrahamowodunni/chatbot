from src.helper import load_pdf, text_split, download_hugging_face_embeddings
from langchain.vectorstores import Pinecone
from pinecone import Pinecone as pc
from dotenv import load_dotenv
import os

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
pine = pc(api_key= PINECONE_API_KEY)

extracted_data = load_pdf("pdfs/")
text_chunks = text_split(extracted_data)
embeddings = download_hugging_face_embeddings()


index_name="fitnesschatbot"

#Creating Embeddings for Each of The Text Chunks & storing
docsearch=Pinecone.from_texts([t.page_content for t in text_chunks], embeddings, index_name=index_name)