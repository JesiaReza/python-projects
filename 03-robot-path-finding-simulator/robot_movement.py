def turn_left(direction):

    if direction == "North":
        return "West"
    
    elif direction == "West":
        return "South"
    
    elif direction == "South":
        return "East"
    
    elif direction == "East":
        return "North"


def turn_right(direction):

    if direction == "North":
        return "East"
          
    elif direction == "East":
        return "South"
          
    elif direction == "South":
        return "West"
          
    elif direction == "West":
        return "North"

def move_forward(x,y,direction):

    x1 = x
    y1 = y

    if direction == "North":
        y1 += 1

    elif direction == "South":
        y1 -= 1

    elif direction == "East":
        x1 += 1

    elif direction == "West":
        x1 -= 1

    if 0<= x1 <= 4 and 0<= y1 <= 4:
        return x1,y1,True

    else:
        return x,y,False
