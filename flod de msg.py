import pyautogui, time
time.sleep(5)

while True:
    # Aqui você pode escrever a mensagem a ser enviada
    pyautogui.typewrite('Eu te AMOOOO')
    # Aqui você determina o intervalo no envio de uma mensagem e outra
    time.sleep(1)
    pyautogui.press('enter')