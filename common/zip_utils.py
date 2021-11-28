import os
import zipfile


def zip_dir(dir_path, zip_path):

    """
    :param dir_path: 源文件夹路径
    :param zip_path: 压缩后的文件夹路径
    :return:
    """
    zip = zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED)
    for root, dirnames, filenames in os.walk(dir_path):
        file_path = root.replace(dir_path, '')  # 去掉根路径，只对目标文件夹下的文件及文件夹进行压缩
        # 循环出一个个文件名
        for filename in filenames:
            zip.write(os.path.join(root, filename), os.path.join(file_path, filename))
    zip.close()


current_path = os.path.abspath(os.path.dirname(__file__))
dir_path = os.path.join(current_path, '..', 'reports/禅道UI自动化测试报告V1.3')
zip_path = os.path.join(current_path, '..', 'reports/禅道UI自动化测试报告.zip')
# for root, dirnames, filenames in os.walk(dir_path):
#     file_path = root.replace(dir_path, '')
#     print(file_path)
#     for filename in filenames:
#         print(filename)
#     print('------------------------')
if __name__ == '__main__':

    zip(dir_path, zip_path)
    print('111')

