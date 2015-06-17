Python 中的 namespace
=====================

略微标题党一下，Python 中有 namespace 这个特性吗？就看你如何定义 namespace 了。

背景
----

近期参与一个项目，用 Python 写，设计规划上有点小规模，然后就按出的架构拆分为多个子模块项目了。但这几个子模块项目又关联性比较大，所以看起来要在一个总项目中。

考虑
----

题外话，一直觉得 Python 的模块导入是个挺麻烦是事情，什么绝对导入、相对导入，一定程度提高了使用者的理解成本，以及项目的维护成本。记得 Python 开发者的哲学不是“用一种方法，最好是只有一种方法来做一件事” [#f1]_ 嘛，貌似遵守这个哲学不容易。

最初反应是不拆分项目，直接把各个子模块的代码放在一个总项目中，比如：这个总项目叫 Star Wars [#f2]_ 吧，有 4 个子模块，分别叫 Yoda，Force，Skywalker，R2-D2。

可能源码的目录结构就是这样了

::

   starwars/
   ├── force
   │   └── __init__.py
   ├── __init__.py
   ├── r2d2
   │   └── __init__.py
   ├── skywalker
   │   └── __init__.py
   └── yoda
       └── __init__.py

其实这样开始项目也没什么大关系，只是基于以下几点考虑，后来还是拆分这个项目为多个子模块项目了：

* 按设想的架构展开，这个项目还是有点规模的
* 项目中的某些子模块其实是很基础通用的模块，是可以被外部项目所用的，而外部项目要引入整个项目源码，没这个必要
* 拆分为子项目后，方便由多个小组协同研发
* 对后期项目的软件更新更有利，只更新某个子模块的 Python 模块包就行

问题
----

对 Python 来说，拆分子项目也方便，基本上就是把各个子模块目录作为独立的模块包，以 skywalker 子模块为例就是这样了：

::

   skywalker/
   ├── anakin.py
   ├── __init__.py
   ├── luke.py
   └── shmi.py

然后使用起来就是：

::

   import skywalker

现在问题是可能有很多模块都叫 skywalker，如何避免模块名冲突？

解决
----

很简单，想当然会用 starwars 这个所谓的 namespace，然后使用起来就是：

::

   from starwars import skywalker

对应的，目录结构就是：

::

   starwars/
   ├── __init__.py
   └── skywalker
       ├── anakin.py
       ├── __init__.py
       ├── luke.py
       └── shmi.py

然后写个 setup.py 就可以，目录差不多就是这样：

::

   starwars.skywalker/
   ├── setup.py
   └── starwars
       ├── __init__.py
       ├── __init__.pyc
       └── skywalker
           ├── anakin.py
           ├── __init__.py
           ├── luke.py
           └── shmi.py

其它子模块也类似处理，这样就拆分成多个模块包了。

更优
----

严格来说，上面的模块包，其实是 starwars 的模块包，而不是拆分后的各个子模块的模块包，也就是说安装完毕后的 starwars 可以没有 __init__.py，但也能用这种导入：

::

   from starwars import skywalker

可以参考 Zope [#f3]_ 这个大型的 Python 项目，其实就是把它的子项目拆分为多个模块包，但共享了 zope 这个 namespace。

修改 setup.py
~~~~~~~~~~~~~

增加 **namespace_packages** 就行，例如：

::

   #!/usr/bin/env python

   from setuptools import setup, find_packages

   setup(
       name='starwars.skywalker',
       version='0.0.1',
       packages=find_packages(),
       namespace_packages=['starwars']
   )

修改 __init__.py
~~~~~~~~~~~~~~~~

在 starwars/__init__.py 中增加：

::

   __import__('pkg_resources').declare_namespace(__name__)

需要注意的是，除了这一行，不能有别的代码了。

安装
~~~~

这个时候安装完毕 starwars.skywalker 这个模块包，可以发现安装完毕后的 starwars 是没有 __init__.py 的，但会在 starwars 平级目录多一个类似 starwars.skywalker-0.0.1-py2.7-nspkg.pth 的文件，作用相当于是在 starwars 目录中有了个 __init__.py 一样。

示例
----

说了这么多，直接看代码估计更容易理解，示例代码：

* https://github.com/akun/pm/tree/master/pm/starwars.skywalker
* https://github.com/akun/pm/tree/master/pm/starwars.yoda

或者，直接接安装下亲自感受下：

::

   pip install starwars.skywalker starwars.yoda

可以看下第三方包的安装目录的实际安装情况，在 starwars 目录没有 __init__.py，但可以导入想要的子模块库

::

   from starwars import skywalker, yoda

再或者，随便找个 Zope 的子项目，看下实际的项目是如何做的：

* https://github.com/zopefoundation/zope.annotation

本质
----

问题本质其实算是 Python 不允许模块包，在多个位置来进行导入 [#f4]_ ，所以只能放在比如 starwars 这一个目录下，无论是 starwars 目录下放个 __init__.py 还是严格声明下 namespace 是 starwars 这种方式，最后都是把模块包放在一个位置下来处理。

简单说：

* 就是 Python 不支持所谓的 namespace 这种语法吧。
* 或者说不支持，允许多位置模块包，却共享一个 namespace 这个特性。

参考
----

.. rubric:: 参考清单
.. [#f1] https://zh.wikipedia.org/zh/Python
.. [#f2] http://www.starwars-tw.com/story/character/character.htm
.. [#f3] https://github.com/zopefoundation
.. [#f4] https://pythonhosted.org/setuptools/setuptools.html#namespace-packages
