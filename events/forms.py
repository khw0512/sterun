from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

from django import forms
from .models import GuestRun


class WriteForm(forms.ModelForm):
    class Meta:
        model = GuestRun

        LANGUAGE = (
            ("KO","Korean"),
            ("EN","English"),
            ("JP","Japanese"),
            ("CN","Chinese"),
        )

        fields = [
            "title",
            "manager",
            "start_date",
            "start_time",
            "end_date",
            "end_time",
            "image",
            "route_image",
            "map_link",
            "start_point",
            "level",
            "lang",
            "amount",
            "route",
            "desc",
        ]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "manager": forms.Select(attrs={"class": "form-control"}),
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
            "level": forms.Select(attrs={"class": "form-control"}),
            "lang" : forms.CheckboxSelectMultiple(attrs={"class":"form-lang"}, choices=LANGUAGE),
            "start_point": forms.TextInput(attrs={"class": "form-control"}),
            "amount": forms.NumberInput(attrs={"class": "form-control"}),
            "image": forms.FileInput(
                attrs={"id": "event-main-img", "class": "form-control"}
            ),
            "route_image" : forms.FileInput(
                attrs={"id": "event-route-img", "class": "form-control"}
            ),
            "map_link": forms.TextInput(attrs={"class": "form-control"}),
            "desc": SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}),
            "route": forms.TextInput(attrs={"class": "form-control"}),
        }
        labels = {
            "title":"이벤트 명",
            "manager":"매니저",
            "start_date":"시작일",
            "start_time":"시작시간",
            "end_date":"종료일",
            "end_time":"종료시간",
            "image":"메인 이미지",
            "start_point":"시작 지점",
            "route_image":"루트 이미지",
            "map_link":"네이버맵 링크",
            "level":"난이도",
            "lang":"언어(모두선택)",
            "amount":"참가비(달러)",
            "route":"루트 설명",
            "desc":"이벤트 설명",
        }

class UpdateForm(forms.ModelForm):
    class Meta:
        model = GuestRun

        LANGUAGE = (
            ("KO","Korean"),
            ("EN","English"),
            ("JP","Japanese"),
            ("CN","Chinese"),
        )

        fields = [
            "title",
            "manager",
            "start_date",
            "start_time",
            "end_date",
            "end_time",
            "image",
            "route_image",
            "map_link",
            "start_point",
            "level",
            "lang",
            "amount",
            "route",
            "participant",
            "desc",
            "status",
            "completed"
        ]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "manager": forms.Select(attrs={"class": "form-control"}),
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
            "level": forms.Select(attrs={"class": "form-control"}),
            "lang" : forms.CheckboxSelectMultiple(attrs={"class":"form-lang"}, choices=LANGUAGE),
            "start_point": forms.TextInput(attrs={"class": "form-control"}),
            "amount": forms.NumberInput(attrs={"class": "form-control"}),
            "image": forms.FileInput(
                attrs={"id": "event-main-img", "class": "form-control"}
            ),
            "route_image" : forms.FileInput(
                attrs={"id": "event-route-img", "class": "form-control"}
            ),
            "map_link": forms.TextInput(attrs={"class": "form-control"}),
            "desc": SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}),
            "route": forms.TextInput(attrs={"class": "form-control"}),
            "participant": forms.TextInput(attrs={"class": "form-control"}),
            "status": forms.Select(attrs={"class": "form-control"}),
            "completed":forms.CheckboxInput(attrs={"class": "form-control"}),
        }
        labels = {
            "title":"이벤트 명",
            "manager":"매니저",
            "start_date":"시작일",
            "start_time":"시작시간",
            "end_date":"종료일",
            "end_time":"종료시간",
            "image":"메인 이미지",
            "start_point":"시작 지점",
            "route_image":"루트 이미지",
            "map_link":"네이버맵 링크",
            "level":"난이도",
            "lang":"언어(모두선택)",
            "amount":"참가비(달러)",
            "route":"루트 설명",
            "participant":"참여자 리스트",
            "desc":"이벤트 설명",
            "status": "상태",
            "completed":"완료여부",
        }