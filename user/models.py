from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField((""), max_length=254)
    password = models.CharField(max_length=50)
    date = models.DateField((""), auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.username
    
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateField((""), auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.user
    