-- 查询一个数据库中有哪些个表，表名是什么，需要对应的数据库名例如：qdm712457164_db
select table_name from information_schema.`TABLES` where table_schema= 'qdm712457164_db'