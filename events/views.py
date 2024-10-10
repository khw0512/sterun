from datetime import datetime, date
from django.http import JsonResponse
from django.conf import settings
from django.core.mail import send_mail
from django.core import serializers
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.shortcuts import get_object_or_404, redirect, render
import requests
import calendar
import json

from events.models import GuestRun
from items.models import Item
from rental.models import Reservation
from .forms import *

def event_write(request):
    form = WriteForm(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            
            guestrun = form.save()
            guestrun.save()
            return redirect("community:events")
        else:
            return redirect("community:events")
    else:
        form = WriteForm()
        return render(request, "admin/event_write.html", {"form": form})

def event_register(request, pk):
    event= GuestRun.objects.filter(event_id=pk)
    shoes = Item.objects.filter(category='shoes')
    bag = Item.objects.filter(category='bag')
    top = Item.objects.filter(category='top')
    bottom = Item.objects.filter(category='bottom')
    context = {"events":event, "shoeses":shoes, "bags":bag, "tops":top, "bottoms":bottom}
    if request.method == "POST":
        if Item.objects.filter(pk=request.POST.get("top")).exists():
            top = Item.objects.get(pk=request.POST.get("top"))
        else:
            top = None

        if Item.objects.filter(pk=request.POST.get("bottom")).exists():
            bottom = Item.objects.get(pk=request.POST.get("bottom"))
        else:
            bottom = None

        if Item.objects.filter(pk=request.POST.get("shoes")).exists():
            shoes = Item.objects.get(pk=request.POST.get("shoes"))
        else:
            shoes = None
        if Item.objects.filter(pk=request.POST.get("bag")).exists():
            bag = Item.objects.get(pk=request.POST.get("bag"))
        else:
            bag = None
        if request.POST.get("event") != "":
            event_data = GuestRun.objects.get(pk=request.POST.get("event"))
        else:
            event_data = None
        if request.POST.get("start_date") != "":
            start_date = request.POST.get("start_date")
        else:
            start_date = None
        if request.POST.get("end_date") != "":
            end_date = request.POST.get("end_date")
        else:
            end_date = None
        if request.POST.get("event_date") != "":
            event_date = request.POST.get("event_date")
        else:
            event_date = None
        if request.POST.get("delivery") == 'on':
            delivery = True
        else:
            delivery = False
        username = request.POST.get("username")
        id = username +"_run_"+datetime.now().strftime("T%H%M%S")
        email = request.POST.get("email")

        reservation = Reservation(
            reserv_id=id,
            username=username,
            email=email,
            message=request.POST.get("message"),
            start_date=start_date,
            start_time=request.POST.get("start_time"),
            end_date=end_date,
            end_time=request.POST.get("end_time"),
            top=top,
            bottom=bottom,
            shoes=shoes,
            bag=bag,
            address=request.POST.get("address"),
            event=event_data,
            event_date = event_date,
            event_time = request.POST.get("event_time"),
            delivery = delivery
        )

        reservation.save()

        # LINE Notify 액세스 토큰
        line_token = "keAeVnqfCkgFuxZSRBGUwymSN9aqpQC5NXV68GoOVLB"

        # LINE Notify API 엔드포인트 URL
        url = "https://notify-api.line.me/api/notify"

        # 이미지 파일 열기

        # POST 요청 보내기
        response = requests.post(
            url,
            headers={"Authorization": "Bearer " + line_token},
            data={
                "message": "새로운 예약이 접수되었습니다. 예약자: "
                + str(request.POST.get("username"))
            },
        )

        print(response)

        # E-mail 보내기
        html_message = render_to_string(
                "email.html",
                {"username": username, "id": id},
            )
        plain_message = strip_tags(html_message)
        
        subject = "[STERUN] Thank you for reservation :)"
        '''message = "Your Reaservation id is" +" "+ id'''
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ["sterun@joollab.com",email]
        send_mail(subject, plain_message, email_from, recipient_list, html_message=html_message,)

        return redirect("community:mypage", id)
    else:
        return render(request, "run-form.html", context)
    
def update_event(request, pk):
    event = get_object_or_404(GuestRun, pk=pk)
    form = UpdateForm(request.POST, request.FILES, instance=event)
    if request.method == "POST":
        if form.is_valid():
            lang = form.cleaned_data.get("lang")
            print(lang)
            event = form.save(commit=False)
            event.save()
            return redirect("community:event_table")
        else:
            return redirect("community:event_table")
    else:
        form = UpdateForm(instance=event)
        return render(request, "admin/event_edit.html", {"form": form} )
    
def delevent(request, pk):
    if request.method == "GET":
        reservation = GuestRun.objects.get(pk=pk)
        reservation.delete()
        return redirect("community:event_table")
    else:
        return redirect("community:event_table")
    
def deleventpage(request, pk):
    event = GuestRun.objects.filter(pk=pk)
    return render(request, "admin/event_del.html", {"events": event})

year_now = datetime.now().year
month_now = datetime.now().month
day_now = datetime.now().day

def eventInfo(request):
    month = request.GET.get('month')
    day = request.GET.get('day')
    user_id = request.GET.get('user_id')
    if day !="":
        check_date= date(int(year_now),int(month),int(day))
        print(check_date)
    else:
        check_date= date(2000,1,1)
    guestruns = GuestRun.objects.filter(completed=False).filter(start_date__month=month).filter(manager=user_id)
    print(len(guestruns))

    
    event_list=[]
    for i in guestruns:
        #start_date = guestruns.values()[0]['start_date']
        #end_date = guestruns.values()[0]['end_date']
        start_date = i.start_date
        end_date = i.end_date
        print(start_date)
        print(check_date)
        if start_date <= check_date and check_date <= end_date:
            #context = serializers.serialize("json", guestruns)
            event_list.append(i)
            print(event_list)
        else:
            event_list=event_list
    context = serializers.serialize("json", event_list)
    return JsonResponse(context, safe=False)