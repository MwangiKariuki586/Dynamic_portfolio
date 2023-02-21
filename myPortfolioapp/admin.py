from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Home)
admin.site.register(Profile)
admin.site.register(About)
# admin.site.register(Profile)
class skillsInline(admin.TabularInline):
    model   = Skills
    extra = 2
@admin.register(Category)
class categoryAdmin(admin.ModelAdmin):
    inlines = [skillsInline]
# admin.site.register(Skills)
admin.site.register(Portfolio)


class skillsInline(admin.TabularInline):
    model = Skills
    extra = 2