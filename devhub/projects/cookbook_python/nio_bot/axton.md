### 一些问题
Axton 是谁？
如何使用 Coze 工作流获取 Tweets？
Axton讲过Code lnterpreter吗?

### 爬取内容，为完成例子
pip install requests beautifulsoup4

ID,URL,TITLE
1,https://www.axtonliu.com/jina-reader-api-usage, Jina Reader API 的四种用法
2,https://www.axtonliu.com/another-blog-post, Another Blog Post Title
3,https://www.axtonliu.com/yet-another-post, Yet Another Post Title

### Databse 如何通过自然语言插入

```
请在数据库urls中添加以下三条记录
智图派,博客,https://axtonliu.com
Al精英学院,学校,https://axtonliu.ai
回到Axton,YouTube,https://www.youtube.com/@axtonliu
```

- 数据库urls中有哪些记录?
- select * from urls
- Axton的博客的网址是什么?

### WF：AFTweetsFinder

- 请使用getUsers获取@yuli_kamakura的信息
- 请使用searchTweet查找yuli_kamakura的与Al相关的推文,最多返回10条
- 请使用usersFollowers查找yuli_kamakura的Followers
- 请使用GetTwitterThread获取ID为1802890640763801748的推文
- 请使用GetTwitterTrends获取UnitedStates的推特趋势
<<<<<<< HEAD
- [测试 AITweetsFinder 工作流] 用AlTweetsFinder工作流帮我寻找QueryString为Al的结果,并且输出中文结果。### Databse 如何通过自然语言插入

```
请在数据库urls中添加以下三条记录
智图派,博客,https://axtonliu.com
Al精英学院,学校,https://axtonliu.ai
回到Axton,YouTube,https://www.youtube.com/@axtonliu
```

- 数据库urls中有哪些记录?
- select * from urls
- Axton的博客的网址是什么?
=======
- [测试 AITweetsFinder 工作流] 用AlTweetsFinder工作流帮我寻找QueryString为Al的结果,并且输出中文结果。
>>>>>>> 1ff4b5d (Update axton.md)
