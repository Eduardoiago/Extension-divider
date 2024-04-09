
<img src="https://i.ibb.co/mGyLsGC/title-extdividerpy.png" alt="title-extdividerpy" border="0">

#### Python script to optimize folder organization.

The Extension Divider project was developed in `python`. The script is used to organize a folder with many files, all the extensions in the selected folder are separated. Just add the path of the folder you want to organize and you're done! All the types of extensions that the folder contains will be organized. To organize your folder, simply add the PATH of the folder to the variable (path). Even with very full folders, the script works well, with a delay of 2 seconds for folders over 4GB. The script only separates extensions, folders do not change.

- ## Requirements:

``` python
    import os
    import shutil
```
The `os` library in Python provides an interface for interacting with the underlying operating system. It allows you to perform a variety of tasks related to the operating system, such as manipulating files, obtaining information about the execution environment, manipulating directories, among other things.

The `shutil` library in Python provides high-level operations for manipulating files and directories. It builds on the `os` library and offers more convenient, higher-level functions for performing common file manipulation tasks.

#

## Explaining the code:

``` python
    path = input("Enter path: ")
    files = os.listdir(path)
```

`path = input("Enter path: ")`: O valor inserido pelo usuário é capturado pela função `input()` e atribuído à variável `path`. O usuário deve adicionar o caminho para a pasta de deseja organizar.


``` python
    for file in files:
        filename,extension = os.path.splitext(file)
        extension = extension[1:]
    
        if os.path.exists(path+'/'+extension):
            shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
        else:
            os.makedirs(path+'/'+extension)
            shutil.move(path+'/'+file, path+'/'+extension+'/'+file)    
```

__________________________________________________________



``` python
    path = input("      ➤  Enter path: ")
    files = os.listdir(path)
```


- ## Script demo video:
[![Alt text](https://img.youtube.com/vi/10ejjxfI_XE/0.jpg)](https://www.youtube.com/watch?v=10ejjxfI_XE)

## License
 * [MIT](LICENSE)
