
from django.core.mail import send_mail

def send_email(destinataire):
    return  send_mail(
                "Finalisation d'un ticket",
                "Nous sommes heureux de vous annoncer que votre problème a été résolu. Vous pouvez a présent utiliser votre service sans problème.",
                "franklinfrost14@gmail.com",
                [destinataire],
                fail_silently=False
            )