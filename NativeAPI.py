import ctypes


def EnableHighDPISupport(root):
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
    scaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)
    root.tk.call('tk', 'scaling', scaleFactor/75)
    return scaleFactor
