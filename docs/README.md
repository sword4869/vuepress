# REAME
## bash
```bash
yarn init
yarn add -D vuepress
mkdir docs
mkdir -p .github/workflows
touch .github/workflows/ci.yml

mkdir -p docs/.vuepress
touch docs/.vuepress/config.ts

touch .gitignore
```

```bash
project
├── docs
│   ├── .vuepress
│   │   └── config.ts
│   ├── README.md 
│   └── xxx文件夹 
|       └── xxx.md
├── node_modules
├── package.json
└── yarn.lock
```

## docs/.vuepress/config.ts
```ts
import { defineConfig } from "vuepress/config";

export default defineConfig({
  title: 'Hello VuePress',
  base: '/vuepress-starter/',
  themeConfig: {
    docsRepo: "sword4869/vuepress-starter",
    docsBranch: "main",
    docsDir: 'docs',
    editLinks: true,
    editLinkText: 'Help us improve this page!',

    sidebar: [
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
      }
    ]
  }
});
```
改base，docsRepo，sidebar

## .github/workflows/ci.yml
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
        uses: jenkey2011/vuepress-deploy@master
        env:
          ACCESS_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          TARGET_BRANCH: gh-pages
          BUILD_SCRIPT: yarn install && yarn vuepress:build
          BUILD_DIR: docs/.vuepress/dist/
```
再去仓库设置中激活gitpages.
## .gitignore
```
docs/.vuepress/dist
node_modules
```