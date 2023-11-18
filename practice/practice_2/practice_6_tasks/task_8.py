def CanBePalindrome(string):
    frequency = {letter: string.count(letter) for letter in string}
    count = 0

    for value in frequency.values():
        if value % 2 != 0:
            count += 1
    return count <= 1


string = "aab"

if CanBePalindrome(string):
    print("Можно сделать палиндромом")
else:
    print("Нельзя сделать палиндромом")
