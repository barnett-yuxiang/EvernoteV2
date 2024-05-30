import xml.etree.ElementTree as ET

tree = ET.parse('cb01/bookstore.xml')

root = tree.getroot()

for book in root.findall('book'):
  category = book.get('category')
  title = book.find('title').text
  price = book.find('price').text

  print(f"Category: {category}, Title: {title}, Price: {price}")
