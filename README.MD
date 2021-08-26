# 说明
2个元素x,y的命名元组

# 原理
1. 通过`namedtuple(typename, field_names)`方法动态生成一个`typename`类,
该类继承`tuple`。同时根据`field_names`动态生成`property`只读属性，来控制属性访问。