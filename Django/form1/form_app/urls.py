from django.urls import path
from form_data.views import Form_data

urlpatterns = [
    path('/form', Form_data , name='form-data'),
]