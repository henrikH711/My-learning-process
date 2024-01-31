import random

def otos_lotto_szamok():
    return random.sample(range(1, 91), 5)

lotto_szamok = otos_lotto_szamok()
print("Az ötös lottó számai:", lotto_szamok)