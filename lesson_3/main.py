# from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import WebBaseLoader
from decouple import config


# # pdf loader
# file_path = config('FILE_PATH')
# loader = PyPDFLoader(file_path)
# result = loader.load()
# text_content = result[4].page_content


# # webbase loader
loader = WebBaseLoader(
    web_path = config('WEB_PATH'),
)

docs = []
docs_lazy = loader.lazy_load()

for doc in docs_lazy:
    docs.append(doc)
print(docs[0].page_content[:100])
print(docs[0].metadata)