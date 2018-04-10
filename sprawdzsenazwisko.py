import hashlib

nazwisko = input("Podaj nazwisko wariacie (Z DUZEJ!):")
asciii = ""

for letter in nazwisko:
  asciii = asciii + str(ord(letter))

print("Goracy kodzik:")
print(hashlib.md5(str(asciii).encode('utf-8')).hexdigest())
