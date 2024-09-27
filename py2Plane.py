"""
a collection of functions for movement in 2D coordinates
jesse.naumanen@tuni.fi
"""

def read_input(prompt, error_message="Incorrect input!"):
    """
    input check for floats
    :param prompt: prompt for input
    :param error_message: wrong input error message
    :return: float if possible, error message and prompt else.
    """  
    try:
        return float(input(prompt))

    except ValueError:
        print(error_message)
        return read_input(prompt, error_message)

def move_in_xy(start_x,start_y,new_x,new_y,movement_points):
    """
    movement function for 2D-coordinates
    :param start_x: x:n starting value of x
    :param start_y: y:n starting value of y
    :param new_x: planned value of x
    :param new_y: planned value of y
    :param movement_points: max distance able to move, movement points for example
    :return: maximum distance, new value of x, new value of y
    """
    
    change_x = new_x - start_x
    change_y = new_y - start_y

    if change_x == 0 and change_y == 0: #zero movement
        return movement_points, start_x, start_y

    planned_distance = (change_x**2+change_y**2)**0.5
    
    if movement_points >= planned_distance:
        distance_to_move = planned_distance
    else:
        distance_to_move = movement_points

    print(movement_points)
    movement_points = movement_points - distance_to_move
    print(movement_points)

    distance_x = (distance_to_move*change_x)/planned_distance
    distance_y = (distance_to_move*change_y)/planned_distance
    new_x = start_x + distance_x
    new_y = start_y + distance_y
    return movement_points, new_x, new_y

def movement_points_refill(max_movement_points, rest, movement_points):
    """
    movement_p refill function
    :param max_movement_points: max mp for player
    :param rest: the time to rest (1p / h)
    :param movement_points: current movement points
    :return: new movement points
    """
    movement_points = movement_points + rest
    if movement_points >= max_movement_points:
        return max_movement_points
    else:
        return movement_points

def menu():
    """
    menu function for movement, mp refill and exit
    :return: nothing
    """
    max_movement_points = read_input("How many movement points at max? ")
    movement_points = max_movement_points  # max points at start
    x = 0.0  # Current X coordinate of the player
    y = 0.0  # Current Y coordinate of the player

    while True:
        print("Coordinates x = {:.1f}, y = {:.1f}, "
              "{:.1f} movement points left.".format(x, y, movement_points))

        choice = input("1) Rest 2) Move 3) Quit\n-> ")

        if choice == "1":
            to_rest = read_input("How long to rest? ")
            movement_points = movement_points_refill(max_movement_points, to_rest, movement_points)
        
        elif choice == "2":
            new_x = read_input("x: ")
            new_y = read_input("y: ")
            movement_points, x, y = move_in_xy(x,y,new_x,new_y,movement_points)
        elif choice == "3":
            break
    print("Goodbye!")

#main for testing purposes
def main():
    print("This is py2Plane")
    menu()

if __name__ == "__main__":
    main()
