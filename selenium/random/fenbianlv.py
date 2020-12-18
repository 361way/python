import win32api
dm = win32api.EnumDisplaySettings(None, 0)
dm.PelsHeight = 720
dm.PelsWidth = 1280
dm.BitsPerPel = 32
dm.DisplayFixedOutput = 0
win32api.ChangeDisplaySettings(dm, 0)