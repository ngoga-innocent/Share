import stripe
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
stripe.api_key = settings.STRIPE_SECRET_KEY

def payment_page(request):
    return render(request, './payment.html', {'stripe_public_key': settings.STRIPE_PUBLIC_KEY})

@csrf_exempt
def create_payment_intent(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        amount = data.get('amount', 0)
        if amount <= 0:
                return JsonResponse({'error': 'Invalid amount'}, status=400)
        try:
            intent = stripe.PaymentIntent.create(
                amount=amount,  # Amount in cents (e.g., $10.00)
                currency='usd',
                payment_method_types=['card'],
            )
            return JsonResponse({'client_secret': intent.client_secret})    
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
@method_decorator(csrf_exempt, name='dispatch')
class MomoPayment(View):

    def authenticate(self):
        url = "https://payments.paypack.rw/api/auth/agents/authorize"
        payload = {
            "client_id": "7adeb2ec-2b76-11f0-890a-dead131a2dd9",
            "client_secret": "692dc84ed0e6ac96d5abc73a0e1d687fda39a3ee5e6b4b0d3255bfef95601890afd80709"
        }
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }

        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # raises error if failed
        return response.json()

    def post(self, request):
        try:
            data = json.loads(request.body)
            phone = data.get('phone')
            amount = data.get('amount')

            if not phone or not amount:
                return JsonResponse({'status': 'error', 'message': 'Phone and amount are required'}, status=400)

            print("Received data:", phone, amount)

            auth = self.authenticate()
            token = auth.get("access")

            if not token:
                return JsonResponse({'status': 'error', 'message': 'Authentication failed'}, status=401)

            url = "https://payments.paypack.rw/api/transactions/cashin"
            payload = {
                "amount": int(amount),
                "number": phone
            }
            headers = {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'Authorization': f'Bearer {token}',
            }

            response = requests.post(url, headers=headers, json=payload)
            result = response.json()
            print("Paypack Response:", result)

            return JsonResponse({'status': 'success', 'paypack_response': result})

        except requests.RequestException as e:
            print("API Error:", e)
            return JsonResponse({'status': 'error', 'message': 'Failed to reach Paypack API'}, status=502)

        except Exception as e:
            print("Internal Error:", e)
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
