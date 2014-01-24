.. highlight:: rst

.. _my-reference-label:

用Sphinx编写技术文档
====================

大家会发现，如果一个项目主要是用Python写的，其文档都很类似，比如：Python在线的HTML官方手册。这些项目的文档都来源于一个很不错的项目：Sphinx。
这个Sphinx特指Sphinx doc这个项目（另一个也叫Sphinx的search的项目，虽然都叫一个名字）。

官网：http://sphinx-doc.org/

以下出现Sphinx的地方，都特指Sphinx doc这个项目

使用场景
--------

* 很多开源Python库项目的API手册都是用这个写的，可以看Sphinx官网给的链接：http://sphinx-doc.org/examples.html
* 如果是用Python写的商业软件，也可以用这个来写技术文档，纯文本管理研发文档，保证功能代码、测试代码、相关文档同时更新
* 直接拿来写在线书。比如，这个《软件构建实践系列》就是：https://github.com/akun/pm
* 直接用来做slide等演示幻灯片，从一定程度上替代PowerPoint。比如，http://example.zhengkun.info/slide.html

功能
----

这里就列举个人关心的几个特性：

* 文本是rst格式语法
* 生成HTML、PDF、Slide（需要插件）等格式的文档
* 支持文档、代码等引用
* 支持自定义样式
* 支持插件扩展
* 直接看官网手册了解更多：http://sphinx-doc.org/contents.html

语法简介
--------

就是rst的语法，这里就列举几个常用的：

标题等级
^^^^^^^^

rst如下：

::

   一级标题
   ========

   二级标题
   --------

   三级标题
   ^^^^^^^^

效果如下：

..
   一级标题
   ========
   
   二级标题
   --------
   
   三级标题
   ^^^^^^^^

习惯上，可以用以下字符：“= - ` : ' " ~ ^ _ * + # < >”。最好能约定个依次标题等级。

列表
^^^^

rst如下：

::

   * 列表1
   * 列表2
   * 列表3

效果如下：

* 列表1
* 列表2
* 列表3

列表写法除了用“*”，还可以用：“-”，“+”，最后效果一样。

上面说的是无序列表，如果想用有序列表，可以用“#.”。

rst如下：

::

   #. 列表1
   #. 列表2
   #. 列表3

效果如下：

#. 列表1
#. 列表2
#. 列表3

表格
^^^^

rst如下：

::

   =====  =====  =====
   第1列  第2列  第3列
   =====  =====  =====
   8      1      6
   3      5      7
   4      9      2
   =====  =====  =====

效果如下：

=====  =====  =====
第1列  第2列  第3列
=====  =====  =====
8      1      6
3      5      7
4      9      2
=====  =====  =====

插入图片
^^^^^^^^

rst如下：

::

   .. image:: images/ball1.gif

效果如下：

.. image:: images/ball1.gif

插入代码
^^^^^^^^

展示代码示例，经常会用到：

默认
""""

rst如下：

::

   ::

      print 'Hello World!'

效果如下：

::

   print 'Hello World!'


自定义
""""""

rst如下：

::

   .. code-block:: python
      :linenos:

      print 'Hello World!'

效果如下：

.. code-block:: python
   :linenos:

   print 'Hello World!'

引用代码文件
""""""""""""

rst如下：

::

   .. literalinclude:: code/example.js
      :language: javascript
      :linenos:

效果如下：

.. literalinclude:: code/example.js
   :language: javascript
   :linenos:

提供下载文件链接
^^^^^^^^^^^^^^^^

直接下载该RST本身。

rst如下：

::

   :download:`sphinx.rst <sphinx.rst>`

效果如下：

:download:`sphinx.rst <sphinx.rst>`

目录索引
^^^^^^^^

example1对应sphinx.rst所在目录下的example1.rst文件，example2类似。

rst如下：

::

   .. toctree::
      :maxdepth: 2

      example1
      example2

效果如下：

.. toctree::
   :maxdepth: 2

   example1
   example2

引用
^^^^

可以用于跨rst文档间的内容互相引用。这里以本文档内为例。

rst如下：

::

   .. _my-reference-label:

   用Sphinx编写技术文档
   ====================

   很长的文字内容

   点击回到顶部， :ref:`my-reference-label`.

效果如下：

点击回到顶部， :ref:`my-reference-label`.

文字效果
^^^^^^^^

斜体
""""

rst如下：

::

   *斜体*

效果如下：

*斜体*

粗体
""""

rst如下：

::

   **粗体**

效果如下：

**粗体**

下标
""""

斜杠是为了空格转义，最后显示无空格。

rst如下：

::

   H\ :sub:`2`\ O

效果如下：

H\ :sub:`2`\ O

上标
""""

rst如下：

::

   E = mc\ :sup:`2`

效果如下：

E = mc\ :sup:`2`

.. seealso::

   * 更多说明，详见rst文档：http://docutils.sourceforge.net/rst.html
   * 另外，这本书本身就是个示例：https://github.com/akun/pm

Hello World
-----------

根据上面的介绍，其实常用的语法不多，现在直接用下，自己感受下吧！

安装 & 初始化
^^^^^^^^^^^^^

常用Python安装方式，创建个文件夹，执行命令，按提示自己选择即可。

::

   pip install Sphinx
   mkdir docs
   cd docs
   sphinx-quickstart

根据提示输入相应参数即可，可以一路默认。

尝试编辑
^^^^^^^^

编辑index.rst，只写入以下内容

::

   用Sphinx编写技术文档
   ====================

   使用场景
   --------

生成HTML
^^^^^^^^

很简单，默认支持就很好。

::

   make html
   python -m SimpleHTTPServer 9527

直接浏览器访问9527端口，就可以看到类似Python官方文档的效果。

生成PDF
^^^^^^^

麻烦些，需要依赖库，且需要简单修改下配置。

1. 安装依赖库

::

   pip install rst2pdf

2. 编辑conf.py，增加或修改如下配置：

.. literalinclude:: code/pdf.py
   :language: python
   :linenos:

3. 编辑Makefile，增加如下代码：

Linux下的Makefie：

.. literalinclude:: code/pdf.Makefile
   :linenos:

Windows下的批处理：

.. literalinclude:: code/pdf.bat
   :linenos:

4. 执行生成PDF

::

   make pdf
   python -m SimpleHTTPServer 9527

.. seealso::

   有关PDF的更多配置，可以阅读这个文档：http://ralsina.me/static/manual.pdf

生成Slide
^^^^^^^^^

Slide就是我们常说的演示文档，如：Windows下的PowerPoint（PPT）；Mac下Keynote等等。这里用Sphinx生成在线的HTML5形式的Slide，操作也相对简单，也是需要依赖库和简单修改下配置。

1. 安装依赖库

::

   pip install hieroglyph

2. 编辑conf.py，修改如下配置：

.. literalinclude:: code/slides.py
   :language: python
   :linenos:

3. 编辑Makefile，增加如下代码：

Linux下的Makefie：

.. literalinclude:: code/slides.Makefile
   :linenos:

4. 执行生成Slides

::

   make slides
   python -m SimpleHTTPServer 9527

.. seealso::

   有关Slide的更多信息，可以直接查看这个项目：https://github.com/nyergler/hieroglyph

自定义样式
^^^^^^^^^^

直接拿来主义，直接用别人写的Trac的样式

1. 复制样式文件到静态资源目录，比如，这里是：

::

   cp tracsphinx.css _static/

2. 编辑conf.py，增加或修改如下配置：

.. literalinclude:: code/style.py
   :language: python
   :linenos:

3. 执行生成HTML

::

   make html
   python -m SimpleHTTPServer 9527

直接浏览器访问9527端口，就可以看到类似Trac的官方样式效果。

汇总到一块
^^^^^^^^^^

可以直接看Python项目模板：https://github.com/akun/aproject/\ 只看docs目录即可。

这里提到的几个核心文件示例如下：

* `index.rst <https://raw.github.com/akun/aproject/master/docs/index.rst>`_
* `conf.py <https://raw.github.com/akun/aproject/master/docs/conf.py>`_
* `Makefile <https://raw.github.com/akun/aproject/master/docs/Makefile>`_
* `css <https://raw.github.com/akun/aproject/master/docs/_static/tracsphinx.css>`_

另外推荐一个服务：https://readthedocs.org/

如果你的项目研发文档用Sphinx写的，可以用来做文档的持续集成，相当方便。

这个\ `《软件构建实践系列》 <http://pm.readthedocs.org/>`_\ 就是用的这个服务。

最后
----

这是一篇很简单的项目推广文章，在自己的Python项目中把Sphinx用起来吧！

当然Sphinx不仅支持Python源码的Domain，而且支持C、C++、JavaScript等Domain，即使没有你所用的语言的Domain，它本身还支持写插件扩展，所以其它类型语言的项目也不妨用一下。
