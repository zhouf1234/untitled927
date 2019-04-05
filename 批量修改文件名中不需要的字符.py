import os

"""用来实现删除特定广告文本的函数。

    该函数会搜索检查指定根目录下的所有文件以及子目录，如果子目录下依然
    存在子目录，则会一直查找下去，直到没有子目录为止。然后将目录名与文件
    名中含有的广告词进行删除。
    
    dir2 : str
        指定要检查的根目录。
    ad_text : str
        指定要删除的广告词。
"""

def remove_ad_text(dir2,ad_text):
    #判断传进来的dir2是否目录（文件夹）
    if not os.path.isdir(dir2):
        return
    #判断传进来的dir2末尾是否有路径分隔符，没有就加上
    # if not dir2.endswith(os.path.sep):
    #     dir2 += os.path.sep

    #获取dir2下所有文件和目录列表
    names = os.listdir(dir2)
    #遍历,出dir2下的文件名或目录名
    for name in names:
        # print(name)
        #拼接路径，得到dir2下的文件或目录的完整路径
        sub_path = os.path.join(dir2,name)
        # print(sub_path)
        #判断拼接的路径是不是目录，如果是，就调用本函数
        if os.path.isdir(sub_path):
            remove_ad_text(sub_path,ad_text)
        #如果不是目录，就执行替换文件名中不需要的字符
        name = name.replace(ad_text,'')
        #最后拼接文件路径，重命名操作
        new_path = os.path.join(dir2,name)
        os.rename(sub_path,new_path)
#调用函数，测试
remove_ad_text('C:\\Users\\admin\\PycharmProjects\\untitled927\\data3\\','有')