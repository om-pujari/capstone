from django.core.mail import send_mail

send_mail(
    'Test Email from Django',
    'This is a test email!',
    'omgpujari@gmail.com',
    ['crazyom.666@gmail.com'],  # Replace with recipient's email
    fail_silently=False,
)
