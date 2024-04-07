
<img src="https://i.ibb.co/PZXGj8S/title-EXTD.jpg" alt="title-EXTD">

### Python script to optimize folder organization.

<p>
The Extension Divider project was developed in python. The script is used to organize a folder with many files, all the extensions in the selected folder are separated. Just add the path of the folder you want to organize and you're done! All the types of extensions that the folder contains will be organized. 
</p>

- ## Requirements:

``` python
    import os
    import shutil
```
#

<p>To organize your folder, simply add the PATH of the folder to the variable (path). Even with very full folders, the script works well, with a delay of 2 seconds for folders over 4GB. The script only separates extensions, folders do not change.</p>

``` python
    path = input("      ➤  Enter path: ")
    files = os.listdir(path)
```

## Organizing files:

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

- ## Script demo video:
[![Alt text](https://img.youtube.com/vi/10ejjxfI_XE/0.jpg)](https://www.youtube.com/watch?v=10ejjxfI_XE)

## License
 * [MIT](LICENSE)
