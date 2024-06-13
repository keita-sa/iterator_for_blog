import re
str1 = re.sub('[346]', 'x', '03-5454-68284') # Substitute 3,4,6 for x
print(str1)
str1 = re.sub('[.,:;!?]', '', "He has three pets: a cat, a dog and a giraffe, doesn't he?") # Substitute punctuation for empty string
print(str1)
str1 = re.sub('\(a\)|＠', '@', 'accountname＠test.ecc.u-tokyo.ac.jp') # Substitute spam avoidance string for @
print(str1)