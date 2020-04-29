# 과제 2
import re

a = 'My  naMe  is  Son  Chang  Ha:  my  pin  is  000125-3!!!!!!.'

try1 = " ".join(a.split())
try2 = try1.replace(":",",")
try3 = re.sub('[!]',"",try2)
w = "naMe".lower()
ww = "m".upper()
try4 = try3[:3]
try5 = try3[7:25]
try6 = try3[26:]

print(try4+w+try5+ww+try6) 
