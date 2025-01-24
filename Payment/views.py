import stripe
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
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
