from django.shortcuts import render, get_object_or_404
from .models import *
import datetime
import calendar

# Create your views here.

def day_of_week(day):
    list = {
    0: 'Понедельник',
    1: 'Вторник',
    2: 'Среда',
    3: 'Четверг',
    4: 'Пятница',
    5: 'Суббота',
    6: 'Воскресенье',
    }
    return list[day]

def time_para(pair_number):
    list = {
    1: '8:00 - 9:30',
    2: '9:40 - 11:10',
    3: '11:40 - 13:10',
    4: '13:20 - 14:50',
    5: '15:00 - 16:30',
    6: '16:40 - 18:10',
    }
    return(list[pair_number])


def group_select(request):

    groups = Group.objects.order_by('group_name')
    print(groups)
    return render(request, 'user_raspisanie/raspisanie.html', {'groups': groups})



def view_raspis(request, pk):
    groups = get_object_or_404(Group, kod_of_group=pk)
    raspis = Raspisanie.objects.filter(group=groups.kod_of_group)
    group_name = raspis[0]
    week = Day_of_week.objects.filter()
    chetnoe = raspis.filter(parity=True).order_by('pair_number')
    nechetnoe = raspis.filter(parity=False).order_by('pair_number')
    return render(request, 'user_raspisanie/view_raspisanie.html', {'raspis': raspis, 'group_n': group_name, 'chetnoe': chetnoe, 'nechetnoe': nechetnoe, 'week': week})



def view_changes(request, gruppa):
    groups = get_object_or_404(Group, group_name=gruppa)
    date = datetime.date.today()
    print('today', date)
    for change in Changes.objects.filter(group=groups.kod_of_group):
        if change.date_of_change < date:
            print('Данная дата меньше сегодняшней', change.date_of_change)
            change.delete()
            print('Запись удалена')
    zamena = Changes.objects.filter(group=groups.kod_of_group)
    group = zamena[0]
    return render(request, 'user_raspisanie/view_changes.html', {'zamena': zamena, 'group': group})



def raspis_today(request, pk):
    groups = get_object_or_404(Group, kod_of_group=pk)
    week_day = datetime.date.today().weekday()+1
    date = datetime.date.today()
    raspis = Raspisanie.objects.filter(group=groups.kod_of_group, day_of_week=week_day)
    zamena = Changes.objects.filter(group=groups.kod_of_group, date_of_change=date)
    check = False
    dopoln_para = [[]]
    pair_number = []
    discipline = []
    teacher = []
    auditory = []
    print(date)
    print(zamena[0].date_of_change)
    print('День недели', week_day)
    for para in raspis:
        for zam in zamena:
            if para.pair_number == zam.pair_number:
                para.discipline = zam.discipline
                para.teacher = zam.teacher
                para.auditory = zam.auditory
    for zam in zamena:
        check = False
        for para in raspis:
            if para.pair_number == zam.pair_number:
                check = True
                break
        if check == False:
            print("Замена, которая должна добавиться ", zam, '    ', zam.pair_number)
            pair_number.append(zam.pair_number)
            discipline.append(zam.discipline)
            teacher.append(zam.teacher)
            auditory.append(zam.auditory)
    for i in range(len(pair_number)):
        print(pair_number[i])
        print(discipline[i])
        print(teacher[i])
        print(auditory[i])
        for j in range(len(discipline)):
            dopoln_para[i].append(pair_number[i])
            dopoln_para[i].append(discipline[i])
            dopoln_para[i].append(teacher[i])
            dopoln_para[i].append(auditory[i])
    for i in dopoln_para:
        for j in i:
            print(j)
    return render(request, 'user_raspisanie/raspis_today.html', {'raspis': raspis, 'dop_para': dopoln_para,})



def raspis_tom(request, pk):
    groups = get_object_or_404(Group, kod_of_group=pk)
    week_day = datetime.date.today().weekday()+2
    date = datetime.date.today()
    date += datetime.timedelta(days=1)
    raspis = Raspisanie.objects.filter(group=groups.kod_of_group, day_of_week=week_day)
    zamena = Changes.objects.filter(group=groups.kod_of_group, date_of_change=date)
    check = False
    dopoln_para = [[]]
    pair_number = []
    discipline = []
    teacher = []
    auditory = []
    print(date)
    print(zamena[0].date_of_change)
    print('День недели', week_day)
    for para in raspis:
        for zam in zamena:
            if para.pair_number == zam.pair_number:
                para.discipline = zam.discipline
                para.teacher = zam.teacher
                para.auditory = zam.auditory
    for zam in zamena:
        check = False
        for para in raspis:
            if para.pair_number == zam.pair_number:
                check = True
                break
        if check == False:
            print("Замена, которая должна добавиться ", zam, '    ', zam.pair_number)
            pair_number.append(zam.pair_number)
            discipline.append(zam.discipline)
            teacher.append(zam.teacher)
            auditory.append(zam.auditory)
    for i in range(len(pair_number)):
        print(pair_number[i])
        print(discipline[i])
        print(teacher[i])
        print(auditory[i])
        for j in range(len(discipline)):
            dopoln_para[i].append(pair_number[i])
            dopoln_para[i].append(discipline[i])
            dopoln_para[i].append(teacher[i])
            dopoln_para[i].append(auditory[i])
    for i in dopoln_para:
        for j in i:
            print(j)
    return render(request, 'user_raspisanie/raspis_tomorrow.html', {'raspis': raspis, 'dop_para': dopoln_para,})
