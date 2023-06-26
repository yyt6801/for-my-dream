import random,os

RedList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]  
BlueList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]  
Red_Color = random.sample(RedList, 6)  #从list中随机获取5个元素，作为一个片断返回  
Blue_Color = random.sample(BlueList, 1)  #从list中随机获取5个元素，作为一个片断返回  
print (sorted(Red_Color),Blue_Color) 
os.system("pause")