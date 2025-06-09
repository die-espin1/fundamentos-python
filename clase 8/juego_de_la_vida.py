import time
import os

def count_neighbords(env, x, y):
    l1 = [x-1, x, x+1]
    l2 = [y-1, y, y+1]
    for i in l1:
        for j in l2:
            if i == x and j ==y:
                continue
            if env[i][j] == 1:
                count += 1
    return count

def load_file():
    filepath = input("Ingresa la ruta del archivo: ")
    with open(filepath, 'r', encoding='utf-8') as archivo:
        lines = archivo.readlines()
    return lines

def set_environment(raw_file):
    env = []
    for line in raw_file:
        line = line.strip()
        env.append([int(c) for c in line])
    return env

def print_env(env):
    for row in env:
        for cell in row:
            if cell == 1:
                print('■', end='')
            else:
                print(' ', end='')
        print()

my_file = load_file()
env = set_environment(my_file)
print_env(env)

for generation in range(25):
    for i in range(1, len(env)-1):
        for j in range(1, len(env[0])-1):
            count = count_neighbords(env, i, j)
            if env[i][j] == 1:
                if count < 2 or count > 3:
                  env[i][j] = 0
                if count == 2 or count == 3:
                  env[i][j] = 1
            else:
                if count == 3:
                    env[i][j] = 1
                else:
                    env[i][j] = 0
                    
            
            
            

    
    