from django.db import models

# Create your models here.
class Contact(models.Model):
    Sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True , blank =True)

    def __str__(self):
        return 'Message From '+ self.name

class LYF(models.Model):
    Sno = models.AutoField(primary_key=True)
    OwnerName = models.CharField(max_length=50)
    RoomTitle = models.CharField(max_length=100)
    OwnerEmail = models.CharField(max_length=50)
    OwnerNumber = models.CharField(max_length=15)
    OwnerPostalCode = models.CharField(max_length=6)
    OwnerAddress = models.TextField()
    OwnerPrice = models.IntegerField(default=0)
    OwnerRooms = models.CharField(max_length=15)
    Flooring = models.CharField(max_length=20)
    Floor = models.CharField(max_length=4)
    TOB = models.CharField(max_length=50)
    Hall = models.ImageField(upload_to='Rooms/Images' )
    Bedroom_1 = models.ImageField(upload_to='Rooms/Images' )
    Bedroom_2 = models.ImageField(upload_to='Rooms/Images' )
    Bedroom_3 = models.ImageField(upload_to='Rooms/Images' )
    Kitchen = models.ImageField(upload_to='Rooms/Images' )
    Bathroom = models.ImageField(upload_to='Rooms/Images')

    def __str__(self):
        return 'Room By '+ self.OwnerName