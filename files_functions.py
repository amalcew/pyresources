def convert_to_list(file):
    file = open(file, encoding='utf-8').readlines()
    if "\n" not in file[-1]:
        file[-1] = file[-1] + "\n"
    file = [w[:-1] for w in file]
    return file


def extract_unique(lst):
    unique_lst = []
    for x in lst:
        if x not in unique_lst:
            unique_lst.append(x)
    return unique_lst
