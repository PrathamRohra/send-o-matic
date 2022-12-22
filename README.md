# SEND-O-MATIC
This project helps you send a whatsapp message to a bunch of users whose phone number is not saved on your phone. 
For example, I want to invite the people, who have registered for a particular event, to a group and I don't want to save their number just to send a group invite link and I also don't want to send that message to hunndreds of users manually. So, I can use Send-O-Matic to do the task for me.


### **Prerequisites**
- You should have Python and pip manager installed on your computer
- You should log-in at https://web.whatsapp.com prior to runninng this main.py file.
- Make sure the column having phone numbers is renamed to **Whatsapp**.  Name of the .csv file should be 'Whatsapp.csv'     
    > Note: It's case sensitive.
- Your browser should be opened in full-screen mode.
- The numbers in the .csv file should not be in international format.


### **Steps to use this project**
- Clone this repo using the following command:
  
  `git clone https:// `

- In the same directory where you have cloned this repo, add a new _.csv_ file.

- Then, in the terminal type:
  
  `pip install pywhatkit`

    > Note: If, while installing the pywhatkit library, it shows a flask-related error, type the following command `pip install flask`.

- Now, run the **main.py** file.
