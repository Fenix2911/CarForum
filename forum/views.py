from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, Follow, Notification


class HomePageView(View):
    def get(self, request):
        return render(request, "forum/index.html", )

class RegisterUserView(View):
    def get(self, request):
        return render(request, "forum/register.html")

    def post(self, request):
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        CustomUser.objects.create_user(username=username, email=email, password=password)
        return redirect("login")

class ProfileView(DetailView):
    template_name = "forum/profile.html"
    model = CustomUser
    context_object_name = "profile"
    slug_field = "username"
    slug_url_kwarg = "username"


class SettingsView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "forum/settings.html")


class MostRatedCarsView(View):
    def get(self, request):
        return render(request, "forum/highlighted.html")


class LoginPageView(View):
    def get(self, request):
            return render(request, "registration/login.html")



class LogoutPageView(View):
        def get(self, request):
            logout(request)


class FollowUserView(LoginRequiredMixin, View):
    def post(self, request, user_id):
        user_to_follow = get_object_or_404(CustomUser, id=user_id)
        if request.user != user_to_follow:
            Follow.objects.get_or_create(follower=request.user, following=user_to_follow)
        return HttpResponseRedirect(reverse('profile', args=[user_id]))


class UnfollowUserView(LoginRequiredMixin, View):
    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
        Follow.objects.filter(follower=request.user, following=user_to_unfollow).delete()
        return HttpResponseRedirect(reverse('profile', args=[user_id]))


class MarkNotificationAsReadView(LoginRequiredMixin, View):
    def post(self, request, notification_id):
        notification = get_object_or_404(Notification, id=notification_id, recipient=request.user)
        notification.is_read = True
        notification.save()
        return HttpResponseRedirect(reverse('notifications'))


class MarkAllNotificationsAsReadView(LoginRequiredMixin, View):
    def post(self, request):
        request.user.notifications_received.filter(is_read=False).update(is_read=True)
        return HttpResponseRedirect(reverse('notifications'))


class NotificationListView(LoginRequiredMixin, ListView):
    model = Notification
    template_name = "notifications.html"
    context_object_name = "notifications"

    def get_queryset(self):
        return self.request.user.notifications_received.all()
