from django.shortcuts import render
import requests
from django.http import HttpResponse
def vishwa(request):
    response=requests.get('https://reqres.in/api/users?page=2').json()
    print(response)
    return render(request,'index.html',{'response':response})