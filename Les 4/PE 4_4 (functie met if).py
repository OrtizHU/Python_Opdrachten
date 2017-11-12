def new_password(oldpassword, newpassword):
    cijfer = '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9' or '0'
    if newpassword != oldpassword:
        if len(newpassword) >= 6:
            if cijfer in format(newpassword):
                return bool(1)
    else:
        return bool(0)
print(new_password('password','HUstudent1'))
