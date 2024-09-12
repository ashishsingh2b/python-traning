from django.shortcuts import render
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # Process the data (e.g., save to the database)
            return render(request, 'register.html', {'form': form, 'data': data})
    else:
        form = UserRegistrationForm()
    
    return render(request, 'register.html', {'form': form})
