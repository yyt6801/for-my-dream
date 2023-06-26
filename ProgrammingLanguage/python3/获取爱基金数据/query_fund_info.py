# 调用爱基金的http get请求，查询指定基金代码的基金信息：单位净值、
import requests
from USE_DB import DB  # 调用另一个python中的类和函数， from a import b    a.py不需要加.py

def get_fund_info(code):
    # 发送请求
    str = "https://fund.10jqka.com.cn/data/client/myfund/"
    str += code
    x = requests.get(str)
    x = x.json()

    # 返回网页内容
    print("基金代码 "+x["data"][0]["code"])
    print("基金名称 "+x["data"][0]["name"])
    print("单位净值 "+x["data"][0]["net"])
    print("基金类型 "+x["data"][0]["fundtype"])
    print("基金规模 "+x["data"][0]["asset"])
    print("成立日期 "+x["data"][0]["clrq"])
    print("基金管理人 "+x["data"][0]["orgname"])
    return x

def query_tb_fund_info(code):
    x = {}
    count = 0
    try:
        # with DB() as db:   通过调用DB()函数，把返回的数据给as后面的db
        with DB() as cursor:
            cursor.execute(
                '''select * from TB_FUND where code like '%'''+code+'''%' '''
            )
            # print(cursor)
            for rs in cursor:
                count = count+1
                print(rs)
                x = rs
                code = rs["code"]
                name = rs["name"]
                # 打印结果
                print ("name=%s,code=%s" % \
                    (name, code ))
    except:
        print("Error: unable to fetch data")
    return x

def insert_tb_fund_info(fund_info):
    # 打开数据库连接 connect("ip","用户名","密码","数据库名") 区分大小写

    # 使用cursor()方法创建一个游标对象 cursor
    with DB() as cursor:
        sql = "INSERT INTO qdm712457164_db.TB_FUND (code, name, shares, net, market_value, purchase_date, purchase_amount, net_profit, net_profit_rate, fund_manager, fund_type, fund_management_scale, fund_establishment_date) VALUES('%s', '%s', %s, %s, %s, '%s', %s, %s, %s, '%s', '%s', %s, '%s');" % \
        (fund_info["code"], fund_info["name"], fund_info["shares"], fund_info["net"], fund_info["market_value"], fund_info["purchase_date"], fund_info["purchase_amount"], fund_info["net_profit"], fund_info["net_profit_rate"], fund_info["fund_manager"], fund_info["fund_type"], fund_info["fund_management_scale"], fund_info["fund_establishment_date"])
        try:
            # 执行sql语句
            cursor.execute(sql)
        except:
            # 如果发生错误则回滚
            DB.rollback()
    return x

if __name__ == '__main__':

    code = '420102'
    
    # 从mysql中查该基金代码的信息
    x = query_tb_fund_info(code) 
    if len(x) ==0:
        print("mysql中未查到该基金")
        # 从爱基金中获取信息
        x = get_fund_info(code)
        print("从爱基金中查询该基金最新信息")
        # 保存基金信息到mysql
        x = x["data"][0]
        fund_info = {}
        fund_info["shares"] = 1000
        fund_info["purchase_date"] ='2023-02-27'
        fund_info["purchase_amount"] =1000
        
        fund_info["code"] =x["code"]
        fund_info["name"] =x["name"]
        fund_info["net"] =x["net"]
        fund_info["fund_manager"] =x["orgname"]
        fund_info["fund_type"] =x["fundtype"]
        fund_info["fund_management_scale"] =x["asset"]
        fund_info["fund_establishment_date"] = x["clrq"]
        print(fund_info["fund_establishment_date"])
        fund_info["market_value"] =  (float)(fund_info["shares"]) * (float)(fund_info["net"])
        fund_info["net_profit"] = (float)(fund_info["market_value"]) - (float)(fund_info["purchase_amount"])
        fund_info["net_profit_rate"] =(float)(fund_info["net_profit"]) / (float)(fund_info["purchase_amount"])
        print(fund_info)
        x = insert_tb_fund_info(fund_info) 
        print("保存该基金至mysql中完成")
    else:
        print(x)
    
    
    
    
    
