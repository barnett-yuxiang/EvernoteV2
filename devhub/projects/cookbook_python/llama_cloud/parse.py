# bring in our LLAMA_CLOUD_API_KEY
from dotenv import load_dotenv
load_dotenv()

# bring in deps
from llama_parse import LlamaParse
from llama_index.core import SimpleDirectoryReader

# set up parser
parser = LlamaParse(
    result_type="markdown"  # "markdown" and "text" are available
)

# use SimpleDirectoryReader to parse our file
file_extractor = {".pdf": parser}
documents = SimpleDirectoryReader(input_files=['llama_cloud/data/canada.pdf'], file_extractor=file_extractor).load_data()
print(documents)


# one extra dep
from llama_index.core import VectorStoreIndex

# create an index from the parsed markdown
index = VectorStoreIndex.from_documents(documents)

# create a query engine for the index
query_engine = index.as_query_engine()

# query the engine
query = "What can you do in the Bay of Fundy?"
response = query_engine.query(query)
print(response)
