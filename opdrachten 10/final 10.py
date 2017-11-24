import xmltodict

def uitlezen():
    with open('stations.xml') as myXMLFile:
        filecontentstring = myXMLFile.read()
        xmldictionary = xmltodict.parse(filecontentstring)
        typische = xmldictionary['Stations']['Station']
        for typisch in typische:
            print(typisch['Code'], '-', typisch['Type'])

def inuit():
    with open('stations.xml') as myXMLFile:
        filecontentstring = myXMLFile.read()
        xmldictionary = xmltodict.parse(filecontentstring)
        typische = xmldictionary['Stations']['Station']
        for typisch in typische:
            if typisch['Synoniemen'] != None:
                print(typisch['Code'], '-', typisch['Synoniemen'])

def inlezen():
    with open('stations.xml') as myXMLFile:
        filecontentstring = myXMLFile.read()
        xmldictionary = xmltodict.parse(filecontentstring)
        typische = xmldictionary['Stations']['Station']
        for typisch in typische:
            print(typisch['Code'], '-', typisch['Namen']['Lang'])


print('Dit zijn alle code en types van alle stations.')
uitlezen()
print(' ')
print('Dit zijn alle stations met met een of meerdere synoniemen')
inuit()
print(' ')
print('Dit is de lange naam van elk station: ')
inlezen()

