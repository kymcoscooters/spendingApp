from django.contrib import admin

from .models import User, Receipt, Shop

admin.site.register(User)
admin.site.register(Receipt)
admin.site.register(Shop)
