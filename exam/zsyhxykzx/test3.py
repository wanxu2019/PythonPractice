# -*- coding: utf-8 -*-
#  @Time        :    2018/9/16 19:30
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    test3.py
#  @Place       :    dormitory

def is_good_number(n):
    bad_numbers = ['3', '4', '7']
    good_numbers = ['2', '5', '6', '9']
    n_str = str(n)
    has_good_number = False
    for ch in n_str:
        if ch in bad_numbers:
            return False
        elif ch in good_numbers:
            if not has_good_number:
                has_good_number = True
    return has_good_number


def main():
    n = int(raw_input())
    print(sum(map(is_good_number, (i for i in range(1, n + 1)))))
    pass


if __name__ == '__main__':
    main()
