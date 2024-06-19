import requests
from bs4 import BeautifulSoup
import csv

# 请求博客页面
url = "https://www.axtonliu.com/tag/blog/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# 查找所有博客文章
articles = soup.find_all('article')

# 准备 CSV 文件
with open('all-videos-nosub.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['ID', 'URL', 'TITLE']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # 遍历每篇文章并写入 CSV
    for idx, article in enumerate(articles, start=1):
        title_tag = article.find('h2', class_='entry-title')
        if title_tag and title_tag.a:
            title = title_tag.a.text.strip()
            link = title_tag.a['href']
            writer.writerow({'ID': idx, 'URL': link, 'TITLE': title})

print("CSV 文件已生成：axton_blog.csv")
