def CheckIP(string):
    ip = string.split(".")
    if len(ip) < 4:
        print("Адрес — это четыре числа, разделённые точками.")
    else:
        for nums in ip:
            for num in nums:
                if not num.isdigit():
                    print(f"{nums} — это не целое число.")
                    return False

            if int(nums) > 255:
                print(f"{nums} превышает 255.")
                return False
        return True


string = input("Введите IP: ")

if CheckIP(string):
    print("IP-адрес корректен.")