
# EXTENSIONDIVIDER - Otimizador para organizar pastas.

import os
import shutil

print("""

      
    ██████████ █████ █████ ███████████  ▓█████▄  ██▓ ██▒   █▓ ██▓▓█████▄ ▓█████  ██▀███  
   ░░███░░░░░█░░███ ░░███ ░█░░░███░░░█  ▒██▀ ██▌▓██▒▓██░   █▒▓██▒▒██▀ ██▌▓█   ▀ ▓██ ▒ ██▒
    ░███  █ ░  ░░███ ███  ░   ░███  ░   ░██   █▌▒██▒ ▓██  █▒░▒██▒░██   █▌▒███   ▓██ ░▄█ ▒
    ░██████     ░░█████       ░███      ░▓█▄   ▌░██░  ▒██ █░░░██░░▓█▄   ▌▒▓█  ▄ ▒██▀▀█▄  
    ░███░░█      ███░███      ░███      ░▒████▓ ░██░   ▒▀█░  ░██░░▒████▓ ░▒████▒░██▓ ▒██▒
    ░███ ░   █  ███ ░░███     ░███       ▒▒▓  ▒ ░▓     ░ ▐░  ░▓   ▒▒▓  ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
    ██████████ █████ █████    █████      ░ ▒  ▒  ▒ ░   ░ ░░   ▒ ░ ░ ▒  ▒  ░ ░  ░  ░▒ ░ ▒░
   ░░░░░░░░░░ ░░░░░ ░░░░░    ░░░░░       ░ ░  ░  ▒ ░     ░░   ▒ ░ ░ ░  ░    ░     ░░   ░ 
                     
                               ♦ EXTENSIONDIVIDER™ version 1.0 ♦
      
    ======================================================================================
                  Welcome To ExtDivider! Organize your files by adding a path.      
    ======================================================================================
""")

path = input("      ➤  Enter path: ")
files = os.listdir(path)

for file in files:
    filename,extension = os.path.splitext(file)
    extension = extension[1:]

    if os.path.exists(path+'/'+extension):
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
    else:
        os.makedirs(path+'/'+extension)
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)    

print(' ')
print('    ======================================================================================')
print('                      ☑ You files have been successfully organized! ')
print('    ======================================================================================')
