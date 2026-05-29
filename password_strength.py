password = input("\nEnter your Password: ")
masked_pass = "*" * len(password)

points = 0
has_enough_length = False
has_digits = False
has_upper = False
has_lower = False
has_special = False


if len(password) < 8:
    has_enough_length = False
else:
    has_enough_length = True

for i in password:
    if i.isupper():
        has_upper = True
        break
    else:
        has_upper = False

for i in password:
    if i.islower():
        has_lower = True
        break
    else:
        has_lower = False

for i in password:
    if i.isdigit():
        has_digits = True
        break
    else:
        has_digits = False

sp = "!@#$%&"
for i in password:
    if i in sp:
        has_special = True
        break
    else:
        has_special = False

print("\nPassword :", masked_pass)
print("Length :", has_enough_length)
print("Digits :", has_digits)
print("UpperCase :", has_upper)
print("LowerCase :", has_lower)
print("Special :", has_special)

if has_enough_length:
    points += 2
if has_digits:
    points += 2
if has_upper:
    points += 2
if has_lower:
    points += 2
if has_special:
    points += 2

if points == 10:
    print("\nPassword is Hard")
elif points >= 6:
    print("\nPassword is Medium")
else:
    print("\nPassword is Easy")