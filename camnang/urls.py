from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    #Chi tiết
    path(r'', views.cn_detail, name="cn_detail"),

    #MList Miền Bắc
    path(r'mienbac/', views.cn_mienbac, name="cn_mienbac"),
    path(r'mienbac/topmienbac/', views.cn_topmienbac, name="cn_topmienbac"),
    path(r'mienbac/laocai/', views.cn_laocai, name="cn_laocai"),
    path(r'mienbac/hanoi/', views.cn_hanoi, name="cn_hanoi"),
    path(r'mienbac/haiphong/', views.cn_haiphong, name="cn_haiphong"),
    
    #List Miền Trung
    path(r'mientrung/', views.cn_mientrung, name="cn_mientrung"),
    path(r'mientrung/topmientrung/', views.cn_topmientrung, name="cn_topmientrung"),
    path(r'mientrung/hue/', views.cn_hue, name="cn_hue"),
    path(r'mientrung/quangbinh/', views.cn_quangbinh, name="cn_quangbinh"),
    path(r'mientrung/quangnam/', views.cn_quangnam, name="cn_quangnam"),
    path(r'mientrung/danang/', views.cn_danang, name="cn_danang"),
    path(r'mientrung/phuyen/', views.cn_phuyen, name="cn_phuyen"),
    
    #List Miền Nam
    path(r'miennam/', views.cn_miennam, name="cn_miennam"),
    path(r'miennam/topmiennam/', views.cn_topmiennam, name="cn_topmiennam"),
    path(r'miennam/vungtau/', views.cn_vungtau, name="cn_vungtau"),
    path(r'miennam/phuquoc/', views.cn_phuquoc, name="cn_phuquoc"),
    path(r'miennam/dalat/', views.cn_dalat, name="cn_dalat"),
    path(r'miennam/angiang/', views.cn_angiang, name="cn_angiang"),
]
