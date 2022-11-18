import pymongo
import json

myclient = pymongo.MongoClient("mongodb://170.0.200.116:27017/")
mydb = myclient["bkgy"]
print("ok bkgy")
 
# dblist = myclient.list_database_names()
# # dblist = myclient.database_names() //3.7之前版本
# if "runoobdb" in dblist:
#     print("数据库已存在！")
# else:
#     print("no runoobdb")

collist = mydb. list_collection_names()
# collist = mydb.collection_names()

if "pltcm_asc" in collist:   # 判断 pltcm_asc 集合是否存在
  print("集合已存在！")
  mycol = mydb["pltcm_asc"]
  mycol_new = mydb["pltcm_asc_test"]
  
# #   查询: find_one() find() find(myquery) find().limit(3)
#   x = mycol.find_one() # 查询 文档中的第一条数据 
#   EXTID = x["EXTID"]
#   print(EXTID)
  for y in mycol.find(): # 查询 文档中的所有数据 
    myquery = { "EXTID": y["EXTID"] }
    mydoc = mycol.find(myquery).limit(1)
    for x in mydoc:
      if mycol_new.find_one({"_id": x["EXTID"]}) is None:
        # print("入口卷号:"+ x["ENTID"] +" 长度:"+ str(x["LENGTH"]))
        data = {"_id": x["EXTID"],"extid":x["EXTID"]}
        data["entid"] = x["ENTID"] if("ENTID" in x) else ""
        data["pltcm_no"] = x["PLTCM_NO"] if("PLTCM_NO" in x) else ""
        data["steel_grade"] = x["STEEL_GRADE"] if("STEEL_GRADE" in x) else ""
        data["width"] = x["WIDTH"] if("WIDTH" in x) else 0
        data["thickness"] = x["THICKNESS"] if("THICKNESS" in x) else 0
        data["length"] = x["LENGTH"] if("LENGTH" in x) else 0
        data["en_width"] = x["EN_WIDTH"] if("EN_WIDTH" in x) else 0
        data["en_thickness"] = x["EN_THICKNESS"] if("EN_THICKNESS" in x) else 0
        data["end_time"] = x["END_TIME"] if("END_TIME" in x) else ""
        data["asc_length"] = x["ASC_LENGTH"] if("ASC_LENGTH" in x) else 0
        data["flatave_alarm_length_head"] = x["FLATAVE_ALARM_LENGTH_HEAD"] if("FLATAVE_ALARM_LENGTH_HEAD" in x) else 0
        data["flatave_alarm_length_middle"] = x["FLATAVE_ALARM_LENGTH_MIDDLE"] if("FLATAVE_ALARM_LENGTH_MIDDLE" in x) else 0
        data["flatave_alarm_length_tail"] = x["FLATAVE_ALARM_LENGTH_TAIL"] if("FLATAVE_ALARM_LENGTH_TAIL" in x) else 0
        data["asc_wave_length_ds"] = x["ASC_WAVE_LENGTH_DS"] if("ASC_WAVE_LENGTH_DS" in x) else 0
        data["asc_wave_length_os"] = x["ASC_WAVE_LENGTH_OS"] if("ASC_WAVE_LENGTH_OS" in x) else 0
        data["head_jifen"] = x["HEAD_JIFEN"] if("HEAD_JIFEN" in x) else 0
        data["mid_jifen"] = x["MID_JIFEN"] if("MID_JIFEN" in x) else 0
        data["tail_jifen"] = x["TAIL_JIFEN"] if("TAIL_JIFEN" in x) else 0
        data["asc_desc"] = x["ASC_DESC"] if("ASC_DESC" in x) else ""
        data["flat_class_length"] = x["Flat_Class_Length"] if("Flat_Class_Length" in x) else []
        data["flat_class_rate"] = x["Flat_Class_Rate"] if("Flat_Class_Rate" in x) else []
        data["flat_ave"] = x["Flat_ave"] if("Flat_ave" in x) else []
        data["priterm"] = x["PriTerm"] if("PriTerm" in x) else []
        data["quaterm"] = x["QuaTerm"] if("QuaTerm" in x) else []
        res = mycol_new.insert_one(data) 
        print(res.inserted_id)
        # json_str = json.dumps(data)
        # # sort the result alphabetically by keys:
        # json_str = json.dumps(data, indent=4, sort_keys=True)
        # print(json_str)
        # print ("Python 原始数据：", repr(data))