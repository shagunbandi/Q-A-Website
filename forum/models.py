import os
from django.db import models
from datetime import datetime
from django.db.models.fields.related import OneToOneField
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class Question(models.Model):
    ques = models.CharField(max_length=10000)
    ques_author = models.CharField(max_length=30)
    ques_date = models.DateTimeField(default=datetime.now(), blank=True)

    def get_absolute_url(self):
        return reverse('forum:detail', kwargs={'pk': self.pk})

    def __str__(self):
        if len(self.ques)>30:
            return self.ques[:15] + ' ... ' + self.ques[-15:]
        else:
            return self.ques


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    ans = models.CharField(max_length=10000)
    ans_author = models.CharField(max_length=30)
    ans_date = models.DateTimeField(default=datetime.now(), blank=True)

    def get_absolute_url(self):
        return reverse('forum:detail', kwargs={'pk': self.question.id})

    def __str__(self):
        if len(self.ans) > 30:
            return self.ans[:15] + ' ... ' + self.ans[-15:]
        else:
            return self.ans


#class MyProfile(AbstractUser):
    #is_admin = models.BooleanField(default=False)