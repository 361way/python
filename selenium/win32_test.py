import win32gui
import win32con
 
def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))
 
if __name__ == "__main__":
    results = []
    top_windows = []
    win32gui.EnumWindows(windowEnumerationHandler, top_windows)
    for i in top_windows:
        if "notepad" in i[1].lower():
            print i[1]
            w3hd=win32gui.FindWindow(None,i[1])
            #win32gui.MoveWindow(w3hd, 50, 50, 300, 200, True)
            #0:hiddle 1:display  2:min   3:max 
            win32gui.ShowWindow(w3hd,1)
            #win32gui.ShowWindow(w3hd, win32con.SW_MAXIMIZE)

            '''
            win32gui.ShowWindow(i[0],5)
            win32gui.SetForegroundWindow(i[0])
            '''
            break
