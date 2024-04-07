
<img src="https://i.ibb.co/PZXGj8S/title-EXTD.jpg" alt="title-EXTD">

Python script to optimize folder organization.

#

<p>
The Extension Divider project was developed in python. The script is used to organize a folder with many files, all the extensions in the selected folder are separated, just add the path of the folder you want to organize and that's it! All the types of extensions the folder contains will be separated.
</p>

> <h2>Requirements:</h2>

```{r, engine='python', count_lines}
import os
import shutil
```
<p>To organize your folder, simply add the PATH of the folder to the input.</p>

```{r, engine='python', count_lines}
path = input("      ➤  Enter path: ")
files = os.listdir(path)
```

> <h4>Python script to organize extensions:</h4>

```{r, engine='python', count_lines}
for file in files:
    filename,extension = os.path.splitext(file)
    extension = extension[1:]

    if os.path.exists(path+'/'+extension):
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
    else:
        os.makedirs(path+'/'+extension)
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)    
```

> <h2>Script demo video:</h2>
[![Alt text](https://img.youtube.com/vi/10ejjxfI_XE/0.jpg)](https://www.youtube.com/watch?v=10ejjxfI_XE)
