from django.contrib import admin
from .models import Person, Resume
from .models import Work, Study, Hobby
from .models import Language, SocialMedia, Skill


class PersonInline(admin.StackedInline):
    model = Person


class WorkInline(admin.TabularInline):
    model = Work
    extra = 1


class StudyInline(admin.TabularInline):
    model = Study
    extra = 1


class HobbyInline(admin.TabularInline):
    model = Hobby
    extra = 1


class LanguageInline(admin.TabularInline):
    model = Language
    extra = 1


class SocialMediaInline(admin.TabularInline):
    model = SocialMedia
    extra = 1


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1


class ResumeAdmin(admin.ModelAdmin):
    # Show id in admin page. Great for testing
    readonly_fields = ('id',)
    inlines = [
        PersonInline,
        WorkInline,
        StudyInline,
        HobbyInline,
        LanguageInline,
        SocialMediaInline,
        SkillInline,
    ]


admin.site.register(Resume, ResumeAdmin)
