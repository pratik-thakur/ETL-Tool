import xml.etree.ElementTree as et
tree =et.parse('query.xml')
root =tree.getroot()
i=0
for ele in root:
    i=i+1;
    print(i)
    print(ele[1].text)
    print(type(ele[0].text))
    print(type(ele[1].text))
    print("next")

