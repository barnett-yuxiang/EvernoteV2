import requests
from bs4 import BeautifulSoup
import csv
import os

# 定义文件路径
csv_file_path = 'chatbot/all-videos-nosub.csv'

# 如果文件存在，删除旧文件
if os.path.exists(csv_file_path):
    os.remove(csv_file_path)

# 请求博客页面
url = "https://www.axtonliu.com/tag/blog/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# 查找所有博客文章
articles = soup.find_all('article', class_='gh-card post tag-blog')

# 准备 CSV 文件
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['ID', 'URL', 'TITLE']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # 遍历每篇文章并写入 CSV
    for idx, article in enumerate(articles, start=1):
        title_tag = article.find('h3', class_='gh-card-title is-title')
        link_tag = article.find('a', class_='gh-card-link')
        
        if title_tag and link_tag:
            title = title_tag.text.strip()
            relative_link = link_tag['href']
            link = f"https://www.axtonliu.com{relative_link}"
            writer.writerow({'ID': idx, 'URL': link, 'TITLE': title})

print("CSV 文件已生成：chatbot/all-videos-nosub.csv")
