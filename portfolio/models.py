from django.db import models

class Experience(models.Model):
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    start_date = models.CharField(max_length=20)  # Ej: "2018"
    end_date = models.CharField(max_length=20, blank=True, null=True)  # Ej: "Actualidad"
    key_words = models.CharField(max_length=200)
    description = models.TextField()


    def __str__(self):
        return f"{self.position} en {self.company}"

class Project(models.Model):
    title = models.CharField(max_length=100)
    technologies = models.CharField(max_length=200)
    url = models.URLField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.title
    
class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)  # Ej: "Frontend", "Backend", "DevOps"
    proficiency = models.CharField(max_length=50)  # Ej: "Básico", "Intermedio", "Avanzado"

    def __str__(self):
        return f"{self.name} ({self.category}) - {self.proficiency}"


class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    start_date = models.CharField(max_length=20)  # Ej: "2015"
    end_date = models.CharField(max_length=20, blank=True, null=True)  # Ej: "2019" o "Actualidad"

    def __str__(self):
        return f"{self.degree} en {self.institution}"
    