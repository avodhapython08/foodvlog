from django.contrib import admin

# Register your models here.
from shop.models import categ,product

class categadmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}

admin.site.register(categ,categadmin)

class proadmin(admin.ModelAdmin):
    prepopulated_fields ={'slug':('name',)}
    list_display = ['name','slug','price','stock','img','available']
    list_editable = ['price','stock','img','available']

admin.site.register(product,proadmin)

