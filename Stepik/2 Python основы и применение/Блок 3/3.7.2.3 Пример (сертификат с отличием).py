from xml.etree import ElementTree

tree = ElementTree.parse('example.xml')
root = tree.getroot()

# tree.write('example_copy.xml')

greg = root[0]
# module1 = next(greg.iter('module1'))
# print(module1, module1.text)
# module1.text = str(float(module1.text) + 30)
certificate = greg[2]
certificate.set("type", "with distinction")
description = ElementTree.Element("description")
description.text = "Showed excellent skills during the course"
greg.append(description)  # создание нового элемента внутри элемента student id=1
description = greg.find("description")
greg.remove(description)  # удалили описание

tree.write("example_modified.xml")