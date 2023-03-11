from django.db import models

class Profession(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return self.__str__()
    
class Test(models.Model):
    name = models.TextField()
    profession = models.ForeignKey("Profession", on_delete=models.CASCADE)
    date = models.DateField()
    number_questions = models.IntegerField()
    
    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return self.__str__()
    
    class Meta:
        ordering = ['-id']

class Question(models.Model):
    type = models.BooleanField() #True if Image
    question = models.TextField(blank=True)
    answer = models.TextField(blank=True)
    image = models.ImageField(blank=True)
    test = models.ForeignKey("Test", on_delete=models.CASCADE, related_name='questions')
    
    def __str__(self) -> str:
        return self.question if self.question != "" else self.image.name
    
    def __repr__(self) -> str:
        return self.__str__()
