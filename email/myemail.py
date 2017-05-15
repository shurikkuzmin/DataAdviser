import os
import smtplib
import csv
import time

#import mandrill
#mandrill_client = mandrill.Mandrill('YOUR_API_KEY')


# Note: See for docs
# https://docs.python.org/2/library/email-examples.html

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

text = """Dear {0},

We came across one of your articles about {1}. As people interested in visualization and data analysis, we created a tool that we think will help you as a journalist. It analyzes the text of your articles automatically, searches open databases, and presents the data it finds in a visual and explorable way. 

You can view our examples and submit your own articles at http://dataadviser.floatingpointlab.com to find out how you can enhance your readers' experience. Why not to try this opportunity today while we are still in a free beta stage?

We'd really appreciate any feedback from you, especially if our tool finds great data for your articles!

Thank you,

The DataAdviser team"""

#text = """Dear {0},
#
#We came across one of your articles about {1}.
#
#Thank you,
#
#The DataAdviser team"""

username = "dataadviser@floatingpointlab.com"
password = "datadvice20!%"
#username = "app30707192@heroku.com"
#password = "GSwv7PvxRCPIer5oPxIMVA"

##s = smtplib.SMTP('smtp.mandrillapp.com', 587)

s = smtplib.SMTP('smtpout.secureserver.net', 80)

s.login(username, password)


with open('Chicago_Tribune_3.csv','rU') as f:
    reader = csv.reader(f)
    for counter in range(0,53):
    	row  = reader.next()
        msgText = text.format(row[1],row[2])
    	msgHtml = "" # none for now

        print msgText
	
	    # plaintext message
        msg = MIMEText(msgText)

	    # multipart message    	
        #msg = MIMEMultipart('alternative')
        #part1 = MIMEText(msgText, 'plain') 
        #part2 = MIMEText(msgHtml, 'html')
    	#msg.attach(part1)
        #msg.attach(part2)
	
        msg['Subject'] = "tool for journalists"
        msg['From']    = "Alexandr Kuzmin <dataadviser@floatingpointlab.com>"
        msg['To'] = row[3]
    

        s.sendmail(msg['From'], msg['To'], msg.as_string())

        time.sleep(10)
    #for row in reader:
    #   print row[1], row[3]

s.quit()

