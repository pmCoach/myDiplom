from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Day_of_week(models.Model):
    kod_raspisania = models.AutoField(primary_key = True)
    day_of_week = models.CharField(max_length = 20)

    def __str__(self):
        return self.day_of_week

    def publish(self):
        self.save()



class Discipline(models.Model):
    kod_of_discipline = models.AutoField(primary_key = True)
    name_of_discipline = models.CharField(max_length = 50)

    def __str__(self):
        return str(self.name_of_discipline)

    def publish(self):
        self.save()



class Teacher(models.Model):
    kod_of_teacher = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50)
    second_name = models.CharField(max_length = 50)
    surname = models.CharField(max_length = 50)

    def __str__(self):
        full_name = self.second_name + ' ' + self.name[0] + '. ' + self.surname[0] + '.'
        return full_name

    def publish(self):
        self.save()



class Group(models.Model):
    kod_of_group = models.AutoField(primary_key = True)
    group_name = models.CharField(max_length = 10)

    def __str__(self):
        return self.group_name



class Auditory(models.Model):
    kod_of_auditory = models.AutoField(primary_key = True)
    number_of_auditory = models.IntegerField()

    def __str__(self):
        return str(self.number_of_auditory)



class Pair_number(models.Model):
    kod_of_pair = models.AutoField(primary_key = True)
    pair_number = models.IntegerField()

    def __str__(self):
        return str(self.pair_number)


class Start_semestr_date(models.Model):
    kod_of_date = models.AutoField(primary_key = True)
    date = models.DateField()



class Raspisanie(models.Model):
    kod_of_raspisanie = models.AutoField(primary_key = True)
    day_of_week = models.ForeignKey(Day_of_week, on_delete = models.CASCADE)
    parity = models.BooleanField()
    discipline = models.ForeignKey(Discipline, on_delete = models.CASCADE)
    group = models.ForeignKey(Group, on_delete = models.CASCADE)
    #Данное поле предназначено для заполнения с какой пары начинается дисциплина
    pair_number = models.ForeignKey(Pair_number, on_delete = models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete = models.CASCADE)
    auditory = models.ForeignKey(Auditory, on_delete = models.CASCADE)

    def __str__(self):
        str_new = str(self.day_of_week) + " | Группа: " + str(self.group) + " | " + str(self.discipline) + " | " + str(self.auditory) + " кабинет | Преподаватель: " + str(self.teacher)
        return str_new




class Changes(models.Model):
    kod_of_raspisanie = models.AutoField(primary_key = True)
    date_of_change = models.DateField()
    pair_number = models.ForeignKey(Pair_number, on_delete = models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete = models.CASCADE)
    discipline = models.ForeignKey(Discipline, on_delete = models.CASCADE)
    group = models.ForeignKey(Group, on_delete = models.CASCADE)
    auditory = models.ForeignKey(Auditory, on_delete = models.CASCADE)


    def __str__(self):
        str_new = str(self.date_of_change) + " | Группа: " + str(self.group) + " | " + str(self.discipline) + " | " + str(self.auditory) + " кабинет | Преподаватель: " + str(self.teacher)
        return str_new
