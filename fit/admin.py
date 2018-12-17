from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Tips)

admin.site.register(Person)


admin.site.register(Cataegory_tips)
