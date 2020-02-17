from django.db import models

# Create your models here.


        
class Book(models.Model):
   
    title_book = models.CharField(max_length=50)
    author_book = models.CharField(max_length=50)
    image = models.ImageField(upload_to = 'bookerisell')
    amount = models.IntegerField()

class History(models.Model):
    history_title = models.CharField(max_length=50)
    history_author = models.CharField(max_length=50)
    history_image = models.ImageField(upload_to='bookerisell')
    history_amount = models.IntegerField()
    
class Fiction(models.Model):
    fiction_title= models.CharField(max_length=50)
    fiction_author = models.CharField(max_length=50)
    fiction_image = models.ImageField(upload_to='bookerisell')
    fiction_amount = models.IntegerField()
    
    
    
    
    def save_image(self):
            self.save()

    def delete_image(self):
        self.delete()

        

    @classmethod
    def search_by_title(cls,search_term):
        image = cls.objects.filter(title_book__icontains=search_term)
        return image
        
    
    
    
    
    