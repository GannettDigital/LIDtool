from django.contrib import admin
from lid.models import *

class ReporterAdmin(admin.ModelAdmin):
    pass
admin.site.register(Reporter, ReporterAdmin)


