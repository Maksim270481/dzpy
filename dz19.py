import re


def login(a):
    return re.findall(r'^[A-z_@-]{6,18}$', a)


print(login('my-p@ssword_'))