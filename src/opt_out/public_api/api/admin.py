from django.contrib import admin
from opt_out.public_api.api.models import URL, Submission

admin.site.register(URL)
admin.site.register(Submission)
