import csv
import pywhatkit
import datetime

print('TO CLOSE THIS SCRIPT: Type CTRL+C in the Terminal')
msg = input('Enter the message that you want to send: ')

try: 
    with open('Whatsapp.csv', mode='r') as file:
        csv_reader = csv.DictReader(file)

        for line in csv_reader:
        #Saves current time in each iteration.
            time = datetime.datetime.now()
            hour = int(time.strftime('%H'))
            minutes = int(time.strftime('%M'))
            minutes += 1
        
        # Make sure the csv file has the column name 'Whatsapp'
            phone = '+91'+str(line['Whatsapp'])
        
        # Sending WA msg
            pywhatkit.sendwhatmsg(phone, msg, hour, minutes, 20, True, 5)
except Exception as e:
    print(e)