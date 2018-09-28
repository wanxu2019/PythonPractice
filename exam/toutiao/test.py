# -*- coding: utf-8 -*-
#  @Time        :    2018/9/20 20:40
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    test.py
#  @Place       :    dormitory


def main():
    char_list = raw_input().split("/")
    result = []
    for ch in char_list:
        if ch == '..':
            if len(result) > 0:
                result = result[:-1]
        elif ch != '.' and ch != '':
            result.append(ch)
    print "/" + "/".join(result)


if __name__ == '__main__':
    main()
