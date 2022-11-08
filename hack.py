import time

left = 10

print("select website to attack")
hack = input('')
print("selected", hack)

hacked = 0

print("loading hack")
time.sleep(15)
print("hack loaded")
time.sleep(5)
print("hacking started")
time.sleep(10)

while hacked != 320000 :
    print("\033[38;5;10m"+"1101000010000110110001100000000101000011010011101110110000001")
    print("0100000111110101110101011010101011010000100100010010000010100000000")
    hacked += 1
print("success hack")

while left != 0 :
    print("after", left, "times you have auto exit")
    time.sleep(1)
    left -= 1
exit()