import django_filters
from django_filters.filters import RangeFilter
from django.core.paginator import EmptyPage, Paginator
from .models import *

class HotelFilter(django_filters.FilterSet):
    class Meta:
        model = Hotel
        fields = ['location', 'star', 'mprice']
        
