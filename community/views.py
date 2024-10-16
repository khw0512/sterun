from datetime import datetime
import math
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render
import requests
import calendar
from community.models import ContactUs
from events.models import GuestRun
from rental.models import Reservation

def index(request):
    guestruns = GuestRun.objects.filter(completed=False).order_by('end_date')[:3]
    guestrun = GuestRun.objects.filter(completed=False).order_by('end_date')[:1]
    context={"guestruns" : guestruns, "guestrun":guestrun}

    return render(request,"index.html", context)

def about_us(request):
    return render(request,"about.html")

def cookie_policy(request):
    return render(request,"modal/cookie_policy.html")

def privacy_policy(request):
    return render(request,"modal/privacy_policy.html")

def terms_of_services(request):
    return render(request,"modal/terms_of_services.html")

def mate_guide(request, pg):
    return render(request,"guide/page"+pg+".html")

def events(request):
    events = GuestRun.objects.filter(completed=False).exclude(status="ST1").order_by("status","-end_date")
    lenofevents = len(events)
    page = int(request.GET.get('p', 1)) #없으면 1로 지정
    paginator = Paginator(events, 5) #한 페이지 당 몇개 씩 보여줄 지 지정 
    events = paginator.get_page(page)
    if lenofevents % 5 == 0 :
        page_list = list(range(1,(lenofevents//5)+1))
    else:
        page_list = list(range(1,(lenofevents//5)+2))
    context = {"events": events,"len":lenofevents,"page_list":page_list}
    return render(request,"event.html", context)

def event_detail(request, pk):
    event = GuestRun.objects.filter(event_id=pk)

    context = {"event":event}
    return render(request,"event_detail.html", context)

def rental_items(request):
    return render(request,"rental.html")

def search(request):
    return render(request,"search.html")

def contact_us(request):
    return render(request,"contact.html")

def data(request):
    reservation = Reservation.objects.all().order_by("status","-end_date")
    context = {"reservation": reservation}
    return render(request, "admin/data.html", context)

def event_table(request):
    event = GuestRun.objects.all().order_by("status","-end_date")
    context = {"events": event}
    return render(request, "admin/event-table.html", context)

def mypage(request, pk):
    reservation = Reservation.objects.all()
    if request.method == "GET":
        result = reservation.filter(reserv_id=pk)
        if result: 
            sub_total = result.values()[0]["amount"]
            status = result.values()[0]["status"]
            delivery = result.values()[0]["delivery"]
            event_id = result.values()[0]["event_id"]
            try: 
                guestrun = GuestRun.objects.filter(pk=event_id)
                ticket_amount = guestrun.values()[0]['amount']
            except:
                ticket_amount = 0
            if delivery == True:
                delivery_amount = 5
            else:
                delivery_amount = 0
            amount = sub_total + delivery_amount + ticket_amount
            context = {"result_len": len(result), "id": pk, "sub_total":sub_total,"amount":amount,"delivery":delivery, "status":status, "event_id":event_id, "ticket_amount":ticket_amount, "result": result}
            return render(request, "mypage.html", context)
        else:
            context = {"result":"noresult"}
            return render(request, "search.html", context)
    else:
        return render(request,"mypage.html",{"result":False})

def inquiry(request):
    if request.method == "POST":
        id = "q-" + datetime.now().strftime("%Y%m%dT%H%M%S")
        inquiry = ContactUs(
            q_id=id,
            username=request.POST.get("username"),
            email=request.POST.get("email"),
            shortq=request.POST.get("shortq"),
            category=request.POST.get("category"),
        )

        inquiry.save()

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
                "message": "새로운 문의가 접수되었습니다. 문의자: "
                + str(request.POST.get("username"))
            },
        )

        # 요청 결과 출력
        print(response.text)

        return redirect("community:index")
    else:
        return render(request, "index.html")

def check(request):
    if request.method == "POST":
        reservation_id = request.POST["reservation_id"]
        reservation = Reservation.objects.filter(pk=reservation_id)
        if len(reservation) == 1:
            results = Reservation.objects.get(pk=reservation_id)
            return redirect("community:mypage", results.pk)
        elif len(reservation_id) == 0:
            return redirect("community:mypage", "blank")
        else:
            return redirect("community:mypage", "noresult")
    else:
        return render(
            request, "mypage.html", {"reservation": reservation, "checked": False}
        )
    
def email(request):
    subject = 'Thank you for registering to our site'
    message = 'It means a world to us'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['mylves@hanmail.net']
    send_mail(subject, message, email_from, recipient_list)
    return redirect('community:index')




