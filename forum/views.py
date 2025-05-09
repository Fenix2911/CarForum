from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *
from .forms import RegistrationForm


class HomePageView(ListView):
    model = Post
    template_name = "forum/index.html"
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        latest_post = Post.objects.order_by("-post_date").first()
        other_posts = Post.objects.order_by("-post_date")[1:4]
        context["latest_post"] = latest_post
        context["other_posts"] = other_posts
        return context

    # TODO:Check the model for the posts and the cars and add them to the context, verify template index.html, add Django template tags to display the posts and the cars. Change Shop to spot


class PostDetailView(DetailView):
    model = Post
    template_name = "forum/post_detail.html"
    context_object_name = "post"


class RegisterUserView(CreateView):
    model = CustomUser
    form_class = RegistrationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")  # Zmień na swój URL po rejestracji

    def form_valid(self, form):
        return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = "registration/login.html"  # Ścieżka do szablonu
    redirect_authenticated_user = True

    def get_success_url(self):
        username = self.request.user.username
        return reverse_lazy(
            "profile", kwargs={"username": username}
        )  # Zmień na swój URL po zalogowaniu


class UserLogoutView(LogoutView):
    next_page = reverse_lazy("login")


class ProfileView(DetailView):
    template_name = "forum/profile.html"
    model = CustomUser
    context_object_name = "profile"
    slug_field = "username"
    slug_url_kwarg = "username"

    # TODO: User login template to do


class SettingsView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "forum/settings.html")


class MostRatedCarsView(ListView):
    model = Car
    template_name = "forum/highlighted.html"

    def get_context_data(self, *, object_list=..., **kwargs):
        context = super().get_context_data(**kwargs)
        context["top_cars"] = Car.objects.order_by("-horsepower")[:3]
        return context

    # TODO: Add the like logic to the posts,


class LoginPageView(View):
    def get(self, request):
        return render(request, "registration/login.html")


class UserLogoutView(LogoutView):
    next_page = reverse_lazy("login")


class FollowUserView(LoginRequiredMixin, View):
    def post(self, request, user_id):
        user_to_follow = get_object_or_404(CustomUser, id=user_id)
        if request.user != user_to_follow:
            Follow.objects.get_or_create(
                follower=request.user, following=user_to_follow
            )
        return HttpResponseRedirect(reverse("profile", args=[user_id]))


class UnfollowUserView(LoginRequiredMixin, View):
    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
        Follow.objects.filter(
            follower=request.user, following=user_to_unfollow
        ).delete()
        return HttpResponseRedirect(reverse("profile", args=[user_id]))


class MarkNotificationAsReadView(LoginRequiredMixin, View):
    def post(self, request, notification_id):
        notification = get_object_or_404(
            Notification, id=notification_id, recipient=request.user
        )
        notification.is_read = True
        notification.save()
        return HttpResponseRedirect(reverse("notifications"))


class MarkAllNotificationsAsReadView(LoginRequiredMixin, View):
    def post(self, request):
        request.user.notifications_received.filter(is_read=False).update(is_read=True)
        return HttpResponseRedirect(reverse("notifications"))


class NotificationListView(LoginRequiredMixin, ListView):
    model = Notification
    template_name = "notifications.html"
    context_object_name = "notifications"

    def get_queryset(self):
        return self.request.user.notifications_received.all()
