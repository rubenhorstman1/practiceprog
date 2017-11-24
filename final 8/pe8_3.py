naam = input('geef je naam:')
heenreis = input('Waar begin je:')
terugreis = input('waar eindig je:')
def omzetten(naam):
    return " ".join(str(ord(char)) for char in naam)
def omzet(heenreis):
    return " ".join(str(ord(char)) for char in heenreis)
def omzettend(terugreis):
    return " ".join(str(ord(char)) for char in terugreis)

omzetten('naam')
omzet('heenreis')