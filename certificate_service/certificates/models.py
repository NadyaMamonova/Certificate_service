from django.db import models
from django.core.validators import MinLengthValidator
import uuid

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class School(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Internship(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    supporting_schools = models.ManyToManyField(School, related_name='internships')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def duration(self):
        return (self.end_date - self.start_date).days

    class Meta:
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['start_date', 'end_date']),
        ]

class Certificate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='certificates')
    internship = models.ForeignKey(Internship, on_delete=models.CASCADE, related_name='certificates')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='certificates')
    skills = models.ManyToManyField(Skill, related_name='certificates', blank=True)
    issued_at = models.DateTimeField(auto_now_add=True)
    custom_message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Certificate {self.id} for {self.user}"

    class Meta:
        indexes = [
            models.Index(fields=['id']),
            models.Index(fields=['user']),
            models.Index(fields=['internship']),
            models.Index(fields=['role']),
            models.Index(fields=['issued_at']),
        ]