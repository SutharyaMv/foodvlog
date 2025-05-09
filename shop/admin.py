from django.contrib import admin
from . models import *
# Register your models here.
class categadmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    
admin.site.register(categ,categadmin)

class prodAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    list_display=['name','slug','price','stock','img']
    list_editable=['price','stock','img']
admin.site.register(products,prodAdmin)  