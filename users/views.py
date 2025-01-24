from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout as user_logout
from django.urls import reverse
from django.contrib import messages
from users.models import Registration

# Create your views here.

def home(request):
    return render(request, "usersapp/main.html")


def registration(request):
    if request.user.is_authenticated:
        return redirect(reverse('userprofile'))
    
    if request.method == "POST":
        # Collect data from the POST request safely
        fname = request.POST.get('fname', '').strip()
        mname = request.POST.get('mname', '').strip()
        lname = request.POST.get('lname', '').strip()
        course = request.POST.get('course', '').strip()
        qualification = request.POST.get('qualification', '').strip()
        batch = request.POST.get('batch', '').strip()
        passingyear = request.POST.get('passingyear', '').strip()
        email = request.POST.get('email', '').strip()
        mobnumber = request.POST.get('mobnumber', '').strip()
        dist = request.POST.get('dist', '').strip()
        password = request.POST.get('password', '').strip()

        # Validate email and password
        if not email or not password:
            messages.error(request, 'Email and Password are required.')
            return redirect(reverse('registration'))
        
        if User.objects.filter(email=email).exists():
            messages.warning(request, 'An account with this email already exists.')
            return redirect(reverse('registration'))
        
        # Save the data to the custom Registration model
        try:
            user_data = Registration.objects.create(
                fname=fname,
                mname=mname,
                lname=lname,
                course=course,
                qualification=qualification,
                batch=batch,
                passingyear=passingyear,
                email=email,
                mobnumber=mobnumber,
                dist=dist
            )
            user_data.save()
            
            # Create the Django user
            user = User.objects.create_user(
                username=email,  # Using email as the username
                email=email,
                password=password
            )
            user.save()
            
            messages.success(request, 'Account created successfully. You can now log in.')
            return redirect(reverse('login'))
        except Exception as e:
            messages.error(request, f'Error during registration: {str(e)}')
            return redirect(reverse('registration'))
    else:
        return render(request, 'usersapp/registration.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect(reverse('userprofile'))

    if request.method == "POST":
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, "Logged in successfully.")
            return redirect(reverse('userprofile'))
        else:
            messages.error(request, "Invalid username or password.")
    
    return render(request, "usersapp/login.html")


def userprofile(request):
    if request.user.is_authenticated:
        # Additional logic for the user's profile can go here
        return render(request, "usersapp/userprofile.html", {'user': request.user})
    else:
        messages.error(request, 'You need to log in first.')
        return redirect(reverse('login'))
