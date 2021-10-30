from django.db import models


# describing the subject here
class Article(models.Model):
	title = models.CharField(max_length = 255)
	content = models.TextField(blank = True)  # blank = True means can be empty
	photo = models.ImageField(upload_to = 'photos/%y/%m/%d')
	time_created = models.TimeField(auto_now_add = True)  # accepts current time when creating and will noe change
	time_updated = models.TimeField(auto_now = True)  # refreshes every time we update
	is_published = models.BooleanField(default = True)  # default value is True
