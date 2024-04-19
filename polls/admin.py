from django.contrib import admin

from .models import Article
from .models import Response
from .models import Profile

admin.site.register(Article)
admin.site.register(Response)
admin.site.register(Profile)