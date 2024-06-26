import json

def write_json_file(filename, data):

    if not file_exists(filename):
        create_file(filename, data)
    else:
        append_row(filename, data)


def file_exists(filename):

    try:   
        with open(filename, 'r'):
            return True
    except:
            return False


def create_file(filename, data):

    with open(filename, "w") as jsonfile:
        json.dump([data], jsonfile)


def read_file(filename):

    with open(filename) as jsonfile:
       return json.load(jsonfile)


def append_row(filename, data):
    
    original_data:list = read_file(filename)
    new_data:list = original_data.copy()
    new_data.append(data)

    with open(filename, "w") as jsonfile:
        json.dump(new_data, jsonfile)
       