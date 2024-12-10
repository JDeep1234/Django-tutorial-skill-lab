from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)  # Assuming phone is a string
    joined_date = models.DateField()  # Assuming this is the date the member joined

    def __str__(self):
        return f'{self.firstname} {self.lastname}'