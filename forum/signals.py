from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Notification, Like, Follow


@receiver(post_save, sender=Like)
def create_like_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            recipient=instance.post.author,
            sender=instance.user,
            post=instance.post,
            message=f"{instance.user.username} polubił Twój post.",
        )


@receiver(post_save, sender=Follow)
def create_follow_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            recipient=instance.following,
            sender=instance.follower,
            message=f"{instance.follower.username} zaczął Cię obserwować!",
        )
