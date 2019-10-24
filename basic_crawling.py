import requests

from lxml import html


url = "https://www.w3adda.com/python-tutorial"

result = requests.get(url)

tree = html.fromstring(result.content)

# "//" for search conatins that
# li have "li"
# /a/text() get text in tag a contained by li

isi = tree.xpath("//li/a/text()")
print(type(tree))

print(isi)
