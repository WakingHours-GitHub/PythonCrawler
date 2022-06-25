from lxml import etree

tree = etree.parse("b.html")  # 直接更新同一文件夹下的b.html文件
# tree = etree.XML(resp.text)
result = tree.xpath("/html") # 使用xpath提取一些内容
result = tree.xpath("/html/body/ul/li/a/text()") # 提取标签的内容
# 但是我并不想全部提取出来, 所以使用xpath中的[]索引功能(这里是从1开始)
result = tree.xpath("/html/body/ul/li[1]/a/text()") # 这样就可以截取出来了
# 但是要注意xpath中的索引是从1开始的

# 那么我像要一些特定属性的元素怎么办
result = tree.xpath("/html/body/ul/li/a[@href='http://www.baidu.com']/text()")
# @属性=属性值 从而筛选出来特定的一些属性值

print(result)




ol_li_list = tree.xpath("/html/body/ol/li")
for it in ol_li_list:
    # 从每一个it中提取出来文字信息
    result = it.xpath("./a/text()") # 在li中继续搜寻, 称为相对查找, 不是从根开始查找, 此时开头使用./

    print(result)

    result = it.xpath("./a/@href") # 拿到属性值: @属性 # 直接拿到属性值
    print(result) # 返回的是属性值

# 一个小技巧: 可以去网页使用开发工具(F12)直接获取元素
# 选中节点然后之际赋值xpath, 然后复制回xpath中即可
print(tree.xpath('/html/body/div[1]/text()'))
print(tree.xpath('/html/body/ol/li/a/text()'))
