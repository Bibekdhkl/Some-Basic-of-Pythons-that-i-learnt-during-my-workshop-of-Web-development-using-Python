from django.db import models

# Create your models here.
# dipendra is a instructor
class NewCategory(models.Model):
    title = models.CharField(max_length=100,default='jj')
    taglist = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'newcategory'

class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='news/')#yesle media folder bhitra ko news ma gayera upload huncha
    taglist = models.TextField()
    date = models.DateField()
    newscategory = models.ForeignKey(NewCategory,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
