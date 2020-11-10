from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):

    menu = models.CharField(max_length=100)
    stock = models.IntegerField()
    price = models.IntegerField()
    order = models.IntegerField()
    created_at = models.DateTimeField()

    def __str__(self):
        return f'{self.menu}: {self.stock}: {self.price}: {self.order}'


class Order(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    store = models.CharField(max_length=100)
    date = models.DateField()
    order = models.TextField()
    package = models.TextField()
    pickup = models.TimeField()
    created_at = models.DateTimeField()

    def __str__(self):
        return f'{self.store}: {self.date}: {self.order}: {self.package}: {self.pickup}'

class Items(models.Model):

    store = models.CharField(max_length=100)
    date = models.DateField()
    menu = models.TextField()
    stock = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return f'{self.store}: {self.date}: {self.menu}: {self.stock}: {self.price}'

class Order_User(models.Model):

    store = models.CharField(max_length=100)
    date = models.DateField()
    menu = models.TextField()
    stock = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return f'{self.store}: {self.date}: {self.menu}: {self.stock}: {self.price}'

#여기서부터 댓글

class Comment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE) #여기서 블로그가 뭐여야할까? 
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')
    users = models.ManyToManyField(User, through='Scrap') # 추가해줍니다. 

#여기에 Comment 모델도 있습니다.

class Scrap(models.Model): 
			user = models.ForeignKey(User, on_delete=models.CASCADE)
			post = models.ForeignKey(Post, on_delete=models.CASCADE)
			created_at = models.DateTimeField(auto_now_add=True)