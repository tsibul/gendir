from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User

from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import default_storage
from django.template import loader
from django.urls import reverse

from .models import Persons, Positions, Task_types, Tasks
from django.contrib.auth import authenticate, login
from .forms import LoginForm
import datetime



@login_required
def index(request):
    tasks = Tasks.objects.filter(active=True).order_by('type', '-overal_priority')
    f_tasks = {}
    for task in tasks:
        if task.type not in f_tasks:
            f_tasks[task.type] = []
        f_tasks[task.type].append(task)
    task_len = []
    for tsk in f_tasks:
        task_len.append([tsk.id, len(f_tasks[tsk])])
    context = {'f_tasks': f_tasks, 'task_len': task_len}
    return render(request, 'gendir/index.html', context)


@login_required
def new_task(request):
    date_t = datetime.date.today()
    types = list(Task_types.objects.all())
    persons = list(Persons.objects.all())
    positions = list(Positions.objects.all())
    context = {'date_t': date_t, 'types': types, 'positions': positions, 'persons': persons}
    return render(request, 'gendir/new_task.html', context)


def add_task(request):
    name = request.POST['name']
    user = request.POST['user']
    user = User.objects.get(id=user)
    if name == '':
        date_t = datetime.date.today()
        types = list(Task_types.objects.all())
        persons = list(Persons.objects.all())
        positions = list(Positions.objects.all())
        context = {'date_t': date_t, 'types': types, 'positions': positions, 'persons': persons}
        return render(request, 'gendir/new_task.html', context)
    date_start = datetime.date.today()
    active = True
    person = request.POST['persons_0']
    person = Persons.objects.get(name=person)
    type = request.POST['types_0']
    type = Task_types.objects.get(name=type)
    position = request.POST['positions_0']
    position = Positions.objects.get(name=position)
    priority = int(request.POST['priority'])
    notes = request.POST['notes']
    try:
        last_report_file = request.FILES['last_report_file']
        file_name = str(date_start) + '_' + str(last_report_file.name)
        default_storage.save(file_name, last_report_file)
    except:
        last_report_file = ''
    last_report_summary = request.POST['last_report_summary']
    status = request.POST['status']
    to_do_first = request.POST['to_do_first']
    to_do_second = request.POST['to_do_second']
    other_effect = request.POST['other_effect']
    try:
        income_affect = request.POST['incomeChecked']
    except:
        income_affect = False
    try:
        expenses_affect = request.POST['expensesChecked']
    except:
        expenses_affect = False
    try:
        profit_affect = request.POST['profitChecked']
    except:
        profit_affect = False
    task_new = Tasks(date_start=date_start, name=name, active=active, person=person, type=type, position=position,
                     priority=priority, notes=notes, income_affect=income_affect, expenses_affect=expenses_affect,
                     profit_affect=profit_affect, other_effect=other_effect, to_do_first=to_do_first,
                     to_do_second=to_do_second, last_report_file=last_report_file,
                     last_report_summary=last_report_summary, status=status, log_person=user)
    income_monthly_effect = request.POST['income_monthly_effect']
    expenses_monthly_effect = request.POST['expenses_amount']
    profit_monthly_effect = request.POST['profit_amount']
    investments = request.POST['investments']
    investments_start = request.POST['investments_start']
    investments_period = request.POST['investments_period']
    monthly_expenses = request.POST['monthly_expenses']
    expenses_start = request.POST['expenses_start']
    expenses_period = request.POST['expenses_period']
    date_target = request.POST['date_target']
    current_date = request.POST['current_date']
    if task_new.income_affect and income_monthly_effect != '':
        task_new.income_monthly_effect = float(income_monthly_effect)
    if task_new.expenses_affect and expenses_monthly_effect != '':
        task_new.expenses_monthly_effect = float(expenses_monthly_effect)
    if task_new.profit_affect and profit_monthly_effect != '':
        task_new.profit_monthly_effect = float(profit_monthly_effect)
    if investments != '':
        task_new.investments = float(investments)
        try:
            task_new.investments_start = datetime.datetime.strptime(investments_start, '%Y-%m-%d').strftime('%Y-%m-%d')
            task_new.investments_period = int(investments_period)
        except:
            pass
    if monthly_expenses != '':
        task_new.monthly_expenses = monthly_expenses
        try:
            task_new.expenses_start = datetime.datetime.strptime(expenses_start, '%Y-%m-%d').strftime('%Y-%m-%d')
            task_new.expenses_period = int(expenses_period)
        except:
            pass
    try:
        overal_priority = priority*type.priority/10
        task_new.overal_priority = overal_priority
        task_new.date_target = datetime.datetime.strptime(date_target, '%Y-%m-%d').strftime('%Y-%m-%d')
        task_new.current_date = datetime.datetime.strptime(current_date, '%Y-%m-%d').strftime('%Y-%m-%d')
    except:
        pass
    task_new.save()
    task_id = task_new.id
    task_new.task_id = task_id
    task_new.save()
    date_t = datetime.date.today()
    types = list(Task_types.objects.all())
    persons = list(Persons.objects.all())
    positions = list(Positions.objects.all())
    context = {'date_t': date_t, 'types': types, 'positions': positions, 'persons': persons}
    return render(request, 'gendir/new_task.html', context)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def update_task(request, id):
    task_log = request.POST['task_log']
    user = request.POST['user']
    return HttpResponseRedirect(reverse('gendir/index.html'))

@login_required
def edit_task(request, id):
    date_t = datetime.date.today()
    types = list(Task_types.objects.all())
    persons = list(Persons.objects.all())
    positions = list(Positions.objects.all())
    current_task = Tasks.objects.get(id=id)
    context = {'task': current_task, 'types': types, 'persons': persons, 'positions': positions, 'date_t': date_t}
    return render(request, 'gendir/edit_task.html', context)

