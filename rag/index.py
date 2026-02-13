# indexing phase (load file, splitting, vector embeddings, storing in Qdrant DB)
import os
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_openai import OpenAIEmbeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv

load_dotenv()
pdf_path = Path(__file__).parent / "Unit 4.pdf"

# loading the file path
loader = PyPDFLoader(file_path=pdf_path)
docs = loader.load()

# splitting the text into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 400
)
chunks = text_splitter.split_documents(documents=docs)

# Vector embeddings
embedding_model = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    google_api_key=os.getenv("GEMINI_API_KEY"),
)

# creating store
vector_store = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name = "learning_rag"
)
print("Indexing of documents done..")