import google.generativeai as genai
import os


# 配置 API 密钥
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# 定义模型
MODEL_NAME = "models/gemini-1.5-pro-latest"
model = genai.GenerativeModel(model_name=MODEL_NAME)

# 生成内容
response = model.generate_content("How many miles can I drive the 2024 Cymbal Starlight before I need to change my oil?")

# 打印响应文本
print(response.text)
