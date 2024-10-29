import pymongo

myclient = pymongo.MongoClient("mongodb://admin:ustb_ansteel2130@192.168.10.129:27017/")
mydb = myclient["runoobdb"]
print("ok runoobdb")
 
dblist = myclient.list_database_names()
# dblist = myclient.database_names() //3.7之前版本
if "runoobdb" in dblist:
    print("数据库已存在！")
else:
    print("no runoobdb")