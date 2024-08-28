from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = [
            "username",
            "email",
            "address",
            "start_date",
            "start_time",
            "end_date",
            "end_time",
            "top",
            "bottom",
            "shoes",
            "bag",
            "delivery",
            "event",
            "event_date",
            "event_time",
            "amount",
            "image",
            "message",
            "status",
            "completed",
            "paypal_link",
        ]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.TextInput(attrs={"class": "form-control"}),
            "message": forms.Textarea(attrs={"class": "form-control", "rows": 10}),
            "start_time": forms.TimeInput(
                attrs={"type": "time", "class": "form-control"}, format="%H:%M"
            ),
            "start_date": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "end_time": forms.TimeInput(
                attrs={"type": "time", "class": "form-control"}, format="%H:%M"
            ),
            "end_date": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "top": forms.Select(attrs={"class": "form-control"}),
            "bottom": forms.Select(attrs={"class": "form-control"}),
            "shoes": forms.Select(attrs={"class": "form-control"}),
            "bag": forms.Select(attrs={"class": "form-control"}),
            "event": forms.Select(attrs={"class": "form-control"}),
            "event_date": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "event_time": forms.TimeInput(
                attrs={"type": "time", "class": "form-control"}, format="%H:%M"
            ),
            "address": forms.TextInput(attrs={"class": "form-control"}),
            "amount": forms.NumberInput(attrs={"class": "form-control important"}),
            "image": forms.FileInput(
                attrs={"id": "image_field", "class": "form-control"}
            ),
            "status": forms.Select(attrs={"class": "form-control"}),
            "delivery": forms.CheckboxInput(attrs={"class": "form-control"}),
            "completed": forms.CheckboxInput(attrs={"class": "form-control"}),
            "paypal_link": forms.TextInput(attrs={"class": "form-control"}),
        }
        labels = {
            "username": "예약자",
            "email": "연락처",
            "message": "설명",
            "start_time": "체크인 시간",
            "start_date": "시작날짜",
            "end_time": "체크아웃 시간",
            "end_date": "종료날짜",
            "top": "상의",
            "bottom": "하의",
            "shoes": "운동화",
            "bag": "휴대폰 파우치",
            "event": "게스트 런 티켓",
            "event_date":"게스트 런 날짜",
            "event_time": "게스트런 시간",
            "image": "이미지",
            "address": "숙소 주소",
            "amount":"아이템 가격(티켓가격 제외)",
            "status": "상태",
            "delivery": "배송",
            "completed": "완료여부",
            "paypal_link": "페이팔 결제 링크",
        }
