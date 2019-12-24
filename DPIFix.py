import winreg
from os import path as ospath
from os import execl as osexecl
from sys import executable as sysex
from sys import argv as sysargv

if __name__ == '__main__':
    reg = winreg.ConnectRegistry(None,winreg.HKEY_CURRENT_USER)
    key = winreg.OpenKey(reg, r"Control Panel\Desktop\WindowMetrics")
    print(winreg.QueryValueEx(key, 'AppliedDPI'))
    filefound=True
    if winreg.QueryValueEx(key, 'AppliedDPI')[0]!=96:
        key.Close()
        key = winreg.OpenKey(reg, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Layers", 0, winreg.KEY_ALL_ACCESS)

        ##If testing from SHELL also add these values into registry. This is not needed for complied EXEs. Make sure the path is correct or it won't work.

        winreg.SetValueEx(key, 'C:\python35\pythonw.exe', 0, winreg.REG_SZ, 'HIGHDPIAWARE')
        winreg.SetValueEx(key, 'C:\python35\python.exe', 0, winreg.REG_SZ, 'HIGHDPIAWARE')

        ##If Testing from SHELL change YOUREXE.exe to YOURPYFILE.py, otherwise it should be the name of your compiled EXE.

        exepath=str(ospath.abspath('YourEXE.exe'))
        try:
            winreg.QueryValueEx(key, exepath)
        except:
            print('FileNotFound')
            winreg.SetValueEx(key, exepath, 0, winreg.REG_SZ, 'HIGHDPIAWARE')
            print(winreg.QueryValueEx(key, exepath))
            filefound=False
    print(filefound)
    key.Close()
    reg.Close()