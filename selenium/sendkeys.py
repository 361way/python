import win32com.client
shell = win32com.client.Dispatch("WScript.Shell")
shell.Run("notepad")
shell.AppActivate("notepad")
shell.SendKeys("^o", 0) 
shell.SendKeys("^a", 0)
shell.SendKeys("^c", 0)
