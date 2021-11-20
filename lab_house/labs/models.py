from django.db import models


class Lab(models.Model):
	title = models.CharField(max_length = 200)
	task = models.TextField(blank = True)
	url = models.URLField()
	deadline = models.DateField()
	is_published = models.BooleanField(default = False)

	def __str__(self):
		return self.title
