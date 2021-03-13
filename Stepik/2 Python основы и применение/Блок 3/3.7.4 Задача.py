from xml.etree.ElementTree import XMLParser

colors = {}


class MaxDepth:  # The target object of the parser
    maxDepth = 0
    depth = 0

    def start(self, tag, attrib):  # Called for each opening tag.
        self.depth += 1
        if attrib['color'] not in colors:
            colors[attrib['color']] = self.depth
        else:
            colors[attrib['color']] += self.depth
        if self.depth > self.maxDepth:
            self.maxDepth = self.depth

    def end(self, tag):  # Called for each closing tag.
        self.depth -= 1

    def data(self, data):
        pass

    def close(self):  # Called when all data has been parsed.
        return self.maxDepth


target = MaxDepth()
parser = XMLParser(target=target)
exampleXml = input()
parser.feed(exampleXml)
print(colors['red'], colors['green'], colors['blue'])
