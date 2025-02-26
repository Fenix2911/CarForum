from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


# Create your models here.

class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Name:{self.username}, bio:{self.bio}"

    @property
    def followers_count(self):
        return self.followers.count()

    @property
    def following_count(self):
        return self.following.count()


class Car(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='cars')
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    engine = models.CharField(max_length=100, blank=True, null=True)
    horsepower = models.IntegerField(blank=True, null=True)
    torque = models.IntegerField(blank=True, null=True)
    transmission = models.CharField(
        max_length=50,
        choices=[('manual', 'Manual'), ('automatic', 'Automatic')],
        blank=True,
        null=True
    )
    drivetrain = models.CharField(
        max_length=50,
        choices=[('FWD', 'Front-Wheel Drive'), ('RWD', 'Rear-Wheel Drive'), ('AWD', 'All-Wheel Drive')],
        blank=True,
        null=True
    )
    fuel_type = models.CharField(
        max_length=50,
        choices=[('gasoline', 'Gasoline'), ('diesel', 'Diesel'), ('electric', 'Electric'), ('hybrid', 'Hybrid')],
        blank=True,
        null=True
    )
    image = models.ImageField(upload_to='car_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"


class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=50,
        choices=[('active', 'Active'), ('deleted', 'Deleted')],
        default='active'
    )

    def __str__(self):
        return f"{self.title} by {self.author.username}"

    @property
    def like_count(self):
        return self.likes.count()



class Like(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')

    def __str__(self):
        return f"{self.user.username} liked {self.post.title}"


class Comment(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post}"


class Thread(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='threads')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ForumPost(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='posts')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='forum_posts')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post by {self.author.username} in {self.thread.title}"


class Notification(models.Model):
    recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='notifications_received')
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sent_notifications')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True, related_name='notifications')
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, blank=True, null=True, related_name='notifications')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, blank=True, null=True, related_name='notifications')
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.recipient.username}: {self.message}"



class Follow(models.Model):
    follower = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='following')
    following = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='followers')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following')

    def __str__(self):
        return f"{self.follower.username} follows {self.following.username}"

