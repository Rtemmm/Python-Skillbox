import os


def get_directory_info(path):
    total_files = 0
    total_subdirectories = 0
    total_size = 0

    for root, dirs, files in os.walk(path):
        total_files += len(files)
        total_subdirectories += len(dirs)
        total_size += sum(os.path.getsize(os.path.join(root, name)) for name in files)

    total_size_in_kb = total_size / 1024

    print(f"Общее количество файлов: {total_files}")
    print(f"Общее количество подкаталогов: {total_subdirectories}")
    print(f"Общий размер каталога: {round(total_size_in_kb, 2)} КБ")


get_directory_info(r"H:\Unik\Proj Python\practice\practice_9_tasks")
