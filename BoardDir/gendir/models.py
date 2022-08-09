from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator



class Positions (models.Model):
    """ board of director positions"""
    name = models.CharField(max_length=100)


class Persons (models.Model):
    """ persons with current positions """
    name = models.CharField(max_length=100)
    main_position = models.ForeignKey(Positions, models.SET_NULL, null=True)


class Task_types (models.Model):
    """ Area of the task (finance, sales etc.)
    priority — from 1 to 100 priority of task_type
    """
    name = models.CharField(max_length=100)
    priority = models.SmallIntegerField(default=10, validators=[MaxValueValidator(10), MinValueValidator(1)])


class Tasks (models.Model):
    """ All Tasks
    task_id — task id
    date_start — beginning of the task
    date_target — date of next report
    active — False if the Task closed
    status — comment to current Task status
    date_finish — date of closing task
    finish_reason — fulfilled or reason why rejected
    position — normal position for responsible person
    person — current responsible person
    current_date — last report date
    type — Task type
    name — Task name
    priority — from 1 to 10 priority of task
    overal_priority — Tasks.priority*Task_type.prority/10
    to_do_first, to_do_second — first to steps for solving
    notes — additional information
    income, expenses, profit _affect — True if influence on corresponding element
    income, expenses, profit _monthly_effect — amount of cashflow changes
    other_effect — if affects other busyness processes
    investments — investments amount in thsnds
    investments_start — date of first payment
    investments_period — in months
    monthly_expenses — monthly costs in thsnds
    expenses_period — period in months
    expenses_start — date of first payment
    last_report_file — last report for current task
    last_report_summary — last report summary
    last_log — summary of last changes
    log_person — who made changes
    """
    task_id = models.SmallIntegerField(default=0, help_text='task id')
    date_start = models.DateField(default='2022-08-05', help_text='beginning of the task')
    date_target = models.DateField(default='2022-08-05', help_text='date of next report')
    status = models.CharField(max_length=120, help_text=' comment to current Task status')
    active = models.BooleanField(default=True, help_text='False if the Task closed')
    date_finish = models.DateField(blank=True, null=True, help_text='date of closing task')
    finish_reason = models.CharField(max_length=120, help_text='fulfilled or reason why rejected')
    position = models.ForeignKey(Positions, models.SET_NULL, null=True, blank=True,
                                 help_text='normal position for responsible person')
    person = models.ForeignKey(Persons, models.SET_NULL, null=True, blank=True,
                               help_text='current responsible person')
    current_date = models.DateField(default='2022-08-05', help_text='last report date')
    type = models.ForeignKey(Task_types, models.SET_NULL, null=True, help_text='Task type')
    name = models.CharField(max_length=240, help_text='Task name')
    priority = models.SmallIntegerField(default=10, help_text='from 1 to 10 priority of task',
                                        validators=[MaxValueValidator(10), MinValueValidator(1)])
    overal_priority = models.DecimalField(max_digits=4, decimal_places=1, default=10.00,
                                          help_text='asks.priority*Task_type.prority/10')
    to_do_first = models.CharField(max_length=240, help_text='first step for solving')
    to_do_second = models.CharField(max_length=240, help_text='next step for solving')
    notes = models.CharField(max_length=240, help_text='additional information')
    income_affect = models.BooleanField(default=False, help_text='if affects on income')
    income_monthly_effect = models.FloatField(default=0, help_text='monthly income change')
    expenses_affect = models.BooleanField(default=False, help_text='if affects on expenses')
    expenses_monthly_effect = models.FloatField(default=0, help_text='monthly expenses change')
    profit_affect = models.BooleanField(default=False, help_text='if affects on profit')
    profit_monthly_effect = models.FloatField(default=0, help_text='monthly profit change')
    other_effect = models.CharField(max_length=240, blank=True, help_text='if affects other busyness processes')
    investments = models.FloatField(default=0, help_text='investments amount in thsnds')
    investments_start = models.DateField(blank=True, null=True, help_text='date of first payment')
    investments_period = models.IntegerField(default=0, help_text='in months')
    monthly_expenses = models.FloatField(default=0, help_text='monthly costs in thsnds')
    expenses_start = models.DateField(blank=True, null=True, help_text='date of first payment')
    expenses_period = models.IntegerField(default=0, help_text='period in months')
    last_report_summary = models.CharField(max_length=120, default='отчет', help_text='last report summary')
    last_report_file = models.FileField(blank=True, null=True, help_text='last report for current task')
    last_log = models.CharField(max_length=240, help_text='summary of last changes')
    log_date = models.DateField(default='2022-08-05', help_text='when task changed')
    log_person = models.ForeignKey(User, models.SET_NULL, null=True, blank=True, help_text='who made changes')



