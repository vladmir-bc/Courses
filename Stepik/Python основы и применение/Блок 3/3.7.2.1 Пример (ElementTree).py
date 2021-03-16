from xml.etree import ElementTree

tree = ElementTree.parse("example.xml")  # parse возвращает ElementTree - дерево
root = tree.getroot()
# use root = ElementTree.fromstring(string_xml_data) to parse from str

print(root)  # <Element 'studentsList' at 0x033E6600>
print(root.tag, root.attrib)  # studentsList {}
print(root[0][0].text)  # Dean

for child in root:  # перебрать детей внутри дерева
    print(child.tag, child.attrib)

print('________________________________________________')

for element in root.iter("scores"):
    print(element)
    score_sum = 0
    for child in element:
        score_sum += float(child.text)
    print(score_sum)