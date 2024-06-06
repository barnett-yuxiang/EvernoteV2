import os
from pinecone import Pinecone, ServerlessSpec


# This Python script is designed to interact with the Pinecone service, a vector database for machine
# learning applications.

# 1. Initialize your client connection
pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

# 2. Create a serverless index
index_name = "docs-quickstart-index"

# if index_name not in pc.list_indexes().names():
#     pc.create_index(
#         name=index_name,
#         dimension=2,
#         metric="cosine",
#         spec=ServerlessSpec(
#             cloud='aws', 
#             region='us-east-1'
#         ) 
#     )

# 3. Upsert vectors
index = pc.Index(index_name)

# index.upsert(
#     vectors=[
#         {"id": "vec1", "values": [1.0, 1.5]},
#         {"id": "vec2", "values": [2.0, 1.0]},
#         {"id": "vec3", "values": [0.1, 3.0]},
#     ],
#     namespace="ns1"
# )

# index.upsert(
#     vectors=[
#         {"id": "vec1", "values": [1.0, -2.5]},
#         {"id": "vec2", "values": [3.0, -2.0]},
#         {"id": "vec3", "values": [0.5, -1.5]},
#     ],
#     namespace="ns2"
# )

# 4. Check the index
# print(index.describe_index_stats())

# 5. Run a similarity search
query_results1 = index.query(
    namespace="ns1",
    vector=[1.0, 1.5],
    top_k=3,
    include_values=True
)

print(query_results1)

query_results2 = index.query(
    namespace="ns2",
    vector=[1.0,-2.5],
    top_k=3,
    include_values=True
)

print(query_results2)

# Returns:
# {'matches': [{'id': 'vec1', 'score': 1.0, 'values': [1.0, 1.5]},
#              {'id': 'vec2', 'score': 0.868243158, 'values': [2.0, 1.0]},
#              {'id': 'vec3', 'score': 0.850068152, 'values': [0.1, 3.0]}],
#  'namespace': 'ns1',
#  'usage': {'read_units': 6}}
# {'matches': [{'id': 'vec1', 'score': 1.0, 'values': [1.0, -2.5]},
#              {'id': 'vec3', 'score': 0.998274386, 'values': [0.5, -1.5]},
#              {'id': 'vec2', 'score': 0.824041963, 'values': [3.0, -2.0]}],
#  'namespace': 'ns2',
#  'usage': {'read_units': 6}}
