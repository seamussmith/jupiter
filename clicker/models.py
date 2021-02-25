from django.db import models

# Create your models here.
class Button(models.Model):
    count = models.IntegerField()
    text = models.TextField()
    
    @staticmethod
    def new(text):
        return Button(
            count = 0,
            text = text
        )
    
    def __str__(self):
        return f"{'{'}id: {self.id}, count: {self.count}, text: {self.text}{'}'}"

    def like(self):
        self.count += 1
    def dislike(self):
        self.count -= 1
    def reset(self):
        self.count = 0

    def to_dict(self):
        return {
            "count": self.count,
            "id": self.id,
            "text": self.text
        }
