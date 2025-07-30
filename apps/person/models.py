from django.db import models
from model_utils.models import TimeStampedModel

# class GenderChoices(models.TextChoices):
#     MALE = 'M', 'Male'
#     FEMALE = 'F', 'Female'

class Patient(TimeStampedModel):
    code = models.CharField(max_length=50, null=True, blank=True)
    ci = models.CharField(max_length=50, null=True, blank=True)
    names = models.CharField(max_length=100)
    lastnames = models.CharField(max_length=100)
    birthdate = models.DateField()
    gender = models.CharField(max_length=1, default='M', choices=[('M', 'Male'), ('F', 'Female')])
    # gender = models.CharField(max_length=1, choices=GenderChoices.choices, default=GenderChoices.MALE)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    allergies = models.JSONField(blank=True, null=True)
    bloodType = models.CharField(max_length=5, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    contacts = models.JSONField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.names = self.names.upper()
        self.lastnames = self.lastnames.upper()
        if not self.code: 
            self.generate_code()
        if not self.ci: 
            self.ci = self.code
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.names} {self.lastnames}"
    
    @property
    def full_name(self) -> str:
        return f"{self.names} {self.lastnames}"
    
    @property
    def age(self) -> int:
        from datetime import date
        today = date.today()
        return today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
        
    @property
    def gender_description(self) -> str:
        return 'Masculino' if self.gender == 'M' else 'Femenino'
    
    def generate_code(self):
        count = Patient.objects.all().count() + 1
        self.code = f"P{count:04d}"
        # self.save()