from flask import Flask, render_template, send_from_directory, url_for, request, redirect
import csv
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
#print(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def database_fun(data):
	with open("database.txt", mode="a") as database:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		file = database.write(f'\n{email}')

def database_csv(data):
	with open('database1.csv', newline='', mode='a') as database2:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		print(email)
		csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])

def send_to_my_email(data):
	userid = "3vardhanharsha3@gmail.com"
	pwd = "krishsai"
	email = EmailMessage()
	sender = data["email"]
	email['from'] = '3vardhanharsha3@gmail.com'
	email['to'] = '3vardhanharsha3@gmail.com'
	email['subject'] = data["subject"]
	email_msg = data["message"]
	email.set_content(f'This email has been sent by {sender} \n\n Email Content: {email_msg}')
	with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
		smtp.ehlo()
		smtp.starttls()
		smtp.login(userid, pwd)
		smtp.send_message(email)
	return 'Email sent to harsha..!! Will get back to you shortly :)'


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == "POST":
		data = request.form.to_dict()
		#database_csv(data)
		#print(data)
		send_to_my_email(data)
		return redirect('/thankyou.html')
	else:
		return 'something went wrong :( '