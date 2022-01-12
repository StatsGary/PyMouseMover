# PyMouseMover
A jiggler designed in Python to move your mouse to keep you active on your machine. 

The motivation for this is I work across three machines, so to prevent the screen from locking and me not showing as present on my socials I have designed this simple python script to be triggered in the terminal when you are away from your main machine. This has been designed on **Python 3.7.11** and works with that. It relies on internal base install libraries, so will work when installed on to any Python machine that has a base install and without the need to create a virtual environment. 

## Triggering the tool

```{python}
# Run this in the terminal
python MouseJiggle.py
```

Once triggered in the Terminal / Bash / Powershell or CMD the script will fire and you will see the mouse moving on your machine. The output will look as follows:


```{python}
Please specify a wait time integer? 5
--------------------------------------------------------------------------------
[INFO] action triggered by Gary.Hutson. About to move the mouse... 
Cursor moved to x: 25y: 383
[INFO Cursor has been moved.]
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
[INFO] action triggered by Gary.Hutson. About to move the mouse... 
Cursor moved to x: 454y: 193
[INFO Cursor has been moved.]
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
[INFO] action triggered by Gary.Hutson. About to move the mouse... 
Cursor moved to x: 343y: 499
[INFO Cursor has been moved.]
--------------------------------------------------------------------------------
-

```

The mouse will start to move and you can enjoy some peace and quiet. 

## Breaking out of the script

To break out of the script running in the terminal you need to press CTRL + C, which is the keyboard interrupt commands to exit the script. This works on every script from Python to R. When you do this you will receive an informative message saying that it has now terminated the script.

