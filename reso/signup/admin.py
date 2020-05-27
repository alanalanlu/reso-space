from django.contrib import admin
from .models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    model=User
    list_display = ['name',"email","choosen","team"]
    def email(self,obj):
        return obj.email
    def choosen(self,obj):
        return obj.chosen
    def team(self,obj):
        return obj.team
    # def skills(self,obj):
    #     print(type(obj))
    #     return ", ".join([
    #         skill.languages for skill in obj.User.skills_set.all()
    #     ])
    
admin.site.register(User,UserAdmin)
admin.site.register(Skills)
#admin.site.register(Squad)

class UserInline(admin.TabularInline):
    model = User

class SquadAdmin(admin.ModelAdmin):
    inlines = [UserInline, ]

admin.site.register(Squad, SquadAdmin)

