from django.db import models
from django.urls import reverse


class Profile(models.Model):
    author = models.OneToOneField('auth.User', on_delete=models.CASCADE, db_index=True)
    email = models.EmailField(max_length=150)
    phone_number = models.CharField(max_length=150)
    inform = models.TextField(blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.author.username)

    def get_absolute_url(self):
        return reverse('profile_detail', args=[str(self.id)])


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=200)
    categories = models.ManyToManyField(Category, related_name='topic')
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    info = models.TextField()
    price = models.PositiveIntegerField(default=0)
    publication_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('prod_detail', args=[str(self.id)])
