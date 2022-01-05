#### 1、	在本地新建文件夹，把远程仓库的克隆到本地:
a)	`git clone URL` 
#### 2、	本地修改后同步到远程仓库：  
a)	`git status` (查看本地是否跟踪到)  
b)	`git add . `  (把本地新增的文件添加到缓存)  
c)	再执行 `git status` 查看是否已存放至暂存区  
d)	`git commit –m "changes"` (使用 git add 命令将想要快照的内容写入缓存区， 而执行 *`git commit`* 将缓存区内容添加到仓库中。)  
e)	`git push` (把本地代码放到远程仓库)  
#### 3、	在本地仓库获取同步最新远程仓库：
方法一：	`git fetch` 在本地仓库获取最新的代码同步（常用），检查更新，但并未改动本地文件；**之后需要加上 *`git merge`* 才将本地仓库进行同步。**  至此，修改全部结束。  
方法二：	直接 `git pull` 即可实现同步： (在本地pull远程仓库最新的代码到本地仓库，相当于 *`git fetch + git merge`* )  

#### 4、    取消本地修改内容
`git checkout -- filename`  filename填写需要撤销修改的文件名(需包含路径)，可以清空所修改内容  
`git checkout .`    可清空本地仓库所有未提交的修改  

***
----
## 将本地代码上传到git新仓库中
1.本地仓库中添加Readme.md文件和.gitignore文件  
2.初始化仓库 `git init`  
3.添加当前目录下的所有文件到暂存区： `git add . `  
4.将暂存区内容添加到本地仓库中。： `git commit -m "first commit"`  
5.将本地仓库和github远程仓库绑定：`git remote add origin https://github.com/....git`  
6.提交至远程仓库：`git push -u origin main`  


***
----
## 在新环境中与仓库连接:
ssh key是连接你的电脑和GitHub服务器的一把钥匙，只有两者建立了联系才能把你本地的代码提交到github上。首先要获取到ssh key公钥。  
1.在终端输运行命令：  
`ssh-keygen`  获取ssh-key;  
把生成文件夹中的id_rsa.pub内容(获取到的ssh-key)复制到github自己账户setting中,然后回到终端，设置用户名和邮箱，最好与注册的github一致。这个用户名和邮箱是非常重要的，因为每次Git提交都会使用该信息。它被永远的嵌入到了你的提交中。在团队开发中，可以清楚地看到是谁的提交。  
在终端中输入命令：  
`git config  'user.name'`  
`git config  'useremail@xx'`  
接下来把仓库clone到本地,修改后 *`git commit -am "xxx"`* 提交; 再 *`git push`* 即可.  

### git 使用 *`ssh`* 方式`clone`和`push` 无需用户名密码
若用的是https而不是ssh则每次操作仍需账号和密码。
可以更新一下origin

`git remote remove origin`  
`git remote add origin git@github.com:Username/Your_Repo_Name.git`  
之后你还需要重新设置track branch，比如：  
先 `git pull` 然后执行：
`git branch --set-upstream-to=origin/master master`
即可完成使用ssh连接本地
***
----


## git分支操作：
`$ git checkout -b iss1`  新建一个分支并同时切换到那个分支上   
&nbsp;&nbsp;*`Switched to a new branch "iss1"  `*

它是下面两条命令的简写：  
`$ git branch iss1`  
`$ git checkout iss1`

开始在分支中修改代码...   
...  
修改完成，开始提交到分支iss1  
`$ git commit -am "fix iss1"`  

提交完成后先不要push，切换回master后 需要把分支iss1 合并到master中:  
`$ git checkout master`   切换回master  
`$ git merge iss1`    把iss1合并到当前master中  
&nbsp;&nbsp;*`Updating f42c576..3a0874c`*  
&nbsp;&nbsp;*`Fast-forward`*  
&nbsp;&nbsp;&nbsp;&nbsp;*` index.html | 2 ++`*  
&nbsp;&nbsp;&nbsp;&nbsp;*` 1 file changed, 2 insertions(+)`*  合并完成 

现在分支的修改已完全合并到master中，可以删除分支iss1，然后再push到远程中：  
`$ git branch -d iss1`  删除分支iss1  
`$ git push`  把当前的修改push到远程仓库中  



***
----

## 回退命令git reset：
`$ git reset --hard HEAD^ `        回退到上个版本  
`$ git reset --hard HEAD~3  `      回退到前3次提交之前，以此类推，回退到n次提交之前  
`$ git reset --hard commit_id `    	 退到/进到 指定commit的sha码

***

----

## 修改已提交命令git rebase：
`$ git rebase -i`        弹出交互式的界面让用户编辑完成合并操作 
上面未被注释的部分列出的是我们本次rebase操作包含的所有提交，下面注释部分是git为我们提供的命令说明。每一个commit id 前面的pick表示指令类型，git为我们提供了以下几个命令：

    pick：保留该commit（缩写：p）  
    reword：保留该commit，但我需要修改该commit的注释（缩写：r）  
    edit：保留该commit, 但我要停下来修改该提交（不仅仅修改注释）（缩写：e）  
    squash：将该commit和前一个commit合并（缩写：s）  
    fixup：将该commit和前一个commit合并，但我不要保留该提交的注释信息（缩写：f）  
    exec：执行shell命令（缩写：x）  
    drop：我要丢弃该commit（缩写：d） 
把对应commit前改为edit可修改此次提交，修改完后重新提交即可；
***
----

## git 基本操作注意点总结:
`git clone <source repository> <destination repository>`  复制本地仓库的命令方式。其中 *`<source repository>`* ：想克隆的本地仓库路径。 
*`<destination repository>`*：想克隆去另一个地方的路径。  
例如：  `git clone d:/git e:/git11` 是将 d:/git 的仓库（即包含隐藏文件 .git 的目录）克隆到 e:/git11 目录下。 

---
 
**注意：**  
1、*`<destination repository>`* 目录必须没有在文件系统上创建，或创建了但里面为空，不然会克隆不成功。  
2、与从远程拉取仓库不同，路径的最后不用写 .git 来表明这是一个仓库。  
`git status –s`  获得简短的状态输出。  
`git diff` ：查看工作区与暂存区的不同。  
`git diff –cached [<commit>]` ：查看暂存区与指定提交版本的不同，版本可缺省（为HEAD）。  
`git diff <commit>`：查看工作区与指定提交版本的不同。  
`git diff <commit>..<commit>`：查看2个指定提交版本的不同，其中任一可缺省（为HEAD）。  
`git diff <commit>...<commit>`：查看2个不同分支指定提交版本的不同，其中任一可缺省（为HEAD），该命令相当于 *`git diff $(git-merge-base A B) B`*       
`git commit –am ""` 直接提交全部修改，相当于 `add` 和 `commit` 一起执行了。  
*注意：全部文件为 tracked 才行，你新建了文件为 untracked 时，该命令不会执行*    
`git checkout`  与 git reset 不同，reset 是替换整个目录树，多余的文件将被删除。而 checkout 只是替换指定的文件，对多余的文件保留不做任何处理。  
`git rm`  把文件从工作区和暂存区中删除。使用 *`—cached`* 只从暂存区中删除。使用 *`–rf <directory>`* 可删除指定目录下的所有文件和子目录。  
`git mv <source> <destination>`  在工作区和暂存区中进行移动或重命名。若 *`<destination>`* 不为一个目录名，则执行重命名。如果为一个目录名，则执行移动。  

