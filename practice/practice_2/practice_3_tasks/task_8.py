def IsPalindrom(nums):
    reverseList = []

    for i in range(len(nums) - 1, -1, -1):
        reverseList.append(nums[i])

    if nums == reverseList:
        return True
    return False


def ToPalindrome(nums):
    newNums = []
    answer = []

    for i in range(0, len(nums)):
        for j in range(i, len(nums)):
            newNums.append(nums[j])

        if IsPalindrom(newNums):
            for num in range(0, i):
                answer.append(nums[num])

            answer.reverse()
            return answer

        newNums = []
    return []


n = int(input("Кол-во чисел: "))
nums = []

for i in range(n):
    nums.append(int(input("Число: ")))

print(f"Последовательность: {nums}")

answer = ToPalindrome(nums)

print(f"Нужно приписать чисел: {len(answer)}")
print(f"Сами числа: {answer}")
