# xpath是在XML文档中搜索内容的一门语言
# HTML是XML的一个子集
# 了解一些XML的基础内容
'''
<book> # 称为节点, 包含于下面的子节点
    <id>1</id> # 同一级称为同胞节点
    <name>野花遍地⾹</name>
    <price>1.23</price>
    <author>
        <nick>周⼤强</nick>
        <nick>周芷若</nick>
    </author
 </book>
'''
# xpath就是根据这些节点的包含关系来去搜寻内容
# python中使用xpath:安装lxml模块
# pip install lxml [-i] xxx
# xpath解析
from lxml import etree
# etree.XML().xpath()

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

tree = etree.XML(xml) # 加载一个XML
# tree.xpath() # 通过这个xpath()就可以找寻节点
# result = tree.xpath("/book")  # /表示层级关系. 第一个/是根节点
# result = tree.xpath("/book/name") # 找/book(根)/name 就是找book中的name节点. 打印element name at 地址
# result = tree.xpath("/book/name/text()")  # 我想要name里面的文本, 所以使用text() 拿文本
result = tree.xpath("/bool/author/nick/text()") # 四个人名字.返回一个列表. 但是这样仅仅是找到兄弟节点(同级)的内容
# result = tree.xpath("/book/author/dic/nick/text()") # 打印热热热..
# result = tree.xpath("/book/author//nick/text()")  # // 放两个//, 同样搜索后代, 就是搜索后缩进的内容, 不止局限于当前层    级
# result = tree.xpath("/book/author/*/nick/text()")  # * 任意的节点. 通配符(会儿), 这个就是*的位置搜索同级的了, 不搜索再缩进的(不搜索后代)
result = tree.xpath("/book//nick/text()") # 拿book中的所有nick中的内容
print(result)
