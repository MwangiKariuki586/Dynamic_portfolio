from django.db import models

# Create your models here.
class Home(models.Model):
    name = models.CharField(max_length=20)
    greetings1 = models.CharField(max_length=4)
    greetings2 = models.CharField(max_length=10)
    picture = models.ImageField(upload_to='picture/')
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
class About(models.Model):
    heading = models.CharField(max_length=50)
    career = models.CharField(max_length=20)
    description = models.TextField(blank=False)
    profile_img = models.ImageField(upload_to='profile')
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.career
class Profile(models.Model):
    linkedIn = models.URLField(max_length=500,default='Linkedin link')
    Github = models.URLField(max_length=500,default='github link')
    Whatsapp = models.URLField(max_length=500, default='whatsapp link')
    updated_stamp = models.DateField(auto_now=True)

    def __str__(self):
        return 'profile (self.id)'
class Category(models.Model):
    name = models.CharField(max_length=20)
    updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
    def __str__(self):
        return self.name
class Skills(models.Model):
    Category = models.ForeignKey(Category,on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=20)
class Portfolio(models.Model):
    image = models.ImageField(upload_to='portfolio/')
    link = models.CharField(max_length=200)
    def __str__(self):
        return f'Portfolio (self.id)'