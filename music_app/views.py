from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    if request.method == "POST":
        contact_name = request.POST['contact-name']
        contact_email = request.POST['contact-email']
        contact_company = request.POST['contact-company']
        contact_message = request.POST['contact-message']
        
        
        send_mail(
           'message from ' + contact_name, #Subject
            contact_message, # message
            contact_email, # from email
            contact_company, #
           ['temtopeayobam@gmail.com'], # to email
        )
        
        return render(request, 'apps/home.html', {'contact_name':contact_name})
    else:
        return render(request, 'apps/home.html', {})
        
        
        
        
  



def ticket(request):
    return render(request, 'apps/ticket.html', {})
