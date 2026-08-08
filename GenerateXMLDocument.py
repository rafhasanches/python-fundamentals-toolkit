import xml.etree.ElementTree as ET

# This program is a sample of how to create a XML document thru an array

countries = [
['Germany' ,9],
['Croatia' ,10],
['Argentina' ,1],
['France' ,2],
['United States' ,15],
['Mexico' ,16],
['Japan' ,17],
['Senegal' ,18],
['England' ,3],
['Spain' ,5],
['Portugal' ,6],
['Netherlands' ,7],
['Belgium' ,8],
['Brazil' ,4],
['Morocco' ,11],
['Uruguay' ,13],
['Colombia' ,14],
['Iran' ,19],
['Switzerland' ,20],
['Sweden' ,28],
['Poland' ,29],
['Egypt' ,31],
['Nigeria' ,32],
['Denmark' ,21],
['Austria' ,22],
['South Korea' ,23],
['Australia' ,24],
['Ukraine' ,25],
['Turkey' ,26],
['Ecuador' ,27],
['Algeria' ,33],
['Panama' ,34],
['Canada' ,35],
['Tunisia' ,36],
['Serbia' ,37],
['Paraguay' ,38],
['Czech Republic' ,39],
['Norway' ,40],
['Scotland' ,42],
['Ivory Coast' ,43],
['Saudi Arabia' ,49],
['Qatar' ,51],
['South Africa' ,56],
['Jordan' ,62],
['Uzbekistan' ,64],
['Bosnia and Herzegovina' ,70],
['Haiti' ,83],
['New Zealand' ,85]
]

root = ET.Element('countries')

for country in countries:

    countryElement = ET.SubElement(root, 'country')
    ET.SubElement(countryElement, 'name').text = country[0]
    ET.SubElement(countryElement, 'ranking').text = str(country[1])

tree = ET.ElementTree(root)
tree.write('FIFARanking.xml', encoding='utf-8', xml_declaration=True)