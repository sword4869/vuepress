
---
# Hello VuePress
## 图片格式

```markdown
!['./_images'](./_images/83ad32c958dacc26e343fa0988ac1868f25889fb9f830f60f9946bf11d77dca4.png)  
!['_images'](_images/83ad32c958dacc26e343fa0988ac1868f25889fb9f830f60f9946bf11d77dca4.png)  
!['/_images'](/_images/83ad32c958dacc26e343fa0988ac1868f25889fb9f830f60f9946bf11d77dca4.png)  
``` 

只支持第一种相对路径的格式。

图片不用复制, 因为在html中会转化成base64的格式
```
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACsAAAAqCAIAAAClYzUyAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAE8SURBVFhHY/z8+TPDgAImKD1wYNQFoy4AgVEXjLoABEZdMGRd8PfrvQv3vv6F8igE5Ljg5famwvrChIyO3U+gIpQAcmNB0StM996s7NDCZZcoDAxyXcAma5c3a0FvovieWgoDg6KUyK3iVTF7VoXZS0oCgyIXgACzuHFqPyWBQbELwICSwKCOC0CA3MCgngvAABQYM/r9OY9PmbTtJVSMAKCyCxie7O7ILt/43TI9zV4cKkQAUM8Ff79eWlYYmj3rpUXFlBkVXircUHFCgEouAHo9I6F5v3hi74L+ZGNxZqgwMYBiF5DrdTigyAVf72wj2+twQK4Lfj0+PrcwoXg+0OuzyPI6HJDrgvvblp6Ael2QLK/DAVk9V2D74PJLcV0lbsrshoDRvvOoC0Bg1AWjLgCBUReMuoCBgYEBAF6thKeX41u2AAAAAElFTkSuQmCC" alt="图 1">
```
## directory structure


```bash
.
├── docs
│   ├── .vuepress
│   │   └── config.js
│   └── README.md 
├── node_modules
├── package.json
└── yarn.lock
```
# 用bash命令
## vuepress init(npm version)
```bash
$ cd project

$ npm init

# 将 VuePress 安装为本地依赖
$ npm install -D vuepress

$ vim package.json
"scripts": {
    "vuepress:dev": "vuepress dev docs",
    "vuepress:build": "vuepress build docs"
},

$ mkdir -p docs/.vuepress

$ cd docs/.vuepress

docs/.vuepress$ vim config.js
module.exports = {
    title: 'Hello VuePress',
    description: 'Just playing around',
    base: '/vuepress-starter/'
}

docs/.vuepress$ cd ..

$ npm run vuepress:dev
```

VuePress 会在 <http://localhost:8080> (opens new window)启动一个热重载的开发服务器。

## vuepress init(yarn version)

因为npm会出错（比如win上失败了），而yarn则成功了

```bash
$ cd project

$ yarn init

# 将 VuePress 安装为本地依赖
$ yarn add vuepress -dev

$ vim package.json
"scripts": {
    "vuepress:dev": "vuepress dev docs",
    "vuepress:build": "vuepress build docs"
},

$ mkdir -p docs/.vuepress

$ cd docs/.vuepress

docs/.vuepress$ vim config.js
module.exports = {
    title: 'Hello VuePress',
    description: 'Just playing around',
    base: '/vuepress-starter/'
}

docs/.vuepress$ cd ..

$ yarn vuepress:dev
```
# GitPages

如果懒的话, 不用vuepress, gitpages也可以直接显示md文档


Publishing from a branch: 手动提交到gh-pages
Publishing with a custom GitHub Actions workflow: 提交到主分支时就会自动更新
## Publishing from a branch

![failure](./images/83ad32c958dacc26e343fa0988ac1868f25889fb9f830f60f9946bf11d77dca4.png)

- 自动Publish的分支是`gh-pages`, 其他命名的分支你还得手动去在setting里选.
- 还可以选择`/`或者`/docs`为source(这估计就是为什么vuepresss推荐的官方格式)

<!-- ![picture 1](./_images/83ad32c958dacc26e343fa0988ac1868f25889fb9f830f60f9946bf11d77dca4.png)   -->

[一个自动编译,然后提交到gh-pages分支的脚本](deploy.sh)


## Publishing with a custom GitHub Actions workflow

```bash
$ mkdir -p .github/workflows

$ cd .github/workflows

# 名字随便
.github/workflows$ vim actions.yml
```
创建token
点击你的头像 > Settings > Developer settings > Personal access tokens > Generate new token (classic). 权限至少要勾选repo, workflow

在仓库Settings> Secrets> Actions> New repository secret> 命名变量`ACCESS_TOKEN`, 填上生成token的值


[actions.yml](.github/workflows/actions.yml)

`TARGET_BRANCH`: 这个不是根据哪个分支什么, 而是是要生成的. 所以你会看到自己多了一个gh-pages分支