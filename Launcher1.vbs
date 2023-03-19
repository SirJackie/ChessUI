set objShell=wscript.createObject("wscript.shell")
iReturn=objShell.Run("cmd.exe /C python BridgeServer.py", 0, TRUE)
