from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Car, Post, Like, Comment, Thread, ForumPost, Notification, Follow
# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'followers_count', 'following_count')
    search_fields = ('username', 'email')
    ordering = ('username',)
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('avatar', 'bio')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

# Rejestracja pozostałych modeli
admin.site.register(Car)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Thread)
admin.site.register(ForumPost)
admin.site.register(Notification)
admin.site.register(Follow)
