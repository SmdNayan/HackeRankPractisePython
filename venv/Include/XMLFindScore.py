
import xml.etree.ElementTree as etree
def get_attr_number(node):
    numlines = int(input())
    XML = ''
    for _ in range(numlines):
        XML += input()

    root = etree.fromstring(XML)
    print (sum([len(i.attrib) for i in root.iter()]))

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))