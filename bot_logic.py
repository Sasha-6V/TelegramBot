import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>123456789"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

def game():
    moneta = random.randint(1,2)
    if moneta == 1:
        return "решка"
    else:
        return "орел"
