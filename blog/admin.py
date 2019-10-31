from django.contrib import admin
from .models import Post, Author


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created', 'status')
    list_display_links = ('title',)
    list_filter = ('created', 'status')
    search_fields = ('title', 'body')
    ordering = ('status', 'created')
    prepopulated_fields = {'slug': ('title',)}


# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ('user', 'profile_picture')
#     list_display_links = ('user',)
#     search_fields = ('user',)


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
