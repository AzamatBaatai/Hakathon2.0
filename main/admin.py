from django.contrib import admin
from main.models import *


class ImageInLineAdmin(admin.TabularInline):
    model = Image
    fields = ('image',)
    max_num = 5

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [ImageInLineAdmin, ]



# Register your models here.
