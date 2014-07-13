回顾
----

.. rst-class:: build

   * 软件开发过程杂谈：http://example.zhengkun.info/loop/
   * .. image:: /_static/start.png

前提
----

.. rst-class:: build

   * 这里特指Python项目
   * 需求分析不在讲解范围内

     + 这里前提是认为需求明确了，进行实现阶段的事情
     + 核心引擎、类库等这种类型项目，其实最大的需求来源往往是自身！

   * 按项目的高标准、通用要求，实际操作还是具体问题具体分析

部分要素
--------

.. rst-class:: build

   * 代码/设计
   * 测试
   * 文档
   * 安装/部署
   * 必备三件套：VCS + SCMS + CI
   * 具体问题具体分析（铁三角）

易被忽略的要素之一：测试
------------------------

.. rst-class:: build

   * 一行代码的改动要不要测试？
   * 看到一个统计数据：“...在引入代码评审之前，55%的\ **单行**\ 维护代码改动都是错误的...”
   * 几个案例

.. nextslide::
   :increment:
.. rst-class:: build

   * .. image:: http://coolshell.cn//wp-content/uploads/2014/02/gotofail.jpg
   * .. image:: /_static/space.png
   * .. image:: /_static/dict.png
   * 引入缺陷排行耪：拼写错误、空格、大中小括号、分号等标点。。

.. nextslide::
   :increment:
.. rst-class:: build

   * 编码过程中测试理应花费的时间以及自动化的重要性
   * .. image:: /_static/auto_test.png

.. nextslide::
   :increment:
.. rst-class:: build

   * 单元测试

     + 没有写过单元测试的程序员，你的程序员生涯是不完整的。。
     + 这个说法可能略微夸张。。
     + 保证一定的测试覆盖率
     + 100%？
     + 核心模块、复杂模块尽量保证

   * 功能测试

     + 看情况，比如：AppScan、爬虫这种最好能有对应的功能测试
     + UI更是，尽量自动化，比如：UI功能逐渐用Selenium跑测试

易被忽略的要素之二：文档
------------------------

.. rst-class:: build

   * .. image:: http://www.iconpng.com/png/softdimension/ms-word-2.png
   * Word
   * **No**

.. nextslide::
   :increment:
.. rst-class:: build

   * .. image:: /_static/rst_editor_qt1.png
   * Python Doc | reStructuredText | MarkDown
   * **YES**

.. nextslide::
   :increment:
.. rst-class:: build

   * 最起码需要的技术方面的文档
   * 如何开发项目指导文档
   * 安装/部署文档
   * API/接口文档，特别是类库方面的程序
   * ChangeLog
   * FAQ
   * TODO or 路线图
   * 研发文档，主要：概要设计/构架设计、核心模块设计

.. nextslide::
   :increment:
.. rst-class:: build

   * 程序员A接手一个项目问：有文档吗？
   * 程序员A开发一个项目被要求写文档：文档？笑话！
   * 代码就是文档，文档就是代码，不要分家
   * 推荐

     + Sphinx编写
     + Python项目算是标配
     + 可以代码中的Python Doc直接生成文档
     + 特别是对类库的项目，写API文档很方便
     + 可以版本控制起来

易被忽略的要素之三：安装/部署
-----------------------------

.. rst-class:: build

   * Makefile
   * setup.py
   * install.sh
   * pip install kssched
   * 软件包 or ISO安装镜像

必备三件套简述
--------------

.. rst-class:: build

   * 三件套（公司的闭源项目为例）

     + VCS（版本控制系统）
     + SCMS（软件配置管理系统）
     + CI（持续集成）

   * Subversion系三件套

     + Subversion
     + Trac
     + Bitten

   * Git系三件套

     + Git
     + GitLab
     + GitLab CI

.. nextslide::
   :increment:
.. rst-class:: build

   * 核心是版本控制系统
   * 提交日志详细、规范，方便ChangeLog编写
   * 代码稳定/没特殊情况，保持：

     + 提交粒度细，提交代码量少，降低别人code review单独
     + 一次提交只处理一个事情
     + 区分代码风格修改和代码逻辑修改，分别提交
     + 除非：代码乱，需要重大重构

   * 能版本控制的都加入版本控制

     + 一切开发行为，统一在版本仓库中进行自动记录
     + 不要仅仅将项目的源代码纳入到版本控制下，也应该包括文档、FAQ、设计注释和任何人们希望编辑的内容
     + 二进制、大文件等加入版本控制要慎重
     + 不要将生成的文件置入版本控制
     + 高标准是：功能代码、测试代码、对应文档在一次提交中得到体现

“代码”为王
----------

.. rst-class:: build

   * 设计！设计！设计！

     + 简洁
     + 以最少的代码实现最多的功能

   * API/接口的设计

     + 输入/输出
     + 契约式编程

   * 代码风格，通用约定：PEP 8

.. nextslide::
   :increment:
.. rst-class:: build

   * 代码风格，项目内部约定，比如：

     + UI代码都预留国际化处理等
     + import顺序：Python官方库、第三方库、公司公共库、项目公共库、模块库等
     + 绝对import等
     + 避免魔术数字等
     + 等等有利于此项目的各种约定

   * 必要的注释

     + 注释更多是为了解释为什么这么做
     + 好的命名本身就解释了代码是做什么

   * **Code Review**

     + 大多数的Bug是消灭在这个阶段的

具体问题具体分析
----------------

.. rst-class:: build

   * 没错，这是一句废话。。
   * .. image:: /_static/triangle.png

.. nextslide::
   :increment:
.. rst-class:: build

   * 各种所谓XDD开发哲学
   * TDD / BDD / DDD
   * Test / Behavior / Domain Drive Development
   * Talent / Bug / Deadline Drive Development
   * TDD，测试驱动开发，其实更好的解释应该是：更重视设计的开发流程

总结
----

.. rst-class:: build

   * 要重视的：安装/部署、文档、测试
   * 善用三件套：Git + GitLab + GitLab CI
   * 代码/设计为王
   * 目的：让用户（客户/用户/其他程序员），能更放心、更安心、更开心的使用

题外：Joel衡量法则
------------------

.. rst-class:: build

   * 你们用不用源文件管理系统？
   * 你们可以把整个系统从源码到ＣＤ映像文件一步建成吗？
   * 你们每天白天都把从系统源码到ＣＤ映像做一遍吗？
   * 你们有软件虫管理系统吗？
   * 你们在写新程序之前总是把现有程序里已知的虫解决吗？
   * 你们的产品开发日程安排是否反映最新的开发进展情况？
   * 你们有没有软件开发的详细说明书？
   * 你们的程序员是否工作在安静的环境里？
   * 你们是否使用现有市场上能买到的最好的工具？
   * 你们有没有专职的软件测试人员？
   * 你们招人面试时是否让写一段程序？
   * 你们是否随便抓一些人来试用你们的软件？

参考
----

* http://producingoss.com/zh/
* http://coolshell.cn/articles/11112.html
* http://coolshell.cn/articles/4875.html
* https://code.google.com/p/kcpycamp/wiki/HowtoScm
* http://producingoss.com/zh/vc.html
* http://chinese.joelonsoftware.com/Articles/TheJoelTest.html
* 《软件系统构架：使用视点和视角与利益相关者合作》

Q & A
-----

* ? & [.|!]

