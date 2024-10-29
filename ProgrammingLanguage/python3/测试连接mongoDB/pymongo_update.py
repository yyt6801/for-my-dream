import pymongo
 
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["DBname"]
mycol = mydb["CollName"]
 
myquery = { "mat_no": "X22B554183000" }
newvalues = { "$set": { "data.kv.$[].EX_WEIGHT": 26453 } }

if mycol.find_one(myquery):
    mycol.update_one(myquery, newvalues)
# 输出修改后的  "sites"  集合
for x in mycol.find(myquery):
    print(x)