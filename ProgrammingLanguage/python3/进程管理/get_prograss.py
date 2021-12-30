import psutil

#查看cpu信息：
print(
    str(psutil.cpu_count(logical=False)) + "核" + str(psutil.cpu_count()) +
    "线程")

print(psutil.cpu_times())

psutil.test()
# 查看运行的进程
# pl = psutil.pids()

# for pid in pl:
#     print(str(pid) + " " + psutil.Process(pid).name())
