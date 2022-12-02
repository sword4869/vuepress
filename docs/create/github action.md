# github action
Publishing with a custom GitHub Actions workflow: 提交到主分支时就会自动更新

```bash
$ mkdir -p .github/workflows

$ cd .github/workflows

# 名字随便
.github/workflows$ vim actions.yml
```
创建token
点击你的头像 > Settings > Developer settings > Personal access tokens > Generate new token (classic). 权限至少要勾选repo, workflow

在仓库Settings> Secrets> Actions> New repository secret> 命名变量`ACCESS_TOKEN`, 填上生成token的值


[actions.yml](../../.github/workflows/actions.yml)

`TARGET_BRANCH`: 这个不是根据哪个分支什么, 而是是要生成的. 所以你会看到自己多了一个gh-pages分支