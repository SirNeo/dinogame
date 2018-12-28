### Dinosaurus Game

##### Install dependencies
````bash
pip install -r requierements.txt
````

Alternative:
````bash
pip install pygame
````

##### Run
````bash
py main.py
````


##### Build APK for Android
Install  python-for-android
````bash
pip install python-for-android
````

Check if the installation worked
````bash
python-for-android recipes
````
Alternative
````bash
p4a recipes
````

In Windows, do some changes in this library:
The sh dependency isn't supported in Windows. Install pbs instead.

Change in all files:
````python
import sh
````
to
````python
import pbs as sh
````

Change in all files:
````python
from os import uname
````
to
````python
from platform import uname
````

Modify toolchain.py, about line 25 remove the version check of sh
