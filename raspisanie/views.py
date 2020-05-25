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

#Функция вызывает страницу с выбором группы
def group_select(request):

    groups = Group.objects.order_by('group_name')
    print(groups)
    return render(request, 'user_raspisanie/raspisanie.html', {'groups': groups})


#Функция вызывает расписание занятий
def view_raspis(request, pk):
    groups = get_object_or_404(Group, kod_of_group=pk)
    #получаем строки расписания выбранной группы
    raspis = Raspisanie.objects.filter(group=groups.kod_of_group)
    group_name = raspis[0]
    week = Day_of_week.objects.filter()
    chetnoe = raspis.exclude(parity=False, obe_nedeli=False).order_by('pair_number')
    nechetnoe = raspis.exclude(parity=True).order_by('pair_number')
    return render(request, 'user_raspisanie/view_raspisanie.html', {'raspis': raspis, 'group_n': group_name, 'chetnoe': chetnoe, 'nechetnoe': nechetnoe, 'week': week,})


#Функция позволяет вызвать просмотр замен
def view_changes(request, gruppa):
    groups = get_object_or_404(Group, group_name=gruppa)
    date = datetime.date.today()
    #Данный цикл позволяет удалить замену, если она уже не действительна
    for change in Changes.objects.filter(group=groups.kod_of_group):
        if change.date_of_change < date:
            print('Данная дата меньше сегодняшней', change.date_of_change)
            change.delete()
            print('Запись удалена')
    zamena = Changes.objects.filter(group=groups.kod_of_group)
    group = Group.objects.filter(group_name=gruppa)
    group = group[0]
    return render(request, 'user_raspisanie/view_changes.html', {'zamena': zamena, 'group': group})


#Функция вызывает расписание на сегодняшний день
def raspis_today(request, pk):
    groups = get_object_or_404(Group, kod_of_group=pk)
    week_day = datetime.date.today().weekday()+1
    date = datetime.date.today()
    #Данный блок кода присваивает переменной значения расписания в завимости от четности недели
    chetnost = False
    start_sem = Start_semestr_date.objects.filter()
    start_semestr_date = start_sem[0].date.isocalendar()[1]
    #Если неделя начала семестра четная, то инвертируется
    if start_semestr_date % 2 == 0:
        if datetime.date.today().isocalendar()[1] % 2 == 1:
            chetnost = True
        else:
            chetnost = False
    #Если неделя начала семестра нечетная, то ничего не меняется
    else:
        if datetime.daate.today().isocalendar()[1] % 2 == 1:
            chetnost = False
        else:
            chetnost = True
    if chetnost == True:
        raspis = Raspisanie.objects.filter(group=groups.kod_of_group, day_of_week=week_day).exclude(parity=False, obe_nedeli=False)
    else:
        raspis = Raspisanie.objects.filter(group=groups.kod_of_group, day_of_week=week_day).exclude(parity=True)
    #Ищет все замены на сегодня
    zamena = Changes.objects.filter(group=groups.kod_of_group, date_of_change=date)
    check = False
    #Переменная для добавления записей с заменами
    dopoln_para = []
    order_para = []
    group_name = Raspisanie.objects.filter(group=groups)
    group_name = group_name[0]
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
            dopoln_para.append(Raspisanie(day_of_week= para.day_of_week, parity = para.parity, obe_nedeli = para.obe_nedeli, discipline = zam.discipline, group = zam.group, pair_number = zam.pair_number, teacher = zam.teacher, auditory = zam.auditory))

    for para in dopoln_para:
        for check_para in raspis:
            if para.pair_number.pair_number < check_para.pair_number.pair_number:
                order_para.append(para)
                break

    for para in raspis:
        order_para.append(para)
    for para in dopoln_para:
        if para.pair_number.pair_number > raspis[len(raspis)-1].pair_number.pair_number:
            order_para.append(para)
    return render(request, 'user_raspisanie/raspis_today.html', {'raspis': order_para, 'group_name': group_name,})



def raspis_tom(request, pk):
    groups = get_object_or_404(Group, kod_of_group=pk)
    week_day = datetime.date.today().weekday()+2
    if week_day > 7:
        week_day = week_day - 7
    date = datetime.date.today()
    #Данный блок кода присваивает переменной значения расписания в завимости от четности недели
    date += datetime.timedelta(days=1)
    chetnost = False
    start_sem = Start_semestr_date.objects.filter()
    start_semestr_date = start_sem[0].date.isocalendar()[1]
    print(start_semestr_date)
    #Если неделя начала семестра четная, то инвертируется
    if start_semestr_date % 2 == 0:
        if datetime.date.today().isocalendar()[1] % 2 == 1:
            chetnost = True
        else:
            chetnost = False
    #Если неделя начала семестра нечетная, то ничего не меняется
    else:
        if datetime.daate.today().isocalendar()[1] % 2 == 1:
            chetnost = False
        else:
            chetnost = True
    if chetnost == True:
        raspis = Raspisanie.objects.filter(group=groups.kod_of_group, day_of_week=week_day).exclude(parity=False, obe_nedeli=False)
    else:
        raspis = Raspisanie.objects.filter(group=groups.kod_of_group, day_of_week=week_day).exclude(parity=True)
        #Ищет все замены на завтра
    zamena = Changes.objects.filter(group=groups.kod_of_group, date_of_change=date)
    check = False
    #Переменная для добавления записей с заменами
    dopoln_para = []
    #Переменная используется для сортировки пар
    order_para = []
    group_name = Raspisanie.objects.filter(group=groups)
    group_name = group_name[0]
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
            dopoln_para.append(Raspisanie(day_of_week= para.day_of_week, parity = para.parity, obe_nedeli = para.obe_nedeli, discipline = zam.discipline, group = zam.group, pair_number = zam.pair_number, teacher = zam.teacher, auditory = zam.auditory))

    for para in dopoln_para:
        for check_para in raspis:
            if para.pair_number.pair_number < check_para.pair_number.pair_number:
                order_para.append(para)
                break

    for para in raspis:
        order_para.append(para)
    for para in dopoln_para:
        if para.pair_number.pair_number > raspis[len(raspis)-1].pair_number.pair_number:
            order_para.append(para)

    return render(request, 'user_raspisanie/raspis_tomorrow.html', {'raspis': order_para, 'dop_para': dopoln_para, 'chetnost': chetnost, 'group_name': group_name})
