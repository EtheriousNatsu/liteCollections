# 文件说明
* nameTuple: 2个元素x,y的命名元组
* orderDict: 简易OrderDict

# 原理
## Nametuple
通过`namedtuple(typename, field_names)`方法动态生成一个`typename`类,
该类继承`tuple`。同时根据`field_names`动态生成`property`只读属性，来控制属性访问。

## OrderDict
通过`双向链表`记录插入顺序，如下图

![](https://www.hualigs.cn/image/612b3dc25fa7b.jpg)
