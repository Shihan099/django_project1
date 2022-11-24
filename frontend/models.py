from django.db import models


# Create your models here.


class Service(models.Model):
    icon = models.CharField(max_length=15, null=True, blank=True)
    title = models.CharField(max_length=25, null=True, blank=True)
    des = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class Portfolio(models.Model):
    img = models.ImageField(null=True)
    title = models.CharField(max_length=15, null=True, blank=True)
    des = models.TextField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.title


class About(models.Model):
    img = models.ImageField(null=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    sub_title = models.CharField(max_length=50, null=True, blank=True)
    des = models.TextField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.title


class Team(models.Model):
    img_team = models.ImageField(null=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    des = models.CharField(max_length=20, null=True, blank=True)
    Icon1 = models.CharField(max_length=30, null=True, blank=True)
    Icon2 = models.CharField(max_length=30, null=True, blank=True)
    Icon3 = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.title


class Client(models.Model):
    img = models.ImageField(null=True)

    def __str__(self):
        return self.img


class Footer(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    Icon1 = models.CharField(max_length=30, null=True, blank=True)
    Icon2 = models.CharField(max_length=30, null=True, blank=True)
    Icon3 = models.CharField(max_length=30, null=True, blank=True)
    attr = models.CharField(max_length=50, null=True, blank=True)
    attr2 = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.title
