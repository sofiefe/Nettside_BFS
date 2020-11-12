import json 
import django # pylint: disable=unused-import
import requests # pylint: disable=unused-import
from django.http import HttpResponse, QueryDict # pylint: disable=unused-import
from django.views.decorators.csrf import csrf_exempt # pylint: disable=unused-import
from django.shortcuts import render # pylint: disable=unused-import
from .models import SensorData # pylint: disable=unused-import
from django.middleware import csrf # pylint: disable=unused-import

def index(request):
    print("Dette blir printa i terminalen")
    context = {} # Tom dictionary som blir brukt senere!
    all_sensor_data = SensorData.objects.filter().order_by('-datestamp', '-timestamp')[:50] #Henter ut all sensordata fra databasen. 
    context['all_sensor_data'] = all_sensor_data #Legger sensordata til som en variabel som kan brukes i Template. 
    return render(request, "elsysapp/index.html", context)

@csrf_exempt
def bomstasjon(request):
    if request.method == "POST":
        bombrikkeId = int(request.POST['id'])
        #lagre bombrikkeid i database her:
        p1=SensorData(sensor_id=bombrikkeId)
        p1.save()
        return HttpResponse("Lagret id.")
    elif request.method == "GET":
        csrf.get_token(request)
        return HttpResponse("Nono, bare POST")

# def get_sensor_data(request):
  #  if request.method == "POST": 
   #     data =  QueryDict(request.body) # Gjør data fra request om til en dictionary
    #    sensor_id = data['id'] # Lagrer sensorIDen til requesten 
        #sensor_value = data['sensorData'] # Lagrer sensorverdien til requesten
    
        #Skriv koden for å lage og lagre et sensorobjekt her. 
    
    #elif request.method == "GET":
     #   """Dette MÅ være med! Sikkerhetsgreier."""
      #  csrf.get_token(request)
       # return HttpResponse("")

#@csrf_exempt
#def test_light(request):

 #   if request.method == "GET":
  #      print("Get Request Incoming")
   #     response_string = "Responding from the Django View"
    #    return HttpResponse(response_string)

    #if request.method == "POST":
     #   request_dict = json.loads(request.body)
      #  print(request_dict)
       # return HttpResponse(status=204)

    #return HttpResponse(status=400)

