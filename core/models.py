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
    maxPoints = models.IntegerField(default=-1)
    deadline = models.DateTimeField()
    def __str__(self):
        return self.name

    def groups(self):
        s = ""
        for x in StudentGroup.objects:
            if x in self.group:
                s += str(x) + ' '
        return s


class Profile(models.Model):
    name = models.CharField(max_length=50, default="Ivan")
    surname = models.CharField(max_length=50, default="Ivanov")
    father_name = models.CharField(max_length=50, default="Ivanovich")
    group = models.ManyToManyField(StudentGroup, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_teacher = models.BooleanField(default=False)

    def __str__(self):
        if not self.is_teacher and self.group.all() != []:
            return '%s %s %s %s' % (self.name, self.surname, self.father_name, self.group.all()[0])
        else:
            return '%s %s' % (self.name, self.surname)


class Solution(models.Model):
    task = models.ForeignKey(Task, on_delete=models.PROTECT)
    student = models.ForeignKey(Profile, on_delete=models.PROTECT)
    solution = models.FileField(blank=True)
    time = models.DateTimeField()
    file = models.FileField(blank=True)
    def __str__(self):
        return 'Решение %s от %s' % (self.task.name, self.student)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
