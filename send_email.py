import sendgrid, os, yaml
from sendgrid.helpers.mail import Mail
from utils import open_config_file



def send_email():

    config = open_config_file()

    if not config:
        print('🚨 Error: Could not open the configurarion file')
        return None 
    
    try:

        api_key = config['sendgrid']['api_key']

        sg = sendgrid.SendGridAPIClient(api_key=api_key)
        message = Mail(
            from_email= 'noreply@ricardoracines.com',
            to_emails='ricardo.racinesb@gmail.com, mcervantes21@outlook.com',
            subject='Ya se como mandar correos usando mi dominio ricardoracines.com :)!',
            plain_text_content='This is another email from python :)',
            html_content='<strong style="color:DarkRed;"> This is the HTML content </strong>'
        )

        response = sg.send(message)
        print(f'Status code: {response.status_code}')
    
    except Exception as error:
        print(f'🚨 Error sending the email: {error}')