from USE_DB import DB  # 调用另一个python中的类和函数， from a import b    a.py不需要加.py
if __name__ == '__main__':

    # with DB() as db:   通过调用DB()函数，把返回的数据给as后面的db
    with DB() as db:

        db.execute(
            '''select * from t'''
        )
        print(db)
        for i in db:
            print(i)
