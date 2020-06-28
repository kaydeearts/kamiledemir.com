from django.db import models
from django.urls import reverse
# Create your models here.

class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    profile_bio = models.TextField()

    def __str__(self):
        return "Main_Profile"

class Link(models.Model):
    link_image = models.ImageField(upload_to='link_image', blank=True)
    link_title = models.CharField(max_length=200)
    link_hyperlink = models.TextField()

    def __str__(self):
        return self.link_title

class Bio_Point(models.Model):
    category = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.category

class About_Additional(models.Model):
    category = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.category

class Project_Subgroup(models.Model):
    category = models.CharField(max_length=200) #Technical or Design
    title = models.CharField(max_length=200)
    title_visible = models.BooleanField(default=False)
    post_amount = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Project_Post(models.Model):
    category = models.CharField(max_length=200) #Technical or Design
    subgroup = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    skills = models.TextField()
    text = models.TextField()
    link = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='project_post_images', blank=True)

    def __str__(self):
        return self.title
