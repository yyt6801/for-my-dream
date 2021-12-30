import zipfile
def extract():
    zfile = zipfile.ZipFile('pojie.zip')  # 读取压缩包，如果用必要可以加上'r'
    f = open('10_million_password_list_top_100000.txt', 'r', encoding='UTF-8')
    for password in f.readlines():
        try:
            password.strip('\n')
            zfile.extractall(path='',pwd=password.encode('ascii'))
            print("当前压缩密码为：", password)
            break
        except Exception:
            # print('密码错误'+password)
            pass
    f.close()
    zfile.close()
if __name__=="__main__":
    extract()