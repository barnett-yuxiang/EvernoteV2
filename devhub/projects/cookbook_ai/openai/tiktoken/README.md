
Fast [BPE](https://en.wikipedia.org/wiki/Byte_pair_encoding) tokeniser for use with OpenAI's models

The tokeniser API is documented in `tiktoken/core.py.`

Example code using tiktoken can be found in the [OpenAI Cookbook](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb).

tiktoken is between 3-6x faster than a comparable open source (huggingface) tokeniser:

