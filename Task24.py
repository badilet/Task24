# Напишите функцию которая будет определять полигдром ли введенная строка. Если да 2
# то печатать “True”, если нет “False”.

str = input("Enter a word:")
if str == str[::-1]:
    print("It is polindrom!")
else:
    print("It is not polindrom! :(")
