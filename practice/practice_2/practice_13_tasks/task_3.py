import os


def gen_file_lines(directory='.'):
    for filename in os.listdir(directory):
        if filename.endswith('.py'):
            with open(os.path.join(directory, filename), 'r') as file:
                lines = file.readlines()
                non_comment_lines = [line for line in lines if not line.strip().startswith('#') and line.strip() != '']
                yield len(non_comment_lines)


for lines in gen_file_lines():
    print(lines)
