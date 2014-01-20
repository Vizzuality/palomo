from django.contrib import admin

from integration.models import *

admin.site.register(Release)
admin.site.register(Branch)
admin.site.register(User)
admin.site.register(Server)
admin.site.register(Ticket)
