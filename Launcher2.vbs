set objShell=wscript.createObject("wscript.shell")
iReturn=objShell.Run("cmd.exe /C python TkinterControlee.py", 0, TRUE)
