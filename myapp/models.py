from django.db import models

# Create your models here.
class Profile(models.Model):
    BG_CHOCHES=(
        ('blue','Blue'),
        ('yellow','Yellow'),
        ('green','Grren')
    )

    name=models.CharField( max_length=50)
    slug=models.SlugField(max_length=100)
    bg_choses= models.CharField( max_length=50,choices=BG_CHOCHES)

    def __str__(self):
        return self.name
    

class Link(models.Model):
    text=models.TextField(max_length=100)
    url=models.URLField( max_length=100)
    profile=models.ForeignKey(Profile,  on_delete=models.CASCADE,related_name="Link")
    

    def __str__(self):
        return f"{self.text} | {self.url}"
    
        