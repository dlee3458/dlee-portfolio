from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Message
from .forms import MessageForm

def home(request):
    return render(request, 'portfolio/index.html', {'title': 'Full Stack Developer'})

def about(request):
    return render(request, 'portfolio/about.html', {'title': 'About Me'})

def projects(request):
    return render(request, 'portfolio/projects.html', {'title': 'Projects'})

def skills(request):
    return render(request, 'portfolio/skills.html', {'title': 'Skills'})

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
        return render(request, 'portfolio/contact.html', {'title': 'Contact Me'})

