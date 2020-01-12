from django.db import models
from pyuploadcare.dj.models import ImageField
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    profile_photo = ImageField(blank=True,manual_crop='')
    bio = models.CharField(max_length=240, null=True)
    phone = models.PositiveIntegerField(default=0)
    
    def save_profile(self):
        self.save()

    @classmethod
    def get_profile(cls):
        profile = Profile.objects.all()

        return profile

class Project(models.Model):
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=100, null=True)
    project_image = ImageField(blank=True,manual_crop='')
    description = models.TextField(null=True)
    project_link = models.TextField(null=True)

    @classmethod
    def get_project(cls):
        projects = Project.objects.all()
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
    project = models.ForeignKey(Project, on_delete=models.CASCADE,null=True)
    juror = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    design = models.IntegerField(choices=RATING_CHOICES,null=True)
    usability = models.IntegerField(choices=RATING_CHOICES,null=True)
    content = models.IntegerField(choices=RATING_CHOICES,null=True)
    comment = models.CharField(max_length=200,null=True)

    @classmethod
    def get_reviews(cls):
        reviews = Reviews.objects.all()
        return reviews

