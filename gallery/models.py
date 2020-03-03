from django.db import models
import datetime as dt

# Create your models here.
class Picture(models.Model):
    title = models.CharField(max_length = 60)
    post = models.TextField()
    editor = models.ForeignKey(Editor, on_delete = models.CASCADE)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add = True)
    picture_image = models.ImageField(upload_to = 'pictures/',default = 'image' )

    def save_picture(self):
        self.save()