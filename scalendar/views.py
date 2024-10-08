from django.shortcuts import render
from django.http import JsonResponse
import calendar
from datetime import datetime, date

from events.models import GuestRun

yearNow = datetime.now().year
monthNow = datetime.now().month

def schedule(request,id):

    month_int = int(id)

    guestruns = GuestRun.objects.values().filter(completed=False).filter(start_date__month=month_int).filter(manager='2')
    print(len(guestruns))
    if guestruns:
        start_month = guestruns[0]['start_date'].month
        start_day = guestruns[0]['start_date'].day
        end_month = guestruns[0]['end_date'].month
        end_day = guestruns[0]['end_date'].day
    else:
        start_month = None
        start_day = None
        end_month = None
        end_day = None


    if start_month == monthNow: 
        start_day = start_day
    else:
        start_day = 1
    if end_month == monthNow:
        end_day == end_day
    else:
        end_day == 31
    
    event_period = [start_day,end_day]

    cal = calendar.monthcalendar(yearNow, month_int)

    data_dic = {}
    data = {}

    count=0

    data_dic={'week1':[],'week2':[],'week3':[],'week4':[],'week5':[],'week6':[],}

    for k in cal:
        count+=1
        for i in k:
            if start_day != None and end_day !=None:
                if i >= start_day and i <=end_day:
                    data_dic['week'+str(count)].append([i,1])
                else:
                    data_dic['week'+str(count)].append([i,0])
            else:
                data_dic['week'+str(count)].append([i,0])


    context = {
        'events':guestruns,
        'week_data':cal,
        'year':yearNow,
        'month':month_int,
        'week_data_dic':data_dic,
    }
    return render(request, 'schedule.html', context)

