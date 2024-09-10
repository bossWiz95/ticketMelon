from datetime import datetime
import io
import os
from time import sleep

from selenium.webdriver.chrome.options import Options

from item import *
import cv2
import numpy as np
import winsound as sd

from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

'''
python.exe -m pip install --upgrade pip
pip install webdriver-manager
pip install opencv-python
pip install pyinstaller
'''

options = Options()
# options.add_argument("--disable-gpu")  # GPU 사용 안함
options.add_argument("--no-sandbox")  # 샌드박스 모드 비활성화
options.add_argument("--disable-dev-shm-usage")  # /dev/shm 사용 안함

# 불필요한 리소스 차단
prefs = {
    "profile.default_content_setting_values": {
        "images": 2,  # 이미지 로드 안 함
        "javascript": 2,  # 자바스크립트 로드 안 함
    }
}
# options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=options)
actions = ActionChains(driver)

# 사운드 크기와 지속시간 설정
soundVolume = comm.soundV
soundDuration = comm.soundD

mode = IU_ALL
dayArr = [comm.selSun, comm.dayConfirm]
account = dongbin
conName = "IU"
timeout = 0

def init(type1, type2, type3, type4):
    if type1 == "dongbin":       account = dongbin
    elif type1 == "luv":       account = luv

    if type2 == "sat":  dayArr[0] = comm.selSat
    elif type2 == "sun":  dayArr[0] = comm.selSun

    driver.get(mode.url)
    driver.implicitly_wait(5)

    # 로그인
    onClickBtn(login.loginBtn)
    onClickBtn(login.loginMelon)
    onSendKeys(login.loginId, account.id)
    onSendKeys(login.loginPwd, account.pwd)
    onClickBtn(login.loginSubmit)

    # 일자 선택
    onClickBtn(dayArr[0])
    onClickBtn(dayArr[1])

    # 새로운 팝업 대기
    sleep(15)

    # iframe 이동 (팝업으로)
    driver.switch_to.window(driver.window_handles[-1])
    iframe = driver.find_element(By.ID, 'oneStopFrame')
    driver.switch_to.frame(iframe)

    onClickBtn(mode.openSeat_V)
    onClickBtn(mode.openSeat_R)
    onClickBtn(mode.openSeat_S)
    onClickBtn(mode.openSeat_A)
    onClickBtn(mode.openSeat_B)

    # 좌표 체크(필요 시 사용)
    while False:
        chkXY()

    # 좌석여부 체크 후 미존재 시 새로고침
    for j in range(999999):
        if (datetime.now() - timeout).seconds > 5400:
            quit()

        if "V" in type3:
            for i in range(1, mode.zoneCount_V, 1):
                try:
                    onClickBtn(mode.zoneSelect_V1 + str(i) + mode.zoneSelect_V2)
                    getImage('V', type1, type2, type4)
                except Exception as e:
                    print(f"예외 발생: {e}")
                    break
        if "R" in type3:
            for i in range(1, mode.zoneCount_R, 1):
                try:
                    onClickBtn(mode.zoneSelect_R1 + str(i) + mode.zoneSelect_R2)
                    getImage('R', type1, type2, type4)
                except Exception as e:
                    print(f"예외 발생: {e}")
                    break
        if "S" in type3:
            # /html/body/div/div[2]/div[2]/div/div[1]/div/table/tbody/tr[6]/td/div/ul/li[7]
            if type1 == "dongbin":
                for i in range(5, 10, 1):
                    try:
                        onClickBtn(mode.zoneSelect_S1 + str(i) + mode.zoneSelect_S2)
                        getImage('S', type1, type2, type4)
                    except Exception as e:
                        print(f"예외 발생: {e}")
                        break
            else:
                for i in range(1, mode.zoneCount_S, 1):
                    try:
                        onClickBtn(mode.zoneSelect_S1 + str(i) + mode.zoneSelect_S2)
                        getImage('S', type1, type2, type4)
                    except Exception as e:
                        print(f"예외 발생: {e}")
                        break
        if "A" in type3:
            # /html/body/div/div[2]/div[2]/div/div[1]/div/table/tbody/tr[8]/td/div/ul/li[10]/span[1]
            if type1 == "smg":
                for i in range(1, mode.zoneCount_A, 1):
                    try:
                        onClickBtn(mode.zoneSelect_A1 + str(10) + mode.zoneSelect_A2)
                        getImage('A', type1, type2, type4)
                    except Exception as e:
                        print(f"예외 발생: {e}")
                        break
            else:
                for i in range(1, mode.zoneCount_A, 1):
                    try:
                        onClickBtn(mode.zoneSelect_A1 + str(i) + mode.zoneSelect_A2)
                        getImage('A', type1, type2, type4)
                    except Exception as e:
                        print(f"예외 발생: {e}")
                        break
        if "B" in type3:
            for i in range(6, 12, 1):
                try:
                    onClickBtn(mode.zoneSelect_B1 + str(i) + mode.zoneSelect_B2)
                    getImage('B', type1, type2, type4)
                except Exception as e:
                    print(f"예외 발생: {e}")
                    break


def getImage(data, nm, yo, cnt):
    a1, a2 = 0, 125  # 시작 좌표 (x1, y1)
    b1, b2 = 675, 615  # 끝 좌표 (x2, y2)

    driver.implicitly_wait(2)

    png = driver.get_screenshot_as_png()

    image = Image.open(io.BytesIO(png))
    cropped_image = image.crop((a1, a2, b1, b2))

    img_name = conName + '_' + nm + '_' + yo + '_' + cnt + '.png'
    cropped_image_path = os.path.join(r'C:\dev', img_name)
    cropped_image.save(cropped_image_path)
    cropped_image_cv = cv2.imread(cropped_image_path)
    if dayArr[0] == comm.selSat:
        if data == 'V':
            target_image_cv = cv2.imread(os.path.join(r'C:\dev', 'IU_V_0.png'))
        elif data == 'R':
            target_image_cv = cv2.imread(os.path.join(r'C:\dev', 'IU_R_0.png'))
        elif data == 'S':
            target_image_cv = cv2.imread(os.path.join(r'C:\dev', 'IU_S_0.png'))
        elif data == 'A':
            target_image_cv = cv2.imread(os.path.join(r'C:\dev', 'IU_A_0.png'))
        elif data == 'B':
            target_image_cv = cv2.imread(os.path.join(r'C:\dev', 'IU_B_0.png'))
    else:
        if data == 'V':
            target_image_cv = cv2.imread(os.path.join(r'C:\dev', 'IU_V_1.png'))
        elif data == 'R':
            target_image_cv = cv2.imread(os.path.join(r'C:\dev', 'IU_R_1.png'))
        elif data == 'S':
            target_image_cv = cv2.imread(os.path.join(r'C:\dev', 'IU_S_1.png'))
        elif data == 'A':
            target_image_cv = cv2.imread(os.path.join(r'C:\dev', 'IU_A_1.png'))
        elif data == 'B':
            target_image_cv = cv2.imread(os.path.join(r'C:\dev', 'IU_B_1.png'))

    found = False

    result = cv2.matchTemplate(cropped_image_cv, target_image_cv, cv2.TM_CCOEFF_NORMED)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    print(str(datetime.now()) + " : " + str(max_loc) + "[" + str(max_val) + "]")

    if max_val > 0.8:
        match_x = max_loc[0] + a1 + 3
        match_y = max_loc[1] + a2 + 3

        cropped_image_ed = np.array(cropped_image)
        target_image_ed = np.array(target_image_cv)
        c_rgb_image = cropped_image_ed[match_y - a2, match_x]
        t_rgb_value = target_image_ed[3, 3]

        print("[ " + str(c_rgb_image) + " ] - [ " + str(t_rgb_value) + " ]")

        if int(c_rgb_image[0]) != 244 and int(c_rgb_image[1]) != 244 and int(c_rgb_image[2]) != 244:
            if int(c_rgb_image[0]) != 221 and int(c_rgb_image[1]) != 221 and int(c_rgb_image[2]) != 221:
                if int(c_rgb_image[0]) != 227 and int(c_rgb_image[1]) != 227 and int(c_rgb_image[2]) != 227:
                    if int(c_rgb_image[0]) != 231 and int(c_rgb_image[1]) != 231 and int(c_rgb_image[2]) != 231:
                        if abs(int(c_rgb_image[0]) - int(t_rgb_value[2])) < 20 and abs(
                                int(c_rgb_image[1]) - int(t_rgb_value[1])) < 20 and abs(
                                int(c_rgb_image[2]) - int(t_rgb_value[0])) < 20:
                            # 마우스 커서를 매칭된 위치로 이동
                            actions.move_by_offset(match_x, match_y).click().perform()
                            found = True

    if found:
        onClickBtn(mode.seatConfirm)
        sd.Beep(soundVolume, soundDuration)
        setPayment()


def setPayment():
    sleep(7200)
    onSelValue(mode.ticketCnt, '1')
    onClickBtn(mode.ticketConfirm)
    driver.implicitly_wait(1)
    onSendKeys(mode.pay_num1, account.pNum_p1)
    onSendKeys(mode.pay_num2, account.pNum_p2)
    onSendKeys(mode.pay_num3, account.pNum_p3)
    onClickBtn(mode.pay_type)
    onSelValue(mode.pay_bank, '88')
    onClickBtn(mode.pay_tax)
    onClickBtn(mode.pay_agree)
    onClickBtn(mode.pay_confirm)


def onClickBtn(xPath):
    target = driver.find_element(By.XPATH, xPath)
    driver.execute_script('arguments[0].click();', target)


def onSendKeys(xPath, text):
    target = driver.find_element(By.XPATH, xPath)
    target.clear()
    target.send_keys(text)


def resetSeat():
    onClickBtn(mode.resetSeat)
    onClickBtn(mode.openSeat)
    driver.implicitly_wait(0.5)


def onSelValue(xPath, value):
    target = Select(driver.find_element(By.XPATH, xPath))
    target.select_by_value(value)


def chkXY():
    script = '''
                document.addEventListener('click', function(event) {
                    window.clickCoordinates = { x: event.clientX, y: event.clientY };
                });
            '''
    driver.execute_script(script)

    import time
    time.sleep(3)
    coordinates = driver.execute_script('return window.clickCoordinates;')

    if coordinates:
        print(f'Click coordinates: x={coordinates["x"]}, y={coordinates["y"]}')
    else:
        print('No click event detected or coordinates not found.')



if __name__ == "__main__":
    type1 = input("Enter account >> ")
    type2 = input("Enter day(sat, sun) >> ")
    type3 = input("Enter grade(VRSAB) >> ")
    type4 = input("Enter cnt >> ")
    timeout = datetime.now()

    # 받은 URL 파라미터를 main 함수에 전달합니다.
    init(type1, type2, type3, type4)

