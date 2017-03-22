from __future__ import unicode_literals
import bcrypt
from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+.[a-zA-Z]*$')
class UserManager(models.Manager):
    def register(self, first_name, last_name, email, password, password_confirmation, user_level):
        errors = {}
        if (len(first_name) < 2):
            errors['first_name'] = "First Name needs to be at least two letters long"

        if (len(last_name) < 2):
            errors['last_name'] = "First Name needs to be at least two letters long"

        if (len(password) < 8):
            errors['password'] = "Password needs to be at least eight characters long"

        if (password != password_confirmation):
            errors['password'] = "Passwords do not match"
        try:
            existingUser = self.get(email__iexact=email)
        except:
            existingUser = None
        if (existingUser):
            errors['email'] = 'That email is already registered'

        if (not EMAIL_REGEX.match(email)):
            errors['email'] = 'Invalid email.'

        if (errors):
            return (False, errors)
        else:
            password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            self.create(email=email, first_name=first_name, last_name=last_name, password=password, user_level=user_level, description=' ')
            return (True, self.get(email=email))

    def login(self, email, password):
        try:
            user = self.get(email__iexact=email) # case insensitive comparison
        except:
            user = None
        print user
        # print bcrypt.hashpw(password,user[0].password)
        # print user[0].password
        if user and bcrypt.hashpw(password.encode('utf-8'), user.password.encode('utf-8')) == user.password.encode('utf-8'):
            return (True, user)
            # should be classified as a successful login event!
        return(False,{"login", "login failed"})
            # everything else failed login

    def updatePassword(self, password, password_confirmation, id):
        errors = False
        if (password != password_confirmation):
            errors = True
            return errors
        user = User.objects.get(id=id)
        password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        user.password = password
        user.save()
        return errors
    def addFriend(self, user_id, friend_id):
        user = self.get(id=user_id)
        friend = self.get(id=friend_id)
        Friend.objects.create(user_friend=user, second_friend=friend)
        Friend.objects.create(user_friend=friend, second_friend=user)

    def removeFriend(self, user_id, friend_id):
        user = self.get(id=user_id)
        friend = self.get(id=friend_id)
        friendship1 = Friend.objects.get(user_friend=user, second_friend=friend)
        friendship2 = Friend.objects.get(user_friend=friend, second_friend=user)
        friendship1.delete()
	friendship2.delete()
class User(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    user_level = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    userManager = UserManager()
    objects = models.Manager()
class Friend(models.Model):
    user_friend = models.ForeignKey(User, related_name='requester')
    second_friend = models.ForeignKey(User, related_name='accepter')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    def addFriend(self, user_id, friend_id):
        user = self.get(id=user_id)
        friend = self.get(id=friend_id)
        Friend.objects.create(user_friend=user, second_friend=friend)
        Friend.objects.create(user_friend=friend, second_friend=user)

    def removeFriend(self, user_id, friend_id):
        user = self.get(id=user_id)
        friend = self.get(id=friend_id)
        friendship1 = Friend.objects.get(user_friend=user, second_friend=friend)
        friendship2 = Friend.objects.get(user_friend=friend, second_friend=user)
        friendship1.delete()
        friendship2.delete()

