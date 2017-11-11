from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30),
    last_name = models.CharField(max_length=30),
    about_me = models.TextField(null=True, blank=True),
    email = models.EmailField(),
    website = models.CharField(max_length=50),
    birth_date = models.DateField(),
    street_address = models.CharField(max_length=50),
    street_number = models.IntegerField(),
    postal_code = models.IntegerField(),
    city = models.CharField(max_length=30)

    # class Meta:
    #     unique_together = (('first_name', 'last_name'),)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Work(models.Model):
    name = models.CharField(max_length=30),
    title = models.CharField(max_length=30),
    date_start = models.DateField(null=True, blank=True),
    date_end = models.DateField(null=True, blank=True)


class Study(models.Model):
    name = models.CharField(max_length=30, help_text="Where did you study?"),
    study = models.CharField(max_length=30, help_text="What you studied?"),
    date_start = models.DateField(null=True, blank=True),
    date_end = models.DateField(null=True, blank=True)


class Hobby(models.Model):
    name = models.CharField(max_length=30)


class Language(models.Model):
    name = models.CharField(max_length=30),
    level = models.IntegerField(help_text="0 - 5")


class SocialMedia(models.Model):
    name = models.CharField(max_length=30),
    link = models.CharField(max_length=50)


class Skill(models.Model):
    """
    Representing Skill level of certain skill
    """
    name = models.CharField(max_length=30),
    detail = models.TextField(null=True, blank=True),
    level = models.IntegerField(help_text="0 - 100")

    def __str__(self):
        return self.name


class Resume(models.Model):
    person = models.OneToOneField(Person,
                                  primary_key=True,
                                  on_delete=models.CASCADE),
    work_history = models.ForeignKey(Work, on_delete=models.CASCADE),
    study_history = models.ForeignKey(Study, on_delete=models.CASCADE),
    hobbies = models.ForeignKey(Hobby, on_delete=models.CASCADE),
    languages = models.ForeignKey(Language, on_delete=models.CASCADE),
    social_medias = models.ForeignKey(SocialMedia, on_delete=models.CASCADE),
    skills = models.ForeignKey(Skill, on_delete=models.CASCADE),
