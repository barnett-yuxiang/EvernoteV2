import pdfkit

# 使用本地 HTML 文件路径
file_path = './nio_bot_coze/ET7/ET7用户手册.html'
output_file = 'ET7_manual.pdf'  # 输出的 PDF 文件名

options = {
    'page-size': 'A3',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'no-outline': None,
    'zoom': '1.5'  # 增加缩放以适应网页宽度
}

# 从本地 HTML 文件生成 PDF
pdfkit.from_file(file_path, output_file, options=options)
