#coding=utf8
import xlrd
import pymongo

book = xlrd.open_workbook('243112892processdata.xls')
sheet1 = book.sheet_by_index(0)
print("表单名：", sheet1.name)
print("行数：", sheet1.nrows)
print("列数：", sheet1.ncols)
mat_process_data = {
    "_id" : "A405757500_PROCESS_DATA",
    "PROCESS_DATA" : {
        "F5SPEED":[],
        "F5GLEVEL":[],
        "F5IMRBEND":[],
        "F5WRBEND":[],
        "F5FORCE":[],
        "F5EXTHICK":[]
    },
    "mat_no" : "A405757500",
    "theme" : "PROCESS_DATA",
    "time" : "2022-06-27T08:44:22"
}

if __name__ == "__main__":
    for i in range(1, 214):            
        mat_process_data["PROCESS_DATA"]["F5EXTHICK"].append(sheet1.cell_value(i, 0))
        mat_process_data["PROCESS_DATA"]["F5FORCE"].append(sheet1.cell_value(i, 1))
        mat_process_data["PROCESS_DATA"]["F5WRBEND"].append(sheet1.cell_value(i, 2))
        mat_process_data["PROCESS_DATA"]["F5IMRBEND"].append(sheet1.cell_value(i, 3))
        mat_process_data["PROCESS_DATA"]["F5GLEVEL"].append(sheet1.cell_value(i, 4))
        mat_process_data["PROCESS_DATA"]["F5SPEED"].append(sheet1.cell_value(i, 5))
            
    
    myclient = pymongo.MongoClient("mongodb://192.168.1.1:27017/")
    mydb = myclient["USTB_DB"]
    mycol = mydb["PLTCM1_PROCESS_DATA"]
    myquery = { "mat_no": "A405757500" }
    
    if mycol.find_one(myquery):
        print("存在")
        mycol.replace_one(myquery, mat_process_data)
    else :
        print("不存在")
        x = mycol.insert_one(mat_process_data) 
        print(x)
    print("ok")