from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Host)
admin.site.register(Visitor)
admin.site.register(VisitDetails)
admin.site.register(Event)
admin.site.register(EventVisitor)