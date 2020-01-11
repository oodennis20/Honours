from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    # profile_photo = models.ImageField(upload_to)
    bio = models.CharField(max_length=240, null=True)
    phone = models.PositiveIntegerField(default=0,max_length=10)
    project = models.ForeignKey(Projects,on_delete=models.CASCADE,null=True)

    def save_profile(self):
        self.save()

    @classmethod
    def get_profile(cls):
        profile = Profile.objects.all()

        return profile

class Projects(models.Model):
    posted_by = models.ForeignKey(User, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=100, null=True)
    # project_image = models.ImageField(upload_to='projects/',null=True)
    description = models.TextField(null=True)
    project_link = models.TextField(null=True)

    @classmethod
    def get_projects(cls):
        projects = Projects.objects.all()
        return projects

class Reviews(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    )
    project = models.ForeignKey(Projects)
    juror = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    rating = models.IntegerField(choices=RATING_CHOICES)

