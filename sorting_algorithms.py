import random


def bubble_sort(lst):
    for i in range(0, len(lst)-1):
        for j in range(0, len(lst)-1):
            if lst[j+1] < lst[j]:
                lst[j], lst[j+1] = lst[j+1], lst[j]


def selection_sort(lst):
    for i in range(0, len(lst)):
        minimal = i
        for j in range(i, len(lst)):
            if lst[j] < lst[minimal]:
                minimal = j
        lst[minimal], lst[i] = lst[i], lst[minimal]


def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key


def heap_sort(lst):
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

    n = len(lst)
    sorted_lst = []

    # build max heap
    for i in range(n//2 - 1, -1, -1):
        heapify(lst, n, i)

    for i in range(n - 1, 0, -1):
        # swap root with last element
        lst[i], lst[0] = lst[0], lst[i]
        # heapify the root element
        heapify(lst, i, 0)


def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        left_lst = lst[:mid]
        right_lst = lst[mid:]

        merge_sort(left_lst)
        merge_sort(right_lst)

        i = 0
        j = 0
        k = 0
        while i < len(left_lst) and j < len(right_lst):
            if left_lst[i] <= right_lst[j]:
                lst[k] = left_lst[i]
                i = i+1
            else:
                lst[k] = right_lst[j]
                j = j+1
            k = k+1

        while i < len(left_lst):
            lst[k] = left_lst[i]
            i = i+1
            k = k+1

        while j < len(right_lst):
            lst[k] = right_lst[j]
            j = j+1
            k = k+1


def quick_sort(lst, first_elem, last_elem):
    if first_elem >= last_elem:
        return
    i, j = first_elem, last_elem
    pivot = lst[random.randint(first_elem, last_elem)]
    while i <= j:
        while lst[i] < pivot:
            i += 1
        while lst[j] > pivot:
            j -= 1
        if i <= j:
            lst[i], lst[j] = lst[j], lst[i]
            i, j = i + 1, j - 1
    quick_sort(lst, first_elem, j)
    quick_sort(lst, i, last_elem)