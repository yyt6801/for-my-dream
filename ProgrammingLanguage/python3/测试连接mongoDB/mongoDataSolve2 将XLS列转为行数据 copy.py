#coding=utf8
import xlrd
import pymongo

book = xlrd.open_workbook('连轧A405757500板形数据.xls')
sheet1 = book.sheet_by_index(0)
print("表单名：", sheet1.name)
print("行数：", sheet1.nrows)
print("列数：", sheet1.ncols)
mat_asc_data = {
    "_id" : "A405757500FLATNESS_MAP",
    "FLATNESS_MAP" : {
        "X":[],
        "SHAPE_FB_CH_1":[],
        "SHAPE_FB_CH_2":[],
        "SHAPE_FB_CH_3":[],
        "SHAPE_FB_CH_4":[],
        "SHAPE_FB_CH_5":[],
        "SHAPE_FB_CH_6":[],
        "SHAPE_FB_CH_7":[],
        "SHAPE_FB_CH_8":[],
        "SHAPE_FB_CH_9":[],
        "SHAPE_FB_CH_10":[],
        "SHAPE_FB_CH_11":[],
        "SHAPE_FB_CH_12":[],
        "SHAPE_FB_CH_13":[],
        "SHAPE_FB_CH_14":[],
        "SHAPE_FB_CH_15":[],
        "SHAPE_FB_CH_16":[],
        "SHAPE_FB_CH_17":[],
        "SHAPE_FB_CH_18":[],
        "SHAPE_FB_CH_19":[],
        "SHAPE_FB_CH_20":[],
        "SHAPE_FB_CH_21":[],
        "SHAPE_FB_CH_22":[],
        "SHAPE_FB_CH_23":[],
        "SHAPE_FB_CH_24":[],
        "SHAPE_FB_CH_25":[],
        "SHAPE_FB_CH_26":[],
        "SHAPE_FB_CH_27":[],
        "SHAPE_FB_CH_28":[],
        "SHAPE_FB_CH_29":[],
        "SHAPE_FB_CH_30":[],
        "SHAPE_FB_CH_31":[],
        "SHAPE_FB_CH_32":[]
    },
    "mat_no" : "A405757500",
    "theme" : "ASC_DATA",
    "time" : "2022-06-27T08:44:22"
}

if __name__ == "__main__":
    for i in range(1, 4921):
            row = sheet1.row(i)
            x = sheet1.cell_value(i, 0)
            # questions = questions.upper()
            # print(sheet1.cell_value(i, 0))
            mat_asc_data["FLATNESS_MAP"]["X"] = x
            for j in range(1, 33):
                y = sheet1.cell_value(i, j)
                str_col = "SHAPE_FB_CH_" + str(j)
                mat_asc_data["FLATNESS_MAP"][str_col].append(y)
                # print(y)
                # print(str_col)
                # print(mat_asc_data["FLATNESS_MAP"][str_col])
        # print(mat_asc_data)
    
    myclient = pymongo.MongoClient("mongodb://192.168.1.1:27017/")
    mydb = myclient["USTB_DB"]
    mycol = mydb["PLTCM1_ASC_DATA"]
    myquery = { "mat_no": "A405757500" }
    
    if mycol.find_one(myquery):
        print("存在")
        mycol.replace_one(myquery, mat_asc_data)
    else :
        print("不存在")
        x = mycol.insert_one(mat_asc_data) 
    print(x)