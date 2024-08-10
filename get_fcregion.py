import pyautogui as gui
from dotenv import load_dotenv
load_dotenv()

x=input("フレコ表示箇所の左上にカーソル合わせてEnterを押してください")
fc_region = gui.position()

print('以下を.envファイルに書き込んでください')
print('FCREGION_LEFT =', fc_region.x)
print('FCREGION_TOP =', fc_region.y)