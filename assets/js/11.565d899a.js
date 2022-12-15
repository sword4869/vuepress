(window.webpackJsonp=window.webpackJsonp||[]).push([[11],{308:function(t,s,e){"use strict";e.r(s);var a=e(4),n=Object(a.a)({},(function(){var t=this,s=t._self._c;return s("ContentSlotsDistributor",{attrs:{"slot-key":t.$parent.slotKey}},[s("h1",{attrs:{id:"github-action"}},[s("a",{staticClass:"header-anchor",attrs:{href:"#github-action"}},[t._v("#")]),t._v(" github action")]),t._v(" "),s("p",[t._v("Publishing with a custom GitHub Actions workflow: 提交到主分支时就会自动更新")]),t._v(" "),s("div",{staticClass:"language-bash extra-class"},[s("pre",{pre:!0,attrs:{class:"language-bash"}},[s("code",[t._v("$ "),s("span",{pre:!0,attrs:{class:"token function"}},[t._v("mkdir")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token parameter variable"}},[t._v("-p")]),t._v(" .github/workflows\n\n$ "),s("span",{pre:!0,attrs:{class:"token builtin class-name"}},[t._v("cd")]),t._v(" .github/workflows\n\n"),s("span",{pre:!0,attrs:{class:"token comment"}},[t._v("# 名字随便")]),t._v("\n.github/workflows$ "),s("span",{pre:!0,attrs:{class:"token function"}},[t._v("vim")]),t._v(" actions.yml\n")])])]),s("p",[t._v("如果是这个仓库推送自己，那么直接用action自动生成的"),s("code",[t._v("secrets.GITHUB_TOKEN")]),t._v("。")]),t._v(" "),s("details",[s("summary",[t._v(" 推送到其他仓库才用自定义token ")]),t._v("\n创建token\n点击你的头像 > Settings > Developer settings > Personal access tokens > Generate new token (classic). 权限至少要勾选repo, workflow\n"),s("p",[t._v("在仓库Settings> Secrets> Actions> New repository secret> 命名变量"),s("code",[t._v("ACCESS_TOKEN")]),t._v(", 填上生成token的值")]),t._v(" "),s("p",[t._v("在ci.yml中用"),s("code",[t._v("secrets.ACCESS_TOKEN")])])]),s("p"),t._v(" "),s("p",[s("a",{attrs:{href:"../../.github/workflows/ci.yml"}},[t._v("ci.yml")])]),t._v(" "),s("p",[s("code",[t._v("TARGET_BRANCH")]),t._v(": 这个不是根据哪个分支什么, 而是是要生成的. 所以你会看到自己多了一个gh-pages分支")])])}),[],!1,null,null,null);s.default=n.exports}}]);