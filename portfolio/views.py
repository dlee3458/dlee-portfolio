from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Message
from .forms import MessageForm

def home(request):
    return render(request, 'portfolio/index2.html')

def about(request):
    return render(request, 'portfolio/about.html')

def projects(request):
    return render(request, 'portfolio/projects.html')

def skills(request):
    return render(request, 'portfolio/skills.html')

def contact(request):
    if request.is_ajax() and request.method == 'POST':
        new_message = Message()
        new_message.email = request.POST['email']
        new_message.subject = request.POST['subject']
        new_message.body = request.POST['body']
        new_message.save()
        messages.success(request, 'Message sent!')
        
        html = render_to_string('portfolio/messages.html', request=request)
        return JsonResponse({'message': html})

    else:
        return render(request, 'portfolio/contact.html')

