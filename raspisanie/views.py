from django.shortcuts import render, get_object_or_404
from .models import *
import datetime

# Create your views here.

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
    zamena = Changes.objects.filter(group=groups.kod_of_group)
    group = zamena[0]
    return render(request, 'user_raspisanie/view_changes.html', {'zamena': zamena, 'group': group})


def raspis_tom(request, pk):
    groups = get_object_or_404(Group, kod_of_group=pk)
    return render(request, 'user_raspisanie/raspis_tomorrow.html', {})
