from django.db.models import fields
from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import redirect, render, render_to_response
from django.db.models.query import QuerySet, Q, F
from hotel.models import Hotel
from camnang.models import Camnang2, Comment, Like
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CommentForm
from django.http import JsonResponse
# Create your views here.
def search(request):
    search = request.POST.get('search')
    result1 = Camnang2.objects.filter(Q(camnang_name__icontains=search))  
    result2 = Hotel.objects.filter(Q(location__icontains=search) | Q(hotel_name__icontains=search))
   
    return render(request, 'search.html', { 'result1': result1, 'result2': result2, 'searched': search})

def search_result(request):
    if request.method == 'POST':
        return search(request)
    return render(request, 'search.html')

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "trang_chu.html" 

def trangchu(request):
    outline = Camnang2.objects.all().order_by('-view')[:5] 
    left1 = Camnang2.objects.order_by('-date')[:1]
    left2 = Camnang2.objects.all().order_by('-date')[2:4]
    right1 = Camnang2.objects.all().order_by('-date')[1:2]
    right2 = Camnang2.objects.all().order_by('-date')[4:6]
    if request.method == 'POST':     
        return search(request)
    else: 
        return render(request, 'trang_chu.html', {'oli': outline, 'left1': left1, 'right1': right1, 'left2': left2, 'right2': right2})

#Cẩm nang
def cn_detail(request):
    cn = Camnang2.objects.all().order_by('-date')
    outline = Camnang2.objects.all().order_by('-view')[:5] 
    if request.method == 'POST':     
        return search(request)
    else:
        return render(request, 'camnang/camnang.html', {'cn': cn,'oli': outline})
 

#Miền Bắc
def cn_mienbac(request):
    cn = Camnang2.objects.all().order_by('-date')
    outline = Camnang2.objects.all().order_by('-view')[:5]  
    if request.method == 'POST':     
        return search(request)
    else:
        return render(request, 'camnang/MienBac.html', {'oli': outline, 'cn': cn})

def cn_topmienbac(request):
    Camnang2.objects.filter(camnang_id='CN05').update(view=F('view')+1)
    vi =  Camnang2.objects.get(camnang_id='CN05')
    outline = Camnang2.objects.all().order_by('-view')[:5] 
    user = request.user
    comments = Comment.objects.filter(post_id='CN05').order_by('-created_on')
    comment_form = CommentForm()
    qs = Camnang2.objects.filter(camnang_id='CN05')
    
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
            
            elif 'like' or 'unlike' in request.POST:
                obj = Camnang2.objects.get(camnang_id='CN05')
                if user in obj.liked.all():
                    obj.liked.remove(user)
                else:
                    obj.liked.add(user)
                
                like, created = Like.objects.get_or_create(user=user, id_cn='CN05')

                if not created:
                    if like.value == 'Like':
                        like.value='Unlike'
                    else:
                        like.value='Like'
                like.save() 
        else:
            return redirect ('login')
            
    context = {
        'qs': qs,
        'user': user,
        'comments':comments,
        'form': comment_form,
        'oli': outline,
        'vi': vi,
    }
    return render(request, 'camnang/TopMienBac.html', context)

def cn_hanoi(request):
    Camnang2.objects.filter(camnang_id='CN07').update(view=F('view')+1)
    vi =  Camnang2.objects.get(camnang_id='CN07')
    outline = Camnang2.objects.all().order_by('-view')[:5] 
    user = request.user
    comments = Comment.objects.filter(post_id='CN07').order_by('-created_on')
    comment_form = CommentForm()
    qs = Camnang2.objects.filter(camnang_id='CN07')
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
            
            elif 'like' or 'unlike' in request.POST:
                obj = Camnang2.objects.get(camnang_id='CN07')
                if user in obj.liked.all():
                    obj.liked.remove(user)
                else:
                    obj.liked.add(user)
                
                like, created = Like.objects.get_or_create(user=user, id_cn='CN07')

                if not created:
                    if like.value == 'Like':
                        like.value='Unlike'
                    else:
                        like.value='Like'
                like.save() 
        else:
            return redirect('login')
            
    context = {
        'qs': qs,
        'user': user,
        'comments':comments,
        'form': comment_form,
        'oli': outline,
        'vi': vi,
    }
    return render(request, 'camnang/HaNoi.html', context)

def cn_laocai(request):
    Camnang2.objects.filter(camnang_id='CN03').update(view=F('view')+1)
    vi =  Camnang2.objects.get(camnang_id='CN03')
    outline = Camnang2.objects.all().order_by('-view')[:5]  
    user = request.user
    comments = Comment.objects.filter(post_id='CN03').order_by('-created_on')
    comment_form = CommentForm()
    qs = Camnang2.objects.filter(camnang_id='CN03')
    
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
            
            elif 'like' or 'unlike' in request.POST:
                obj = Camnang2.objects.get(camnang_id='CN03')
                if user in obj.liked.all():
                    obj.liked.remove(user)
                else:
                    obj.liked.add(user)
                
                like, created = Like.objects.get_or_create(user=user, id_cn='CN03')

                if not created:
                    if like.value == 'Like':
                        like.value='Unlike'
                    else:
                        like.value='Like'
                like.save() 
        else:
            return redirect('login')
            
    context = {
        'qs': qs,
        'user': user,
        'comments':comments,
        'form': comment_form,
        'oli': outline,
        'vi': vi,
    }
    return render(request, 'camnang/LaoCai.html', context)

def cn_haiphong(request):
    Camnang2.objects.filter(camnang_id='CN01').update(view=F('view')+1)
    vi =  Camnang2.objects.get(camnang_id='CN01')
    outline = Camnang2.objects.all().order_by('-view')[:5]  
    user = request.user
    comments = Comment.objects.filter(post_id='CN01').order_by('-created_on')
    comment_form = CommentForm()
    qs = Camnang2.objects.filter(camnang_id='CN01')
    
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
            
            elif 'like' or 'unlike' in request.POST:
                obj = Camnang2.objects.get(camnang_id='CN01')
                if user in obj.liked.all():
                    obj.liked.remove(user)
                else:
                    obj.liked.add(user)
                
                like, created = Like.objects.get_or_create(user=user, id_cn='CN01')

                if not created:
                    if like.value == 'Like':
                        like.value='Unlike'
                    else:
                        like.value='Like'
                like.save() 
        else:
            return redirect('login')
            
    context = {
        'qs': qs,
        'user': user,
        'comments':comments,
        'form': comment_form,
        'oli': outline,
        'vi': vi,
    }
    return render(request, 'camnang/HaiPhong.html', context)

#Miền Trung
def cn_mientrung(request):
    cn = Camnang2.objects.filter(location='Trung').order_by('date')
    outline = Camnang2.objects.all().order_by('-view')[:5]  
    if request.method == 'POST':     
        return search(request)
    else: 
        return render(request, 'camnang/MienTrung.html', {'oli': outline, 'cn': cn})

def cn_topmientrung(request):
    Camnang2.objects.filter(camnang_id='CN10').update(view=F('view')+1)
    vi =  Camnang2.objects.get(camnang_id='CN10')
    outline = Camnang2.objects.all().order_by('-view')[:5]  
    user = request.user
    comments = Comment.objects.filter(post_id='CN10').order_by('-created_on')
    comment_form = CommentForm()
    qs = Camnang2.objects.filter(camnang_id='CN10')
    
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
            
            elif 'like' or 'unlike' in request.POST:
                obj = Camnang2.objects.get(camnang_id='CN10')
                if user in obj.liked.all():
                    obj.liked.remove(user)
                else:
                    obj.liked.add(user)
                
                like, created = Like.objects.get_or_create(user=user, id_cn='CN10')

                if not created:
                    if like.value == 'Like':
                        like.value='Unlike'
                    else:
                        like.value='Like'
                like.save() 
        else:
            return redirect('login')
            
    context = {
        'qs': qs,
        'user': user,
        'comments':comments,
        'form': comment_form,
        'oli': outline,
        'vi': vi,
    }
    return render(request, 'camnang/TopMienTrung.html', context)

def cn_hue(request):
    Camnang2.objects.filter(camnang_id='CN11').update(view=F('view')+1)
    vi =  Camnang2.objects.get(camnang_id='CN11')
    outline = Camnang2.objects.all().order_by('-view')[:5]  
    user = request.user
    comments = Comment.objects.filter(post_id='CN11').order_by('-created_on')
    comment_form = CommentForm()
    qs = Camnang2.objects.filter(camnang_id='CN11')
    
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
            
            elif 'like' or 'unlike' in request.POST:
                obj = Camnang2.objects.get(camnang_id='CN11')
                if user in obj.liked.all():
                    obj.liked.remove(user)
                else:
                    obj.liked.add(user)
                
                like, created = Like.objects.get_or_create(user=user, id_cn='CN11')

                if not created:
                    if like.value == 'Like':
                        like.value='Unlike'
                    else:
                        like.value='Like'
                like.save() 
        else:
            return redirect('login')
            
    context = {
        'qs': qs,
        'user': user,
        'comments':comments,
        'form': comment_form,
        'oli': outline,
        'vi': vi,
    }
    return render(request, 'camnang/Hue.html', context)

def cn_quangnam(request):
    Camnang2.objects.filter(camnang_id='CN04').update(view=F('view')+1)
    vi =  Camnang2.objects.get(camnang_id='CN04')
    outline = Camnang2.objects.all().order_by('-view')[:5]
    user = request.user
    comments = Comment.objects.filter(post_id='CN04').order_by('-created_on')
    comment_form = CommentForm()
    qs = Camnang2.objects.filter(camnang_id='CN04')
    
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
            
            elif 'like' or 'unlike' in request.POST:
                obj = Camnang2.objects.get(camnang_id='CN04')
                if user in obj.liked.all():
                    obj.liked.remove(user)
                else:
                    obj.liked.add(user)
                
                like, created = Like.objects.get_or_create(user=user, id_cn='CN04')

                if not created:
                    if like.value == 'Like':
                        like.value='Unlike'
                    else:
                        like.value='Like'
                like.save() 
        else:
            return redirect('login')
            
    context = {
        'qs': qs,
        'user': user,
        'comments':comments,
        'form': comment_form,
        'oli': outline,
        'vi': vi,
    }
    return render(request, 'camnang/QuangNam.html', context)

def cn_quangbinh(request):
    Camnang2.objects.filter(camnang_id='CN08').update(view=F('view')+1)
    vi =  Camnang2.objects.get(camnang_id='CN08')
    outline = Camnang2.objects.all().order_by('-view')[:5]  
    user = request.user
    comments = Comment.objects.filter(post_id='CN08').order_by('-created_on')
    comment_form = CommentForm()
    qs = Camnang2.objects.filter(camnang_id='CN08')
    
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
            
            elif 'like' or 'unlike' in request.POST:
                obj = Camnang2.objects.get(camnang_id='CN08')
                if user in obj.liked.all():
                    obj.liked.remove(user)
                else:
                    obj.liked.add(user)
                
                like, created = Like.objects.get_or_create(user=user, id_cn='CN08')

                if not created:
                    if like.value == 'Like':
                        like.value='Unlike'
                    else:
                        like.value='Like'
                like.save() 
        else:
            return redirect('login')
        
    context = {
        'qs': qs,
        'user': user,
        'comments':comments,
        'form': comment_form,
        'oli': outline,
        'vi': vi,
    }
    return render(request, 'camnang/QuangBinh.html', context)

def cn_phuyen(request):
    Camnang2.objects.filter(camnang_id='CN15').update(view=F('view')+1)
    vi =  Camnang2.objects.get(camnang_id='CN15')
    outline = Camnang2.objects.all().order_by('-view')[:5] 
    user = request.user
    comments = Comment.objects.filter(post_id='CN15').order_by('-created_on')
    comment_form = CommentForm()
    qs = Camnang2.objects.filter(camnang_id='CN15')
    
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
            
            elif 'like' or 'unlike' in request.POST:
                obj = Camnang2.objects.get(camnang_id='CN15')
                if user in obj.liked.all():
                    obj.liked.remove(user)
                else:
                    obj.liked.add(user)
                
                like, created = Like.objects.get_or_create(user=user, id_cn='CN15')

                if not created:
                    if like.value == 'Like':
                        like.value='Unlike'
                    else:
                        like.value='Like'
                like.save() 
        else:
            return redirect('login')
            
    context = {
        'qs': qs,
        'user': user,
        'comments':comments,
        'form': comment_form,
        'oli': outline,
        'vi': vi,
    }
    return render(request, 'camnang/PhuYen.html', context)

def cn_danang(request):
    Camnang2.objects.filter(camnang_id='CN02').update(view=F('view')+1)
    vi =  Camnang2.objects.get(camnang_id='CN02')
    outline = Camnang2.objects.all().order_by('-view')[:5]
    user = request.user
    comments = Comment.objects.filter(post_id='CN02').order_by('-created_on')
    comment_form = CommentForm()
    qs = Camnang2.objects.filter(camnang_id='CN02')
    
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
            
            elif 'like' or 'unlike' in request.POST:
                obj = Camnang2.objects.get(camnang_id='CN02')
                if user in obj.liked.all():
                    obj.liked.remove(user)
                else:
                    obj.liked.add(user)
                
                like, created = Like.objects.get_or_create(user=user, id_cn='CN02')

                if not created:
                    if like.value == 'Like':
                        like.value='Unlike'
                    else:
                        like.value='Like'
                like.save() 
        else:
            return redirect('login')
            
    context = {
        'qs': qs,
        'user': user,
        'comments':comments,
        'form': comment_form,
        'oli': outline,
        'vi': vi,
    }
    return render(request, 'camnang/DaNang.html', context)
#Miền Nam
def cn_miennam(request):
    cn = Camnang2.objects.filter(location='Nam').order_by('date')
    outline = Camnang2.objects.all().order_by('-view')[:5]  
    if request.method == 'POST':     
        return search(request)
    else: 
        return render(request, 'camnang/MienNam.html', {'oli': outline, 'cn': cn})

def cn_topmiennam(request):
    Camnang2.objects.filter(camnang_id='CN14').update(view=F('view')+1)
    vi =  Camnang2.objects.get(camnang_id='CN14')
    outline = Camnang2.objects.all().order_by('-view')[:5]  
    user = request.user
    comments = Comment.objects.filter(post_id='CN14').order_by('-created_on')
    comment_form = CommentForm()
    qs = Camnang2.objects.filter(camnang_id='CN14')
    
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
            
            elif 'like' or 'unlike' in request.POST:
                obj = Camnang2.objects.get(camnang_id='CN14')
                if user in obj.liked.all():
                    obj.liked.remove(user)
                else:
                    obj.liked.add(user)
                
                like, created = Like.objects.get_or_create(user=user, id_cn='CN14')

                if not created:
                    if like.value == 'Like':
                        like.value='Unlike'
                    else:
                        like.value='Like'
                like.save() 
        else:
            return redirect('login')
            
    context = {
        'qs': qs,
        'user': user,
        'comments':comments,
        'form': comment_form,
        'oli': outline,
        'vi': vi,
    }
    return render(request, 'camnang/TopMienNam.html', context)

def cn_vungtau(request):
    Camnang2.objects.filter(camnang_id='CN06').update(view=F('view')+1)
    vi =  Camnang2.objects.get(camnang_id='CN06')
    outline = Camnang2.objects.all().order_by('-view')[:5]  
    user = request.user
    comments = Comment.objects.filter(post_id='CN06').order_by('-created_on')
    comment_form = CommentForm()
    qs = Camnang2.objects.filter(camnang_id='CN06')
    
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
            
            elif 'like' or 'unlike' in request.POST:
                obj = Camnang2.objects.get(camnang_id='CN06')
                if user in obj.liked.all():
                    obj.liked.remove(user)
                else:
                    obj.liked.add(user)
                
                like, created = Like.objects.get_or_create(user=user, id_cn='CN06')

                if not created:
                    if like.value == 'Like':
                        like.value='Unlike'
                    else:
                        like.value='Like'
                like.save() 
        else:
            return redirect('login')
            
    context = {
        'qs': qs,
        'user': user,
        'comments':comments,
        'form': comment_form,
        'oli': outline,
        'vi': vi,
    }
    return render(request, 'camnang/VungTau.html', context)

def cn_phuquoc(request):
    Camnang2.objects.filter(camnang_id='CN12').update(view=F('view')+1)
    vi =  Camnang2.objects.get(camnang_id='CN12')
    outline = Camnang2.objects.all().order_by('-view')[:5]  
    user = request.user
    comments = Comment.objects.filter(post_id='CN12').order_by('-created_on')
    comment_form = CommentForm()
    qs = Camnang2.objects.filter(camnang_id='CN12')
    
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
            
            elif 'like' or 'unlike' in request.POST:
                obj = Camnang2.objects.get(camnang_id='CN12')
                if user in obj.liked.all():
                    obj.liked.remove(user)
                else:
                    obj.liked.add(user)
                
                like, created = Like.objects.get_or_create(user=user, id_cn='CN12')

                if not created:
                    if like.value == 'Like':
                        like.value='Unlike'
                    else:
                        like.value='Like'
                like.save() 
        else: 
            return redirect('login')
            
    context = {
        'qs': qs,
        'user': user,
        'comments':comments,
        'form': comment_form,
        'oli': outline,
        'vi': vi,
    }
    return render(request, 'camnang/PhuQuoc.html', context)

def cn_angiang(request):
    Camnang2.objects.filter(camnang_id='CN09').update(view=F('view')+1)
    vi =  Camnang2.objects.get(camnang_id='CN09')
    outline = Camnang2.objects.all().order_by('-view')[:5]  
    user = request.user
    comments = Comment.objects.filter(post_id='CN09').order_by('-created_on')
    comment_form = CommentForm()
    qs = Camnang2.objects.filter(camnang_id='CN09')
    
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
            
            elif 'like' or 'unlike' in request.POST:
                obj = Camnang2.objects.get(camnang_id='CN09')
                if user in obj.liked.all():
                    obj.liked.remove(user)
                else:
                    obj.liked.add(user)
                
                like, created = Like.objects.get_or_create(user=user, id_cn='CN09')

                if not created:
                    if like.value == 'Like':
                        like.value='Unlike'
                    else:
                        like.value='Like'
                like.save() 
        else:
            return redirect('login')
            
    context = {
        'qs': qs,
        'user': user,
        'comments':comments,
        'form': comment_form,
        'oli': outline,
        'vi': vi,
    }
    return render(request, 'camnang/AnGiang.html', context)

def cn_dalat(request):
    Camnang2.objects.filter(camnang_id='CN13').update(view=F('view')+1)
    vi =  Camnang2.objects.get(camnang_id='CN13')
    outline = Camnang2.objects.all().order_by('-view')[:5]  
    user = request.user
    comments = Comment.objects.filter(post_id='CN13').order_by('-created_on')
    comment_form = CommentForm()
    qs = Camnang2.objects.filter(camnang_id='CN13')
    
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
            
            elif 'like' or 'unlike' in request.POST:
                obj = Camnang2.objects.get(camnang_id='CN13')
                if user in obj.liked.all():
                    obj.liked.remove(user)
                else:
                    obj.liked.add(user)
                
                like, created = Like.objects.get_or_create(user=user, id_cn='CN13')

                if not created:
                    if like.value == 'Like':
                        like.value='Unlike'
                    else:
                        like.value='Like'
                like.save() 
        else: 
            return redirect('login')
            
    context = {
        'qs': qs,
        'user': user,
        'comments':comments,
        'form': comment_form,
        'oli': outline,
        'vi': vi,
    }
    return render(request, 'camnang/DaLat.html', context)



""" """ """ """ """ """ """  """ """ """ """ """ """ """



