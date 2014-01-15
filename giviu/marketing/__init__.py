from django.core.mail import EmailMultiAlternatives
from django.template import Context
from django.template.loader import get_template
from django.conf import settings


def event_user_registered(email, name):
    '''This event triggers when the user registers.'''
    c = Context({'name': name})
    html_content = get_template('marketing_welcome.html').render(c)
    text_content = get_template('marketing_welcome.text').render(c)
    if settings.DEBUG:
        email = 'licorna@gmail.com'
    msg = EmailMultiAlternatives('Bienvenido a Giviu',
                                 text_content,
                                 settings.EMAIL_DEFAULT_FROM,
                                 [email])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


def event_user_buy_product_confirmation(email, **kwargs):
    '''This event gets triggered when the user buys a giftcard.
    At the same time he sees the Purchase Confirmation page.'''
    c = Context(kwargs)
    html_content = get_template('marketing_buy_confirmation.html').render(c)
    text_content = get_template('marketing_buy_confirmation.text').render(c)
    if settings.DEBUG:
        email = 'licorna@gmail.com'
    msg = EmailMultiAlternatives('Confirmacion de compra en Giviu',
                                 text_content,
                                 settings.EMAIL_DEFAULT_FROM,
                                 [email])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


def event_user_receives_product(email, **kwargs):
    '''This is the email a receiving users gets when he receives
    a giftcard indicating on how to proceed.'''
    c = Context(kwargs)
    html_content = get_template('marketing_giftcard.html').render(c)
    text_content = get_template('marketing_giftcard.text').render(c)
    if settings.DEBUG:
        email = 'licorna@gmail.com'
    msg = EmailMultiAlternatives('Has recibido una giftcard!',
                                 text_content,
                                 settings.EMAIL_DEFAULT_FROM,
                                 [email])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


def event_user_confirmation_sends_giftcard(email, **kwargs):
    '''This event triggers when a giftcard a users bought is send to
    the destination party.'''
    c = Context(kwargs)
    html_content = get_template('marketing_sender_notification.html').render(c)
    text_content = get_template('marketing_sender_notification.text').render(c)
    if settings.DEBUG:
        email = 'licorna@gmail.com'
    msg = EmailMultiAlternatives('Has enviado una giftcard!',
                                 text_content,
                                 settings.EMAIL_DEFAULT_FROM,
                                 [email])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


def event_merchant_notification_giftcard_was_bought(email, **kwargs):
    '''This event triggers when a users buys a giftcard. At the same time
    the user receives the Purchase Confirmation email, the merchant gets
    this email confirming a new Giftard was bought.'''
    c = Context(kwargs)
    html_content = get_template('marketing_merchant_notification.html').render(c)
    text_content = get_template('marketing_merchant_notification.text').render(c)
    if settings.DEBUG:
        email = 'licorna@gmail.com'
    msg = EmailMultiAlternatives('Has recibido una giftcard!',
                                 text_content,
                                 settings.EMAIL_DEFAULT_FROM,
                                 [email])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()