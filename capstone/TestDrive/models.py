from django.db import models

class TestDrive(models.Model):
    user = models.ForeignKey('User.User', on_delete=models.CASCADE)
    bike = models.ForeignKey('Bike.Bike', on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    test_drive_date = models.DateField()
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Approved', 'Approved'),('Rejected','Rejected')], default='Pending')

    def __str__(self):
        return f"{self.user.name} - {self.bike.name}"
