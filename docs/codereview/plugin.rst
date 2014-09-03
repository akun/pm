Pylint插件：忽略Django的国际化代码调用报错
==========================================

**NOTICE：如果更新到Django1.4+以上版本后，就不会报类似Error级别的提示了。**

用Django写Web开发类型的程序，经常会用到程序的国际化操作，例如，保存如下代码为example.py：

.. literalinclude:: example.py


如果项目中用到Pylint来检查代码，执行如下：

::

   pylint -E example.py

这个时候会显示一个Error级别的提示，如下：

::

   No config file found, using default configuration
   ************* Module example
   E:  3,6: _ is not callable

熟悉Django的人，一定会觉得很奇怪，怎么可能函数不能被调用，这里就不具体展开说明原因了：

* 可以认为是Pylint不够智能
* 也可以认为Python本身太灵活，Django中调用的国际化模块，刚好用了一些动态语言的特性

怎么办？
--------

* Pylint提供了灵活的配置设置，过了一遍配置，发现没有自定义设置可以忽略这个情况
* Google之，但很多是说直接忽略那条规则，这样虽然可以达到忽略的效果，但是同样也忽略了不应该忽略的检查，比如：a = 1; a()这种语法错误
* 看Pylint官方文档，发现Pylint扩展性还是不错的，提供自定义插件机制，--load-plugin参数指定插件即可，那么就自己写个插件来处理这种情况吧！
* 继续Google，发现有人写过类似插件，虽然是处理别的问题，但很类似：http://www.logilab.org/blogentry/78354

写个插件！
----------

代码很简单，原理就是写个假的函数调用，在Pylint执行该模块的函数检查时候，直接调用了假的函数，从而绕过该报错，但又不会影响这条规则检查其它代码时候报告Error级别信息。保存如下代码为astng_django.py

.. literalinclude:: astng_django.py

这个时候执行命令（需要PYTHONPATH能找到astng_django.py）

::

   pylint -E example.py --load-plugins=astng_django

输出如下：

::

   No config file found, using default configuration

就没有刚才的Error级别的提示了。

保存如下代码为error.py，再验证下报错的情况是否被忽略：

.. literalinclude:: error.py

执行命令：

::

   pylint -E error.py --load-plugins=astng_django

输出如下：

::

   No config file found, using default configuration
   ************* Module error
   E:  2,0: fake_function is not callable

这样就算初步解决这个问题了，即可以不让Django程序报干扰的Error级别信息，又不会忽略的确需要报的Error级别信息。

占个坑~
-------

照例，GitHub上先占个坑：https://github.com/akun/pylint_plugin

后续TODO：

* 前面有说明必须指定PYTHONPATH，有点麻烦，但作为临时解决问题是够了。后续需要做个完整的Python库，然后发布到PyPI，然后作为正式的安装包，就更方便别人使用了。
* 另外，这个插件还是相对简单，其实Django中的国际化处理有好多函数，需要后续补充。
* 将上述的相关验证转化为对应的测试代码。
