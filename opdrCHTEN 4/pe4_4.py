oldpassword = input('geef je oude wachtwoord:')
wachtwoord = input('geef een nieuw wachtwoord:')
def new_password(oldpassw, newpassw):
    if oldpassword != wachtwoord and len(wachtwoord) >= 6:
        return True
    else:
        return False

print(new_password(oldpassword,wachtwoord))

