from django.contrib import admin
from Blog.models import *

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(UserProfile)
admin.site.register(Log)
