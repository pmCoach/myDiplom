from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Day_of_week(models.Model):
    kod_raspisania = models.AutoField(primary_key = True)
    day_of_week = models.CharField(max_length = 20, verbose_name="День недели")

    class Meta:
        verbose_name="День недили"
        verbose_name_plural="Дни недели"

    def __str__(self):
        return self.day_of_week

    def publish(self):
        self.save()



class Discipline(models.Model):
    kod_of_discipline = models.AutoField(primary_key = True)
    name_of_discipline = models.CharField(max_length = 50, verbose_name="Название дисциплины")

    class Meta:
        verbose_name="Дисциплину"
        verbose_name_plural="Дисциплины"

    def __str__(self):
        return str(self.name_of_discipline)

    def publish(self):
        self.save()



class Teacher(models.Model):
    kod_of_teacher = models.AutoField(primary_key = True)
    second_name = models.CharField(max_length = 50, verbose_name="Фамилия")
    name = models.CharField(max_length = 50, verbose_name="Имя")
    surname = models.CharField(max_length = 50, verbose_name="Отчество")

    class Meta:
        verbose_name="Преподавателя"
        verbose_name_plural="Преподаватели"


    def __str__(self):
        full_name = self.second_name + ' ' + self.name[0] + '. ' + self.surname[0] + '.'
        return full_name

    def publish(self):
        self.save()



class Group(models.Model):
    kod_of_group = models.AutoField(primary_key = True)
    group_name = models.CharField(max_length = 10, verbose_name="Группа")

    class Meta:
        verbose_name="Группу"
        verbose_name_plural="Группы"

    def __str__(self):
        return self.group_name



class Auditory(models.Model):
    kod_of_auditory = models.AutoField(primary_key = True)
    number_of_auditory = models.IntegerField(verbose_name="Номер аудитории")

    class Meta:
        verbose_name="Аудиторию"
        verbose_name_plural="Аудитории"

    def __str__(self):
        return str(self.number_of_auditory)



class Pair_number(models.Model):
    kod_of_pair = models.AutoField(primary_key = True)
    pair_number = models.IntegerField(verbose_name="Номер пары")
    pair_start = models.TimeField(verbose_name="Начало пары")
    pair_end = models.TimeField(verbose_name="Конец пары")

    class Meta:
        verbose_name="Номер пары"
        verbose_name_plural="Номера пар"

    def __str__(self):
        return str(self.pair_number)


class Start_semestr_date(models.Model):
    kod_of_date = models.AutoField(primary_key = True)
    date = models.DateField(verbose_name="Дата начала семестра")

    class Meta:
        verbose_name="Дату начала семестра"
        verbose_name_plural="Дата начала семестра"

    def __str__(self):
        data = str(self.date)
        return data

class Raspisanie(models.Model):
    kod_of_raspisanie = models.AutoField(primary_key = True)
    day_of_week = models.ForeignKey(Day_of_week, on_delete = models.CASCADE, verbose_name="День недели")
    parity = models.BooleanField(verbose_name="Четность")
    obe_nedeli = models.BooleanField(verbose_name="Обе недели")
    discipline = models.ForeignKey(Discipline, on_delete = models.CASCADE, verbose_name="Дисциплина")
    group = models.ForeignKey(Group, on_delete = models.CASCADE, verbose_name="Группа")
    #Данное поле предназначено для заполнения с какой пары начинается дисциплина
    pair_number = models.ForeignKey(Pair_number, on_delete = models.CASCADE, verbose_name="Номер пары")
    teacher = models.ForeignKey(Teacher, on_delete = models.CASCADE, verbose_name="Преподаватель")
    auditory = models.ForeignKey(Auditory, on_delete = models.CASCADE, verbose_name="Аудитория")

    def __str__(self):
        str_new = str(self.day_of_week) + " | Группа: " + str(self.group) + " | " + str(self.discipline) + " | " + str(self.auditory) + " кабинет | Преподаватель: " + str(self.teacher)
        return str_new

    class Meta:
        verbose_name = 'Пару'
        verbose_name_plural = 'Расписание'




class Changes(models.Model):
    kod_of_raspisanie = models.AutoField(primary_key = True)
    date_of_change = models.DateField(verbose_name="Дата замены")
    pair_number = models.ForeignKey(Pair_number, on_delete = models.CASCADE, verbose_name="Номер пары")
    teacher = models.ForeignKey(Teacher, on_delete = models.CASCADE, verbose_name="Преподаватель")
    discipline = models.ForeignKey(Discipline, on_delete = models.CASCADE, verbose_name="Дисциплина")
    group = models.ForeignKey(Group, on_delete = models.CASCADE, verbose_name="Группа")
    auditory = models.ForeignKey(Auditory, on_delete = models.CASCADE, verbose_name="Аудитория")

    class Meta:
        verbose_name="Замену"
        verbose_name_plural="Замены"


    def __str__(self):
        str_new = str(self.date_of_change) + " | Группа: " + str(self.group) + " | " + str(self.discipline) + " | " + str(self.auditory) + " кабинет | Преподаватель: " + str(self.teacher)
        return str_new
