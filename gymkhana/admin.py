from django.contrib import admin

# Register your models here.
from gymkhana.models import * 

admin.site.register(Users)
admin.site.register(Diagrams)
admin.site.register(Challenges)
admin.site.register(Games)
