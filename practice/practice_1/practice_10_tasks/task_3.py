fileSize = float(input("Введите размер файла обновления в мегабайтах: "))
speed = float(input("Введите скорость интернет-соединения в мегабайтах в секунду: "))
seconds = 0
downloaded = 0
while downloaded < fileSize:
    downloaded += speed
    seconds += 1
    percentage_downloaded = round((downloaded / fileSize) * 100)
    if percentage_downloaded > 100:
        percentage_downloaded = 100
    if downloaded > fileSize:
        downloaded = fileSize
    print(f"Прошло {seconds}секунд. Скачано {round(downloaded)} MB файла. {percentage_downloaded}% файла.")
print(f"Скачивание заняло {seconds} секунд.")
