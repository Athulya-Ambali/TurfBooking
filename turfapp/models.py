from django.db import models

# Create your models here.
class Sport(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Turf(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=5000)
    # sports=models.CharField(max_length=30)
    sports=models.ManyToManyField(Sport)
    def __str__(self):
        return self.name


    # turf_id=models.AutoField(primary_key=True)

class Slot(models.Model):
    turf = models.ForeignKey(Turf,on_delete=models.CASCADE)
    opentime=models.TimeField()
    closetime=models.TimeField(max_length=30)
    # time_id=models.AutoField(primary_key=True)
    
    def __str__(self):
        return f"{self.opentime} - {self.closetime}"
   

class Hour(models.Model):
    turf = models.ForeignKey(Turf,on_delete=models.CASCADE)
    hours=models.CharField(max_length=30)
    cost=models.CharField(max_length=30)
    # hour_id=models.AutoField(primary_key=True)
    def __str__(self):
        return f"{self.hours}"







class Booking(models.Model):
    turf = models.ForeignKey(Turf,on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    contact=models.CharField(max_length=30)
    sport=models.ForeignKey(Sport,on_delete=models.CASCADE)
    slot = models.ForeignKey(Slot,on_delete=models.CASCADE)
    hour=models.ForeignKey(Hour,on_delete=models.CASCADE)
    players=models.CharField(max_length=30)
    book_date = models.DateField()
    STATUS_CHOICES = [
        ('Approve','Approve'),
        ('Cancel','Cancel'),
        ('Pending','Pending'),
        ('Draft','Draft')
    ]
    status = models.CharField(max_length=30,choices=STATUS_CHOICES,default='draft')

    def __str__(self):
        return self.name



    







