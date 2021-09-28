from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)


    def __str__(self):
        return self.title



class Projects(models.Model):
    photo = models.ImageField(upload_to="images/")
    name = models.CharField(max_length=250)
    link = models.CharField(max_length=250)

    def __str__(self):
        return self.name



class Team(models.Model):
    photo = models.ImageField(upload_to="images/")
    name = models.CharField(max_length=200)
    job = models.CharField(max_length=250)
    text = models.TextField()
    telegram = models.CharField(max_length=250)
    instagram = models.CharField(max_length=250)
    facebook = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Bolg(models.Model):
    name = models.TextField()
    text = models.TextField()
    photo = models.ImageField(upload_to="images/")


    def __str__(self):
        return self.name
