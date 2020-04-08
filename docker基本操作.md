# docker 使用场景:
Docker提供了轻量级的虚拟化，它几乎没有任何额外开销，这个特性非常酷。
首先你在享有Docker带来的虚拟化能力的时候无需担心它带来的额外开销。其次，相比于虚拟机，你可以在同一台机器上创建更多数量的容器。
Docker的另外一个优点是容器的启动与停止都能在几秒中内完成。
### 1. 简化配置
虚拟机的最大好处是能在你的硬件设施上运行各种配置不一样的平台（软件、系统），Docker在降低额外开销的情况下提供了同样的功能。它能让你将运行环境和配置放在代码中然后部署，同一个Docker的配置可以在不同的环境中使用，这样就降低了硬件要求和应用环境之间耦合度。
### 2. 代码流水线（Code Pipeline）管理
前一个场景对于管理代码的流水线起到了很大的帮助。代码从开发者的机器到最终在生产环境上的部署，需要经过很多的中间环境。而每一个中间环境都有自己微小的差别，Docker给应用提供了一个从开发到上线均一致的环境，让代码的流水线变得简单不少。
### 3. 提高开发效率
这就带来了一些额外的好处：Docker能提升开发者的开发效率。
不同的开发环境中，我们都想把两件事做好。一是我们想让开发环境尽量贴近生产环境，二是我们想快速搭建开发环境。
理想状态中，要达到第一个目标，我们需要将每一个服务都跑在独立的虚拟机中以便监控生产环境中服务的运行状态。然而，我们却不想每次都需要网络连接，每次重新编译的时候远程连接上去特别麻烦。这就是Docker做的特别好的地方，开发环境的机器通常内存比较小，之前使用虚拟机的时候，我们经常需要为开发环境的机器加内存，而现在Docker可以轻易的让几十个服务在Docker中跑起来。
### 4. 隔离应用
有很多种原因会让你选择在一个机器上运行不同的应用，比如之前提到的提高开发效率的场景等。
我们经常需要考虑两点，一是因为要降低成本而进行服务器整合，二是将一个整体式的应用拆分成松耦合的单个服务（微服务架构）。如果你想了解为什么松耦合的应用这么重要，请参考Steve Yege的这篇论文，文中将Google和亚马逊做了比较。
### 5. 整合服务器
正如通过虚拟机来整合多个应用，Docker隔离应用的能力使得Docker可以整合多个服务器以降低成本。由于没有多个操作系统的内存占用，以及能在多个实例之间共享没有使用的内存，Docker可以比虚拟机提供更好的服务器整合解决方案。
### 6. 调试能力
Docker提供了很多的工具，这些工具不一定只是针对容器，但是却适用于容器。它们提供了很多的功能，包括可以为容器设置检查点、设置版本和查看两个容器之间的差别，这些特性可以帮助调试Bug。你可以在《Docker拯救世界》的文章中找到这一点的例证。
### 7. 多租户环境
另外一个Docker有意思的使用场景是在多租户的应用中，它可以避免关键应用的重写。我们一个特别的关于这个场景的例子是为IoT（物联网）的应用开发一个快速、易用的多租户环境。这种多租户的基本代码非常复杂，很难处理，重新规划这样一个应用不但消耗时间，也浪费金钱。
使用Docker，可以为每一个租户的应用层的多个实例创建隔离的环境，这不仅简单而且成本低廉，当然这一切得益于Docker环境的启动速度和其高效的diff命令。
### 8. 快速部署
在虚拟机之前，引入新的硬件资源需要消耗几天的时间。虚拟化技术（Virtualization）将这个时间缩短到了分钟级别。而Docker通过为进程仅仅创建一个容器而无需启动一个操作系统，再次将这个过程缩短到了秒级。这正是Google和Facebook都看重的特性。
你可以在数据中心创建销毁资源而无需担心重新启动带来的开销。通常数据中心的资源利用率只有30%，通过使用Docker并进行有效的资源分配可以提高资源的利用率。



----------------------------------------
# docker使用基本操作

## 搜索镜像
    docker search mongo

## 拉取镜像到本地
    docker pull mongo

    docker pull mysql:5.6    拉取5.6版本的mysql镜像

## 查看所有镜像
    docker images -a

## 把镜像做成容器并运行
    docker run --name mongodb -v ~/docker/mongo:/data/db -p 27017:27017 -d mongo

    docker run -p 3306:3306 --name mymysql -v $PWD/test-mysql/conf:/etc/mysql/conf.d -v $PWD/test-mysql/logs:/logs -v $PWD/test-mysql/data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=123456 -d mysql:5.6
### 各参数含义:
* `--name` 设置了容器的自定义名字
* `-v` 设置了路径的映射, 将本地路径映射到容器中（把一个本地/宿主机上的目录挂载到镜像里）. 此处, 路径可以自定义：冒号前为宿主机目录，必须为绝对路径，冒号后为镜像内挂载的路径。 
-v $PWD/conf:/etc/mysql/conf.d：将主机当前目录下的 conf/my.cnf 挂载到容器的 /etc/mysql/my.cnf  
-v $PWD/logs:/logs：将主机当前目录下的 logs 目录挂载到容器的 /logs  
-v $PWD/data:/var/lib/mysql ：将主机当前目录下的data目录挂载到容器的 /var/lib/mysql
* `-p` 设置了端口的映射, 将容器的27017(右侧) 映射到了本地的27017(右侧)     
    -P参数会随机分配一个49000~49900之间的端口到容器内部开放的网络（通过EXPORT指定的）端口  
    -p则可以具体指定要映射的端口，并且在一个指定端口上只能绑定一个容器    
* `-d` 设置当前容器为守护进程,后台运行    
* `-e` MYSQL_ROOT_PASSWORD=123456：初始化 root 用户的密码。    

## 查看所有的容器
    docker ps -a

## 开启/关闭容器
    docker start/stop +CONTAINER_NAME

## 查看容器详细信息:
    docker inspect +CONTAINER_NAME

## 进入容器交互模式:
    docker exec -it mongodb bash    
使用交互的形式, 在 名字为 `mongodb` 的容器中实行 `bash`这个命令

## 删除某容器
    docker rm +CONTAINER_NAME

## 删除某镜像
    docker rmi +IMAGE_NAME

## 更新镜像
##### 通过命令 docker commit来提交容器副本  
    docker commit -m="has update" -a="runoob" e218edb10161 +NEW_IMAGE_NAME:+TAG_NAME   
##### 各个参数说明：
* `-m`:提交的描述信息    
* `-a`:指定镜像作者    
* `e218edb10161`：容器ID    
* `runoob/ubuntu:v2`:指定要创建的目标镜像名和标签名    

### 交互模式下常用vim编辑,需更新安装vim:
#### 更新源
    apt-get update
#### 安装 vim
    apt-get install vim
#### 修改 mongo 配置文件
vim /etc/mongod.conf.orig




关于使用docker的一些问题:    
Q: 修改部署的容器配置,如tomcat中的一些端口配置等的修改    
A: 通过vim编辑修改?    

Q:随机端口映射,如何设置    
A:用-P为随机端口映射,用-p为制定端口映射.但同一端口不能被两个容器使用.

Q:已配置好的容器如何运行到其他电脑中? 如果跨平台呢?    
A:把容器打包save成镜像




安装和常用CLI：
添加阿里云镜像：sudo yum-config-manager --add-repo https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
安装命令：sudo yum install -y  docker-ce docker-ce-cli containerd.io
启动命令：sudo systemctl start docker
添加当前用户到docker用户组：sudo usermod -aG docker $USER （需注销），newgrp docker （立即生效）
Helloworld：docker run hello-world  （本地没有镜像的话会自动从远端仓库pull）
pull nginx 镜像：docker pull nginx（等效于nginx:latest）
运行：docker run -【d】（后台运行不阻塞shell） 【-p 80:80】（指定容器端口映射，内部：外部） nginx
查看正在运行：docker ps
删除容器：docker rm -f <container id(不用打全，前缀区分)>
进入bash：docker exec -it <container id(不用打全，前缀区分)> bash
commit镜像：docker commit <container id(不用打全，前缀区分)>  <name>
查看镜像列表：docker images （刚才commit的镜像）
使用运行刚才commit的镜像：docker run -d <name>
使用Dockerfile构建镜像：docker build -t <name> <存放Dockerfile的文件夹>
删除镜像：docker rmi <name>
保存为tar：docker save <name> > <tar name>
从tar加载：docker load < <tar name>

一些启动参数：
后台运行容器：-d
容器内外端口映射：-p 内部端口号:外部端口号
目录映射：-v 'dir name' : <dir>
指定映像版本：<name>:<ver>


----------------

docker中宿主机与容器（container）互相拷贝传递文件的方法

### 1、从容器拷贝文件到宿主机

docker cp mycontainer:/opt/testnew/file.txt /opt/test/
### 2、从宿主机拷贝文件到容器

docker cp /opt/test/file.txt mycontainer:/opt/testnew/