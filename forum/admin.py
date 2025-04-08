from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    CustomUser,
    Car,
    Post,
    Like,
    Comment,
    Thread,
    ForumPost,
    Notification,
    Follow,
)

# Register your models here.


class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "followers_count", "following_count")
    search_fields = ("username", "email")
    ordering = ("username",)
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("avatar", "bio")}),)


class CarAdmin(admin.ModelAdmin):
    list_display = ("brand", "model", "year", "horsepower", "owner")
    search_fields = ("brand", "model")
    ordering = ("brand", "model")


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "car", "post_date", "status")
    search_fields = ("title", "author__username", "car__brand", "car__model")
    ordering = ("-post_date",)


admin.site.register(CustomUser, CustomUserAdmin)

# Rejestracja pozostałych modeli
admin.site.register(Car, CarAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Thread)
admin.site.register(ForumPost)
admin.site.register(Notification)
admin.site.register(Follow)
