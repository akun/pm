Subversion项目迁移Git
=====================

* kun
* 2014-06-05

Step1 - 准备环境 + 规范Subversion
---------------------------------

.. rst-class:: build

   * 安装用到的工具的软件包（以Ubuntu为例）

     ::

        $ sudo apt-get install subversion git
        $ sudo apt-get install git-core libsvn-perl perl libterm-readkey-perl

   * 确认Subversion地址

     ::

        # 后面统一用$PROJECT表示项目的Subversion地址
        # 这里的示例项目名称是west
        https://scms.example.com/svn/projects/west/

.. nextslide::
   :increment:
.. rst-class:: build

   * 规范项目在Subversion的目录结构

     + 标准的trunk、branches、tags目录布局
     + branches和tags目录下的分支和标签保持平级，例如：tags/v1.0.0可以；tags/1.x/v1.0.0多了层目录

     + 如果不是平级，以tags为例，先执行svn mv操作

       ::

          # 方式1 远程svn mv
          $ svn mv $PROJECT/tags/1.x/v1.0.0 $PROJECT/tags/v1.0.0

          # 方式2 本地svn mv
          $ svn co $PROJECT west_subversion
          $ cd west_subversion
          $ svn mv tags/1.x/v1.0.0 tags/v1.0.0

.. nextslide::
   :increment:
.. rst-class:: build

   * 最后规范后的目录示例如下

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

Step3 - 生成提交者ID和邮箱
--------------------------

.. rst-class:: build

   ::

      # example.com代表组织的邮箱，比如：knownsec.com
      # 但如果个人邮箱不是统一的组织的话，就需要手工编辑users.txt了
      svn log $PROJECT --xml | grep -P "^<author" | \sort -u | perl -pe \
      's/<author>(.*?)<\/author>/$1 = $1 \<$1\@example.com\>/' > users.txt

Step4 - 迁出项目代码（git svn）
-------------------------------

.. rst-class:: build

   ::

      # --authors-file是得到的git log提交记录映射好提交者的信息
      # --no-metadata是得到的git log不带上对应的Subversion信息了，更干净
      # --localtime是得到的git log以本地时间为准，建议用上
      # --stdlayout是先前准备的按规范目录风格来迁出代码
      git svn clone $PROJECT --authors-file=users.txt --no-metadata \
      --localtime --stdlayout

Step5 - 转化成Git的仓库格式（tags和branches）
---------------------------------------------

.. rst-class:: build

   ::

      # 处理tag
      git for-each-ref refs/remotes/tags | cut -d / -f 4- | grep -v @ | \
      while read tagname; do git tag "$tagname" "tags/$tagname"; \
      git branch -r -d "tags/$tagname"; done

      # 处理branch
      git for-each-ref refs/remotes | cut -d / -f 3- | grep -v @ | \
      while read branchname; do git branch "$branchname" "refs/remotes/$branchname"; \
      git branch -r -d "$branchname"; done

Step6 - 添加到远程仓库（以GitLab为例）
--------------------------------------

.. rst-class:: build

   * GitLab中创建项目west
   * 添加本地Git项目到刚创建的远程Git仓库

     ::

        git remote add origin git@scms.example.com:group/west.git
        git push origin --all
        git push origin --tags

Step7 - 一些清理工作
--------------------

.. rst-class:: build

   * Subversion历史上错误的tags
   * Subversion历史上临时的branches
   * 都会完整转化到Git仓库中的tag和branch
   * 可以在GitLab上直接删除这些不要的

Step8 - 完成迁移
----------------

.. rst-class:: build

   * TODO: 迁移前用Trac做SCMS的Subversion的项目截图
   * TODO: 迁移后用GitLab做SCMS的Git的项目截图

遗留问题
--------

.. rst-class:: build

   * Subversion允许空目录，转化Git用git svn，处理空目录带上--preserve-empty-dirs可能会报错
   * 类似svn:externals，svn:ignore，svn:merge等属性丢失
   * 不过问题不大，可以接受
   * Subversion迁移Git算是基本平滑迁移

参考
----

* http://git-scm.com/book/zh/
* https://www.semitwist.com/articles/article/view/the-better-svn-git-guide
* http://git.661346.n2.nabble.com/PATCH-1-2-git-svn-fix-occasional-quot-Failed-to-strip-path-quot-error-on-fetch-next-commit-td7584266.html
* http://git.661346.n2.nabble.com/git-svn-error-quot-Not-a-valid-object-name-quot-td7579457.html
* http://git.661346.n2.nabble.com/SVN-gt-Git-but-with-special-changes-td6840904.html

Q & A
-----

* ? & [.|!]

END
---

* Thanks!
