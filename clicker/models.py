from django.db import models

# Create your models here.
class Button(models.Models):
    count = models.IntegerField()
    text = models.TextField()
    
    @staticmethod
    def new(text):
        return Button(
            count = 0,
            text = text
        )
    
    def like(self):
        self.count += 1
    def dislike(self):
        self.count -= 1
    def reset(self):
        self.count = 0
