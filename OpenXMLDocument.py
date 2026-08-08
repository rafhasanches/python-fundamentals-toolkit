import xml.etree.ElementTree as ET

countries = []

tree = ET.parse('FIFARanking.xml')
root = tree.getroot()

for country in root:
    name = country.find('name').text
    ranking = int(country.find('ranking').text)

    countries.append([name,ranking])

print(countries)
