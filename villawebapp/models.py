from django.db import models

# Create your models here.
##########################################################################################################################################
class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='static/assets/images/rooms/')
    square_meters = models.IntegerField()
    paragraph = models.TextField()
    paragraph2 = models.TextField()


    class Meta:
        verbose_name_plural = "01. Portfolio"

    def __str__(self):
        return self.title
##########################################################################################################################################

class Message(models.Model):
    name = models.CharField(max_length=200, help_text="Name of the sender")
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "02.  Costumer Message"

    def __str__(self):
        return self.name