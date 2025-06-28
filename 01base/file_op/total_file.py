import os

def count_files_in_current_dir():
    count = 0
    for entry in os.listdir('.'):
        if os.path.isfile(entry):
            count += 1
    print(f"当前目录下文件数量: {count}")

if __name__ == "__main__":
    count_files_in_current_dir()