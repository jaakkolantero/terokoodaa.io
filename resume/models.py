import datetime

from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone


class Resume(models.Model):
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.person.first_name + " " + self.person.last_name

    def was_updated_recently(self):
        return self.last_updated >= timezone.now() - datetime.timedelta(days=1)


class Person(models.Model):
    first_name = models.CharField(max_length=30, default=" ")
    last_name = models.CharField(max_length=30, default=" ")
    profile_picture = models.ImageField(upload_to="resume_profile/", blank=True, null=True)
    about_me = models.TextField(null=True, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True)  # validators should be a list
    email = models.EmailField(null=True, blank=True)
    website = models.CharField(max_length=50, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    street_address = models.CharField(max_length=50, null=True, blank=True)
    street_number = models.IntegerField(null=True, blank=True)
    postal_code = models.IntegerField(null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
    resume = models.OneToOneField(Resume,
                                  on_delete=models.CASCADE, null=True)

    class Meta:
        unique_together = (('first_name', 'last_name'),)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Work(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    title = models.CharField(max_length=30, null=True, blank=True)
    date_start = models.DateField(null=True, blank=True)
    date_end = models.DateField(null=True, blank=True)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, null=True, related_name='works')

    def __str__(self):
        return self.name


class Study(models.Model):
    name = models.CharField(max_length=30, help_text="Where did you study?", null=True, blank=True)
    study = models.CharField(max_length=60, help_text="What you studied?", null=True, blank=True)
    date_start = models.DateField(null=True, blank=True)
    date_end = models.DateField(null=True, blank=True)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, null=True, related_name='studies')

    def __str__(self):
        return self.name


class Hobby(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, null=True, related_name='hobbys')

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    level = models.IntegerField(help_text="0 - 100", default=0)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, null=True, related_name='languages')

    def __str__(self):
        return self.name


class SocialMedia(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    link = models.CharField(max_length=50, default="#")
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, null=True, related_name='socialmedias')

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    detail = models.TextField(null=True, blank=True)
    level = models.IntegerField(help_text="0 - 100", default=0)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, null=True, related_name='skills')

    def __str__(self):
        return self.name
