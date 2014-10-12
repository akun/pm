项目如何从 Subversion 迁移到 Git
================================

很多有点历史的项目，都是用的 Subversion 作为版本控制工具的，随着项目需要，很多\
团队就打算采用 Git 作为替代工具了。好，现在问题来了：项目如何平滑的从 \
Subversion 迁移到 Git。

这里所谓的迁移是按照版本控制要求来迁移，包括：

* 尽可能完整的由谁提交的代码、做出的代码变更记录，提交日志等。
* 尽可能完整的分支、标签等。

因为毕竟是不同的版本控制工具，转化过程难免会有瑕疵。

Step 0 - 准备环境
-----------------

安装用到的工具的软件包，这里以 Ubuntu 为例

::

   $ sudo apt-get install subversion git
   $ sudo apt-get install git-core libsvn-perl perl libterm-readkey-perl

Step 1 - 规范 Subversion
------------------------

确认项目的 Subversion 地址：

::

   # 后面统一用 $PROJECT 表示项目的 Subversion 地址
   # 这里的示例项目名称是 west
   https://scms.example.com/svn/projects/west/


规范项目在 Subversion 的目录结构：

* 标准的 trunk、branches、tags 目录布局
* branches 和 tags 目录下的分支和标签保持平级，例如：

  + tags/v1.0.0 可以。
  + tags/1.x/v1.0.0 多了层目录就不可以。

* 如果不是平级，以 tags 为例，先执行 svn mv 操作

方式 1 - 远程 svn mv

::

   $ svn mv $PROJECT/tags/1.x/v1.0.0 $PROJECT/tags/v1.0.0

方式 2 - 本地 svn mv

::

   $ svn co $PROJECT west_subversion
   $ cd west_subversion
   $ svn mv tags/1.x/v1.0.0 tags/v1.0.0

最后规范后的目录示例如下：

::

   west
   ├── trunk
   │   ├── docs
   │   ├── west
   │   ├── setup.py
   │   └── README.rst
   ├── branches
   │   ├── hotfix_add_user_error
   │   ├── hotfix_issuse_9527
   │   ├── feature_unittest4app
   │   └── feature_multi_add_user
   └── tags
       ├── v1.0.0
       ├── v1.0.1
       ├── v2.0.0
       └── v2.1.0

Step 3 - 生成提交者 ID 和邮箱
-----------------------------

* example.com代表组织的邮箱，比如：knownsec.com
* 但如果个人邮箱不是统一的组织的话，就需要手工编辑 users.txt 了

::

   svn log $PROJECT --xml | grep -P "^<author" | \sort -u | perl -pe 's/<author>(.*?)<\/author>/$1 = $1 \<$1\@example.com\>/' > users.txt

Step 4 - 迁出项目代码（git svn）
--------------------------------

::

   git svn clone $PROJECT --authors-file=users.txt --no-metadata --localtime --stdlayout

* ``--authors-file`` 是得到的 git log 提交记录映射好提交者的信息
* ``--no-metadata`` 是得到的 git log 不带上对应的 Subversion 信息了，更干净
* ``--localtime`` 是得到的 git log 以本地时间为准，建议用上
* ``--stdlayout`` 是先前准备的按规范目录风格来迁出代码

Step 5 - 转化成Git的仓库格式（tags 和 branches）
------------------------------------------------

处理 tag：

::

   git for-each-ref refs/remotes/tags | cut -d / -f 4- | grep -v @ | while read tagname; do git tag "$tagname" "tags/$tagname"; git branch -r -d "tags/$tagname"; done

处理 branch：

::

   git for-each-ref refs/remotes | cut -d / -f 3- | grep -v @ | while read branchname; do git branch "$branchname" "refs/remotes/$branchname"; git branch -r -d "$branchname"; done

Step 6 - 一些清理工作
---------------------

由于这个转化转化会将及历史上的 branches 和 tags 也都生成一个 Git 的分支和标签\
，所以还是得清理下你认为不用的分支和标，可能包括：

* Subversion 历史上错误的 tags。
* Subversion 历史上临时的 branches。
* 冗余的 trunk 分支（其实跟转化后的 Git master 分支一样）。

Step 7 - 添加到远程 Git 仓库
----------------------------

* 比如：GitHub 上创建项目 west
* 添加本地 Git 项目到刚创建的远程 Git 仓库

::

   git remote add origin git@github.com:akun/west.git
   git push origin --all
   git push origin --tags

Step 8 - 完成迁移
-----------------

这样，可以直接在 Git 下来继续你的项目了。

::

   git clone git@github.com:akun/west.git

有关 Git 日常的使用，可以参考 :doc:`usage`

遗留问题
--------

上述方式转化其实还有瑕疵，比如：

* Subversion 允许空目录，转化 Git 用 git svn，处理空目录带上 \
  ``--preserve-empty-dirs`` 可能会报错，不处理，可能项目的程序原先依赖空目录的处理就得修改。
* 类似 svn:externals，svn:ignore，svn:merge 等属性丢失

不过问题不大，可以接受，Subversion 迁移 Git 算是基本平滑迁移。

参考
----

* http://git-scm.com/book/zh/
* https://www.semitwist.com/articles/article/view/the-better-svn-git-guide
* http://git.661346.n2.nabble.com/PATCH-1-2-git-svn-fix-occasional-quot-Failed-to-strip-path-quot-error-on-fetch-next-commit-td7584266.html
* http://git.661346.n2.nabble.com/git-svn-error-quot-Not-a-valid-object-name-quot-td7579457.html
* http://git.661346.n2.nabble.com/SVN-gt-Git-but-with-special-changes-td6840904.html
