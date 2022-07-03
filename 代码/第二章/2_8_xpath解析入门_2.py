from lxml import etree

# etree.XML().xpath()


tree = etree.parse("b.html")  # 直接加载同一文件夹下的b.html文件
# result = tree.xpath('/html') # 使用xpath提取一些内容
# result = tree.xpath("/html/body/ul/li/a/text()") # 提取出标签中的内容
# 但是我不想全提取出来, 所以我使用xpath中的[]索引功能(这里是从1开始)
# result = tree.xpath("/html/body/ul/li[1]/a/text()")  # xpath的顺序是从1开始数的, []表示索引

# result = tree.xpath("/html/body/ol/li/a[@href='dapao']/text()")  # [@xxx=xxx] 属性的筛选
# @属性=属性值: 删选特定的属性值

# print(result)

# ol_li_list = tree.xpath("/html/body/ol/li")
#
# for li in ol_li_list:
#     # 从每一个li中提取到文字信息
#     result = li.xpath("./a/text()")  # 在li中继续去寻找. 相对查找, 不是从根查找, 此时开头使用./
#     print(result)
        # ./开头是相对查找
#     result2 = li.xpath("./a/@href")  # 拿到属性值: @属性
#     print(result2)

# 一行代码拿到所有的href
# print(tree.xpath("/html/body/ul/li/a/@href"))


# 一个小技巧: 可以去网页使用开发工具(F12)直接获取元素
# 选中节点然后之际赋值xpath, 然后复制回xpath中即可
print(tree.xpath('/html/body/div[1]/text()'))
print(tree.xpath('/html/body/ol/li/a/text()'))

