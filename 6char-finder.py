import pyautogui
import dataclasses
import pyocr
import keyboard
import os
from dotenv import load_dotenv
load_dotenv()

@dataclasses.dataclass
class FCRegion:
    left: int = int(os.getenv('FCREGION_LEFT'))
    top: int = int(os.getenv('FCREGION_TOP'))
    width: int = 350
    height: int = 65

def fc_generate():
    # 画面からフレコを取得
    fc_img_path = 'screenshot_tmp.png'
    fc_region = (FCRegion.left, FCRegion.top, FCRegion.width, FCRegion.height)
    img = pyautogui.screenshot(fc_img_path, region=fc_region)
    tools = pyocr.get_available_tools()
    tool = tools[0]
    fc_str = tool.image_to_string(
        img,
        lang='eng',
        builder=pyocr.builders.TextBuilder(tesseract_layout=6)
    )

    fc_str = fc_str.lower()

    if len(fc_str) >= 7 or not fc_str:
        # fc_strが7文字以上の場合,フレコをリセット,Trueを返す
        pyautogui.click('reset-button.png')
        print('Skip:', fc_str)
        return True
    else:
        # 7文字未満ならフレコを設定して終了,Falseを返す
        pyautogui.click('done-button.png')
        print('Success!!\nYour friend code:', fc_str)
        return False

# main loop
while fc_generate():
    # qキーが押されたら終了
    if keyboard.is_pressed('q'):
        print('手動で終了されました')
        break
