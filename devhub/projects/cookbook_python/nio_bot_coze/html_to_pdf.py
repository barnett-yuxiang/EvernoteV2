import pdfkit

# Set the path to wkhtmltopdf
path_wkhtmltopdf = r'/usr/local/bin/wkhtmltopdf'  # Please modify according to the actual path, needs installation with brew install wkhtmltopdf
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

# URL of the webpage to convert
url = 'https://www.nio.cn/cdn-static/www/user-instructions/20231122/ES6/index.html'

# Output PDF file path
output_path = 'ES6_User_Manual.pdf'

# Set options, remove unsupported --timeout option
options = {
    'load-error-handling': 'ignore',
    'load-media-error-handling': 'ignore',
    'enable-local-file-access': None  # Allows access to local files
}

# Convert webpage to PDF
pdfkit.from_url(url, output_path, configuration=config, options=options)
