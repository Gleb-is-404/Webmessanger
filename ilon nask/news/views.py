from django.shortcuts import render
from .models import chat, user
from django.http import JsonResponse
import django.contrib.auth
from urllib.parse import unquote
from django.views.decorators.http import require_http_methods
from django.core.management import call_command
import base64
'''
from .forms import PostForm
from django.views.generic import DetailView, UpdateView, DeleteView'''
from django.http import HttpResponse
# Create your views here.
import copy
import json
import io
import sys

'''user.objects.all().delete()'''
# Establish a connection to your MySQL database
def func_do(inp, request):
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
def data_saver(inp, request):
    int_info.objects.create(function_name=inp['function_name'], function_description=inp['function_description'], function_input=inp['function_input'], function_function=inp['function_function'], function_tags=inp['function_tags'])
    '''int_info.objects.create(function_name='ijoj', function_description='jkllk', function_input=['j90', 'jol'], functipython manage.py runserveron_function='jkjkj')'''
    return inp
def registrator(inp, request):
    users.objects.create(name=inp['name'], surname=inp['surname'], email_address=inp['email'], points=100)
    '''int_info.objects.create(function_name='ijoj', function_description='jkllk', function_input=['j90', 'jol'], function_function='jkjkj')'''
    return inp
def deleter(inp, request):
    if inp['mon']=='delete' and chat.objects.filter(id=inp['del_id'])[0].name==request.session['user_data']:
        chat.objects.filter(id=inp['del_id']).delete()
    if inp['mon']=='change' and chat.objects.filter(id=inp['del_id'])[0].name==request.session['user_data']:
        n=chat.objects.filter(id=inp['del_id'])[0]
        n.text=inp['text']
        n.save()
    if inp['mon']=='send':
        image_file = request.FILES.get('image')
        print(image_file)
        if image_file:
            with open('static/image/image.jpg', 'wb+') as destination:
                for chunk in image_file.chunks():
                    destination.write(chunk)
        chat.objects.create(name=inp['name'], text=inp['text'], like=0, files=image_file )
    if inp['mon']=='repost':
        chat.objects.create(name=inp['name'], text=inp['text'], like=inp['del_id'])
    return inp
def chat_loader(inp, request):
    inp['chat_feald']=''
    for x in list(chat.objects.all().order_by('id')):
        n=x.text.replace("\n", "<br>")
        if x.like==0 or list(chat.objects.filter(id=x.like))==[]:
            inp['chat_feald']+=f'<button id={x.id} oncontextmenu="panel(); change_log({x.id});" style="text-align: left;">{x.name}| {n}</button><b style="font-size: small;">{str(x.create_time)[5:16]}</b><div onclick="data_set[\'emo\']=\'{x.id}\';send(\'emotion\');">{len(x.emo)}👍</div><br>'
        else:
            y=chat.objects.filter(id=x.like)[0]
            m=y.text.replace("\n", "<br>")
            inp['chat_feald']+=f'<button style="border:solid; text-align: left;" onclick="document.getElementById({y.id}).scrollIntoView({{behavior:\'smooth\'}})">{y.name}| {m}_</button><b style="font-size: small;">{str(y.create_time)[5:16]}</b><br><b>↪⇾⇾⇾⇾</b><button id={x.id} oncontextmenu="panel(); change_log({x.id})" style="text-align: left;">{x.name}| {n}</button><b style="font-size: small;">{str(x.create_time)[5:16]}</b><div onclick="data_set[\'emo\']=\'{x.id}\';send(\'emotion\');">{len(x.emo)}👍</div><br>'
        inp['chat_feald']+=f'<img src="/media/{x.files}" alt="Image" width="70vw" height="70vw"><br>'
    inp['chat_feald']+="<div id=end></div>"
    return inp
def emotion(inp, request):
    a = list(chat.objects.filter(id=inp['emo']))[0]

    e = list(a.emo)  # Make a copy of the list
    if not request.session['user_data'] in e:
        e.append(request.session['user_data'])
        a.emo = e  # Update the 'emo' attribute
        a.save()  # Save the changes to the database
    return inp
def save(inp, request):
    if list(user.objects.filter(password=inp['password']))==[]:
        user.objects.create(name=inp['name'], password=inp['password'])
    return inp
def send(inp, request):
    chat.objects.create(name=inp['name'], text=inp['text'], like=0, files=inp['file'])
    return inp
function_list={'data_saver':data_saver, 'func_do':func_do, 'save':save, 'registrator':registrator, 'send':send, 'chat_loader':chat_loader, 'deleter':deleter, 'emotion':emotion}
def handle(request):
    x = json.loads(request.POST.get('data'))
    return JsonResponse({'out':function_list[x['function']](x, request)})
def handle_request(request):
    if request.method == 'POST':

        try:
            # Get data from the POST request
            data = json.loads(request.body.decode('-32'))

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

    return render(request, 'news/information.html', {'name':x, 'h':0})
    '''if x!='':
        request.session['user_data'] = x
    if x=='' and 'user_data' in dict(request.session):
        x=request.session['user_data']
    if list(user.objects.filter(password=request.session['user_data']))!=[]:
        return render(request, 'news/information.html', {'name':x})'''
