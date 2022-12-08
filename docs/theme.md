
# theme

## github edit
```ts
themeConfig: {
    // if your docs are in a different repo from your main project:
    docsRepo: "sword4869/vuepress-starter",
    // if your docs are in a specific branch (defaults to 'master'):
    docsBranch: "main",
    // if your docs are not at the root of the repo:
    docsDir: 'docs',
    // defaults to false, set to true to enable
    editLinks: true,
    // custom text for edit link. Defaults to "Edit this page"
    editLinkText: 'Help us improve this page!'
}
```
效果:

![picture 1](../images/adae92a53549c0e6f4a9b5094e78c466f87c99bd57641f07e93317ab82274b9d.png)
 
![picture 2](../images/321b27a8bc06a3bfa3cff2c58e8c45e7ffc59c4881d5244fb13cf3d6382c161c.png)  

## sidebar

```ts
themeConfig: {
  sidebar: {
    "/": [
      ["/", "README"],
      ["/theme.md", "theme.md"],
      {
        title: "create",
        children: [
          ["/create/deploy脚本.md", "deploy脚本.md"],
          ["/create/github action.md", "github action.md"],
          ["/create/图片格式.md", "图片格式.md"],
          ["/create/空项目.md", "空项目.md"],
          { title: "fake", children: [["/create/fake/test.md", "test.md"]] },
        ],
      },
    ],
  },
}
```
## 确认  
- "vuepress-plugin-code-copy"
  
  代码块的复制

- "vuepress-plugin-helper-live2d"

  看板娘

- "vuepress-plugin-reading-progress"

  在最上方以进度条的形式显示阅读进度

## 阅读时长(失败)
```bash
yarn add -D @mr-hope/vuepress-plugin-reading-time
```
```ts
plugins: [
    [
      "@mr-hope/reading-time",
      {
        // 配置选项
      },
    ],
  ],
```