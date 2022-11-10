from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField


class Post(models.Model):
	title = models.CharField(max_length=200)
	title_tag = models.CharField(max_length=200)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	# content = models.TextField()
	image = models.ImageField(null=True, blank=True, upload_to="images/")
	content = RichTextField(blank=True, null=True)
	created_on = models.DateField(auto_now_add=True)
	category = models.CharField(max_length=200, default='coding')
	snippets = models.CharField(max_length=200)
	likes = models.ManyToManyField(User, related_name='blog_posts')

	class Meta:
		ordering = ['-created_on']

	def total_likes(self):
		return self.likes.count()

	def __str__(self):
		return self.title + ' | ' + str(self.author)

	def get_absolute_url(self):
		return reverse('home')

class Category(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('home')

class UserProfile(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	bio = models.TextField()
	profile_pic = models.ImageField(null=True, blank=True)
	web_url = models.CharField(max_length=200, null=True, blank=True)
	fb_url = models.CharField(max_length=200, null=True, blank=True)
	instagram_url = models.CharField(max_length=200, null=True, blank=True)
	linkedin_url = models.CharField(max_length=200, null=True, blank=True)
	whatsapp_url = models.CharField(max_length=200, null=True, blank=True)


	def __str__(self):
		return str(self.user)

	def get_absolute_url(self):
		return reverse('home')

class Comment(models.Model):
	post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	body = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-date_added']
	

	def __str__(self):
		return '%s - %s' % (self.post.title, self.name)
		