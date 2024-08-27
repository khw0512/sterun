from django.shortcuts import redirect, render
import requests
import json

from rental.models import Reservation


def paypal(request):
    return render(request, "paypal/paypal_test.html")


def payment(request, pk, amount):

    reservation = Reservation.objects.get(pk=pk)
    print(reservation)
    # reservation.update(status="ST3")

    data_token = {
        "grant_type": "client_credentials",
    }

    response_token = requests.post(
        "https://api-m.sandbox.paypal.com/v1/oauth2/token",
        data=data_token,
        auth=(
            "AQlqTdcOGeH2fDUDWVNJVguF-ovRUwYBk8r0NAciDMAIki9q8-JEcFazT-79-mQKyWMNOIg9e3JJZRku",
            "ECZMjMFupOl752UrYbWqOywHubc5cwmyzNtiYV0GP0XbdYV9AfVpRQ7HVaIrtuWsXMWOhH0S6kOObbQO",
        ),
    )

    print(json.loads(response_token.text)["access_token"])
    token = json.loads(response_token.text)["access_token"]

    headers = {
        "Content-Type": "application/json",
        # "PayPal-Request-Id": "7b92603e-77ed-4896-8e78-5dea2050476a",
        "Authorization": "Bearer " + token,
    }

    data_pay = (
        '{ "intent": "CAPTURE", "purchase_units": [ { "reference_id": "d9f80740-38f0-11e8-b467-0ed5f89f718b", "amount": { "currency_code": "USD", "value":'
        + str(amount)
        + ' } } ], "payment_source": { "paypal": { "experience_context": { "payment_method_preference": "IMMEDIATE_PAYMENT_REQUIRED", "brand_name": "STERUN Web", "locale": "en-US", "landing_page": "LOGIN", "shipping_preference": "NO_SHIPPING", "user_action": "PAY_NOW", "return_url": "https://sterun.kr/paypal/check-payment/'
        + pk
        + '", "cancel_url": "https://sterun.kr" } } } }'
    )

    response_pay = requests.post(
        "https://api-m.sandbox.paypal.com/v2/checkout/orders",
        headers=headers,
        data=data_pay,
    )

    print(json.loads(response_pay.text)["links"][1]["href"])
    url = json.loads(response_pay.text)["links"][1]["href"]
    print(pk)

    return redirect(url)


def checkPayment(request, pk):
    reservation = Reservation.objects.filter(reserv_id=pk)
    print("reserv")
    print(reservation)
    reservation.update(status="ST3")
    return redirect("community:mypage", pk)
