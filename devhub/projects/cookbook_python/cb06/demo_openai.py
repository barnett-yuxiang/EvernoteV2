import tiktoken

encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
encoding.encode("tiktoken is great!")

print(encoding)
