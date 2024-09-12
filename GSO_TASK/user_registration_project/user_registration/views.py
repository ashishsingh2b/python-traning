from django.shortcuts import render, redirect
from .forms import UserProfileForm

def register_user(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the form data to the database
            # Optionally, you can handle further processing or redirects here
            return redirect('registration_success')  # Redirect to a success page or render the same page with data
    else:
        form = UserProfileForm()
    
    return render(request, 'registration/register.html', {'form': form})

def registration_success(request):
    # Render a success page or redirect to another view
    return render(request, 'registration/success.html')
