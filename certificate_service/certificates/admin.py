from django.contrib import admin
from .models import User, School, Skill, Role, Internship, Certificate

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email')

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    search_fields = ('name',)

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Internship)
class InternshipAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date')
    search_fields = ('name',)
    filter_horizontal = ('supporting_schools',)

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'internship', 'role', 'issued_at')
    search_fields = ('id', 'user__first_name', 'user__last_name', 'user__email')
    list_filter = ('role', 'internship')
    filter_horizontal = ('skills',)
    readonly_fields = ('issued_at',)
