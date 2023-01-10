import re
a = input('Введите дату в формате dd-mm-YYYY: ')
# res = r'\d{2,4}?'
res = r'[1-9]{2,4}'
print(re.findall(res, a))
