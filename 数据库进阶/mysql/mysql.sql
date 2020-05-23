-- 查询一个数据库中有哪些个表，表名是什么，需要对应的数据库名例如：qdm712457164_db
select table_name from information_schema.`TABLES` where table_schema= 'qdm712457164_db'

-- 创建数据表
CREATE TABLE TB_URL_COLLECTIONS (URL_ID INT  NOT NULL,URL  CHAR(80) NOT NULL,TITLE  CHAR(20),NOTES  CHAR(20), TAG_ID INT, USER_ID INT )

-- mysql默认是不支持中文的，建表时需加上 character set = utf8 这条语句则可支持中文
create table entries2 ( id int auto_increment, title  text, content  text, posted_on  datetime, primary key (id) ) character set = utf8;

-- 若表已建号表，则执行该条语句，可支持之后的中文，但之前的中文乱码无法改变
alter table TB_URL_COLLECTIONS convert to character set utf8