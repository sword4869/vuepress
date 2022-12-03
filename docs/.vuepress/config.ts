import { defineConfig } from "vuepress/config";

export default defineConfig({
  /**
   * Type is `DefaultThemeConfig`
   */
  title: "Hello VuePress",
  base: "/vuepress-starter/",
  themeConfig: {
    // if your docs are in a different repo from your main project:
    docsRepo: "sword4869/vuepress-starter",
    // if your docs are in a specific branch (defaults to 'master'):
    docsBranch: "main",
    // if your docs are not at the root of the repo:
    docsDir: "docs",
    // defaults to false, set to true to enable
    editLinks: true,
    // custom text for edit link. Defaults to "Edit this page"
    editLinkText: "Help us improve this page!",

    sidebar: [
      ["README.md", "README.md"],
      ["theme.md", "theme.md"],
      {
        title: "create",
        children: [
          ["deploy脚本.md", "deploy脚本.md"],
          ["github action.md", "github action.md"],
          ["图片格式.md", "图片格式.md"],
          ["空项目.md", "空项目.md"],
        ],
      },
    ],
  },
});
