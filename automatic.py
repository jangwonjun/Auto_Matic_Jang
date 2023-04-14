import pyautogui
import time
#반복
#화면 위치 세팅 1924 1040 기준
# Intro M : (0.0)~(514.1045) 
# Papago : (512.0)~(1040,1042)
#59 603 마이크 버튼 
print(pyautogui.position())

pyautogui.moveTo(60, 888)
pyautogui.click(button='left')
print("마이크로 이야기해보세요!")
time.sleep(7)
print("마이크 버튼 입력완료")
#203 413 글자 두번 클릭 복사
pyautogui.moveTo(158, 427)
pyautogui.click(clicks=3, button='left')
pyautogui.hotkey('ctrl', 'c')
print("글자복사완료1")
time.sleep(3)
pyautogui.moveTo(627, 238)
pyautogui.click(button='left')
pyautogui.hotkey('ctrl', 'v')
print("글자복사완료2")
time.sleep(3)
pyautogui.moveTo(548, 332)
pyautogui.click(button='left')
time.sleep(3)
print("tts 접근")
#초기화
pyautogui.moveTo(368, 543)
pyautogui.click(button='left')
pyautogui.hotkey('ctrl','f5')
time.sleep(1)
pyautogui.moveTo(993, 240)
pyautogui.click(button='left')
print("초기화 완료")


