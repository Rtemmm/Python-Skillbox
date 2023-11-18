n = int(input("Количество видеокарт: "))
gpu = []

for i in range(n):
    gpu.append(int(input(f"Видеокарта {i + 1}: ")))

print("Старый список видеокарт: ", gpu)

maxGpu = max(gpu)
while maxGpu in gpu:
    gpu.remove(maxGpu)

print("Новый список видеокарт: ", gpu)
