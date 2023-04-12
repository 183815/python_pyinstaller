import os

if __name__ == '__main__':
    while(True):
        try:
            mode=input("请输入你要安装的模块名称(版本)：")
            cmd=f'pip install {mode}'
            os.system(cmd)
            os.system("pause")
            os.system("cls")
        except:
            print("模块安装错误！请检查模块名称是否正确！")