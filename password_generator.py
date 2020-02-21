# Heres a simple code of a password generator .



def generatePword(acceptable_pwords, not_acceptable_pwords):
    base = []

    while True:

        userName = input("Enter your username: ")
        userPassword = input("Enter your password: ")

        if userName == "" or userPassword =="":
            break

        pword = {
            "name": userName,
            "password" : userPassword
        }

        base.append(pword)

    for i in base:

        name = i["name"]
        word = i["password"]

        if i["password"] == i["name"] or "1234" in word or len(word) < 5:
            not_acceptable_pwords.append({"Name: " + name+", "+"Password: "+ word})
        else:
            acceptable_pwords.append({"Name: " + name+", "+"Password: "+ word})

    # return acceptable_pwords
    return not_acceptable_pwords


print("Non-acceptable users: ", generatePword(list(), list()))


# There is whole lotta ways to check if passwords are strong or acceptable .