from django.contrib import admin
from .models import *

class RaspisanieAdmin(admin.ModelAdmin):
    list_display= ('day_of_week', 'group', 'pair_number', 'parity', 'obe_nedeli', 'discipline', 'group', 'teacher', 'auditory')
    search_fields = ['group__group_name',]
    list_filter = ('day_of_week', 'group__group_name')

class ChangesAdmin(admin.ModelAdmin):
    list_display= ('date_of_change', 'group', 'pair_number', 'discipline', 'teacher', 'auditory' )
    search_fields = ['group__group_name',]

class AuditoryAdmin(admin.ModelAdmin):
    list_display= ('number_of_auditory',)

class Day_of_weekAdmin(admin.ModelAdmin):
    list_display= ('day_of_week', )

class DisciplineAdmin(admin.ModelAdmin):
    list_display= ('name_of_discipline',)

class GroupAdmin(admin.ModelAdmin):
    list_display= ('group_name',)

class Pair_numberAdmin(admin.ModelAdmin):
    list_display= ('pair_number', 'pair_start', 'pair_end')

class TeacherAdmin(admin.ModelAdmin):
    list_display= ('second_name', 'name', 'surname')

class Start_semestr_dateAdmin(admin.ModelAdmin):
    list_display= ('date',)
# Register your models here.
admin.site.register(Auditory,AuditoryAdmin)
admin.site.register(Day_of_week, Day_of_weekAdmin)
admin.site.register(Discipline, DisciplineAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Pair_number, Pair_numberAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Raspisanie, RaspisanieAdmin)
admin.site.register(Changes, ChangesAdmin)
admin.site.register(Start_semestr_date, Start_semestr_dateAdmin)
