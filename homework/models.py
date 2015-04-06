from django.db import models

class Topic(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User)
    topic = models.ForeignKey(Topic)
    body = models.CharField(max_length=255)

    def __str__(self):
        return "msg:%s" % self.user

class Subscription(models.Model):
    user = models.ForeignKey(User)
    topic = models.ForeignKey(Topic)

    def __str__(self):
        return "User:%s -> Topic:%s" % (self.user, self.topic)

