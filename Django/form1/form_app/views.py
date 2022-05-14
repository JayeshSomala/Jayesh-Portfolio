from django.shortcuts import render
import imp
from django.shortcuts import render
from form_app.models import Form
from django.http import JsonResponse

# Create your views here.
def Form_data(request):
    Form_data = Form.objects.all()
    data = {
        'Contact Details' : list(Form_data.values())
    }
    return JsonResponse(data)