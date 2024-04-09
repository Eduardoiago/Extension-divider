
<img src="https://i.ibb.co/mGyLsGC/title-extdividerpy.png" alt="title-extdividerpy" border="0">

#### Python script to optimize folder organization.

The Extension Divider project was developed in `python`. The script is used to organize a folder with many files, all the extensions in the selected folder are separated. Just add the path of the folder you want to organize and you're done! All the types of extensions that the folder contains will be organized. To organize your folder, simply add the PATH of the folder to the variable (path). Even with very full folders, the script works well, with a delay of 3 seconds for folders over 4GB. The script only separates extensions, folders do not change.

- ## Requirements:

``` python
    import os
    import shutil
```
The `os` library in Python provides an interface for interacting with the underlying operating system. It allows you to perform a variety of tasks related to the operating system, such as manipulating files, obtaining information about the execution environment, manipulating directories, among other things.

The `shutil` library in Python provides high-level operations for manipulating files and directories. It builds on the `os` library and offers more convenient, higher-level functions for performing common file manipulation tasks.

__________________________________________________________

## Explaining the code:

### Variables

``` python
    path = input("Enter path: ")
    files = os.listdir(path)
```

`path = input("Enter path: ")`: The value entered by the user is captured by the `input()` function and assigned to the `path` variable. The user must add the path to the folder they want to organize.

`os.listdir`: This part of the code uses the `listdir()` function of the `os` module in Python. This function returns a list of all the files and directories in the path specified as an argument.

`files = os.listdir(path)`: The result returned by the `os.listdir(path)` function is assigned to the `files` variable.

### Loop

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

**Loop `for`**: This code snippet starts with a `for` loop, which iterates over each element of the `files` list. For each iteration, the current file name is stored in the `file` variable.

**`os.path.splitext(file)`**: Inside the loop, the `os.path.splitext(file)` function is used to split the file name into two parts: the file name (stored in the `filename` variable) and the file extension (stored in the `extension` variable). For example, if `file` is "example.txt", `filename` will be "example" and `extension` will be ".txt".

**`extension = extension[1:]`**: Here, a modification is made to the extension. The original extension starts with a dot (e.g. ".txt"). This line removes that dot from the extension, leaving only the extension part (e.g. "txt"). This is done by assigning the variable `extension` a slice of the string `extension`, starting from the second character onwards.

**Checking the existence of the directory**: The line `if os.path.exists(path+'/'+extension):` checks whether a directory with the name of the current extension (`extension`) already exists. `os.path.exists()` is a function that returns `True` if the specified path exists in the file system, otherwise it returns `False`.

**Move file to existing extension directory**: If the directory for the current extension already exists, the current file is moved to that directory using `shutil.move()`. The file is moved from its original location to the new location, which is constructed by concatenating the `path`, the extension and the filename.

**Creating the directory if it doesn't exist**: If the directory for the current extension doesn't exist, the line `os.makedirs(path+'/'+extension)` creates that directory. `os.makedirs()` is a function that creates directories recursively.

**Move the file to the newly created directory**: After creating the directory, the file is moved to that directory in the same way as was done previously.

_In short, this code snippet goes through all the files in the `files` list, separates each file by its extension and moves these files to separate directories based on their extensions. If the directory corresponding to the extension already exists, the file is moved there; otherwise, the directory is created before moving the file._
__________________________________________________________

## Interface:

## Script demo video:
[![Alt text](https://img.youtube.com/vi/10ejjxfI_XE/0.jpg)](https://www.youtube.com/watch?v=10ejjxfI_XE)

## License
 * [MIT](LICENSE)

__________________________________________________________
