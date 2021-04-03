import sys

X, Y = (0, 0)
count = ''
direction = 'North'


def right():
    global direction
    if direction == 'North':
        direction = 'East'
    elif direction == 'East':
        direction = 'South'
    elif direction == 'South':
        direction = 'West'
    elif direction == 'West':
        direction = 'North'


def left():
    global direction
    if direction == 'North':
        direction = 'West'
    elif direction == 'East':
        direction = 'North'
    elif direction == 'South':
        direction = 'East'
    elif direction == 'West':
        direction = 'South'


def walk():
    global count, X, Y, direction
    if count == '':
        return None

    if direction == 'North':
        Y += int(count)
    elif direction == 'East':
        X += int(count)
    elif direction == 'South':
        Y -= int(count)
    elif direction == 'West':
        X -= int(count)
    count = ''
    return None


command = ''
try:
    command = sys.argv[1].lower()
except:
    print('[-] Please enter a bot command.')
    exit(0)

for i in range(len(command)):
    if command[i] == 'r':
        walk()
        right()

    elif command[i] == 'l':
        walk()
        left()

    elif command[i] == 'w':
        walk()
        i += 1
        continue
    else:
        count += command[i]
if count != '':
    walk()


print(f'X: {X} Y: {Y} Direction: {direction}')
