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

import json
import io
import sys
def first_page(request):
    return render(request, 'html/gl.html')
