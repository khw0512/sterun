from datetime import datetime
from django.shortcuts import get_object_or_404, redirect, render
import requests
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from events.models import GuestRun
from items.models import Item
from rental.forms import ReservationForm
from rental.models import Reservation
from scalendar.models import Days


def rental_register(request):
    event = GuestRun.objects.filter(completed=False)
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
        if request.POST.get("event_date") != "":
            event_date = request.POST.get("event_date")
        else:
            event_date = None
        if request.POST.get("event_time") != "":
            event_time = request.POST.get("event_time")
        else:
            event_time = None

        username = request.POST.get("username")
        id = username+"_item_" + datetime.now().strftime("T%H%M%S")
        email = request.POST.get("email")
        if request.POST.get("delivery") == 'on':
            delivery = True
        else:
            delivery = False

        reservation = Reservation(
            reserv_id=id,
            username=username,
            email=email,
            address=request.POST.get("address"),
            top=top,
            bottom=bottom,
            shoes=shoes,
            bag=bag,
            delivery = delivery,
            start_date=request.POST.get("start_date"),
            start_time=request.POST.get("start_time"),
            end_date=request.POST.get("end_date"),
            end_time=request.POST.get("end_time"),
            event=event_data,
            event_date = event_date,
            event_time = event_time,
            message=request.POST.get("message"),
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
        return render(request, "rental-form.html", context)
    
def update(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    form = ReservationForm(request.POST, request.FILES, instance=reservation)
    if request.method == "POST":
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.save()
            return redirect("community:data")
        else:
            return redirect("community:data")
    else:
        form = ReservationForm(instance=reservation)
        if reservation.start_date != None or reservation.end_date !=None:
            days = (reservation.end_date-reservation.start_date).days
        else:
            days = 0
        shoes_amount = 0
        top_amount = 0
        bottom_amount = 0
        bag_amount = 0
        if reservation.shoes != None and days < 5:
            shoes_amount= 10+3*(days-1)
        elif reservation.shoes == None:
            shoes_amount=0
        else:
            shoes_amount= 20
        if reservation.top != None and days<5:
            top_amount= 5+2*(days-1)
        elif reservation.top == None:
            top_amount=0
        else:
            top_amount= 10
        if reservation.bottom != None and days<5:
            bottom_amount= 5+2*(days-1)
        elif reservation.bottom == None:
            bottom_amount=0
        else:
            bottom_amount= 10
        if reservation.bag != None and days<5:
            bag_amount= 3+1*(days-1)
        elif reservation.bag == None:
            bag_amount=0
        else:
            bag_amount= 5
        return render(request, "admin/edit.html", {"form": form, "days":days, "shoes_amount":shoes_amount, "top_amount":top_amount, "bottom_amount":bottom_amount, "bag_amount":bag_amount, "item_amount":shoes_amount+top_amount+bottom_amount+bag_amount})
    
def delreserv(request, pk):
    if request.method == "GET":
        reservation = Reservation.objects.get(pk=pk)
        days = Days.objects.filter(reservation_id=reservation.reserv_id)
        days.delete()
        reservation.delete()
        return redirect("community:data")
    else:
        return redirect("community:data")
    
def delpage(request, pk):
    reservation = Reservation.objects.filter(pk=pk)
    return render(request, "admin/delete.html", {"reservation": reservation})