from django.db import models

class SensorData(models.Model):
    sensor_id = models.IntegerField()
    timestamp = models.TimeField(auto_now_add=True)
    datestamp = models.DateField(auto_now_add=True)
    
    def __str__(self):
        #Funksjon som skriver ut et person-objekt. 
        string = "Sensor ID: {}, Timestamp: {}, Datestamp: {}".format(self.sensor_id, self.timestamp, self.datestamp)
        return str(string)
# Create your models here.