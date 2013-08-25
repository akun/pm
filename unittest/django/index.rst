Django中的单元测试
==================

^
--

上篇文章《:doc:`../python`\》有提到，“TestResult和TextTestRunner这两个很有用的东西”，但并没有展开讲，这篇介绍Django中的单元测试的文章，在后面一小部分会以Django源码为例简单展开下。

先进入主要部分，简单讲解Django中单元测试的使用。

show me the code
----------------

照例，先来一段简单示例代码作为讲解。

比如，有如下一个简单的功能代码，意思是GET方式请求一个URL，200返回需要JSON的响应。代码如下：

.. literalinclude:: example.py

如果平时手工测试，我们可能就访问下浏览器，看下是否返回结果是否符合预期，如果每次测试都这样，其实很烦，所以我们写个测试，比如访问的URL地址是“/get-json/”，那么代码如下：

.. literalinclude:: test_example.py

Django有自己一套测试框架，所以Django的项目提供了一个运行单元测试的命令：

::

   python manage.py test

这只是一个简单的示例，展示下Django里写单元测试然后执行。

另外，< Python 2.7的建议安装unitest2

常见场景
--------

* 测试数据库模拟
* 测试数据构造
* HTTP请求：POST、GET
* response：200/404/30X、content、context
* 表单验证
* 测试模版
* 测试数据定义

* 需要登录/注销
* 测试cookie/session
* 浏览器：selenium

* override_settings

* 执行所有/某个app/某个TestCase/某个测试条目
* 出错了，立马报错，结束测试

* 忽略某些测试

* 额外：MongoDB、修改文件

* 运行
* 测试数据库
* client
* fixtures
* assert，这文章会讲到的Django中的单元测试框架，封装了不少适合Web开发中的assertXXXX，比如：判断是否URL跳转等。
* **MongoDB特殊处理**

Django单元测试框架源码简析
--------------------------

* runner

* 模拟

参考
----

* https://docs.djangoproject.com/en/1.5/topics/testing/

$
--

这里介绍的其实也很简单，更详细的内容，就直接：
* RTFM - Read The Fucking Manual
* RTFS

后续
----

既然讲到了Web开发，那就离不开Web前端开发，而JavaScript又是Web前端开发中的主流，下次就以JavaScript为例来说明下单元测试好了。

资源下载
--------

示例代码
