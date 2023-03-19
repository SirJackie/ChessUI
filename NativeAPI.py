import ctypes


def EnableHighDPISupport(root):
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
    scaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)
    root.tk.call('tk', 'scaling', scaleFactor/75)
    return scaleFactor


def GetScreenResolution():
    user32 = ctypes.windll.user32
    return user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
