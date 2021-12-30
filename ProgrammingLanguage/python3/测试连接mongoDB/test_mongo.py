import pymongo

myclient = pymongo.MongoClient("mongodb://192.168.1.46:27017/")
mydb = myclient["runoobdb"]
print("ok runoobdb")
 
# dblist = myclient.list_database_names()
# # dblist = myclient.database_names() //3.7之前版本
# if "runoobdb" in dblist:
#     print("数据库已存在！")
# else:
#     print("no runoobdb")