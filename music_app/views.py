from django.shortcuts import render

def home(request):
    if request.method == "POST":
        contact_name = request.POST['contact-name']
        contact_email = request.POST['contact-email']
        contact_company = request.POST['contact-company']
        contact_message = request.POST['contact-message']
        
        return render(request, 'apps/home.html', {'contact_name':contact_name})
    else:
        return render(request, 'apps/home.html', {})
        
        
        
        
  



def ticket(request):
    return render(request, 'apps/ticket.html', {})
