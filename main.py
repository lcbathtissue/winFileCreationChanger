from datetime import datetime
import os, pywintypes, win32file, win32con

def changeFileCreationTime(fname, newtime):
    wintime = pywintypes.Time(newtime)
    winfile = win32file.CreateFile(
        fname, win32con.GENERIC_WRITE,
        win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE | win32con.FILE_SHARE_DELETE,
        None, win32con.OPEN_EXISTING,
        win32con.FILE_ATTRIBUTE_NORMAL, None)

    win32file.SetFileTime(winfile, wintime, None, None)

    winfile.close()


dt = datetime.today()  # Get timezone naive now
seconds = dt.timestamp()

text = str(seconds)

head, sep, tail = text.partition('.')

filePath = input("Please enter the name of the file [for example ' README.txt ']: ")
str(filePath)
print()
print("Times for file " + filePath + " have been set to now!")

times = int(head)
os.utime(filePath, (times, times))

changeFileCreationTime(filePath, times)