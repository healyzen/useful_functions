"""
256x256 LED-panel test
jesse.naumanen@tuni.fi
"""
from time import sleep
import random
#PANEL ARRANGEMENT
"""
         1
        ####
       #    #
       #    #
   2   #    #   3
       # 4  #
        ####
       #    #
       #    #
   5   #    #   6
       # 7  #
        ####
"""
numbers_l = {
    1 : [0,0,1,0,0,1,0],
    2 : [1,0,1,1,1,0,1],
    3 : [1,0,1,1,0,1,1],
    4 : [0,1,1,1,0,1,0],
    5 : [1,1,0,1,0,1,1],
    6 : [1,1,0,1,1,1,1],
    7 : [1,0,1,0,0,1,0],
    8 : [1,1,1,1,1,1,1],
    9 : [1,1,1,1,0,1,1],
}

array_size = [16,16]
array_width = array_size[0]
array_height = array_size[1]

empty_marker = "."
lit_marker = "o"
fill = 5 * empty_marker
double_lit = lit_marker + 4 * empty_marker + lit_marker

def horizontal_panel(value = 0):
    """
    this prints a horizontal panel of the 7 piece number display
    :param value: on or off value (1,0)
    :return: no return
    """
    if value == 1:
        print(f"{fill} {4 * lit_marker} {fill}")
    else:
        print(f"{array_width * empty_marker}")

def vert_panel(value = 1):
    """
    this prints the vertical sections of the 7 piece display
    :param value: value for display part 1,2,3
    :return:
    """
    if value == 1:
        for i in range(0,4):
            print(f"{2 * fill}{lit_marker}{fill}")

    elif value == 2:
        for i in range(0,4):
            print(f"{fill}{lit_marker}{2 * fill}")

    elif value == 3:
        for i in range(0,4):
            print(f"{fill}{double_lit}{fill}")

def print_number(number = 8):
    """
    this function prints a number using a 7 piece number display
    :param number:
    :return:
    """
    print(f"{array_width * empty_marker} \n{array_width * empty_marker}")
    panel_list = numbers_l[number]

    horizontal_panel(panel_list[0])

    vert_panel(2*panel_list[1]+panel_list[2])

    horizontal_panel(panel_list[3])

    vert_panel(2*panel_list[4]+panel_list[5])

    horizontal_panel(panel_list[6])

    print(f"{array_width * empty_marker}\n{array_width * empty_marker}\n{array_width * empty_marker}")


#main for testing purposes
def main():
    wait = 0.25
    prize = 3
    while True:
        number = random.randint(1,6)
        n = 0
        while n != number:
            n += 1
            print_number(n)
            sleep(wait)
        sleep(prize)

if __name__ == "__main__":
    main()
