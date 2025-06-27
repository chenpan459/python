#!/usr/bin/python3

import os

def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            return sum(1 for _ in f)
    except Exception as e:
        print(f"跳过文件 {file_path}，错误: {e}")
        return 0

def count_lines_in_dir(root_dir):
    total_lines = 0
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_lines += count_lines_in_file(file_path)
    return total_lines

if __name__ == "__main__":
    current_dir = os.getcwd()
    total = count_lines_in_dir(current_dir)
    print(f"总行数: {total}")
