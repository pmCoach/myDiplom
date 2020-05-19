from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

def group_select(request):

    groups = Group.objects.order_by('group_name')
    print(groups)
    return render(request, 'user_raspisanie/raspisanie.html', {'groups': groups})


def view_raspis(request, pk):
    groups = get_object_or_404(Group, kod_of_group=pk)
    raspis = Raspisanie.objects.filter(group=groups.kod_of_group)
    group_name = raspis[0]
    chetnoe = raspis.filter(parity=True)
    nechetnoe = raspis.filter(parity=False)
    return render(request, 'user_raspisanie/view_raspisanie.html', {'raspis': raspis, 'group_n': group_name, 'chetnoe': chetnoe, 'nechetnoe': nechetnoe})


def view_changes(request, gruppa):
    groups = get_object_or_404(Group, group_name=gruppa)
    zamena = Changes.objects.filter(group=groups.kod_of_group)
    return render(request, 'user_raspisanie/view_changes.html', {'zamena': zamena})
