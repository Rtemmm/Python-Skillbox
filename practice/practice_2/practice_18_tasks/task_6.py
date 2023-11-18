import json


def compare_json_files(file1, file2, diff_list):
    with open(file1, 'r') as f:
        data1 = json.load(f)

    with open(file2, 'r') as f:
        data2 = json.load(f)

    result = {}
    for key in diff_list:
        if data1.get(key) != data2.get(key):
            result[key] = data2.get(key)

    return result


def write_to_json_file(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)


file1 = 'json_old.json'
file2 = 'json_new.json'
diff_list = ['services', 'staff', 'datetime']

result = compare_json_files(file1, file2, diff_list)
write_to_json_file(result, 'result.json')

print(result)
