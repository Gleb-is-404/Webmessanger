from django.shortcuts import render
from .models import chat, user
from django.http import JsonResponse
import django.contrib.auth
from urllib.parse import unquote
from django.views.decorators.http import require_http_methods
'''
from .forms import PostForm
from django.views.generic import DetailView, UpdateView, DeleteView'''
from django.http import HttpResponse
# Create your views here.
import mysql.connector
import json
import io
import sys
for x in list(chat.objects.all()):
    print(x.text, 'gg')
# Establish a connection to your MySQL database
def func_do(inp):
    locals().update(inp['function_exec'])
    original_stdout = sys.stdout
    sys.stdout = open('output.txt', 'w')
    result = exec(inp['function'])
    sys.stdout.close()
    sys.stdout = original_stdout
    with open('output.txt', 'r') as output_file:
        captured_output = output_file.read()
    inp['text']=captured_output
    return inp
def data_saver(inp):
    int_info.objects.create(function_name=inp['function_name'], function_description=inp['function_description'], function_input=inp['function_input'], function_function=inp['function_function'], function_tags=inp['function_tags'])
    '''int_info.objects.create(function_name='ijoj', function_description='jkllk', function_input=['j90', 'jol'], functipython manage.py runserveron_function='jkjkj')'''
    return inp
def registrator(inp):
    users.objects.create(name=inp['name'], surname=inp['surname'], email_address=inp['email'], points=100)
    '''int_info.objects.create(function_name='ijoj', function_description='jkllk', function_input=['j90', 'jol'], function_function='jkjkj')'''
    return inp
def chat_loader(inp):
    inp['chat_feald']=''
    for x in list(chat.objects.all()):
        inp['chat_feald']+=f'{x.name}: {x.text}<br>'
    return inp
def save(inp):
    if list(user.objects.filter(password=inp['password']))==[]:
        user.objects.create(name=inp['name'], password=inp['password'])
    return inp
def send(inp):
    chat.objects.create(name=inp['name'], text=inp['text'], like=0)
    return inp
function_list={'data_saver':data_saver, 'func_do':func_do, 'save':save, 'registrator':registrator, 'send':send, 'chat_loader':chat_loader}
def handle(request):
    x=json.loads(unquote(request.body))
    return JsonResponse({'out':function_list[x['function']](x['data'])})
def handle_request(request):
    if request.method == 'POST':

        try:
            # Get data from the POST request
            data = json.loads(request.body.decode('utf-8'))

            # Your processing logic here
            # ...

            # Return a JSON response
            response_data = {'status': 'success', 'message': 'Data received successfully', 'n':data}
            return JsonResponse(function_list[data['function']](data['data']))
        except Exception as e:
            # Log the exception for debugging
            print('Error:', e)
            return JsonResponse({'status': 'error', 'message': 'Internal Server Error'})
    else:
        # Handle other HTTP methods if needed
        return JsonResponse({'status': 'error', 'message': 'Invalid HTTP method'})
def add_data(request):
    print(request.session['user_data'])
    if list(users.objects.filter(email_address=request.session['user_data']))!=[]:
        return render(request, 'news/kek.html')
def signup(request):
    return render(request, 'news/cotolog.html')
def main_page(request):
    x = unquote(request.GET.get('x', ''))
    if x!='':
        request.session['user_data'] = x
    return render(request, 'news/main.html', {'email':x})

def signin(request):
    return render(request, 'news/signin.html')
def chats(request):
    x = unquote(request.GET.get('x', ''))
    if x!='':
        request.session['user_data'] = x
    if x=='' and 'user_data' in dict(request.session):
        x=request.session['user_data']
    if list(user.objects.filter(password=request.session['user_data']))!=[]:
        return render(request, 'news/information.html', {'name':x})
