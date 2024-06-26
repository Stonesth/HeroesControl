from Tools import tools_v000 as tools
import os
from os.path import dirname
import keyboard
from keyboard import KEY_UP, KEY_DOWN, press, press_and_release
import time
from PIL import Image

# Mouse move
# https://automatetheboringstuff.com/chapter18/
import pyautogui

# -13 for the name of this project HeroesControl
save_path = os.path.dirname(os.path.abspath("__file__"))
# propertiesFolder_path = save_path + "/"+ "Properties"

# Example of used
# user_text = tools.readProperty(propertiesFolder_path, 'HeroesControl', 'user_text=')

def uppercase(enter):
    keyboard.press_and_release(KEY_UP)
    time.sleep(0.3)
    keyboard.press_and_release(KEY_UP)
    time.sleep(0.3)
    press('enter')
    time.sleep(0.3)
    press('enter')
    time.sleep(0.3)
    enter()

def enter():
    press('enter')
    time.sleep(0.3)
    press('enter')
    time.sleep(0.3)
    press('enter')
    time.sleep(0.3)

def switch_letter_number():
    keyboard.press_and_release(KEY_UP)
    time.sleep(0.3)
    keyboard.press_and_release(KEY_UP)
    time.sleep(0.3)
    keyboard.press_and_release(KEY_UP)
    time.sleep(0.3)
    press('enter')
    time.sleep(0.3)
    enter()

def and_commercial():
    keyboard.press_and_release(KEY_UP)
    time.sleep(0.3)
    press('enter')
    time.sleep(0.3)
    keyboard.press_and_release(KEY_UP)
    time.sleep(0.3)
    keyboard.press_and_release(KEY_UP)
    time.sleep(0.3)
    press('enter')
    time.sleep(0.3)
    keyboard.press_and_release(KEY_UP)
    time.sleep(0.3)
    enter()

def password_send():
    keyboard.press_and_release(KEY_UP)
    time.sleep(0.3)
    keyboard.press_and_release(KEY_UP)
    time.sleep(0.3)
    keyboard.press_and_release(KEY_UP)
    time.sleep(0.3)
    press('enter')
    time.sleep(0.3)
    keyboard.press_and_release(KEY_UP)
    time.sleep(0.3)
    keyboard.press_and_release(KEY_UP)
    time.sleep(0.3)
    enter()
    time.sleep(4)



def number_1():
    press('enter')
    time.sleep(1.3)
    press('enter')
    time.sleep(1.3)
    enter()

def number_3():
    press('enter')
    time.sleep(1.3)
    press('enter')
    time.sleep(1.3)
    keyboard.press_and_release(KEY_UP)
    time.sleep(1.3)
    keyboard.press_and_release(KEY_UP)
    time.sleep(1.3)
    enter()

def number_8():
    press('enter')
    time.sleep(1.3)
    keyboard.press_and_release(KEY_UP)
    time.sleep(1.3)
    keyboard.press_and_release(KEY_UP)
    time.sleep(1.3)
    press('enter')
    time.sleep(1.3)
    keyboard.press_and_release(KEY_UP)
    time.sleep(1.3)
    enter()

def number_9():
    press('enter')
    time.sleep(1.3)
    keyboard.press_and_release(KEY_UP)
    time.sleep(1.3)
    keyboard.press_and_release(KEY_UP)
    time.sleep(1.3)
    press('enter')
    time.sleep(1.3)
    keyboard.press_and_release(KEY_UP)
    time.sleep(1.3)
    keyboard.press_and_release(KEY_UP)
    time.sleep(1.3)
    enter()

def letter_e():
    time.sleep(1.3)
    keyboard.press_and_release(KEY_UP)
    press('enter')
    time.sleep(1.3)
    press('enter')
    time.sleep(1.3)
    keyboard.press_and_release(KEY_UP)
    time.sleep(1.3)
    keyboard.press_and_release(KEY_UP)
    time.sleep(1.3)
    enter()

def letter_h():
    time.sleep(1.3)
    keyboard.press_and_release(KEY_UP)
    time.sleep(1.3)
    press('enter')
    time.sleep(1.3)
    keyboard.press_and_release(KEY_UP)
    time.sleep(1.3)
    press('enter')
    time.sleep(1.3)
    keyboard.press_and_release(KEY_UP)
    time.sleep(1.3)
    keyboard.press_and_release(KEY_UP)
    time.sleep(1.3)
    enter()

def letter_o():
    time.sleep(1.3)
    keyboard.press_and_release(KEY_UP)
    time.sleep(1.3)
    press('enter')
    time.sleep(1.3)
    keyboard.press_and_release(KEY_UP)
    time.sleep(1.3)
    keyboard.press_and_release(KEY_UP)
    press('enter')
    time.sleep(1.3)
    keyboard.press_and_release(KEY_UP)
    time.sleep(1.3)
    keyboard.press_and_release(KEY_UP)
    time.sleep(1.3)
    enter()

def letter_p():
    time.sleep(1.3)
    press('enter')
    keyboard.press_and_release(KEY_UP)
    time.sleep(1.3)
    keyboard.press_and_release(KEY_UP)
    time.sleep(1.3)
    press('enter')
    time.sleep(1.3)
    keyboard.press_and_release(KEY_UP)
    time.sleep(1.3)
    keyboard.press_and_release(KEY_UP)
    time.sleep(1.3)
    keyboard.press_and_release(KEY_UP)
    time.sleep(1.3)
    enter()

def letter_r():
    time.sleep(1.3)
    keyboard.press_and_release(KEY_UP)
    press('enter')
    time.sleep(1.3)
    time.sleep(1.3)
    keyboard.press_and_release(KEY_UP)
    press('enter')
    time.sleep(1.3)
    enter()

def letter_s():
    time.sleep(1.3)
    keyboard.press_and_release(KEY_UP)
    time.sleep(1.3)
    keyboard.press_and_release(KEY_UP)
    press('enter')
    time.sleep(1.3)
    press('enter')
    time.sleep(1.3)
    keyboard.press_and_release(KEY_UP)
    time.sleep(1.3)
    enter()

def letter_t():
    time.sleep(1.3)
    press('enter')
    time.sleep(1.3)
    keyboard.press_and_release(KEY_UP)
    time.sleep(1.3)
    press('enter')
    time.sleep(1.3)
    keyboard.press_and_release(KEY_UP)
    time.sleep(1.3)
    enter()

def locateCenterOnScreen(name) :
    # Controle de selection
    pyautogui.move(1000,1000)
    while True: # loop because it could be the blue or pink Play button displayed at the moment.
        pos = pyautogui.locateCenterOnScreen(name)
        if pos is not None:
            break
    time.sleep(1)
    # print(pos)
    # print(pos[0] - (pos[0] / 2), pos[1] - (pos[1] / 2) )

    pyautogui.click(pos[0] - (pos[0] / 2), pos[1] - (pos[1] / 2) )

def activate_deactivate_controle() :
    locateCenterOnScreen('accessibility_8h36.png')
    locateCenterOnScreen('controle.png')

def activate_deactivate_controle_old() :
    # pyautogui.click(1030, 10, button='left')
    pyautogui.click(1005, 10, button='left')
    time.sleep(1)
    pyautogui.click(1005, 460, button='left')
    time.sleep(3)
    pyautogui.click(1005, 10, button='left')
    time.sleep(1)

def activate_control_devise() :
    locateCenterOnScreen('appareil.png')
    locateCenterOnScreen('iphone12.png')
    locateCenterOnScreen('connect.png')


def activate_control_devise_old() :
    pyautogui.click(820, 90, button='left')
    time.sleep(10)
    pyautogui.click(100, 90, button='left')
    time.sleep(3)
    pyautogui.click(100, 90, button='left')
    time.sleep(1)

def go_to_terminal() :
    pyautogui.click(500, 600, button='left')
    time.sleep(10)

def open_iphone12() :
    print('Open Iphone 12')
    
    # Need to stop the cursor
    print('Need to stop the cursor')
    keyboard.press_and_release(KEY_DOWN)
    keyboard.press_and_release(KEY_UP)

    # Menu
    print('Menu')
    keyboard.press_and_release(KEY_UP)
    time.sleep(1)
    keyboard.press_and_release(KEY_UP)
    time.sleep(1)
    press('enter')
    time.sleep(1)
    press('enter')
    keyboard.press_and_release(KEY_UP)
    time.sleep(1)
    press('enter')

    # Wait to display the password
    print('Wait to display the password')
    time.sleep(5)

    print('Enter the password')
    # Choose the upper key
    uppercase(enter)

    # letter P
    letter_p()

    # Switch_letter_number
    switch_letter_number()

    # Number 3
    number_3()

    # Number 3
    number_9()

    # Number 3
    number_8()

    # Number 3
    number_3()

    # Switch_letter_number
    switch_letter_number()

    # letter t
    letter_t()

    # letter h
    letter_h()

    # Switch_letter_number
    switch_letter_number()

    # Number 1
    number_1()

    # &
    and_commercial()

    # send the password
    password_send()
    print('END Open Iphone 12')

def open_iphone7() :
    print('Open Iphone 7')

    # Menu
    print('Open Iphone')
    press('esc')
    time.sleep(3)
    keyboard.press_and_release(KEY_UP)
    time.sleep(3)
    keyboard.press_and_release(KEY_UP)
    time.sleep(3)
    press('enter')
    time.sleep(3)
    keyboard.press_and_release(KEY_UP)
    time.sleep(3)
    press('enter')
    time.sleep(3)
    press('enter')
    time.sleep(3)

    
    print('END Open Iphone 7')

def open_search_application() :
    print('Search application')

    time.sleep(3)
    press('enter')
    time.sleep(3)
    press('enter')
    time.sleep(3)
    press('enter')
    time.sleep(3)
    keyboard.press_and_release(KEY_UP)
    time.sleep(3)
    press('enter')
    time.sleep(3)
    keyboard.press_and_release(KEY_UP)
    time.sleep(3)
    press('enter')
    time.sleep(3)

    print('End Search application')

def enter_search_string() :
    print('Enter the search string')
    
    print('Go to keyboard')
    keyboard.press_and_release(KEY_UP)
    time.sleep(3)

    print('Search the application Heroes')
    letter_h()
    letter_e()
    letter_r()
    letter_o()
    letter_e()
    letter_s()
    time.sleep(3)   

    print('End Enter the search string')

def select_application_heroes() :
    print('Select application Heroes')

    open_search_application()
    
    enter_search_string()


    print('Select the application')
    press('esc')
    time.sleep(1)
    keyboard.press_and_release(KEY_UP)
    time.sleep(1)
    keyboard.press_and_release(KEY_UP)
    time.sleep(1)
    enter()


    print('END Select application Heroes')

def select_application_heroes_old() :

    print('Select application Heroes')
    # Need to stop the cursor
    print('Need to stop the cursor')
    keyboard.press_and_release(KEY_DOWN)
    keyboard.press_and_release(KEY_UP)
    time.sleep(0.3)
    keyboard.press_and_release(KEY_UP)
    time.sleep(0.3)
    keyboard.press_and_release(KEY_UP)

    # Need to select the application
    print('Need to select the application')
    time.sleep(0.3)
    press('enter')
    time.sleep(0.3)
    # Select the line where is the folder with the game
    print('Select the line where is the folder with the game')
    keyboard.press_and_release(KEY_UP)
    time.sleep(0.3)
    keyboard.press_and_release(KEY_UP)
    time.sleep(0.3)
    press('enter')
    time.sleep(0.3)

    # Select the folder where are store the game
    print('Select the folder where are store the game')
    keyboard.press_and_release(KEY_UP)
    time.sleep(0.3)
    keyboard.press_and_release(KEY_UP)
    time.sleep(0.3)
    keyboard.press_and_release(KEY_UP)
    time.sleep(0.3)
    enter()

    # Select the game
    print('Select the game')
    time.sleep(1)
    press('enter')
    time.sleep(1)
    press('enter')
    time.sleep(1)
    press('enter')
    time.sleep(1)
    press('enter')
    time.sleep(1)
    press('enter')
    time.sleep(1)
    press('enter')
    time.sleep(1)

    # Wait to avoid problem with selector
    print('Wait to avoid problem with selector and the first connection')
    time.sleep(5)

    print('END Select application Heroes')

def wait_to_avoid_problem() :
    
    # Wait to avoid problem with selector
    print('Wait to avoid problem with selector and the first connection')
    time.sleep(5)
    press('esc')
    time.sleep(5)
    press('esc')
    time.sleep(5)
    press('esc')
    time.sleep(5)
    press('esc')
    time.sleep(5)
    press('esc')
    time.sleep(5)
    press('esc') 

def activate_BandeCurseur():
    # keyboard.press_and_release(KEY_UP)
    # time.sleep(1.3)
    press('enter')
    time.sleep(1.3)
    keyboard.press_and_release(KEY_UP)
    time.sleep(1.3)
    press('enter')
    time.sleep(1.3)
    keyboard.press_and_release(KEY_UP)
    time.sleep(1.3)
    press('enter')
    time.sleep(1.3)
    press('enter')
    time.sleep(1.3)
    press('esc')

def deactivate_BandeCurseur():
    keyboard.press_and_release(KEY_UP)
    time.sleep(1.3)
    keyboard.press_and_release(KEY_UP)
    time.sleep(1.3)
    keyboard.press_and_release(KEY_UP)
    time.sleep(1.3)
    keyboard.press_and_release(KEY_UP)
    press('enter')
    time.sleep(1.3)
    keyboard.press_and_release(KEY_UP)
    time.sleep(1.3)
    press('enter')
    time.sleep(1.3)
    keyboard.press_and_release(KEY_UP)
    time.sleep(1.3)
    press('enter')
    time.sleep(1.3)
    press('enter')
    time.sleep(1.3)
    press('esc')

def go_to_objectif():
    print('Go to objectif')
    go_to_position(3.5, 0.5, 1.8, 0.5)
    print('End of go to objectif')

def go_to_light():
    print('Go to light side')
    go_to_position(1.5, 1.5, 1.1, 1.1)
    print('End of light side')

def choose_second_tab():
    print('Go to choose_second_tab')
    go_to_position(0.8, 1.5, 0.3, 1.5)
    print('End of choose_second_tab')

def slide_screen() :
    print ("Begin slide_screen")
    press('enter')
    time.sleep(1)
    press('enter')
    time.sleep(1)
    press('enter')
    time.sleep(1)
    press('enter')
    time.sleep(1)

    print ("choose the option move")
    press('enter')
    time.sleep(1)
    keyboard.press_and_release(KEY_UP)
    time.sleep(1)
    press('enter')
    time.sleep(1)
    press('enter')
    time.sleep(1)
    keyboard.press_and_release(KEY_UP)
    time.sleep(1)
    press('enter')
    time.sleep(1)
    keyboard.press_and_release(KEY_UP)
    time.sleep(1)
    press('enter')
    time.sleep(1)
    keyboard.press_and_release(KEY_UP)
    time.sleep(1)
    keyboard.press_and_release(KEY_UP)
    time.sleep(1)
    keyboard.press_and_release(KEY_UP)
    time.sleep(1)
    press('enter')
    time.sleep(1)
    press('esc')
    time.sleep(1)

    print ("move the pointer where we want to slide")
    keyboard.press_and_release(KEY_UP)
    time.sleep(3)
    keyboard.press_and_release(KEY_UP)
    time.sleep(1)
    keyboard.press_and_release(KEY_UP)
    time.sleep(1)
    keyboard.press_and_release(KEY_UP)
    time.sleep(1)
    press('enter')
    time.sleep(1)
    press('enter')
    time.sleep(1)

    time.sleep(6)
    press('esc')
    print ("End slide_screen")

def go_to_take_daily_bonus():
    print('Select the Daily Bonus')
    time.sleep(5)
    go_to_position(3.5, 0.5, 1.6, 0.5)
    

def go_to_Ancien_Ewok():
    print('Go to Ancien_Ewok')
    go_to_light()
    time.sleep(5)
    choose_second_tab()
    time.sleep(5)
    slide_screen()
    time.sleep(5)
    go_to_position(1.8, 1.1, 0.9, 0.4)
    time.sleep(5)
    go_to_position(3.6, 1.1, 1.6, 0.4)
    time.sleep(5)

def go_to_Chargements_first():
    print('Go to Chargements 1')
    time.sleep(1)
    go_to_position(1.5, 1.1, 0.8, 0.4)
    time.sleep(1)
    go_to_position(2, 1.0, 1.5, 0.4)
    time.sleep(1)
    go_to_position(0.5, 0.5, 0.5, 0.5)

def go_to_Chargements_second():
    print('Go to Chargements 2')
    time.sleep(1)
    go_to_position(2, 1.1, 0.8, 0.4)
    time.sleep(1)
    go_to_position(2, 1.0, 1.5, 0.2)
    time.sleep(1)
    go_to_position(0.5, 0.5, 0.5, 0.5)
    
def go_to_Chargements_third():
    print('Go to Chargements 3')
    time.sleep(1)
    go_to_position(2.8, 1.0, 0.8, 0.4)
    time.sleep(1)
    go_to_position(1.8, 1.0, 1.5, 0.2)
    time.sleep(1)
    go_to_position(0.5, 0.5, 0.5, 0.5)

def go_to_Chargements_fourst():
    print('Go to Chargements 4')
    time.sleep(1)
    go_to_position(1.5, 1.1, 1.5, 0.4)
    time.sleep(1)
    go_to_position(2, 1.0, 1.5, 0.2)
    time.sleep(1)
    go_to_position(0.5, 0.5, 0.5, 0.5)

def go_to_Chargements():
    print('Go to Chargements')
    time.sleep(1)
    go_to_position(1.8, 1.1, 0.7, 0.2)
    if (True):
        time.sleep(1)
        go_to_Chargements_first()
        time.sleep(1)
        go_to_Chargements_second()
        time.sleep(1)
        go_to_Chargements_third()
        time.sleep(1)
        go_to_Chargements_fourst()

    print('Close the Chargements')
    time.sleep(1)
    go_to_position(3.0, 1.3, 0.3, 0.4)

def go_to_Boutique():
    print('Go to Boutique')
    time.sleep(1)
    go_to_position(2.4, 1.0, 0.7, 0.4)
    # Select the Bronzium
    time.sleep(1)
    go_to_position(0.5, 0.5, 1, 0.5)
    # Select the button gratuit
    time.sleep(1)
    go_to_position(3.5, 0.5, 1.7, 0.5)
    # Select Terminer
    time.sleep(1)
    go_to_position(3.5, 0.5, 1.7, 0.7)

def go_to_selectionner_une_bataille():
    time.sleep(1)
    go_to_position(3.5, 0.5, 1.6, 0.5)

def go_to_Combattre():
    print('Go to Combattre button')
    time.sleep(1)
    go_to_position(3.5, 0.5, 1.8, 0.5)
    # To wait the load of the game
    time.sleep(3)
    go_to_position(1, 1, 1, 1)

def go_to_select_team():
    # Selectionner l'escouade
    print('Selectionner l escouade')
    time.sleep(1)
    go_to_position(2.5, 0.5, 1.8, 0.5)
    # Selectionner Par défaut
    print('Selectionner Par défaut')
    time.sleep(1)
    go_to_position(0.5, 0.3, 0.8, 0.5)
    # Select the team
    print('Select the team')
    time.sleep(1)
    go_to_position(3.5, 0.5, 1.0, 0.5)

def go_to_auto():
    print('Select the button auto')
    time.sleep(3)
    go_to_position(0.8, 0.5, 0.3, 0.5)

def wait_task(timer):
    for i in range(timer):
        time.sleep(1)
        go_to_position(0.7, 0.7, 0.7, 0.7)
        print(i)

def go_to_1_rewards():
    time.sleep(1)
    go_to_position(1.7, 0.5, 1.2, 0.5)

def go_to_2_rewards():
    time.sleep(1)
    go_to_position(1.8, 0.5, 1.4, 0.5)

def go_to_3_rewards():
    time.sleep(1)
    go_to_position(1.6, 0.5, 0.9, 0.5)

def go_to_4_rewards():
    time.sleep(1)
    go_to_position(1.6, 0.5, 1.1, 0.5)

def go_to_5_rewards():
    time.sleep(1)
    go_to_position(1.8, 0.5, 1.4, 0.5)

def go_to_6_rewards():
    time.sleep(1)
    go_to_position(1.6, 0.6, 0.9, 0.5)

def go_to_7_rewards():
    time.sleep(1)
    go_to_position(1.6, 0.5, 1.1, 0.5)

def go_to_8_rewards():
    time.sleep(1)
    go_to_position(1.8, 0.5, 1.4, 0.5)

def go_to_9_rewards():
    time.sleep(1)
    go_to_position(1.8, 0.5, 0.9, 0.5)

def go_to_10_rewards():
    time.sleep(1)
    go_to_position(1.6, 0.5, 1.1, 0.5)

def go_to_continuer():
    time.sleep(1)
    go_to_position(2, 0.5, 1.6, 0.5)

def go_to_Batailles_Galactiques():
    print('Go to Batailles Galactiques')
    time.sleep(1)
    go_to_position(3.2, 1.0, 0.7, 0.4)
    # Select the button PARTICIPER
    time.sleep(1)
    go_to_position(1.5, 0.4, 1.7, 0.4)
    # Select the button RECOMMENCER
    if (True):
        time.sleep(1)
        go_to_position(1.4, 0.5, 1.8, 0.5)

        # Confirmation
        time.sleep(1)
        go_to_position(2.5, 0.5, 1.2, 0.5)
    
    if (True):
        print('Combat 1')
        go_to_selectionner_une_bataille()
        go_to_select_team()
        go_to_Combattre()
        go_to_auto()
        wait_task(12)
        go_to_1_rewards()
        go_to_continuer()

    if (True):
        print('Combat 2')
        go_to_selectionner_une_bataille()
        go_to_select_team()
        go_to_Combattre()
        go_to_auto()
        wait_task(12)
        go_to_2_rewards()
        go_to_continuer()

    if (True):
        print('Combat 3')
        go_to_selectionner_une_bataille()
        go_to_select_team()
        go_to_Combattre()
        go_to_auto()
        wait_task(15)
        go_to_3_rewards()
        go_to_continuer()

    if (True):
        print('Combat 4')
        go_to_selectionner_une_bataille()
        go_to_select_team()
        go_to_Combattre()
        go_to_auto()
        wait_task(15)
        go_to_4_rewards()
        go_to_continuer()

    if (True):
        print('Combat 5')
        go_to_selectionner_une_bataille()
        go_to_select_team()
        go_to_Combattre()
        go_to_auto()
        wait_task(15)
        go_to_5_rewards()
        go_to_continuer()

    if (True):
        print('Combat 6')
        go_to_selectionner_une_bataille()
        go_to_select_team()
        go_to_Combattre()
        go_to_auto()
        wait_task(15)
        go_to_6_rewards()
        go_to_continuer()

    if (True):
        print('Combat 7')
        go_to_selectionner_une_bataille()
        go_to_select_team()
        go_to_Combattre()
        go_to_auto()
        wait_task(20)
        go_to_7_rewards()
        go_to_continuer()

    if (True):
        print('Combat 8')
        go_to_selectionner_une_bataille()
        go_to_select_team()
        go_to_Combattre()
        go_to_auto()
        wait_task(20)
        go_to_8_rewards()
        go_to_continuer()
    
    if (True):
        print('Combat 9')
        go_to_selectionner_une_bataille()
        go_to_select_team()
        go_to_Combattre()
        go_to_auto()
        wait_task(20)
        go_to_9_rewards()
        go_to_continuer()

    if (True):
        print('Combat 10')
        go_to_selectionner_une_bataille()
        go_to_select_team()
        go_to_Combattre()
        go_to_auto()
        wait_task(20)
        go_to_10_rewards()
        go_to_continuer()


def go_to_home_button() :
    print('Go to Home button')
    go_to_position(3.8, 1, 0.2, 0.4)
    print('End of Home button')

def go_to_deactivate_promotions():
    print('Go to deactivate promotions')
    time.sleep(1)
    go_to_position(3, 1.1, 0.4, 0.4)
    print('End of deactivate promotions')


def close_the_application():
    print('Begin close_the_application')

    press('enter')
    time.sleep(1)
    press('enter')
    time.sleep(1)
    keyboard.press_and_release(KEY_UP)
    time.sleep(1)
    press('enter')
    time.sleep(1)
    press('enter')
    time.sleep(1)
    press('enter')
    time.sleep(1)
    print('We are normally out the application')
    time.sleep(2)
    press('esc')
    time.sleep(1)
    press('enter')
    time.sleep(1)
    press('enter')
    time.sleep(1)
    press('enter')
    time.sleep(1)
    keyboard.press_and_release(KEY_UP)
    time.sleep(1)
    keyboard.press_and_release(KEY_UP)
    time.sleep(1)
    keyboard.press_and_release(KEY_UP)
    press('enter')
    time.sleep(1)
    press('enter')
    time.sleep(1)
    press('enter')
    time.sleep(1)
    press('esc')

    print('End close_the_application')

def go_to_position(X1, X2, Y1, Y2) :
    # print('Begin go_to_position')
    keyboard.press_and_release(KEY_UP)
    time.sleep(X1)

    keyboard.press_and_release(KEY_UP) 
    time.sleep(X2)

    keyboard.press_and_release(KEY_UP)
    time.sleep(Y1)

    keyboard.press_and_release(KEY_UP)
    time.sleep(Y2)
    keyboard.press_and_release(KEY_UP)
    time.sleep(0.4)
    press('enter')
    time.sleep(1)
    press('esc')
    time.sleep(1)
    # print('End go_to_position')





# Need to activate "Activer le contrôle de sélection"
# Préférence système
# check the check button to activate 
print('Activation of the control')
activate_deactivate_controle()
activate_control_devise()

# Go to the terminal of the Visual Studio Code
go_to_terminal()



if (True) :
    open_iphone12()
else :
    open_iphone7()

select_application_heroes()

wait_to_avoid_problem()

# Need to activate "Bande-Curseur"
print('Need to activate "Bande-Curseur')
time.sleep(1.3)
activate_BandeCurseur()
time.sleep(1)


if (False) :
    go_to_deactivate_promotions()
    go_to_take_daily_bonus()
    go_to_home_button()

if (False):
    go_to_home_button()

if (False) :
    go_to_deactivate_promotions()
    # Need to execute this task at 7h at 13h and at 19h
    go_to_Chargements()
    time.sleep(1)
    go_to_home_button()

if (False):
    go_to_deactivate_promotions()
    # 10 times go to Boutique
    go_to_Boutique()
    time.sleep(1)
    go_to_home_button()
    time.sleep(1)
    go_to_deactivate_promotions()

if (False):
    time.sleep(1)
    go_to_Batailles_Galactiques()

    time.sleep(1)

if (False) :
    go_to_Ancien_Ewok()



time.sleep(1)


if (False):
    go_to_deactivate_promotions()
    go_to_home_button()


time.sleep(1)





time.sleep(1)


print('deactivate_BandeCurseur')
deactivate_BandeCurseur()

time.sleep(5)

close_the_application()

# End of the program
print('activate_deactivate_controle')
activate_deactivate_controle()
time.sleep(3)

# Go to the Run button (For testing only)
if (False) :
    pyautogui.click(1340, 70, button='left')
    time.sleep(1)


