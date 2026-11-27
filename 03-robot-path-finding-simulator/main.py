from robot import turn_left, turn_right, move_forward
x = 0
y = 0
direction = "North"

commands = input("Enter commands: ").strip().upper()

for command in commands:

    if command == "F":
        x,y,moved = move_forward(x,y,direction)
        if not moved:
            print("Warning: Grid boundary reached!")

    elif command == "L":
        direction = turn_left(direction)

    elif command == "R":
        direction = turn_right(direction)

    else:
        print("Warning: Unknown command:", command)
        continue

    print("Command: ",  command)
    print("Position: ", (x,y))
    print("Direction: ", direction)
    print("--------------------")

print("\nFinal Result")
print("Final Position:", (x, y))
print("Final Direction:", direction)



    


