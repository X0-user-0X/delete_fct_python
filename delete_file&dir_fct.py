import os
import shutil
from sys import argv


def delete_dir_file_fct(list_to_erase, current_file: bool = False) -> None:
    '''
    :param list_to_erase: list of string containing the path of all the file and directories to be deleted
    :param current_file: boolean, delete the current_file where the function is implemented. Default value: False
    :return:
    '''
    for file in list_to_erase:
        if os.path.isfile(file):
            os.remove(file)
        else:
            shutil.rmtree(file)

    if current_file == True:
        answer = input("Are you really sure that you want to erase the current running file?Y/N \n")
        if answer == "Y":
            os.remove(argv[0])


testList = []
delete_dir_file_fct(testList, True)