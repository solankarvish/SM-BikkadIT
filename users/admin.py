from django.contrib import admin
from users.models import Registration

# Register your models here.

class Ragistration(admin.ModelAdmin):
    list_display = [
        'fname','mname','lname','email',
        'course','qualification','batch',
        'passingyear','mobnumber','dist'
        ]
admin.site.register(Registration,Ragistration)
