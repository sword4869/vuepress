import os
import sys

path = os.getcwd()
print(f'path={path}')

# for root, dirs, files in os.walk(path, topdown=True):
#     print(root)
#     print(dirs)
#     print(files)
#     # 用途一：遍历文件
#     # for name in files:
#     #     print(os.path.join(root, name))

#     # 用途二：遍历所有的文件夹
#     for name in dirs:
#         print(os.path.join(root, name))

#     print('-'*10)

a = [
    ('/home/lab/git/learn_python/docs', 
        ['命令行', '声音处理', '配置', '图像', 'other', 'virtual environment', '压缩', '路径', '.vuepress', '控制台效果', '读写文件'], 
        ['README.md']),
     ('/home/lab/git/learn_python/docs/命令行', [],
      ['readme.md', 'sh.py', 'sh.ipynb', 'tmp_log.log']),
     ('/home/lab/git/learn_python/docs/声音处理', [], ['pydub.md']),
     ('/home/lab/git/learn_python/docs/配置', ['配置文件', '读取命令行'], []),
     ('/home/lab/git/learn_python/docs/配置/配置文件',
      ['csv', 'json', 'ini', 'yaml', 'configargparse'], ['regex.md']),
     ('/home/lab/git/learn_python/docs/配置/配置文件/csv', [],
      ['csv.ipynb', 'some.csv']),
     ('/home/lab/git/learn_python/docs/配置/配置文件/json', [],
      ['json.md', 'some.json', 'json.ipynb']),
     ('/home/lab/git/learn_python/docs/配置/配置文件/ini', [], ['ini.md']),
     ('/home/lab/git/learn_python/docs/配置/配置文件/yaml', [],
      ['yaml.ipynb', 'yaml.md', 'some.yaml']),
     ('/home/lab/git/learn_python/docs/配置/配置文件/configargparse', [],
      ['some.ini', 'some.txt', 't.py', 'some.yaml', 'configargparse.md']),
     ('/home/lab/git/learn_python/docs/配置/读取命令行', [],
      ['readme.md', 'argparse.md', 'sys and getopt.md']),
     ('/home/lab/git/learn_python/docs/图像', [],
      ['PIL.ipynb', '1.jpg', 'skvideo.io.ipynb', 'ffmpy.md']),
     ('/home/lab/git/learn_python/docs/other', [],
      ['adb.md', 'the use guidance of jupyter notebook.md', '调试pdb.ipynb']),
     ('/home/lab/git/learn_python/docs/virtual environment', [],
      ['pip.md', 'requirements.md', 'virtualenv.md', 'conda.md']),
     ('/home/lab/git/learn_python/docs/压缩', [], ['pickle.md']),
     ('/home/lab/git/learn_python/docs/路径', [],
      ['readme.md', 't.ipynb', 'os.md']),
     ('/home/lab/git/learn_python/docs/.vuepress', [], ['config.ts']),
     ('/home/lab/git/learn_python/docs/控制台效果', [],
      ['color.md', 'print.md', '进度条.ipynb']),
     ('/home/lab/git/learn_python/docs/读写文件', [], ['filename.ipynb'])]

# [
#       {
#         title: 'create',
#         children: [
#           ['/create/空项目.md','空项目.md'],
#           ['/create/deploy脚本.md','deploy脚本.md'],
#           ['/create/github action.md','github action.md'],
#           ['/create/图片格式.md','图片格式.md'],
#         ],
#       },
#       {
#         title: 'theme',
#         children: [
#           ['theme.md','theme.md'],
#         ]
#       }
#     ]
#   }
# ]
result = []

for name in a[0][1]:
    if os.path.isdir(os.path.join(root, name)):
        result.append({
            'title': name,
            'children': []
        })
    else:
        result.append(name)

def getDD(path):
    root, dirs, files = a[0]
    for dir in dirs:
        result.append({
            'title': name,
            'children': []
        })
    result += files