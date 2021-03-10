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


def heapify(lst, n, index):
    largest = index
    child_left = 2 * index + 1
    child_right = 2 * index + 2

    # check if left child of root exists and is greater than root
    if child_left < n and lst[largest] < lst[child_left]:
        largest = child_left
    # check if right child of root exists and is greater than root
    if child_right < n and lst[largest] < lst[child_right]:
        largest = child_right
    # swap root and continue process if root is not largest
    if largest != index:
        lst[index], lst[largest] = lst[largest], lst[index]  # swap
        heapify(lst, n, largest)


def heap_sort(lst):
    n = len(lst)
    sorted_lst = []

    # build max heap
    for i in range(n//2 - 1, -1, -1):
        heapify(lst, n, i)

    for i in range(n - 1, 0, -1):
        # swap root with last element
        lst[i], lst[0] = lst[0], lst[i]
        # append max element and pop it from the heap
        sorted_lst.append(lst.pop(i))
        # heapify the root element
        heapify(lst, i, 0)

    # append the remaining root element
    sorted_lst.append(lst[i - 1])
    # reverse the sorted list
    return sorted_lst[::-1]
