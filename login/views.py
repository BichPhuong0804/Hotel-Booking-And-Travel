from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.urls import reverse_lazy
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.models import User,auth
from django.core.mail import EmailMessage,send_mail, BadHeaderError
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode
from django.utils.http import urlsafe_base64_encode
from hotel.forms import BookingForm
from web_django import settings
from django.utils.encoding import force_bytes,force_text
from django.contrib.auth.decorators import login_required
from . tokens import generate_token
from .forms import contactForm
from .models import Profile
from django.http import HttpResponse
from hotel.models import Hotel, Booking
from camnang.models import Camnang2
from django.db.models.query import Q
import datetime

# Create your views here.

from .forms import (
    RegistrationForm, 
    EditProfile,
    PasswordChangingForm
)

from django.template.loader import render_to_string

def search(request):
    search = request.POST.get('search')
    result1 = Camnang2.objects.filter(Q(camnang_name__icontains=search))  
    result2 = Hotel.objects.filter(Q(location__icontains=search) | Q(hotel_name__icontains=search))
   
    return render(request, 'search.html', { 'result1': result1, 'result2': result2, 'searched': search})

def activate(request, uidb64, token):
    try: 
        uid = force_text(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser = None
    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        login(request,myuser, backend='django.contrib.auth.backends.ModelBackend')
        messages.info(request,'Xác nhận thành công')
        return render(request,'trang_chu.html',{'User':myuser})
    else:
        return render(request, 'account/activation_false.html')   
 
def login_user (request):
    form = RegistrationForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password2 = request.POST.get('password2')

        user=authenticate(request, username=username, password=password2)
        if user is not None:
            login(request, user)
            return redirect('trangchu')
        else:
            messages.info(request, 'Username or Password is incorrect')
    context = {}
    return render(request, 'account/login.html', context)

def register (request):
    messages.info(request, '')
    if request.method =="POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username đã tồn tại!')
            return redirect('login')
        
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email đã tồn tại!')
            return redirect('login')
        
        elif not username.isalnum():
            messages.error(request, 'Username không được chứa ký tự đặc biệt!')
            return redirect('login')
        else:
            myuser = User.objects.create_user(username, email, password)
            myuser.gender = ""
            myuser.is_active = False
            myuser.save()
            
            current_site = get_current_site(request)
            email_subject = "Xác nhận tài khoản"
            mesage2 = render_to_string(('account/email_confirm.html'),{
                'username':username,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
                'token': generate_token.make_token(myuser)

            })
            email = EmailMessage(
                email_subject,
                mesage2,
                settings.EMAIL_HOST_USER,
                [email],
            )
            
            email.fail_silently = True
            email.send()        

            messages.info(request, 'Tạo tài khoản thành công vui lòng xác nhận email!')
            return redirect('login')
            
    return render(request,'account/register.html') 

def logout(request):
    auth.logout(request)
    return redirect('trangchu')

def logout_user(request):
    logout(request)
    return redirect('trangchu')

def profile (request):
    if request.user.is_anonymous():
        return render(request, 'trang_chu.html')
    else:
        args = {'user': request.user}
        return render(request, 'account/profile.html')
    

def edit_profile(request):
    if request.method == 'POST':
        if 'search' in request.POST:
            return search(request)
        else:
            form = EditProfile(request.POST)
            
            if form.is_valid():
                form.save()
                return redirect('/profile/')
    else:
        form = EditProfile(instance=request.user)
    return render(request, 'account/profile.html', {'form': form})

def change_success(request):
    if request.method == 'POST':
        if 'search' in request.POST:
            return search(request)          
    return render(request, 'account/change_success.html', {})

class PasswordsChangeView(PasswordChangeView):
    from_class = PasswordChangingForm
    success_url = reverse_lazy('change_success')

def history(request):
    usern = str(request.user)
    if request.method == 'POST':
        if 'search' in request.POST:
            return search(request)
    hist = Booking.objects.raw(''' select r.*, h.*, b.* from (hotel_hotel h join hotel_booking b on h.hotel_id = cast(b.hotel_id as int)) join hotel_room r on cast(b.room_id as int) = r.room_id
                                where b.user = %s ''', [usern])
    
    return render(request, 'account/history.html',{'history': hist})

def change_password(request):
    return render(request, 'account/change_password.html')

def contact(request):
    form = contactForm()
    if request.method == 'POST':
        if 'search' in request.POST:
            return search(request)
        else:
            form = contactForm(request.POST)
            if form.is_valid():
                subject = f'Message from {form.cleaned_data["name"]}'
                message = form.cleaned_data["message"]
                sender = form.cleaned_data["email"]
                recipient = ["napun28@gmail.com"]
                
                try:
                    send_mail(subject, message, sender, recipient, fail_silently=True)
                except BadHeaderError:
                    return HttpResponse('Invalid header found')            
            return render(request, 'contact.html', {'form': form})
    else:
        return render(request, 'contact.html', {'form': form})
    
def deleteOrder(request, booking_id):
    order = Booking.objects.get(pk=booking_id)
    order.delete()
    return redirect('history')

   



