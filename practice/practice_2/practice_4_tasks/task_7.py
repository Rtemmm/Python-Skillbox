nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

firstPart =[]
answer = []

tmp = [firstPart.extend(x) for x in nice_list]
tmp = [answer.extend(x) for x in firstPart]

print(answer)
