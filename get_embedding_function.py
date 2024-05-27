from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain_community.embeddings.bedrock import BedrockEmbeddings
from langchain_openai import OpenAIEmbeddings
import os

print(os.environ)

def get_embedding_function():
    # embeddings = BedrockEmbeddings(
    #     credentials_profile_name="default", region_name="us-east-1"
    # )
    # embeddings = OllamaEmbeddings(model="nomic-embed-text")

    embeddings = OpenAIEmbeddings(api_key=os.environ["OPENAI_API_KEY"])
    # embeddings = embeddings_model.embed_documents(

    return embeddings