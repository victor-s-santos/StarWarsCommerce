from django.db.models import signals
from django.dispatch import receiver
from .models import Product
from django.contrib.auth.models import User
from django.core import mail

@receiver(signals.post_save, sender=Product)
def product_registered(sender, instance, created, **kwargs):
    users = User.objects.all()
    users_list = []
    for i in range(len(users)):
        users_list.append(users[i].email)
    if instance.product_name != '':
        message = f'A new product has been registered in Star Wars Commerce. Please, visit us to more news! The following product has been registered:{instance.product_name}!'
        mail.send_mail('Thank you to be our custommer^^',
                                message,
                                'victorsantos.py@gmail.com',#remetente
                                users_list #destinatário
                        )