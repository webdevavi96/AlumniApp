from django.db import models

# Create your models here.


class Alumni(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    graduation_year = models.IntegerField()
    user_type = models.CharField(max_length=10, choices=[('alumni', 'Alumni'),])
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    password = models.CharField(max_length=100, blank=False, null=False, default="Password123")
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    
class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    user_type = models.CharField(max_length=10, choices=[('teacher', 'Teacher'),])
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    password = models.CharField(max_length=100, blank=False, null=False, default="Password123")
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    branch = models.CharField(max_length=100, choices=[
        ('CSE', 'Computer Science and Engineering'),
        ('ECE', 'Electronics Engineering'),
        ('EE', 'Electrical Engineering'),
    ])
    user_type = models.CharField(max_length=10, choices=[('student', 'Student'),])
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    password = models.CharField(max_length=100, blank=False, null=False, default="Password123")
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    
    
    def __str__(self):
        return self.title
    
    
class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    blog_image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    author = models.ForeignKey(Alumni, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title