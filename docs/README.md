# REAME
## bash
```bash
yarn init
yarn add -D vuepress
mkdir docs

mkdir -p .github/workflows
touch .github/workflows/ci.yml

touch .gitignore
```

```bash
project
├── docs
│   ├── README.md 
│   └── xxx文件夹 
|       └── xxx.md
├── node_modules
└── package.json
```
## package.json

```js
    "scripts": {
        "vuepress:dev": "vuepress dev docs",
        "vuepress:build": "vuepress build docs"
    },
    "devDependencies": {
        "vuepress": "^1.9.7",
        "vuepress-plugin-code-copy": "^1.0.6",
        "vuepress-plugin-helper-live2d": "^1.0.2",
        "vuepress-plugin-reading-progress": "^1.0.10"
    }
```
## .github/workflows/ci.yml

`docs/.vuepress/config.ts` 已经完全不用写了，我已经将其集成到action [sword4869/vuepress-deploy](https://github.com/sword4869/vuepress-deploy)中了。

```yaml
name: Build and Deploy
on: 
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: vuepress-deploy
        uses: sword4869/vuepress-deploy@main
        env:
          ACCESS_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          TARGET_BRANCH: gh-pages
          BUILD_SCRIPT: yarn install && yarn vuepress:build
          BUILD_DIR: docs/.vuepress/dist/
          INFO_REPOSITORY: ${{ github.repository }}
```
再去仓库设置中激活gitpages.
## .gitignore
```
docs/.vuepress/*
!docs/.vuepress/config.ts
node_modules
yarn.lock
package-lock.json
```


## 自定义版本

```bash
mkdir -p docs/.vuepress
touch docs/.vuepress/config.ts
```
```ts
import { defineConfig } from "vuepress/config";
export default defineConfig({
  title: "Hello sword4869/vuepress-starter",
  base: "/vuepress-starter/",
  plugins: [
    "vuepress-plugin-helper-live2d",
    "vuepress-plugin-reading-progress",
    "vuepress-plugin-code-copy",
  ],
  themeConfig: {
    docsRepo: "sword4869/vuepress-starter",
    docsBranch: "main",
    docsDir: "docs",
    editLinks: true,
    editLinkText: "Help us improve this page!",
    sidebar: {
      "/": [
        ["/", "README"],
        ["/theme.md", "theme.md"],
        {
          title: "create",
          children: [
            ["/create/deploy\u811a\u672c.md", "deploy\u811a\u672c.md"],
            ["/create/github action.md", "github action.md"],
            [
              "/create/\u56fe\u7247\u683c\u5f0f.md",
              "\u56fe\u7247\u683c\u5f0f.md",
            ],
            ["/create/\u7a7a\u9879\u76ee.md", "\u7a7a\u9879\u76ee.md"],
            { title: "fake", children: [["/create/fake/test.md", "test.md"]] },
          ],
        },
      ],
    },
  },
});
```
```
name: Build and Deploy
on: 
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: vuepress-deploy
        uses: jenkey2011/vuepress-deploy@master
        env:
          ACCESS_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          TARGET_BRANCH: gh-pages
          BUILD_SCRIPT: yarn install && yarn vuepress:build
          BUILD_DIR: docs/.vuepress/dist/
```