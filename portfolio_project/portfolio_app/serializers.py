from rest_framework import serializers
from .models import Profile, Project_Post, Link, Bio_Point

# Profile
class Profile_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('profile_pic', 'profile_bio')

# Link
class Link_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ('link_image', 'link_title', 'link_hyperlink')

# BioPoint
class BioPoint_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Bio_Point
        fields = ('category', 'text')

# Project_Post
class Project_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Project_Post
        fields = ('title', 'category', 'description', 'image', 'link')
