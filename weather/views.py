from django.shortcuts import render
import urllib.request
import json
from hotel.models import Hotel
from camnang.models import Camnang2
from django.db.models.query import Q

# Create your views here.
def search(request):
    search = request.POST.get('search')
    result1 = Camnang2.objects.filter(Q(camnang_name__icontains=search))  
    result2 = Hotel.objects.filter(Q(location__icontains=search) | Q(hotel_name__icontains=search))
   
    return render(request, 'search.html', { 'result1': result1, 'result2': result2, 'searched': search})

def weather(request):
    if request.method == 'POST':
        if 'search' in request.POST:
            return search(request)
        elif 'city' in request.POST:
            city = request.POST['city']
            source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&lang=vi&appid=5d4cc4eaad0b30e58bcad0820772e02f').read()
            list_of_data = json.loads(source)
            
            data = {
                "country_code": str(list_of_data['sys']['country']),
                "coordinate": str(list_of_data['coord']['lon']) + ', ' + str(list_of_data['coord']['lat']),
                "temp": str(list_of_data['main']['temp']) + ' °C',
                "pressure": str(list_of_data['main']['pressure']),
                "humidity": str(list_of_data['main']['humidity']),
                'main': str(list_of_data['weather'][0]['main']),
                'description': str(list_of_data['weather'][0]['description']),
                'icon': list_of_data['weather'][0]['icon'],
                'city': city,
            }     
            print(data)
            return render(request, "weather/weather.html", data)
        else:
            data={}
    else:
        data = {}
        return render(request, "weather/weather.html")


