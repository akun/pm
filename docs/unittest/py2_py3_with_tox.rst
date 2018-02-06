用 tox 进行 Python 2 和 Python 3 的兼容性测试
=============================================

背景
----

不少项目会遇到从 Python 2 到 Python 3 过渡的问题，由于过渡需要持续一段时间，所\
以代码得保证在 Python 2 和 Python 3 中都能运行正常。为了解决这个问题，所以需要\
引入 tox 这个工具。

tox 简介
--------

tox 项目代码地址：https://github.com/tox-dev/tox

按官网描述，该项目目前是为了自动化和标准化 Python 的测试工作。主要整合了 2 块\
内容：分别是，virtualenv 管理不同版本 Python，以及结合不同测试工具命令行调用。\

tox 有以下用处：

* 用不同 Python 版本的解释器，来检查 Python 包是否能正确安装；
* 调用你选择的测试工具，在不同 Python 版本的环境下运行测试；
* 更方便集成到 CI（持续集成）中，减少或合并一些可能会产生的重复内容。

使用说明
--------

安装
~~~~

::

   pip install tox

可以把 tox 纳入你的工程项目的研发环境常用依赖库。

配置
~~~~

用向导工具生成 tox 配置

::

   tox-quickstart

或者直接编辑新建 tox.ini 文件，常见配置如下：

.. literalinclude:: tox.ini

相当于声明了会在 Python 2.7、Python 3.4、Python 3.5、Python 3.6 这 4 个不同环\
境下进行：发布、安装、测试相关的工作。

这里因为包测试需要依赖：coverage 和 nose，分别进行测试覆盖率统计和方便测试的\
调用。

这里借用了 nose 进行测试，所以执行的对应测试命令就是 nosetests，具体测试配置写\
在 nose.cfg 里，后续单独开个主题讲下 nose 的使用。

运行
~~~~

::

   tox

没错，就这么简单，如果不想细究更多参数的话。如果运行没问题就会输出类似信息：

::

   ...
   py27: commands succeeded
   py34: commands succeeded
   py35: commands succeeded
   py35: commands succeeded
   congratulations :)

表示在这些 Python 解释器环境下能执行通过，说明可以兼容这些版本 Python 解释器。

例子
----

用一个小的 Python 工程项目举例说明并感受下 tox 的使用，具体如下：

main.py
~~~~~~~

.. literalinclude:: ../../pm/onepiece/onepiece/main.py

test_main.py
~~~~~~~~~~~~

.. literalinclude:: ../../pm/onepiece/tests/test_main.py

setup.py
~~~~~~~~

.. literalinclude:: ../../pm/onepiece/setup.py

tox.ini
~~~~~~~

.. literalinclude:: ../../pm/onepiece/tox.ini

运行结果
~~~~~~~~

命令行下执行 tox，输出示例如下：

.. literalinclude:: tox_result.log

完整示例
~~~~~~~~

可以实际演练下，更方便理解，可以在这里查看更完整示例：\
https://github.com/akun/pm/tree/master/pm/onepiece

总结
----

简单总结下：

* tox 可以让你更轻松地在不同 Python 版本的解释器上进行测试；
* tox 只是个辅助工具，关键还是得有足够单元测试代码覆盖来检验 Python 2 和 \
  Python 3 兼容；
* tox 使用起来，可以把更多重点放到 Python 2 和 Python 3 兼容的写法上。后续单独\
  开个主题讲下 Python 2 和 Python 3 兼容的写法。

参考
----

* https://github.com/tox-dev/tox
* https://tox.readthedocs.io/
* https://docs.python.org/3/library/unittest.html
* http://python-future.org/quickstart.html
