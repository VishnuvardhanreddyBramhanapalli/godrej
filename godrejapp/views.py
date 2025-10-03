from django.shortcuts import render, redirect
from .forms import ContactRequestForm
from .models import ContactRequest  # Import your model

def index(request):
    if request.method == 'POST':
        form = ContactRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Prevent form resubmission
    else:
        form = ContactRequestForm()
    return render(request, 'godrejapp/index.html', {'form': form})

def contact_list(request):
    contacts = ContactRequest.objects.all()  # Query the model, not the form
    return render(request, 'godrejapp/contact_list.html', {'contacts': contacts})

def contact_table(request):
    data = ContactRequest.objects.all()
    return render(request, 'godrejapp/contacts_table.html', {'contacts': data})
