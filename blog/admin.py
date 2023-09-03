from django.contrib import admin

from blog.models import Post, Category, Tag, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','category', 'title', 'description', 'create_dt')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name','description')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id','name')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # Comment model 에서 __str__ @property 메서드로 코멘트 내용 보여주기
    list_display = ('id','post', 'short_content','create_dt', 'update_dt')