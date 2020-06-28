from django.contrib import admin
from portfolio_app.models import Profile, Link, Bio_Point, Project_Post, About_Additional, Project_Subgroup
# Register your models here.
admin.site.register(Profile)
admin.site.register(Link)
admin.site.register(Bio_Point)
admin.site.register(Project_Post)
admin.site.register(About_Additional)
admin.site.register(Project_Subgroup)
