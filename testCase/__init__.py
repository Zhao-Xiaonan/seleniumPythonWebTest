# -*- coding: utf-8 -*-
# 在执行import语句时，如下：
# 1、创建一个新的、空的module对象（可能包含多个module）
# 2、把这个module对象插入sys.module中
# 3、装载module代码（如果需要，首先逆序编译）
# 4、执行新的module中对应的代码
# 在第三步，找到module位置，搜索顺序：
# 当前路径（及指定的sys.path）-- PYTHONPATH -- 安装默认路径

# 先构建一个package（包含__init__.py），以普通module方式导入，
# 就可以直接访问packet中的各个module，而不是系统标准module。

# 在testCase文件夹中创建__init__.py，标识目录可引用
import baiduTest,youdaoTest,cloudTest,widgetTest,collectTest