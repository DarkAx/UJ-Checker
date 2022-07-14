#!/usr/bin/env python3
import requests; import smtplib
from time import sleep; from platform import platform; from os.path import exists,getsize
# ODUS Credentials
ID="YourID"; pwd_odus="YourODUSPassword" 
# Email Credentials
sender="OutlookEmail" # The sender email MUST be an outlook email, otherwise it won't work.
pwd_email="SenderEmailPassword" # sender email password
reciever="RecieverEmail" # any email in the world
# Printing the system and device information of whatever device execute this script 
info=platform()


def UJChecker(ID, pwd_odus):
    #Connecting to ODUS
    url="https://ssb.uj.edu.sa/banprod/twbkwbis.P_ValLogin" 
    url2="https://ssb.uj.edu.sa/banprod/ywsksinf.P_Display_All_Info"
    data_dict = {"sid": ID, "PIN": pwd_odus, "ButtonSelected":""}
    response_post = requests.post(url,data=data_dict,cookies=requests.get(url).cookies.get_dict())
    
    if response_post.status_code in range(200,300):
        print("Sucessfuly logged in..")
        response_get=requests.get(url2,cookies=response_post.cookies)
        
        if response_get.status_code in range(200,300):
            print("---------------------------------------------------------")
            # Checking if "cont.txt" is exist
            transcript=response_get.headers['Content-length']
            if exists("cont.txt"):

                file=open("cont.txt","r+")

                if file.read() == transcript:
                    file.close(); print("\nNot yet..\n")    #Checks if the page content length equals the old page content.
            
                elif getsize("cont.txt") == 0:  #If "con.txt" exists but it is null then it add the page content length to it.
                    file.close()
                    with open("cont.txt","w") as file:
                        file.write(transcript); print("\nNot yet..file was empty\n")
            
                else:
                    file.seek(0); return smtp(file,transcript)


            else:
                with open("cont.txt","w+") as file:
                    print("Seems it is your first time running the script or 'cont.txt' got deleted\n\nCopying the content length for next use...")
                    file.write(response_get.headers['Content-length'])  # Create "con.txt" and appends content length to it; if it wasn't created before.
                
           
        else:
            print("\nError\n",response_get+"\n\nYou can get more information about this error by editing this print function(line 54) to print(response_get.text)")
    else:
        print("\nError\n",response_post+"\n\nYou can get more information about this error by editing this print function(line 56) to print(response_post.text)")


def smtp(file,transcript): # Last step, which is sending the user an email informing him that the page got updated..
    global num, error, sender, pwd_email, reciever, info # Making them global variables to avoid errors.
    print("New update, GO!\n")
    print("---------------------------------------------------------\nSending you an email..")
    try:
        UJ = smtplib.SMTP('smtp.office365.com', 587)
        UJ.ehlo()
        UJ.starttls()
        UJ.ehlo()
        UJ.login(sender, pwd_email)
        UJ.sendmail(sender, reciever,"""/
Subject: New update!

Just wanted to tell you
the page got updated :)

This email has been sent
due to script execution from :"""+"\n\n"+info+"\n\nNumber of updates for today : "+str(num))
        print("\nEmail sent!")
    
    except smtplib.SMTPAuthenticationError:
        error=True
        print("\nSomething wrong happend.. probably your email or password is incorrect.")
    
    except (smtplib.SMTPServerDisconnected,smtplib.SMTPConnectError):
        error=True
        print("\nSomething wrong happend.. Check your connection.")

    
    else:
        file.close()
        with open("cont.txt","w") as file:
            file.write(transcript)
    
    if error:
        file.close(); num-=1

num=0
while True:
    error=False
    num+=1
    UJChecker(ID, pwd_odus)
    sleep(3600) #Wait 3600 seconds (1 hour) before re-entering the cycle

# It is recommended that you dont change the "time" function, so the university site doesn't block you or sender email get suspended.


#... Important notes ..


# * Do not edit the "cont.txt" as you might break this script


# * When you are done with this script, don't forget to delete "cont.txt" :

# ||File location||

# You might find it in

# - C:\Windows\System32\cont.txt

# - Python PATH


# ** Remember that "cont.txt" gets created WHEREVER the script get executed.
