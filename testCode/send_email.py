from mailer import Mailer

mail = Mailer(email='', password='')
mail.send(receiver='',
          subject='TEST',
          message='From Python!')
