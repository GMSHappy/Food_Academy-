from django.db import models


class Module(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateTimeField("start date")
    end_date = models.DateTimeField("end date")

    def __str__(self):
        return self.title


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    enrolled_modules = models.ManyToManyField(Module)
    enrollment_date = models.DateTimeField(auto_now_add=True)  # New field
    last_updated = models.DateTimeField(auto_now=True)  # New field

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
