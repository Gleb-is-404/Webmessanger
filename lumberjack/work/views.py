from django.shortcuts import render

from django.http import JsonResponse
import django.contrib.auth
from urllib.parse import unquote
from django.views.decorators.http import require_http_methods


'''
from .forms import PostForm
from django.views.generic import DetailView, UpdateView, DeleteView'''
from django.http import HttpResponse
# Create your views here.
from .models import data
from django.forms.models import model_to_dict
import json
import io
import sys
#data.objects.all().delete()

def first_page(request):
    info={'data':data.objects.all()}

    return render(request, 'html/gl.html', info)
def second_page(request):
    if request.method == 'POST':

        n=data(
            name = request.POST.get('name'),
            surname = request.POST.get('surname'),
            age = request.POST.get('age'),
            gender = request.POST.get('gender'),
            n1 = request.POST.get('1'),
            n2 = request.POST.get('2'),
            n3 = request.POST.get('3'),
            n4 = request.POST.get('4'),
            n5 = request.POST.get('5'),
            n6 = request.POST.get('6'),
            n7 = request.POST.get('7'),
            n8 = request.POST.get('8'),
            n9 = request.POST.get('9'),
            n10 = request.POST.get('10'),
            n11 = request.POST.get('11'),
            n12 = request.POST.get('12'),
            n13 = request.POST.get('13'),
            n14 = request.POST.get('14'),
            n15 = request.POST.get('15'),
            n16 = request.POST.get('16'),
            n17 = request.POST.get('17'),
            n18 = request.POST.get('18'),
            n19 = request.POST.get('19'),
            n20 = request.POST.get('20'),
            n21 = request.POST.get('21'),
            n22 = request.POST.get('22'),
            n23 = request.POST.get('23'),
            )
        n.save()
            

    return render(request, 'html/questions.html')
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow: /admin/",
        "Disallow: /private-messages/",
        "Allow: /forum/",
        "Allow: /chat/",
        "Allow: /luumberjack/",
         # If you have a sitemap
        # Add more rules as needed
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")