from django.contrib import admin
from django_comments.admin import CommentsAdmin

from .models import ImprovedComment

admin.site.register(ImprovedComment, CommentsAdmin)
