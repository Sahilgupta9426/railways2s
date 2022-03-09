import imp
from django.contrib import admin
from .models import ProfileFace, ppe, textdetaction
# Register your models here.
admin.site.register(ProfileFace)
admin.site.register(ppe)
admin.site.register(textdetaction)