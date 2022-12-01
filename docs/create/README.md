# 图片格式

# A
```bash
project
├── docs
│   ├── README.md
│   └── .vuepress
│       └── config.js
├── images
├── node_modules
├── package.json
└── yarn.lock
```
```markdown
![](../images/83ad32c958dacc26e343fa0988ac1868f25889fb9f830f60f9946bf11d77dca4.png)  
![](images/83ad32c958dacc26e343fa0988ac1868f25889fb9f830f60f9946bf11d77dca4.png)  
![](/images/83ad32c958dacc26e343fa0988ac1868f25889fb9f830f60f9946bf11d77dca4.png)  
``` 

只支持第一种相对路径的格式。

生成后在`dist`中没有图片, 因为在html中会转化成base64的格式. 所以重要的只是让vue在编译过程中根据md文档来找到图片的位置.
```html
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACsAAAAqCAIAAAClYzUyAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAE8SURBVFhHY/z8+TPDgAImKD1wYNQFoy4AgVEXjLoABEZdMGRd8PfrvQv3vv6F8igE5Ljg5famwvrChIyO3U+gIpQAcmNB0StM996s7NDCZZcoDAxyXcAma5c3a0FvovieWgoDg6KUyK3iVTF7VoXZS0oCgyIXgACzuHFqPyWBQbELwICSwKCOC0CA3MCgngvAABQYM/r9OY9PmbTtJVSMAKCyCxie7O7ILt/43TI9zV4cKkQAUM8Ff79eWlYYmj3rpUXFlBkVXircUHFCgEouAHo9I6F5v3hi74L+ZGNxZqgwMYBiF5DrdTigyAVf72wj2+twQK4Lfj0+PrcwoXg+0OuzyPI6HJDrgvvblp6Ael2QLK/DAVk9V2D74PJLcV0lbsrshoDRvvOoC0Bg1AWjLgCBUReMuoCBgYEBAF6thKeX41u2AAAAAElFTkSuQmCC" alt="图 1">
```

## B

```bash
mkdir -p docs/.vuepress/public/images
rm -r docs/.vuepress/public/images
cp -r images/ docs/.vuepress/public/images
```
```bash
project
├── docs
│   ├── README.md
│   └── .vuepress
│       ├── config.ts
│       └── public
│           └── images
├── node_modules
├── package.json
└── yarn.lock
```
```markdown
![](/images/83ad32c958dacc26e343fa0988ac1868f25889fb9f830f60f9946bf11d77dca4.png)  
```
`images`放在`docs/.vuepress/public`下, 就可以直接用根目录的格式. 

这种格式就是原本没有用vuepress写的markdown的格式, 就可以不用修改格式, 直接把文档和图片移动就行.

生成后在`dist`中会有`images`文件夹
```html
<img src="/images/3187ee42998b26ccb76cf1237b1e5714686b3f425ca50a2e34b4c34ce93dc7f6.png" alt="image">
```

但是用deploy.sh脚本部署的时候出现了`base`前缀的问题。图片https的地址是带前缀的，但是html索引过去的地址是不带前缀的。