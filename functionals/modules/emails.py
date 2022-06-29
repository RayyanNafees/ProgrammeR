
import smtplib
from email.message import EmailMessage
from imghdr import what
import os

class Send:
    '''
    Why to take the complex way? The Send context manager does all the mind boggling
    emailing for you which you might have to do as in PyDocs.
    Stop screwing through the hard way and enjoy the ease of Send(ing) emails.
    '''

    def __init__(self, From: 'email', to: 'email', subject = 'no title', server = 'localhost') -> None:
        '''
        Initialize your email info.
        Send to multiple recipients by seperating each address with a ',' .
        '''
        self.msg = EmailMessage()
        self.s = From
        self.r = to
        self.t = subject
        self.server = server

        self.msg['From'] = From
        self.msg['To'] = to
        self.msg['Subject'] = self.t


    def __enter__(self) -> 'msg':
        '''Returns the email object'''
        return self


    def sub(self, subject: str) -> None:
        '''Initialize the Subject/Title for your mail body.'''
        self.msg['Subject'] = subject

    title = sub


    def body(self, text: str) -> None:
        '''Use triple quoted strings for writing your email text.'''
        self.msg.set_content(text)


    def add_images(self, locations: list, subtitle = ''):
        '''Fetches the images from the supplied list of locations.'''
        for Img in locations:
            with open(Img, 'rb') as image:
                img = image.read()

            self.msg.add_attatchment(img, maintype = 'image', subtype = what(None, img))

        self.msg.preamble(subtitle)


    def add_img(self, src: str, caption = '') -> None:
        '''Attatches the image from the supplied source directory.'''
        add_images([src],caption)


    def add_html(self, script: str, resources: tuple) -> None:
        '''Provides your mail with the html script and the required supplied resources.
           Add your script in triple-quoted strings to secure its readability.'''
        from email.headerregitry import Address
        import email.utils

        cid = email.utils.make_msgid()
        self.msg['From'] = Address(self.s)
        self.msg['To'] = tuple(Address(url) for url in self.r.split(','))

        self.msg.add_alternative(script.format(asparagus_cid = cid[1:1], subtype = 'html'))
        # To be continued ...


    def get_contents_of(self, folder: dir = os.getcwd()) -> None:
        '''Attatch the entire contents from the supplied location of folder (directory).'''
        pass


    def __exit__(self, exc_type, exc_value, exc_trace) -> None:
        '''Sends the message using SMTP.'''
        try:
            with smtplib.SMTP(self.server) as sender:
                sender.send_message(self.msg)
        except ConnectionRefusedError:
            raise ConnectionError('Check your Internet connection! <server not found>.')


'''
import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS = 'my_address@example.comm'
PASSWORD = 'mypassword'

def get_contacts(filename):
    """
    Return two lists names, emails containing names and email addresses
    read from a file specified by filename.
    """
    
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails

def read_template(filename):
    """
    Returns a Template object comprising the contents of the 
    file specified by filename.
    """
    
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def main():
    names, emails = get_contacts('mycontacts.txt') # read contacts
    message_template = read_template('message.txt')

    # set up the SMTP server
    s = smtplib.SMTP(host='your_host_address_here', port=your_port_here)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # For each contact, send the email:
    for name, email in zip(names, emails):
        msg = MIMEMultipart()       # create a message

        # add in the actual person name to the message template
        message = message_template.substitute(PERSON_NAME=name.title())

        # Prints out the message body for our sake
        print(message)

        # setup the parameters of the message
        msg['From']=MY_ADDRESS
        msg['To']=email
        msg['Subject']="This is TEST"
        
        # add in the message body
        msg.attach(MIMEText(message, 'plain'))
        
        # send the message via the server set up earlier.
        s.send_message(msg)
        del msg
        
    # Terminate the SMTP session and close the connection
    s.quit()
    
if __name__ == '__main__':
    main()
'''
