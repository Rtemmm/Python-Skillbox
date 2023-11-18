import os


def gen_files_path(directory='/', target_dir=None):
    for root, dirs, files in os.walk(directory):
        if target_dir and os.path.basename(root) == target_dir:
            for file in files:
                yield os.path.join(root, file)
        else:
            for file in files:
                yield os.path.join(root, file)


for file_path in gen_files_path(target_dir='my_directory'):
    print(file_path)
