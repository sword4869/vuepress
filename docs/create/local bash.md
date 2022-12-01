
# 空项目

## vuepress init(yarn version)

因为npm会出错（比如win上失败了），而yarn则成功了

```bash
$ mkdir project && cd project

$ yarn init

# 将 VuePress 安装为本地依赖
$ yarn add -D vuepress

# 添加运行命令
$ vim package.json
"scripts": {
    "vuepress:dev": "vuepress dev docs",
    "vuepress:build": "vuepress build docs"
}

# 文档放置的地方
$ mkdir docs

# 一篇文档
$ echo '# Hello VuePress' > docs/README.md

# VuePress 站点的基本配置文件的文件夹
$ mkdir -p docs/.vuepress
# VuePress 站点的基本配置文件
$ vim docs/.vuepress/config.ts
import { defineConfig } from "vuepress/config";
export default defineConfig({
  title: 'Hello VuePress',
  base: '/vuepress-starter/',
});

$ yarn vuepress:dev
```
VuePress 会在 <http://localhost:8080> (opens new window)启动一个热重载的开发服务器。


```bash
project
├── docs
│   ├── .vuepress
│   │   └── config.js
│   └── README.md 
├── node_modules
├── package.json
└── yarn.lock
```

# 推送空项目到GitPages

如果懒的话, 不用vuepress, gitpages也可以直接显示md文档


手动提交到gh-pages

## Publishing from a branch

![failure](/images/83ad32c958dacc26e343fa0988ac1868f25889fb9f830f60f9946bf11d77dca4.png)

- 自动Publish的分支是`gh-pages`, 其他命名的分支你还得手动去在setting里选.

- 还可以选择`/`或者`/docs`为source(这估计就是为什么vuepresss推荐的文档放在docs文件夹中)


[一个自动编译,然后提交到gh-pages分支的脚本](../../deploy.sh)


