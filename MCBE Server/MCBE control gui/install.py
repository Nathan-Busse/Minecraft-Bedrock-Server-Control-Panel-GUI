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

sys.exit()