from django.contrib import admin
from .models import Posts, Article

# Register your models here.

class PostsAdmin(admin.ModelAdmin):
      list_display = ('fname','lname','phone','email','address')


class ArticleAdmin(admin.ModelAdmin):
      list_display = ('title','body','slug')



admin.site.register(Posts, PostsAdmin)
admin.site.register(Article, ArticleAdmin)
