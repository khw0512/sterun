from datetime import datetime
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.shortcuts import redirect, render
import requests

from events.models import GuestRun
from items.models import Item
from rental.models import Reservation
from .forms import WriteForm

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
    events = {"events":event}
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

        username = request.POST.get("username")
        id = username + datetime.now().strftime("T%H%M%S")
        email = request.POST.get("email")

        reservation = Reservation(
            reserv_id=id,
            username=username,
            email=email,
            message=request.POST.get("message"),
            start_date=request.POST.get("start_date"),
            start_time=request.POST.get("start_time"),
            end_date=request.POST.get("end_date"),
            end_time=request.POST.get("end_time"),
            top=top,
            bottom=bottom,
            shoes=shoes,
            bag=bag,
            address=request.POST.get("address"),
            event=event_data,
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
        return render(request, "run-form.html", events)