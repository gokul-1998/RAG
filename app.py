import os
from langchain.chains import RetrievalQA
from langchain.document_loaders import TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI

# Set OpenAI API Key
# os.environ["OPENAI_API_KEY"] = "your-openai-api-key"

# Step 1: Load Documents
loader = TextLoader("path_to_your_text_file.txt")
documents = loader.load()

# Step 2: Create Embeddings
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model="sentence-transformers/all-mpnet-base-v2")
# Step 3: Set up Vector Store (FAISS)
vectorstore = FAISS.from_documents(documents, embeddings)

# Step 4: Create a Retriever
retriever = vectorstore.as_retriever()

# Step 5: Set up the Q&A Chain
llm = OpenAI(temperature=0)
qa_chain = RetrievalQA(llm=llm, retriever=retriever)

# Step 6: Ask a Question
query = "What is the capital of France?"
answer = qa_chain.run(query)
print(answer)
