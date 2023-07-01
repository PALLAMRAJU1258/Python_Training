dict_={
    "username":"sunny@email.com",
    "password":"TheNun"
}

username=input("Enter username:")
password=input("Enter password:")
if username == dict_["username"] :
    if password!=dict_["password"] :
        print("password is incorrect")
    else:
        print("Email and password are found")
else :
    print("The entered email is not found")
