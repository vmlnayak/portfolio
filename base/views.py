from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from base.forms import ContactForm
from django.core.mail import EmailMessage
from django.template.loader import get_template
from .models import Media_Post
# from django.views.generic import TemplateView
from . import forms

#for login
from django.contrib.auth import authenticate,login
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.generic import CreateView,TemplateView


# Create your views here.
def Home(request):
    return render(request,'base/home.html')

def Achievement(request):
    return render(request,'base/achievement.html')

def Media(request):
    post=Media_Post.objects.all()
    context={'topic':post}
    return render(request,'base/media.html',context)

class SignUp(CreateView):
    form_class=forms.UserCreateForm
    success_url=reverse_lazy('login')
    template_name='base/signup.html'

def Contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')
            # print(form_content)
            # Email the profile with the
            # contact information
            template =get_template('base/contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)
            print(content)
            # email = EmailMessage("New contact form submission",content,"Your website" +'',['vimalhnayak@gmail.com'],headers = {'Reply-To': contact_email })
            email=EmailMessage('message from '+contact_name,content,'vimalhnayak@gmail.com',['vimalhnayak@gmail.com'])
            print(email)
            email.content_subtype = 'html'
            email.send(fail_silently = True)
            return redirect('contact')

    return render(request,'base/contact.html',{
        'form': form_class,
    })
