# -*- coding: utf-8 -*-
#  @Time        :    2018/7/7 1:40
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    python_q14.py
#  @Place       :    dormitory

import os
import platform
from functools import wraps


def get_system_str():
    return platform.system()


def filter_hide_path(forbidden_path):
    print "decorator path:" + str(forbidden_path)

    def hide(_traverse):
        @wraps(wrapped=_traverse)
        def real_traverse(path, suffix):
            absolute_path = os.path.abspath(path)
            inter_forbidden_path = forbidden_path
            if not inter_forbidden_path:
                return _traverse(path, suffix)
            else:
                # 以下写法违反了python的闭包机制，内部函数不能先读再写外部变量，要写就得一开始就写，作为内部变量
                # forbidden_path=os.path.abspath(forbidden_path)
                # 将forbidden_path转为绝对路径
                if isinstance(inter_forbidden_path, (tuple, list)):
                    inter_forbidden_path = map(os.path.abspath, list(inter_forbidden_path))
                else:
                    inter_forbidden_path = os.path.abspath(inter_forbidden_path)
            if isinstance(inter_forbidden_path, (tuple, list)):
                for fp in inter_forbidden_path:
                        # 检测时使用绝对路径
                    if absolute_path.startswith(fp):
                        # 打印时只打印传入的路径，不打印绝对路径
                        print("\"" + path + "\" is forbidden")
                        return
                return _traverse(path, suffix)
            else:
                if absolute_path.startswith(inter_forbidden_path):
                    # 打印时只打印传入的路径，不打印绝对路径
                    print("\"" + path + "\" is forbidden")
                else:
                    return _traverse(path, suffix)

        return real_traverse

    return hide


def get_forbidden_path():
    sys_str = get_system_str()
    if sys_str == "Windows":
        return [r"C:\BK-courses\pynotes\FirstWeek\test_data_q14\save1",
                r"C:\BK-courses\pynotes\FirstWeek\test_data_q14\save2"]
    elif sys_str == "Linux":
        return [r"../../data/small_size/test_data_q14/save1", r"../../data/small_size/test_data_q14/save2"]
    else:
        return None


@filter_hide_path(forbidden_path=get_forbidden_path())
def traverse(path, suffix):
    if not path:
        raise Exception("Path cannot be None!")
    # 默认遍历所有文件
    if not suffix:
        suffix = ""
    if not os.path.exists(path):
        raise Exception("\"" + path + "\" do not exists")
    file_list = os.listdir(path)
    for f in file_list:
        # 求出完整路径
        whole_path = os.path.join(path, f)
        if os.path.isdir(whole_path):
            # 遍历子文件夹
            traverse(whole_path, suffix)
        else:
            # 检测文件后缀名
            if isinstance(suffix, (tuple, list)):
                # 多种后缀名检测
                for s in suffix:
                    if whole_path.endswith(s):
                        print whole_path
                        break
            else:
                # 单个后缀名检测
                if whole_path.endswith(suffix):
                    print whole_path


def win_case():
    # Win
    traverse(r"C:\BK-courses\pynotes\FirstWeek\test_data_q14", None)
    print("=" * 50)
    traverse(r"C:\BK-courses\pynotes\FirstWeek\test_data_q14", "txt")
    print("=" * 50)
    traverse(r"C:\BK-courses\pynotes\FirstWeek\test_data_q14", [".aa", ".txt"])


def linux_case():
    # Linux
    traverse(r"../../data/small_size", None)
    print("=" * 50)
    traverse(r"../../data/small_size", "txt")
    print("=" * 50)
    traverse(r"../../data/small_size", [".aa", ".txt"])


def run_on_system():
    sys_str = get_system_str()
    if sys_str == "Windows":
        print "Call Windows tasks"
        win_case()
    elif sys_str == "Linux":
        print "Call Linux tasks"
        linux_case()
    else:
        print "Other System tasks"
        print "Not support yet"


def main():
    run_on_system()
    pass


if __name__ == '__main__':
    main()
