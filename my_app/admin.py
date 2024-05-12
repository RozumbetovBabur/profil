from django.contrib import admin

# Register your models here.
from .models import MessageChat
class MessageAdmin(admin.ModelAdmin):
    list_display = ['name','email','teme','message']

admin.site.register(MessageChat,MessageAdmin)