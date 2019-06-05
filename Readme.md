# CUC-wechat-crawler
Collect articles detail data from WeChat Official Platform

## Requirement: 
  1. pip install 三个包：selenium/time/unicodecsv
  2. 下载符合本地chrome版本的google chromedriver
  
## 2019-6-5 Information
  1. 可以通过登陆后台抓取指定公众号的全部文章的发布日期、URL、标题，结果保存在csv中
  2. 过程是模拟真实用户浏览网站时输入、点击的过程
  3. 会面临抓取过程中系统提示操作频繁导致失败的问题
  4. 在运行前需要更改一些参数，在py注释中已体现
  
## Future Plan
  1. 还有很多要抓取的信息，会比抓取这些内容更麻烦一些，不过难度不高，都是通过包中的click()或者find_element_by_xxx_name()函数
  2. 需要放到Flask框架中，实现Web中的可视化
  
