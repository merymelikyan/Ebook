from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Message


@csrf_exempt
def receive_message(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        

        if name and email :
            Message.objects.create(name=name, email=email)
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Missing data'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})


