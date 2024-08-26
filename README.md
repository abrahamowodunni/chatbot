# Fitness Chatbot Project

This project aims to develop a fitness chatbot tailored to specific company data. The chatbot will assist users with personalized fitness advice, workout plans, and general health tips by leveraging custom data and advanced AI techniques.

## Project Overview

We are building a fitness chatbot that interacts with users to provide information and guidance on various fitness-related topics. The chatbot will be trained on the company's proprietary fitness data, enabling it to deliver accurate and contextually relevant responses.

### Key Features:
- **Custom Data Ingestion:** The chatbot will work with data extracted from PDF files, enabling it to understand and utilize the company's specific fitness information.
- **Text Chunking:** To overcome token limitations in Large Language Models (LLMs), the extracted text will be divided into manageable chunks. Chunk overlap will be applied to ensure better context retention.
- **Embeddings Creation:** We will create embeddings using models such as Word2Vec, GloVe, BERT, or OpenAI's Embeddings to represent the text data in a format suitable for efficient retrieval and understanding.
- **Vector Database:** A vector database will be created using Pinecone to store and manage the embeddings, facilitating quick and accurate information retrieval based on user queries.
- **User Interaction:** When users ask questions, the chatbot will retrieve the most relevant information from the knowledge base, rank it, and generate a coherent response using the LLM.

## Project Architecture

The architecture of the fitness chatbot project can be broken down into the following components:

1. **Data Ingestion:**
   - **PDF Extractor:** Extracts text data from PDF files containing fitness information.
   - **Text Preprocessing:** Cleans and preprocesses the extracted text for further processing.

2. **Text Chunking:**
   - **Chunking Engine:** Splits the preprocessed text into smaller chunks to handle LLM token limitations and overlap for context retention.

3. **Embeddings Creation:**
   - **Embedding Model:** Converts text chunks into vector embeddings using models like Word2Vec, GloVe, BERT, or OpenAI Embeddings.

4. **Vector Database:**
   - **Pinecone:** Stores the generated embeddings in a vector database for efficient similarity search and information retrieval.

5. **LLM Query Handling:**
   - **User Query Interface:** Captures user input (questions) and processes the query.
   - **Similarity Search:** Searches for the most relevant text chunks from the vector database based on the query.
   - **LLM Response Generator:** Uses LLaMA 3 to generate a contextually accurate response from the retrieved chunks.

6. **Web Application:**
   - **Flask/Streamlit Interface:** Provides a user-friendly interface for interacting with the chatbot.
   - **Backend Integration:** Connects the web interface with the LLM and vector database to process and respond to user queries.

### High-Level Architecture Diagram

Below is a high-level architecture diagram illustrating the flow of data and interactions within the system:
### High-Level Architecture Diagram

Below is a high-level architecture diagram illustrating the flow of data and interactions within the system:

### High-Level Architecture Diagram

Below is a high-level architecture diagram illustrating the flow of data and interactions within the system:

```plaintext
+--------------+       +----------------+       +----------------+       +----------------+       
|  PDF Files   |       |  Text Chunking |       |  Embeddings    |       |  VectorDB      |       
|  (Fitness    | ----> |  Engine        | ----> |  Creation      | ----> |  (Pinecone)    |       
|  Information)|       |                |       |  (BERT, GloVe) |       |                |       
+--------------+       +----------------+       +----------------+       +----------------+       
                                                                                  |
                                                                                  v
+----------------+                                                     +----------------+
|  User Query    | <--------------------------------------------------- |   LLaMA 3      |
|  Interface     |                                                     |  Response Gen.  |
+----------------+                                                     +----------------+

```


## Tech Stack

- **Programming Language:** Python
- **Generative AI Framework:** LangChain
- **Web Application Framework:** Flask or Streamlit (to be decided based on project needs)
- **Large Language Model (LLM):** LLaMA 3
- **Vector Database:** Pinecone