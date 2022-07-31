# أداة بايثون لطلاب جامعة جدة | UJ Checker
### تقوم الأداة بالتحقق من أي تغيير يطرأ على صفحة "الإستعلام الأكاديمي الشامل" للطالب في موقع نظام الأودس وإرسال رسالة على بريده الإلكتروني في حال حدث هذا التغيير لإشعاره بذلك, مما يوفر عليه وقت دخول الموقع والتأكد من نزول الدرجات أو جدول المحاضرات إلخ..

### يمكنك تشغيل الأداة في كل مرة تفتح فيها جهازك وتركها تعمل أو بكل بساطة يمكنك جعلها تعمل 'بالخلفية' في كل مرة تشغل فيها جهازك, مما يوفر عليك الجهد, وسيتقدم شرح الطريقة وهي بسيطة.

### الشرح  التالي سيكون باللغة الإنجليزية.

### These are the variables that should get changed by you :
`ID , pwd_odus , sender , pwd_email , reciever`
### - Your University ID - Password for ODUS - Sender email (SHOULD BE OUTLOOK OTHERWISE IT WONT WORK), Password for email, Reciever email.
### You can put the sender email same as the reciever one.

## Install

### You should first download Python 3 if you don't have it, then you can install this tool by cloning or downloading the zip.

### After you install the script, if it was a zip file then extract it. then go to `cmd (Command prompt)` and write `pip install requests`
#### ^ This is a Python module which is required to run the script.

![173392174-fb911311-1f07-49a7-9cd4-60ae9f35d06d](https://user-images.githubusercontent.com/107263975/179049731-b5e4d74d-7dc7-4589-a29d-b1b358213b48.jpg)

### Now put your credentials in the first lines of the script in each variable ``ID``, ``pwd_odus``, ``sender``, ``pwd_email``, ``reciever``
### First time you execute the program in ``any text editor for code`` :

![173366188-09fe893a-19a7-428f-9b25-de734f79e95e](https://user-images.githubusercontent.com/107263975/179048972-0930a1ef-c61e-4199-b5bf-3069350fc9d1.jpg)

### If no updates to the page yet:

![173366212-806fc704-11c9-4d90-ae5a-58072919e238](https://user-images.githubusercontent.com/107263975/179048984-10878409-4dff-4fce-9242-9315701c13d7.jpg)

### If there was a new update to the page:

![173366749-8d602135-abaa-4812-9d67-c88de854a1f0](https://user-images.githubusercontent.com/107263975/179049021-86f30466-e837-408e-9350-f2130909929f.jpg)


## Tool in startup

### You can see that the program will be partially useless and boring if you need to run it manually everytime you turn on your PC, so what can we do then?

### To let the script run by itself everytime you turn on your PC background; then we will put it in ``Startup apps``, follow these steps carefully :

### Press ``Windows key + R`` , and write ``shell:startup`` then press ``OK``

![173373747-40a8b407-9cef-433c-ae56-d1465005e61f](https://user-images.githubusercontent.com/107263975/179049054-76a8e5e3-7b8c-45b3-b531-4bc141282a1f.jpg)

### You will be transferred to ``Startup apps folder``, so ``right click`` anywhere inside the folder and go to ``New`` then click on ``Shortcut``

![173373811-6ec15a5d-f3cc-48e5-9bc6-7f285b6651f1](https://user-images.githubusercontent.com/107263975/179049072-352ef025-b152-4ec2-982e-48055c54c76e.jpg)

### Now write the full path to the script: 

### ``pythonw C:\path\to\UJ.py`` 
#### ^ This is an example, you should put your own path.

![173373820-b71729dc-0b6a-4d64-b76a-346d4ed3037b](https://user-images.githubusercontent.com/107263975/179049089-0a43a166-034c-4646-9704-6f84cd90caae.jpg)


### Write anything you want but leave ``.exe`` at the end 

![173373828-816d979f-ce0f-47fa-ad01-c33708019b80](https://user-images.githubusercontent.com/107263975/179049118-0325afaf-4800-404f-8126-bb8578f7fb91.jpg)
### مبروك :) 


### From now on, the script will run in the background everytime you turn on your PC, and whenever it finds a change in the page it will send you an email telling you that, it will look like this :

![173410167-c3df70f0-330f-4c01-a122-c5e0d0daf056](https://user-images.githubusercontent.com/107263975/179050820-2520cc74-3042-47dd-9bdc-b20a4906bb19.png)


## Important notes

### Your sender email should be outlook ``@outlook.com`` or ``@uj.edu.sa`` or any other outlook

### Do not edit the `cont.txt` as you might break this script. ( It is a file that gets created to save the old `Content-Length` of the page to compare it to the new one)

### If you dont want this script anymore, don't forget to delete `"cont.txt"` :

#### You might find it in

#### - ``C:\Windows\System32\cont.txt``

#### - ``Python PATH``

#### - Any directory you have executed the script in

#### - Remember that `cont.txt` gets created WHEREVER the script get executed.



### There is a possibility that this tool get more updates.
# الحمد لله.
