from django.contrib import admin
from django.contrib.admin.decorators import display


admin.site.site_header="DEATH MANAGEMENT SYSTEM"
admin.site.site_title="semitary mgt"
admin.site.index_title="Death mgt"
# Register your models here.
from .import models

@admin.register(models.Deceased)
class Deceasedadmin(admin.ModelAdmin):
    list_display=('id','surname','district','regdate','image','city','dateofdeath','nameofhospital')
    
@admin.register(models.burial)
class Burialadmin(admin.ModelAdmin):
    list_display=('id','place','region','district','county','subcounty','parish','village','comment')
