from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Tasks(models.Model):
    title = models.CharField(max_length=200)
    description= models.TextField()
    created_at = models.DateTimeField(auto_now_add= True)
    is_completed= models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title