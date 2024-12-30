from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Task

@receiver(post_save, sender=Task)
def send_task_notification(sender, instance, created, **kwargs):
    if created:  # Solo enviar correo cuando la tarea es nueva
        send_mail(
            subject='Nueva Tarea Creada',
            message=f'Se ha creado una nueva tarea: {instance.title}',
            from_email='jolurn7@gmail.com',
            recipient_list=[instance.user.email],
        )
