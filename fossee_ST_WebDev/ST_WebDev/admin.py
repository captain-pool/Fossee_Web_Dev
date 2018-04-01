from django.contrib import admin
from .models import user,foss,tutorial_detail,payment

# Register your models here.
admin.site.register(user)
admin.site.register(foss)
admin.site.register(tutorial_detail)
admin.site.register(payment)
