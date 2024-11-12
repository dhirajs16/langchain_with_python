# from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from decouple import config


# # pdf loader
# file_path = config('FILE_PATH')
# loader = PyPDFLoader(file_path)
# doc = loader.load()


# # webbase loader
loader = WebBaseLoader(
    web_path = config('WEB_PATH'),
)
doc = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 200)
chunks = text_splitter.split_document(doc)