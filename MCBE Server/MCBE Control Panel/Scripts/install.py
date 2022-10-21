import os
import sys


print('\033[2;32;43m Installing python packages...')	

os.system('cmd /c "pip install pathlib"')
os.system('cmd /c "pip install shutil"')
os.system('cmd /c "pip install re"')
os.system('cmd /c "pip install subprocess"')
os.system('cmd /c "pip install contextlib"')
os.system('cmd /c "pip install threading"')
os.system('cmd /c "pip install inspect"')
os.system('cmd /c "pip install requests"')
os.system('cmd /c "pip install pyautogui"')
os.system('cmd /c "pip install PySimpleGUI"')

dirname = os.path.dirname("Prepare")
file_path = 'c:/users/' + os.getlogin()
filename = os.path.join(dirname, file_path,'./Documents/MCBE Server/Server' )

os.mkdir(filename)

# mode
mode = 0o666
  
# Path
path = os.path.join(filename)
  
print("Directory '% s' created" )

sys.exit()