"""
xpath是在XML文档中搜索内容的一门语言
HTML是XML的一个子集
这节课我们了解一下XML的一些基础内容

"""

'''
这种标签称之为节点。
并且标签之间的关系是存在父子关系的。

<book> # 称为节点, 包含于下面的子节点
    <id>1</id> # 同一级称为同胞节点(兄弟节点)
    <name>野花遍地⾹</name>
    <price>1.23</price>
    <author>
        <nick>周⼤强</nick>
        <nick>周芷若</nick>
    </author
 </book>
 
所以我们如果想要查找某个节点的数据, 我们是一层一层去查找的.
这就是xpath
'''

# xpath就是根据这些节点的包含关系来去搜寻内容
# python中使用xpath语法, 需要安装XML模块 -> lxml模块
# pip install lxml
# xpath解析:

from lxml import etree

# 因为etree是能够直接调出xpath的, 所以我们需要借助etree调用xpath这个功能的.
# 下面一起认识认识xpath


# 这是一个写好的xml
xml = """ 
<book>
    <id>1</id>
    <name>野花遍地香</name>
    <price>1.23</price>
    <nick>臭豆腐</nick>
    <author>
        <nick id="10086">周大强</nick>
        <nick id="10010">周芷若</nick>
        <nick class="joy">周杰伦</nick>
        <nick class="jolin">蔡依林</nick>
        <div>
            <nick>热热热热热1</nick>
        </div>
        <span>
            <nick>热热热热热2</nick>
        </span>
    </author>

    <partner>
        <nick id="ppc">胖胖陈</nick>
        <nick id="ppbc">胖胖不陈</nick>
    </partner>
</book>
"""

tree = etree.XML(xml)  # 加载一个XML, 返回一个etree对象.
# 然后通过该对象使用xpath的这些功能.
# tree.xpath() # 通过这个xpath()就可以寻找节点
result = tree.xpath("/book")  # /表示层级关系, 开头一个/代表是根节点,开始
print(result) # [<Element book at 0x181e55826c0>] # 表示元素.
result = tree.xpath("/book/name")  # 这个的意思是找/book/name 就是找book中的name节点, 然后打印出来ele name at 地址

# 那么我们不想要地址, 而是想要其中的内容. 我们可以使用text()直接获取内容,.
result = tree.xpath("/book/name/text()")  # text()这个就可以取出节点中的内容
print(result) # ['野花遍地香'] # 这就拿到了节点中的文本.

result = tree.xpath("/book/author/nick/text()")  # 这样仅仅是在一个节点下寻找四个名字
print(result) # ['周大强', '周芷若', '周杰伦', '蔡依林']

result = tree.xpath("/book/author/div/nick/text()")  # '热热热热'


# 我们想要打印一个大节点下,所有的nick, 我们该怎么办
# //表示搜索所有后代. 的节点.
result = tree.xpath("/book/author//nick/text()")  # 放两个//, 这样就可以在父节点下搜索后代了,不仅仅局限于当前缩进的标签

# *表示通配符, 表示任意的节点, 进行匹配. 也就是只打印author下一级的nick节点.
result = tree.xpath("/book/author/*/nick/text()")  # *表示任意的节点,通配符,这个*的位置就是占一个,搜索下一级的nick
print(result)

result = tree.xpath("/book//nick/text()")  # 打印book节点中的所有nick

print(result)
