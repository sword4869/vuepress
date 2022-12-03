import os
import sys

path = os.getcwd()
print(f"path={path}")


"""
for root, dirs, files in a[1:]:
    print(root)
    print(dirs)
    print(files)

    
    # 用途一：遍历文件
    for name in files:
        result.append((root, name))

    # 用途二：遍历所有的文件夹
    for name in dirs:
        print(os.path.join(root, name))
"""


walks = [
    (
        "",
        [
            "命令行",
            "声音处理",
            "配置",
            "图像",
            "other",
            "virtual environment",
            "压缩",
            "路径",
            ".vuepress",
            "控制台效果",
            "读写文件",
        ],
        ["README.md"],
    ),
    ("命令行", [], ["readme.md", "sh.py", "sh.ipynb", "tmp_log.log"]),
    ("声音处理", [], ["pydub.md"]),
    ("配置", ["配置文件", "读取命令行"], []),
    ("配置/配置文件", ["csv", "json", "ini", "yaml", "configargparse"], ["regex.md"]),
    ("配置/配置文件/csv", [], ["csv.ipynb", "some.csv"]),
    ("配置/配置文件/json", [], ["json.md", "some.json", "json.ipynb"]),
    ("配置/配置文件/ini", [], ["ini.md"]),
    ("配置/配置文件/yaml", [], ["yaml.ipynb", "yaml.md", "some.yaml"]),
    (
        "配置/配置文件/configargparse",
        [],
        ["some.ini", "some.txt", "t.py", "some.yaml", "configargparse.md"],
    ),
    ("配置/读取命令行", [], ["readme.md", "argparse.md", "sys and getopt.md"]),
    ("图像", [], ["PIL.ipynb", "1.jpg", "skvideo.io.ipynb", "ffmpy.md"]),
    ("other", [], ["adb.md", "the use guidance of jupyter notebook.md", "调试pdb.ipynb"]),
    (
        "virtual environment",
        [],
        ["pip.md", "requirements.md", "virtualenv.md", "conda.md"],
    ),
    ("压缩", [], ["pickle.md"]),
    ("路径", [], ["readme.md", "t.ipynb", "os.md"]),
    (".vuepress", [], ["config.ts"]),
    ("控制台效果", [], ["color.md", "print.md", "进度条.ipynb"]),
    ("读写文件", [], ["filename.ipynb"]),
]


'''
[
      {
        title: 'create',
        children: [
          ['/create/空项目.md','空项目.md'],
          ['/create/deploy脚本.md','deploy脚本.md'],
          ['/create/github action.md','github action.md'],
          ['/create/图片格式.md','图片格式.md'],
        ],
      },
      {
        title: 'theme',
        children: [
          ['theme.md','theme.md'],
        ]
      },
    ]
  }
]
'''


items = []

for root, dirs, files in walks:    
    # 用途一：遍历文件
    for name in files:
        print((root, name))
        items.append((root, name))


print(items)

for root, name in items:
    root_splits = root.split("/")
    root_splits_length = 0 if root=="" else len(root_splits)








def add_directory(part_result, root_splits_length, dirs):
    for dir in dirs:
        part_result.append({"title": dir, "children": []})

def add_file(part_result, root_splits_length, files):
    for file in files:
        part_result.append([file, file])















items = list(a)
k = 1
def fu(k):
    print(f'k={k}')
    j = 0
    index = 0
    while index < len(items):
        root, dirs, files = items[index]
        
        if root == "":
            for dir in dirs:
                result.append({"title": dir, "children": []})
            for file in files:
                result.append([file, file])
            items.pop(index)
            break

        root_splits = root.split("/")
        
        if len(root_splits) == k:
            # 直接是文件,就添加
            if len(dirs) == 0:
                for file in files:
                    result[j]["children"].append(file)
                items.pop(index)
                j += 1
                index -=1
    

        index += 1
        

    k += 1
    


# while len(items) > 0:
for k in range(2):
    fu(k)
    print(items)
    print(result)