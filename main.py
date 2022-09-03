import xml.etree.ElementTree as ET


tree = ET.parse("country.xml")
root = tree.getroot()

for child in root:
    print(child.tag, child.attrib)

for neighbor in root.iter("neighbor"):
    print(neighbor.attrib)

for country in root.findall("country"):
    rank = country.find("rank").text
    name = country.get("name")
    print(name, rank)
