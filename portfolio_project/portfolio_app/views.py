from portfolio_app.models import Profile, Link, Bio_Point, Project_Subgroup, Project_Post, About_Additional
from rest_framework import generics
from django.http import HttpResponse
from django.shortcuts import render, redirect


def index(request):
    profile_object = Profile.objects.order_by('profile_bio')
    bio_points_object = Bio_Point.objects.all()
    additional_points_object = About_Additional.objects.all()
    project_subgroup_object = Project_Subgroup.objects.all()
    project_post_object = Project_Post.objects.order_by('subgroup')
    link_object = Link.objects.all()
    technical_array = []
    design_array = []
    slideContent_number = {}
    for subgroup in project_subgroup_object:
        temp_array = []
        if subgroup.category == "Technical":
            if subgroup.title_visible:
                subgroup_header = {"title_visible": subgroup.title_visible, "title":subgroup.title}
                temp_array.append(subgroup_header)
            for post in project_post_object:
                if post.subgroup == str(subgroup):
                    temp_array.append(post)
                    post.post_num = subgroup.post_amount
            technical_array.append(temp_array)
        elif subgroup.category == "Design":
            if subgroup.title_visible:
                subgroup_header = {"title_visible": subgroup.title_visible, "title":subgroup.title}
                temp_array.append(subgroup_header)
            for post in project_post_object:
                if post.subgroup == str(subgroup):
                    temp_array.append(post)
                    post.post_num = subgroup.post_amount
            design_array.append(temp_array)
    projects = {"technical" : technical_array, "design": design_array}

    objects_dict = {"profiles":profile_object,
    "bio_points": bio_points_object,
    "additional_points": additional_points_object,
    "technical_projects": technical_array, "design_projects": design_array,
    "links": link_object,
    }
    return render(request, 'portfolio_app/index.html', context=objects_dict)

# Django REST API Framework
# # Profile
# class Profile_ListCreate(generics.ListCreateAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = Profile_Serializer
#
# # Link
# class Link_ListCreate(generics.ListCreateAPIView):
#     queryset = Link.objects.all()
#     serializer_class = Link_Serializer
#
# # BioPoint
# class BioPoint_ListCreate(generics.ListCreateAPIView):
#     queryset = Bio_Point.objects.all()
#     serializer_class = BioPoint_Serializer
#
# # Project
# class Project_ListCreate(generics.ListCreateAPIView):
#     queryset = Project_Post.objects.all()
#     serializer_class = Project_Serializer
