import csv

def write_csv_file(filename, fieldnames, data):

    if not file_exists(filename):
        create_file(filename, fieldnames)

    append_row(filename, fieldnames, data)

def file_exists(filename):
    try:   
        with open(filename, 'r', newline="") as csvfile:
            return True
    except:
            return False
    
def create_file(filename, fieldnames):
    with open(filename, 'w', newline="") as csvfile:
        writer = csv.DictWriter(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, fieldnames=fieldnames)
        writer.writeheader()


def append_row(filename, fieldnames, data):
    with open(filename, 'a', newline="") as csvfile:
        writer = csv.DictWriter(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, fieldnames=fieldnames)
        writer.writerow(data)