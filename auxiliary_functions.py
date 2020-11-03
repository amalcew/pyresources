# Module with various utilities to help with other tasks
import ssl
import os


def determine_ssl():
    if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
            getattr(ssl, '_create_unverified_context', None)):
        ssl._create_default_https_context = ssl._create_unverified_context


def binary_search(lst, num):
    m = len(lst)//2
    if lst[m] == num:
        return True
    if m != 0:
        if lst[m] > num:
            return binary_search(lst[:m], num)
        elif lst[m] < num:
            return binary_search(lst[m:], num)
    else:
        return False
