import re
s1 = '+7 499-456-45-78'
s2 = '+74994564578'
s3 = '7 (499) 456 45 78'
s4 = '+7 (499) 456-45-78'
reg = r'^(\+7|7).*?(\d{3}).*?(\d{3}).*?(\d{2}).*?(\d{2})$'
print(re.findall(reg, s1))
print(re.findall(reg, s2))
print(re.findall(reg, s3))
print(re.findall(reg, s4))


