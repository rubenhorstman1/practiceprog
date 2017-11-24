import xmltodict

def uitlezen():
    with open('stations.xml') as myXMLFile:
        filecontentstring = myXMLFile.read()
        xmldictionary = xmltodict.parse(filecontentstring)
        typische = xmldictionary['artikelen']['artikel']
        for typisch in typische:
            print(typisch['naam'])

uitlezen()