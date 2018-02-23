from glob import glob
import os
import shutil

def check_img_num():
    '''检查文件夹中图片数量是否大于90'''
    i = 0
    my_dir0 = 'D:\\temp\\pic\\mm131'
    my_dirs = glob(os.path.join(my_dir0, '*'))
    for my_dir in my_dirs:
        page = len(glob(os.path.join(my_dir, '*')))
        if page > 90:
            print(page)
            i += 1
    if i < 1:
        print('没有大于90张图片的文件夹')

def check_num():
    '''核对文件夹中图片数量,并把数量不符的文件夹名打印出来'''
    my_dir0 = 'D:\\temp\\pic\\mm131'
    my_dirs = glob(os.path.join(my_dir0,'*'))
    print(len(my_dirs))            #文件夹总数
    for my_dir in my_dirs:
        my_dir1 = my_dir.split('\\')
        my_dir1 = my_dir1[-1]      #文件夹名
        my_dir2 = my_dir1[-2:]
        try:
            page = int(my_dir2)
        except:
            my_dir2 = my_dir2[-1]
            page = int(my_dir2)
        if page != len(glob(os.path.join(my_dir,'*'))):
            print(my_dir)

def del_files():
    '''删除图片数量不够的文件夹'''
    my_dir0 = 'D:\\temp\\pic\\mm131'
    my_dirs = glob(os.path.join(my_dir0, '*'))
    for my_dir in my_dirs:
        my_dir1 = my_dir.split('\\')
        my_dir1 = my_dir1[-1]  # 文件夹名
        my_dir2 = my_dir1[-2:]
        try:
            page = int(my_dir2)
        except:
            my_dir2 = my_dir2[-1]
            page = int(my_dir2)
        if page != len(glob(os.path.join(my_dir, '*'))):
            shutil.rmtree(os.path.join(my_dir))

if __name__ == '__main__':
    check_num()