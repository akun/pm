Git使用分享（上）
=================

* kun
* 2014-05-29

Why Git Now!
------------

.. rst-class:: build

   * 产品或项目到了一定阶段

     + 成熟度++
     + 客户/用户++
     + 定制++
     + 突发情况++

   * 各种分支++

.. nextslide::
   :increment:
.. rst-class:: build

   * Subversion的分支。。呵呵。。
   * 也有一个不错的SCMS：GitLab

.. nextslide::
   :increment:
.. rst-class:: build

   * 标准三件套（公司的私有项目）
   * VCS（版本控制系统）
   * SCMS（软件配置管理系统）
   * CI（持续集成）

.. nextslide::
   :increment:
.. rst-class:: build

   * 旧的三件套
   * .. image:: http://subversion.apache.org/images/svn-square.jpg
   * .. image:: http://www.edgewall.org/gfx/trac_logo.png
   * .. image:: http://www.edgewall.org/gfx/bitten_logo_small.png

.. nextslide::
   :increment:
.. rst-class:: build

   * 新的三件套
   * .. image:: http://git-scm.com/images/logo@2x.png
   * .. image:: http://contributors.gitlab.org/assets/gitlab_logo-e9826f83c629f000403fb0e64b91bf03.png
   * .. image:: http://jenkins-ci.org/sites/default/files/jenkins_logo.png

版本控制历史回顾
----------------

.. rst-class:: build

   * 本地

     + 不利于合作

   * 集中化

     + 单点故障
     + 数据丢失
     + 没备份

.. nextslide::
   :increment:
.. rst-class:: build

   * 分布式

     + 不是最新的版本快照
     + 而是整个代码仓库镜像
     + 但切记设定好协作流程

       - 比如层次模型，集中化那种就没法实现

   * 回头看版本控制的发展历史，都解决了软件开发中的什么问题？

Git? Git!
---------

.. rst-class:: build

   * 分布式的版本控制
   * 出色的合并追踪（merge tracing）能力
   * 软件配置管理
   * 起源：为更好地管理Linux内核开发而设计

     + 旧：BitKeeper

.. nextslide::
   :increment:
.. rst-class:: build

   * 流行的其它原因（个人观点）

     + Linus Torvalds这哥们的号召力

       .. image:: /_static/git_log.png

     + GitHub的流行：代码托管 + SCMS + 社交（程序员）

       .. image:: /_static/github_blog.png

Hello World
-----------

Ubuntu下为例

.. rst-class:: build

   * 安装

     ::

        $ apt-get install git
        $ git --version

   * 配置

     ::

        $ git config --global user.name "akun"
        $ git config --global user.email "6awkun@gmail.com"

.. nextslide::
   :increment:
.. rst-class:: build

   * 个人配置

     https://github.com/akun/config/blob/master/.gitconfig

     ::

        [core]
            editor = vim
        [color]
            diff = auto
            ui = true
        [user]
            name = akun
            email = 6awkun@gmail.com
        [alias]
            br = branch
            ci = commit
            co = checkout
            diffs = diff --staged
            st = status
            lg = log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold cyan)%aD%C(reset) %C(bold green)(%ar)%C(reset)%C(bold yellow)%d%C(reset)%n''          %C(white)%s%C(reset) %C(dim white)- %an%C(reset)' --all

几个概念
--------

.. rst-class:: build

   * 记录快照，而非差异

     + 示例图中，第一张是差异，第二张是快照
     + .. image:: http://git-scm.com/figures/18333fig0104-tn.png
     + .. image:: http://git-scm.com/figures/18333fig0105-tn.png

.. nextslide::
   :increment:
.. rst-class:: build

   * 三种状态

     + 工作目录 | 暂存区域 | Git目录
     + .. image:: http://git-scm.com/figures/18333fig0106-tn.png

.. nextslide::
   :increment:
.. rst-class:: build

   * 结合命令说明三种状态

     .. image:: /_static/git_3_kingdom.png

.. nextslide::
   :increment:
.. rst-class:: build

   * add到暂存
   * commit到本地Git
   * 默认，diff工作区和缓存区
   * 加参数--cached或--staged，diff缓存区和本地Git

常用命令（日常研发场景）
------------------------

.. rst-class:: build

   * 新项目开始喽

     ::

        $ git init
        $ touch README.rst
        $ git add README.rst
        $ git commit
        $ git remote add git@github.com:akun/learn.git
        $ git push -u origin master

   * 顺便推荐1个工具

     + cookiecutter - 项目模板，方便初始化新项目，DRY

       ::

          $ pip install cookiecutter  # 安装要用到的Python库
          $ cookiecutter https://github.com/akun/aproject.git # 按提示输入

.. nextslide::
   :increment:
.. rst-class:: build

   * 中途加入一个项目（fork后的场景）
   * 初来乍到

     ::

        $ git clone git@github.com:akun/learn.git  # 获得项目源代码
        $ cd learn  # 进入项目根目录
        $ git log  # 查看提交日志，了解下最近的提交都干嘛了

   * 增删改查代码

     ::

        $ git add TODO.rst  # 如果是新增文件，就增加文件到暂存区域
        $ git rm  tmp.txt  # 有时候会清理不需要的文件
        $ vim config.py  # 增加/修改源代码
        $ git mv README README.rst  # 有时候会修改文件名
        $ git tag

.. nextslide::
 :increment:
.. rst-class:: build

   * 更新代码 **下次主题详细说明**

     ::

        $ git fetch
        $ git rebase  # or git merge等其它操作

   * 准备提交代码

     ::

        $ git status  # 查看源码的版本控制状态
        $ git diff  # 一般放到暂存区域或提交Git目录前会检查下代码变更情况
        # 如果已经加入暂存区域，准备提交到Git目录前会检查下代码变更情况
        $ git diff --staged  # or `git diff --cached`

   * 提交代码到本地Git

     ::

        $ git ci  # DO NOT USE LIKE: git ci -m 'fixed sth.'

.. nextslide::
   :increment:
.. rst-class:: build

   * 推送代码到远程Git

     ::

        $ git push -u origin master

   * 顺便推荐4个工具

     + editorconfig - 编辑器约定，项目中的缩进、换行等约定也可以版本控制起来
     + PyLint - 代码检查，更好接近PEP 8风格
     + nose - 测试套件，执行nosetests，方便自动查找测试代码，省去写testrunner的麻烦
     + coverage - 代码单元测试覆盖率检查，更好量化单元测试进展
     + 写个简单的脚本，不就是个本地使用的小型CI？

对比Subversion
--------------

.. rst-class:: build

   * \ **已经习惯Git了不建议看**\ ，只是为了方便习惯用svn命令的人过度到git命令

     +------------------------+-------------------+---------------------------+------------------------------------------------------------------------------------+
     | 场景                   | Subversion(svn)   | Git(git)                  | 备注                                                                               |
     +------------------------+-------------------+---------------------------+------------------------------------------------------------------------------------+
     | 新项目开始喽           | svn import        | git init                  |                                                                                    |
     +------------------------+-------------------+---------------------------+------------------------------------------------------------------------------------+
     | 初来乍到               | svn co            | git clone                 | git checkout是另外的概念了                                                         |
     +------------------------+-------------------+---------------------------+------------------------------------------------------------------------------------+
     |                        | svn log           | git log                   |                                                                                    |
     +------------------------+-------------------+---------------------------+------------------------------------------------------------------------------------+
     | 增删改查代码           | svn add           | git add                   | Git有暂存区域的概念                                                                |
     +------------------------+-------------------+---------------------------+------------------------------------------------------------------------------------+
     |                        | svn rm            | git rm                    |                                                                                    |
     +------------------------+-------------------+---------------------------+------------------------------------------------------------------------------------+
     |                        | svn mv            | git mv                    |                                                                                    |
     +------------------------+-------------------+---------------------------+------------------------------------------------------------------------------------+
     |                        | svn ls            | 无合适概念                | 如果想查看branches、tags的话，直接git branch, git tag                              |
     +------------------------+-------------------+---------------------------+------------------------------------------------------------------------------------+
     |                        | svn cat           | 无合适概念                |                                                                                    |
     +------------------------+-------------------+---------------------------+------------------------------------------------------------------------------------+
     | 更新代码               | svn up            | git fetch + git rebase    | 还可以是git merge等其它操作，慎用git pull                                          |
     +------------------------+-------------------+---------------------------+------------------------------------------------------------------------------------+

.. nextslide::
   :increment:
.. rst-class:: build

   * \ **已经习惯Git了不建议看**\ ，只是为了方便习惯用svn命令的人过度到git命令

     +------------------------+-------------------+---------------------------+------------------------------------------------------------------------------------+
     | 场景                   | Subversion(svn)   | Git(git)                  | 备注                                                                               |
     +------------------------+-------------------+---------------------------+------------------------------------------------------------------------------------+
     | 准备提交代码           | svn st            | git status                | Git会显示三个区域的概念，Subversion如果要有区域概念的话也就2个：本地、远程版本控制 |
     +------------------------+-------------------+---------------------------+------------------------------------------------------------------------------------+
     |                        | svn diff          | git diff                  | Git有三个区域的概念，所以有个--staged or --cached参数                              |
     +------------------------+-------------------+---------------------------+------------------------------------------------------------------------------------+
     | 提交（推送）代码到远程 | svn ci            | git commit + git push     | 这里可以理解为Git是分布式版本控制系统，所以会拆分出2个命令                         |
     +------------------------+-------------------+---------------------------+------------------------------------------------------------------------------------+
     | 其它杂项               | svn info          | git config --local --list |                                                                                    |
     +------------------------+-------------------+---------------------------+------------------------------------------------------------------------------------+
     |                        | svn pe svn:ignore | vim .gitignore            |                                                                                    |
     +------------------------+-------------------+---------------------------+------------------------------------------------------------------------------------+
     |                        | svn blame         | git blame                 |                                                                                    |
     +------------------------+-------------------+---------------------------+------------------------------------------------------------------------------------+
     |                        | svn sw            | git checkout              | 切换分支，两者分支的概念还是有很大不同的                                           |
     +------------------------+-------------------+---------------------------+------------------------------------------------------------------------------------+

团队合作场景（分支初步介绍）
----------------------------

分支模型

.. rst-class:: build

   * Subversion模式

     .. image:: http://git-scm.com/figures/18333fig0501-tn.png

.. nextslide::
   :increment:
.. rst-class:: build

   * GitHub/GitLab模式

     .. image:: http://git-scm.com/figures/18333fig0502-tn.png

.. nextslide::
   :increment:
.. rst-class:: build

   * Linux内核模式

     .. image:: http://git-scm.com/figures/18333fig0503-tn.png

.. nextslide::
   :increment:
.. rst-class:: build

   文章介绍：《一个成功的分支模型》

   * .. image:: http://nvie.com/img/2009/12/bm002.png

.. nextslide::
   :increment:
.. rst-class:: build

   * .. image:: http://nvie.com/img/2009/12/fb.png

.. nextslide::
   :increment:
.. rst-class:: build

   * **下次主题详细说明**
   * .. image:: http://nvie.com/img/2010/01/merge-without-ff.png

.. nextslide::
   :increment:
.. rst-class:: build

   * .. image:: http://nvie.com/img/2010/01/hotfix-branches1.png

.. nextslide::
   :increment:
.. rst-class:: build

   * .. image:: http://nvie.com/img/2009/12/Screen-shot-2009-12-24-at-11.32.03.png
        :height: 407px
        :width: 305px
   * 点击查看大图

.. nextslide::
   :increment:
.. rst-class:: build

   * 上面完整的模型，看起来稍显复杂，建议：

     + 做项目的研发团队，可以拆分成开发组和支持维护组的时候使用
     + 理想配备，每组3-4人

   * 现实资源紧缺情况下，3-4人小团队的简化模型

.. nextslide::
   :increment:
.. rst-class:: build

   * .. image:: /_static/git_simple.png
        :height: 451px
        :width: 249px

   * 说明：圆圈的虚线表示私有分支；圆圈的实现表示公有分支
   * 点击查看大图

.. nextslide::
   :increment:
.. rst-class:: build

   * 招人层面控制：比如，所谓“全栈工程师”
   * 任务拆分层面控制：拆分成可以1个人完成1个独立特性
   * 私有feature分支：从公有master中fork一份代码
   * 公有develop分支：递交merge请求到公有的develop分支
   * 线性的版本策略：人员有限，避免出现研发下个版本和当前版本发布并行的情况
   * release分支：干掉
   * 公有master：干净稳定的tag
   * 私有hotfix分支：保留。可以通过code review、结对编程等保障hostfix的代码质量
   * 上述得有个完善的自动化的功能测试、单元测试、发布、部署、持续集成等套件的保障

.. nextslide::
   :increment:
.. rst-class:: build

   * 涉及命令用法 **下次主题详细说明**

     ::

        $ git brach
        $ git checkout
        $ git fetch
        $ git merge
        $ git rebase
        $ # git pull
        $ git push
        $ git tag

Tips
----

.. rst-class:: build

* 缩略/定制git命令

  ::

     $ git config -e
     # 增加下列缩写
     br = branch
     ci = commit
     co = checkout
     diffs = diff --staged
     st = status
     lg = log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold cyan)%aD%C(reset) %C(bold green)(%ar)%C(reset)%C(bold yellow)%d%C(reset)%n''          %C(white)%s%C(reset) %C(dim white)- %an%C(reset)' --all

* 不用缩写也行，可以配合按2下Tab，会自动罗列备选内容，而不用特别记忆

.. nextslide::
   :increment:

.. rst-class:: build

* “空”文件夹加入Git版本控制

  ::

     # Ignore everything in this directory
     *
     # Except this file
     !.gitignore

* 可以用下zsh，进入Git版本控制的项目，会显示当前分支

  + 拿来主义的人可以直接用
  + 有控制洁癖的，不习惯用zsh的可以尝试提取核心功能代码，hack下自己的Shell

参考
----

.. rst-class:: build

* http://git-scm.com/book/zh/
* http://rogerdudler.github.io/git-guide/
* http://nvie.com/posts/a-successful-git-branching-model/
* http://marklodato.github.io/visual-git-guide
* http://stackoverflow.com/questions/115983/how-do-i-add-an-empty-directory-to-a-git-repository
* https://git.wiki.kernel.org/index.php/GitFaq#Can_I_add_empty_directories.3F
* http://source.android.com/source/developing.html
* http://zh.wikipedia.org/wiki/Git
* http://zh.wikipedia.org/wiki/GitHub

Next(May be)
------------

.. rst-class:: build

* 服务/软件使用介绍

  + GitHub
  + Bitbucket
  + GitLab

* HEAD的概念（本地/远程）
* 分支++
* 撤回提交/重写历史
* 从Subversion迁移到Git

.. nextslide::
   :increment:

.. rst-class:: build

* 高级主题或日常开发人员不常用（更偏重于，运维人员、配置管理人员、构建管理人员、发布管理人员、项目管理人员）

  + 发布，打标签
  + 子模块
  + 钩子
  + 运维管理相关
  + 项目管理相关

* 阅读更多其它主题：http://pm.readthedocs.org/

