import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>123456789"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

def game():
    moneta = random.randint(1, 100)
    if moneta <= 49:
        return "решка"
    elif moneta >= 50 and moneta <= 99:
        return "орел"
    else:
        return "монета встала на ребро"
    
def dice():
    dice = random.randint(1, 6)
    return dice
