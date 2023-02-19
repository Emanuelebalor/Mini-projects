import string
import random


password = "This..is..A..5est"


# checks pass requirements len, upper/lower case, digit and special character
def check_req(pas: str):

    req_dict = {"lower": 0,
                "upper": 0,
                "digits": 0,
                "special_char": 0,
                "length": 0}

    if len(pas) in range(8, 33):
        req_dict["length"] = 1
    else:
        return False

    for elem in pas:
        if elem in string.ascii_lowercase:
            req_dict["lower"] = 1
            continue
        elif elem in string.ascii_uppercase:
            req_dict["upper"] = 1
            continue
        elif elem in string.digits:
            req_dict["digits"] = 1
            continue
        elif elem in string.punctuation:
            req_dict["special_char"] = 1
            continue
    if sum(req_dict.values()) == 5:
        return True
    else:
        return False


# sets an encription rule, each element in the password will be set as a dict key and given a random value between 1-9
# the resuulting key will be saved in a separate file
def rule(pas: str):
    rul_dict = {}
    for i in range(len(pas)):
        if pas[i] not in rul_dict.keys():
            rul_dict[f"char{i}"] = random.randint(1, 9)
        else:
            continue
    f = open("keys", "w")
    for value in rul_dict.values():
        f.write(f"{value}")
    f.close()
    pass


# gets the key from the page, key is different each time rule is called
def get_key():
    f = list(list(open("keys", 'r'))[0])
    return f


# encript rule, each char of the old pass = ascii value - it's value from the random dict
def enc_rule():
    temp = get_key()
    new_pass = ""
    for i in range(len(temp)):
        new_pass += chr(ord(password[i]) - int(temp[i]))
    return new_pass

# reverse the encription
def decr_rule():
    temp = get_key()
    old_pass = ''
    for i in range(len(temp)):
        old_pass += chr(ord(enc_rule()[i]) + int(temp[i]))
    return old_pass


if __name__ == '__main__':
    check_req(password)
    rule(password)
    get_key()
    print(enc_rule())  # Pfhr*-gm,*8&+1cjs -> key is random, can be other result hereq
    print(decr_rule())  # This..is..A..5est
