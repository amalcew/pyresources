def bubble_sort(lst):
    for i in range(0, len(lst)-1):
        for j in range(0, len(lst)-1):
            if lst[j+1] < lst[j]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


def selection_sort(lst):
    for i in range(0, len(lst)):
        minimal = i
        for j in range(i, len(lst)):
            if lst[j] < lst[minimal]:
                minimal = j
        lst[minimal], lst[i] = lst[i], lst[minimal]
    return lst


def insertion_sort(lst):
    sorted_lst = []
    for i in range(0, len(lst)):
        sorted_lst.append(lst[i])
        for j in range(len(sorted_lst)-1):
            if sorted_lst[-1] < sorted_lst[j]:
                sorted_lst[j], sorted_lst[-1] = sorted_lst[-1], sorted_lst[j]
    return sorted_lst