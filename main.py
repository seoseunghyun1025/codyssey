print('Hello Mars')

f = open("mission_computer_main.log", 'r')

while True:
    line = f.readline()
    if not line: break  
    print(line)

f.close()