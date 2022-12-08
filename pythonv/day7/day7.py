from dataclasses import dataclass
from functools import reduce
true_sum = sum

testInput = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

def is_command(parts):
    return parts[0] == '$'

def is_dir(parts):
    return parts[0] == 'dir'

def is_file(parts):
    try:
        size = int(parts[0])
        return True
    except:
        return False

def parse_output(parts):
    res = {
        "is_command": False,
        "is_dir": False,
        "is_file": False,
    }
    if is_command(parts):
        res["is_command"] = True
        res["command"] = parts[1]
        res["dir_name"] = None if len(parts) < 3 else parts[2]
    if is_dir(parts):
        res["is_dir"] = True
        res["dir_name"] = parts[1]
    if is_file(parts):
        res["is_file"] = True
        res["size"] = int(parts[0])
        res["file_name"] = parts[1]
    return res

@dataclass
class FileItem:
    name: str
    is_dir: bool = False
    size: int = None
    files: list = None

full_path = lambda fs: reduce(lambda c, a: c + a + '/', fs)

def generate_files(input):
    # input = testInput.split('\n')
    fs = []
    files = {}
    curr_dir = lambda: fs[-1]
    paths = lambda: list(map(lambda f: f.name, fs))

    for line in input:
        parts = line.split(' ')
        data = parse_output(parts)
        print('executing', data)
        if data["is_command"]:
            if data["command"] == 'ls':
                continue
            if data["command"] == 'cd':
                dir_name = data["dir_name"]
                if dir_name == '..':
                    fs.pop()
                    continue
                dir = FileItem(name=dir_name, is_dir=True, files=[])
                if dir_name in files:
                    raise Exception("duplicate file name")
                fs.append(dir)
                files[full_path(paths())] = dir
        if data["is_dir"]:
            curr_dir().files.append(data["dir_name"])
        if data["is_file"]:
            file_name = data["file_name"]
            file = FileItem(name=file_name, size=data["size"])
            files[full_path(paths() + [file_name])] = file
            curr_dir().files.append(file_name)
    
    sum_under_100k = 0
    sums = []
    def calc_size(path):
        dir = files[full_path(path)]
        if dir.size is not None:
            if dir.is_dir:
                print("unexpectedly fetching size for dir")
            return dir.size
        sum = 0
        for file_name in dir.files:
            file_path = path + [file_name]
            file = files[full_path(file_path)]
            if file is None:
                raise f"couldn't find file {file}"
            file.size = calc_size(file_path)
            sum += file.size
        # print('calculated dir', path, sum)
        if sum <= 100000:
            # global sum_under_100k
            # sum_under_100k = sum_under_100k + sum
            sums.append(sum)
            print('sums', true_sum(sums))
        return sum
    # 40913445
    root_size = calc_size(['/'])
    files['/'].size = root_size
    return files
    print(root_size)
    # sum = 0
    # for file in files:
    #     if not file.is_dir:
    #         continue
    #     if file.size > 100_000:
    #         continue
    #     sum += file.size
    # print(sum)
    print(sum_under_100k)
    # print(files)

def part1(input):
    generate_files(input)

def part2(input):
    files = generate_files(input)
    total_space = 70000000
    needed_free_space = 30000000
    needed_space = (files["/"].size  + needed_free_space) - total_space
    print(needed_space)
    dir_sizes = []
    
    def find_dirs(path):
        file = files[full_path(path)]
        if not file.is_dir:
            return
        dir_sizes.append(file.size)
        for child in file.files:
            find_dirs(path + [child])
    
    print(find_dirs(['/']))
    print(dir_sizes)
    print(needed_space)
    dir_sizes = list(filter(lambda s: s >= needed_space, dir_sizes))
    print(min(dir_sizes))


