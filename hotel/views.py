from django.shortcuts import render, redirect
from hotel.models import Hotel, Room, Firnish, Img_slide
from camnang.models import Camnang2, Comment
from django.core.paginator import EmptyPage, Paginator
from django.db.models.query import Q
from hotel.models import Hotel, Booking
from hotel.forms import BookingForm, BookingRoom
from camnang.forms import CommentForm
from django.contrib.auth.decorators import login_required
from .filter import HotelFilter
from time import gmtime, strftime
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
import datetime
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from login.tokens import generate_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage,send_mail, BadHeaderError
from web_django import settings
# Create your views here.
def search(request):
    search = request.POST.get('search')
    result1 = Camnang2.objects.filter(Q(camnang_name__icontains=search))  
    result2 = Hotel.objects.filter(Q(location__icontains=search) | Q(hotel_name__icontains=search))
    
    context = {
        'result1': result1,
        'result2': result2,
        'searched': search,
    }
    
    return render(request, 'search.html', context)
    
def hotel (request):
    if request.method == 'POST':
        if 'search' in request.POST:
            return search(request)            
    
    ht = Hotel.objects.all().order_by('-star')
    left1 = Camnang2.objects.order_by('-date')[:1]
    left2 = Camnang2.objects.all().order_by('-date')[2:4]
    right1 = Camnang2.objects.all().order_by('-date')[1:2]
    right2 = Camnang2.objects.all().order_by('-date')[4:6]  
        
    myFilter = HotelFilter(request.GET, queryset=Hotel.objects.all())
    if request.GET.get('mprice')=='lt':
        myFilter = HotelFilter(request.GET, queryset=Hotel.objects.all().order_by('-mprice'))
    elif request.GET.get('mprice')=='gt':
        myFilter = HotelFilter(request.GET, queryset=Hotel.objects.all().order_by('mprice'))
    else: 
        myFilter = HotelFilter(request.GET, queryset=Hotel.objects.all())
        
    haha = myFilter.qs
    p = Paginator(haha, 9)
    page_num = request.GET.get('page', 1)
    
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
        
    htel = Hotel.objects.get(hotel_id = 12)
    haha = htel.favorite.filter(id=request.user.id).exists()
            
    context = {
        'left1': left1,
        'right1': right1,
        'left2': left2,
        'right2': right2,
        'items': page,
        'filter': myFilter,
        'ht': ht,
        'haha': haha,
    }
    
    return render(request, 'hotel/khach_san.html', context)


@login_required(login_url='login')
def booking (request, hotel_id):
    hotel = Hotel.objects.filter(hotel_id = hotel_id)
    booked = Room.objects.filter(room_id=request.GET.get('room_id'))
    showtime = strftime("%Y-%m-%d %H:%M:%S", gmtime())

    form = BookingForm(request.POST)
    if request.method == 'POST':
        if 'search' in request.POST:
            return search(request)
        else:
            if form.is_valid():
                form.save()
                current_site = get_current_site(request)
                myuser = User.objects.get(username=request.user)
                email_subject = "Xác nhận đặt khách sạn"
                mesage2 = render_to_string(('hotel/booking_email_confirm.html'),{
                    'username':request.user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
                    'token': generate_token.make_token(myuser)

                })
                email = EmailMessage(
                    email_subject,
                    mesage2,
                    settings.EMAIL_HOST_USER,
                    [request.user.email],
                )
                
                email.fail_silently = True
                email.send()        
                return render(request, 'hotel/booking_success.html', {'form': form})
    
    context = {
        'hotel': hotel,
        'booked': booked,
        'form': form,
        'time': showtime,
    }
    return render(request, 'hotel/booking.html', context)

def hotel_detail (request, hotel_id):
    ht = Hotel.objects.filter(hotel_id = hotel_id)
    fn = Firnish.objects.filter(hotel_id = hotel_id)
    r = Room.objects.filter(hotel_id = hotel_id)
    im = Img_slide.objects.filter(hotel_id = hotel_id)
    user = request.user
    comments = Comment.objects.filter(post_id = hotel_id).order_by('-created_on')
    comment_form = CommentForm()
    qs = Hotel.objects.filter(hotel_id = hotel_id)
    
    check_in = request.GET.get('check_in')
    check_out = request.GET.get('check_out')
    today = datetime.datetime.now().strftime ("%m-%d-%Y")
    check = Room.objects.raw('''
                            select r.* from hotel_room r where (r.hotel_id_id=%s and %s >= %s and %s >= %s)
                            except 
                            select r.* from hotel_room r join hotel_booking b on r.room_name = b.room_type
                            where ((b.check_in <= %s and %s <= b.check_out) or (%s >= b.check_in and %s <= b.check_out))''',[hotel_id, check_out, check_in, check_in, today, check_in, check_in, check_out, check_out])
    br = BookingRoom()
    if request.method == 'POST':
        if 'search' in request.POST:   
            return search(request)
            
        if request.user.is_authenticated:
            if 'comment_submit' in request.POST:
                comment_form = CommentForm(data=request.POST)
                if comment_form.is_valid():
                    comment_form.save()
                else:
                    comment_form = CommentForm() 
        else:
            return redirect('login') 
            
    context = {
        'qs': qs,
        'user': user,
        'comments':comments,
        'form': comment_form,
        'ht': ht,
        'fn': fn,
        'r': r,
        'img': im,
        'check': check,
        'check_in': check_in,
        'check_out': check_out,
        'br': br,
    }        
    return render(request, 'hotel/khach_san_single.html', context)

def success_booking (request):
    if request.method == 'POST':
        if 'search' in request.POST:
            return search(request)          
    return render(request, 'hotel/booking_success.html')

def booking_detail (request, booking_id):
    if request.method == 'POST':
        if 'search' in request.POST:
            return search(request)
    detail = Booking.objects.raw('''select r.*, h.*, b.* from (hotel_hotel h join hotel_booking b on h.hotel_id = cast(b.hotel_id as int)) join hotel_room r on cast(b.room_id as int) = r.room_id
                                    where b.booking_id=%s''', [booking_id])          
    return render(request, 'hotel/booking_detail.html', {'detail': detail})

def wishlist(request):
    ht = Hotel.objects.filter(favorite=request.user)
    return render(request, "hotel/user_wish_list.html", {"wishlist": ht})

def favorite(request, hotel_id):
    htel = get_object_or_404(Hotel, hotel_id = hotel_id)
    if htel.favorite.filter(id=request.user.id).exists():
        htel.favorite.remove(request.user)
        love = get_object_or_404(Hotel, hotel_id = hotel_id)
    else:
        htel.favorite.add(request.user)
        love = ''
    return HttpResponseRedirect(request.META["HTTP_REFERER"], {'love': love})
