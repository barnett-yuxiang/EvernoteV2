from jinja2 import Environment, FileSystemLoader
import datetime


# 设置 Environment，指定模板文件夹
env = Environment(loader=FileSystemLoader('cb01'))

# 加载模版
template = env.get_template('article_list.html')

# 准备数据
articles = [
    {'title': 'Jinja2 Tutorial', 'author': 'John Doe', 'date': datetime.date(2023, 5, 1)},
    {'title': 'Advanced Python', 'author': 'Jane Smith', 'date': datetime.date(2023, 5, 2)}
]

# 渲染模版，传递数据
output = template.render(articles=articles)

print(output)
