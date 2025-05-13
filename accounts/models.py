from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    ROLE_CHOICES = [
        ('ADMIN',   'Administrativo'),
        ('LAVAGEM', 'Lavagem'),
        ('CAIXA',   'Caixa'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} – {self.get_role_display()}"

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Ao criar um User, já instanciamos um Profile vazio e sempre
    salvamos o profile ao salvar o usuário.
    """
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
