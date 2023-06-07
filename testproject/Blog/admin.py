from django.contrib import admin
from Blog.models import *


admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)