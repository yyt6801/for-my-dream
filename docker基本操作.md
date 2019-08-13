## 搜索镜像
docker search mongo

## 拉取镜像到本地
docker pull mongo

## 查看所有镜像
docker images -a

## 把镜像做成容器并运行
docker run --name mongodb -v ~/docker/mongo:/data/db -p 27017:27017 -d mongo
### 各参数含义:
`--name` 设置了容器的名字 * 
`-v` 设置了路径的映射, 将本地路径映射到容器中. 此处, 路径可以自定义 * 
`-p` 设置了端口的映射, 将容器的27017(右侧) 映射到了本地的27017(右侧)

## 查看所有的容器
docker ps -a

## 开启/关闭容器
docker start/stop +CONTAINER_NAME

## 查看容器详细信息:
docker inspect +CONTAINER_NAME

## 进入容器交互模式:
docker exec -it mongodb bash
使用交互的形式, 在 名字为 `mongodb` 的容器中实行 `bash`这个命令

### 交互模式下常用vim编辑,需更新安装vim:
#### 更新源
apt-get update
#### 安装 vim
apt-get install vim
#### 修改 mongo 配置文件
vim /etc/mongod.conf.orig