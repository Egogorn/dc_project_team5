from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


class StudentGroup(models.Model):
    name = models.CharField(default="", max_length=5)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=400)
    group = models.ManyToManyField(StudentGroup)

    def __str__(self):
        return self.name


class Profile(models.Model):
    name = models.CharField(max_length=50, default="Ivan")
    surname = models.CharField(max_length=50, default="Ivanov")
    group = models.ForeignKey(StudentGroup, on_delete=models.CASCADE, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_teacher = models.BooleanField(default=False)

    def __str__(self):
        return '%s %s' % (self.name, self.surname)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
