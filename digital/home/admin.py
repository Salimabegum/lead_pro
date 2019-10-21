from django.contrib import admin

# Register your models here.

from .models import Register, Joining

admin.site.register(Register)
admin.site.register(Joining)
 