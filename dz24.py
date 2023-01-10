import re

s = '1x, Text ABC 123 A1B2C3'
reg = r'[\w+" "]\d[\w+" "]'
print(re.findall(reg, s))