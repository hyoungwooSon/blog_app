from django.contrib import admin
from .models import Post
# Register your models here.
#어드민페이지에서 보이게하려면 여따적음
admin.site.register(Post)