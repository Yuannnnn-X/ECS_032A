# password.py
# Yuan Xie
#
# password statistics

# prompt the password
Password = input("Enter password:")
# check the length
if len(Password) >= 8:
    print("Has length")
for i in Password:
    # check the lowercase
    if i.islower():
        print("Has lower case")
        break
for i in Password:
    # check the uppercase
    if i.isupper():
        print("Has upper case")
        break
for i in Password:
    # check the udigit
    if i.isdigit():
        print("Has digit")
        break
for i in Password:
    # check the special
    if i == '!' or i == '@' or i == '#' or i == '$' or i == '%' or i == '&':
        print("Has special")
        break
    

