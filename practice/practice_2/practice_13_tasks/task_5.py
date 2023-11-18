def error_log_generator(filepath):
    with open(filepath, 'r') as file:
        for line in file:
            if 'ERROR' in line:
                yield line


def write_error_logs_to_file(input_filepath, output_filepath):
    with open(output_filepath, 'w') as file:
        for line in error_log_generator(input_filepath):
            file.write(line)


input_filepath = 'path_to_your_log_file.log'
output_filepath = 'error_logs.log'
write_error_logs_to_file(input_filepath, output_filepath)
