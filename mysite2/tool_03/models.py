from django.db import models

# Create your models here.
class Blog(models.Model):
	id = models.IntegerField(default=1,primary_key=True)
	name=models.CharField(max_length=50,default='default name')
	user_id=models.IntegerField(default=1)
	user_name=models.CharField(max_length=10,default='default name')
	content=models.TextField()
	create_at=models.DateTimeField()

	def __str__(self):
		return self.name

class Comment(models.Model):
	blog_id=models.IntegerField(default=1)
	user_name=models.CharField(max_length=10,default='default name')
	content=models.CharField(max_length=500,default='default content')
	create_at=models.DateTimeField()
	class Meta:
		ordering = ('create_at',)
	def __str__(self):
		return 'Comments by {} on {}'.format(self.user_name, self.content)
	
	