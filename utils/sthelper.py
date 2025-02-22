import time
from pymouse import PyMouse
from pykeyboard import PyKeyboard
import pyperclip
import csv
import os

m = PyMouse()
k = PyKeyboard()

def create_st_project(projectname,projectlocation,language,FileDirectory):
    time.sleep(3)  # 等待3秒，点开sourcetrail界面
    m.click(24, 34)  # 点击project
    time.sleep(0.5)  # 等待0.5秒让机器反应
    m.click(95, 60)  # 点击new project
    time.sleep(1)  # 等待1秒让机器反应进入第2个界面

    m.click(996, 314)  # 点击并输入projectname
    k.type_string(projectname)
    k.tap_key(k.enter_key)
    time.sleep(0.5)  # 等待0.5秒让机器反应
    m.click(1012, 345)  # 点击并输入projectlocation
    k.type_string(projectlocation)
    k.tap_key(k.enter_key)
    m.click(1202, 796)  # 点击add source group
    time.sleep(1)  # 等待1秒让机器反应进入第个3界面

    if language=='cpp':
        m.click(752, 347)  # 点击C++
        time.sleep(0.5)  # 等待0.5秒让机器反应
        m.click(881, 539)  # 点击C++ Empty Source Group
        time.sleep(1)  # 等待1秒让机器反应进入第个3界面
    elif language=='java':
        m.click(758, 425)  # 点击Java
        time.sleep(0.5)  # 等待0.5秒让机器反应
        m.click(1120, 411)  # 点击Java Empty Source Group
        time.sleep(1)  # 等待1秒让机器反应进入第个3界面
    elif language=='python':
        m.click(747, 464)  # 点击Python
        time.sleep(0.5)  # 等待0.5秒让机器反应
        m.click(900, 416)  # 点击Empty Python Source Group
        time.sleep(1)  # 等待1秒让机器反应进入第个3界面
    m.click(1194, 754)  # 点击next
    time.sleep(1)  # 等待1秒让机器反应进入第个4界面
    
    if language=='cpp':
        m.click(1340, 700)
    elif language == 'java':
        m.click(1344, 567)  # 点击edit小图标
    elif language == 'python':
        m.click(946, 381)   # Python executable path
        # Do not use this, this is too slow and will cause problems
        # k.type_string('C:\\Users\\ThisRabbit\\AppData\\Local\\Programs\\Python\\Python38\\')
        pyperclip.copy('C:\\Users\\ThisRabbit\\AppData\\Local\\Programs\\Python\\Python38\\')
        k.press_keys([k.control_key, 'v'])
        time.sleep(3)   # Wait for path checking (will change coordinates of latter components)
        m.click(1344, 567)
    time.sleep(1)  # 等待1秒让机器反应进入第个5界面
    
    m.click(770, 350)  # 点击File & Directories to Index进入第六个界面
    k.type_string(FileDirectory)
    k.tap_key(k.enter_key)
    time.sleep(0.5)  # 等待0.5秒让机器反应
    m.click(1167, 757)  # 点击save回到第五个界面
    time.sleep(1)  # 等待1秒让机器反应
    m.click(1344, 796)  # 点击create创建项目
    time.sleep(10)  # 等待10秒让机器反应
    m.click(882, 631)  # 点击cancel取消分析
    return

from_line = 85
end_line = 85

for lang in ['python']:
    project_names = []
    try:
        with open(f'../lists/{lang} project list final.csv', 'r', encoding='utf-8') as file:
            project_list = csv.reader(file)
            count = 0
            for row in project_list:
                if (count >= from_line) and (count <= end_line):
                    project_name = row[0].split("/")[-1]
                    project_names.append(project_name)
                count += 1
    except EnvironmentError:
        print('Error in reading csv file')

    for project_name in project_names:
        print(f'Creating SourceTrail DB on {project_name}, please get the window ready')

        try:
            os.remove(f'../out/sourcetrail/{project_name}.srctrlbm')
            os.remove(f'../out/sourcetrail/{project_name}.srctrldb')
            os.remove(f'../out/sourcetrail/{project_name}.srctrlprj')
            print(f'Removed old files for project {project_name}')
        except:
            print(f'Cannot find old files for project {project_name}')

        create_st_project(project_name, f'D:\\ASE2022\\UsabilityTest\\out\\sourcetrail', lang, f'D:\\ASE2022\\UsabilityTest\\repo\\{project_name}')
        print(f'Created {lang} project {project_name}')
