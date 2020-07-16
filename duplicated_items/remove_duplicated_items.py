def remove_duplicated_items(list_with_duplicated_items):
    return(list(set(list_with_duplicated_items)))

def create_list_from_file(file_with_duplicated_items):
    with open(file_with_duplicated_items, 'r') as file:
        raw_file = file.read()
        list_from_file = list(raw_file.split())
        return(list_from_file)

def create_file_from_list(list_to_file, file_name):
    with open(file_name, 'w') as file:
        for i in list_to_file:
            file.write(i)
            file.write('\n')

input_file = input("Input file: ")
output_file = input_file + '_without_duplicated_items.txt'

try:
    raw_list = create_list_from_file(input_file)
    list_without_duplicated_elements = remove_duplicated_items(raw_list)
    list_without_duplicated_elements.sort()
    create_file_from_list(list_without_duplicated_elements, output_file)
except FileNotFoundError:
        print("File does not exist.")
