from django.contrib import admin
from trecapp.models import Track, Task,Researcher, Run

# Register the various models with the admin interface
admin.site.register(Track)
admin.site.register(Task)
admin.site.register(Researcher)
admin.site.register(Run)
