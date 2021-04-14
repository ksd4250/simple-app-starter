import json
"""
find.py
Finds duplicates entries in a csv file and outputs them to a json file
Author: Kelsey Donovan
"""

entries = [] #non-duplicate entries
duplicate_entries = [] #duplicate entries


def find_duplicate_entries():
    with open('test-files/normal.csv', 'r') as my_file:
        for line in my_file:
            element = line.strip().split(',')
            if element[2] not in entries:
                #populate the non-duplicate entries list
                entries.append(element[2])
            else:
                # populate the duplicate entries list
                duplicate_entries.append(element[2])


def duplicates_textfile():
    #Add the duplicates to a txt file that can then be moved into a json file
    if len(duplicate_entries) > 0:
        with open('duplicateElements.txt', 'w') as out_file:
            with open('test-files/normal.csv, 'r') as my_file:
                      for line in my_file:
                element = line.strip().split(',')
            if element[2] in duplicate_entries:
                out_file.write(line)
            else:
                print("No duplications")


def non_duplicates_textfile():
    #Add the non-duplicates to a txt file that can then be moved into a json file
    if len(entries) > 0:
        with open('elements.txt', 'w') as out_file:
            with open('test-files/normal.csv', 'r') as my_file:
                for line in my_file:
                    element = line.strip().split(',')
                    if element[2] in entries:
                        out_file.write(line)
    else:
        print("Only duplications")


def moving_to_json_file():
    filename = 'duplicateElements.txt'
    # creating dictionary for the elements
    Elements = {}
    with open(filename) as fh:
        for line in fh:
            #Removes any extra spaces
            command, description = line.strip().split(None, 1)
            Elements[command] = description.strip()
    #Converting elements.txt to a list
    a_file = open("elements.txt", "r")

    list_of_lists = []
    for line in a_file:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        list_of_lists.append(line_list)

    a_file.close()

    # creating json output file
    out_file = open("duplicateElements.json", "w")
    json.dump(Elements, out_file, indent=4, sort_keys=False)
    json.dump(list_of_lists, out_file, indent=4, sort_keys=False)


def main():
    find_duplicate_entries()
    duplicates_textfile()
    non_duplicates_textfile()
    moving_to_json_file()


main()