import os
import sys

"""
[
    {
        title: 'create',
        children: [
            ['/create/空项目.md','空项目.md'],
            ['/create/deploy脚本.md','deploy脚本.md'],
            ['/create/github action.md','github action.md'],
            {
                title: 'create',
                children: [
                    ['/create/空项目.md','空项目.md'],
                    ['/create/deploy脚本.md','deploy脚本.md'],
                    ['/create/github action.md','github action.md'],
                    ['/create/图片格式.md','图片格式.md'],
                ],
            },
        ],
    },
    ['theme.md','theme.md']
]
"""


def tree_dir(dir, part_result, prefix=""):
    files = sorted(os.listdir(dir))
    file_lst = []
    dir_lst = []
    for file in files:
        file_path = os.path.join(dir, file)
        if os.path.isfile(file_path):
            # docs/README.md 会报错，也不能显示
            if prefix == '' and file == 'README.md':
                continue
            file_lst.append(file)
        else:
            # 我们不显示 docs/.vuepress文件夹
            if file == '.vuepress':
                continue
            dir_lst.append(file)


    for file in file_lst:
        part_result.append([prefix + file, file])

    for subdir in dir_lst:
        subdir_path = os.path.join(dir, subdir)
        part_result.append({"title": subdir, "children": []})
        tree_dir(subdir_path, part_result[-1]["children"], prefix + "/" + subdir + "/")


result = {"title": "starter", "children": []}
tree_dir(sys.argv[1], result["children"])
print(result)
