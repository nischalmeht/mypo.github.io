from django.shortcuts import render
from django.conf import settings

from django.core.mail import send_mail

# Create your views here.
def index(request):
    if request.method == "POST":
       name = request.POST.get('full-name')
       email = request.POST.get('email')
       subject = request.POST.get('subject')
       message = request.POST.get('message')

       data = { 
                'name': name,
                'email':email,
                'subject':subject,
                'message': message 

       }
       message = '''
       New message:{}
        
        from:{}
       ''' .format(data['message'], data['email'])
       send_mail(data['subject'], message, '', ['nish.mehta10@gmail.com'])
     

    return HttpResponse('thankyou for submitting we reach u after some time')
    return render(request,"index.html" ,{})