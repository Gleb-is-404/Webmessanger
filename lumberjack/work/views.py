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
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow: /admin/",
        "Disallow: /private-messages/",
        "Allow: /forum/",
        "Allow: /chat/",
        "Sitemap: https://yourdomain.com/sitemap.xml",  # If you have a sitemap
        # Add more rules as needed
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")
