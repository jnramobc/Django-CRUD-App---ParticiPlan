from django.db import models

PARTICIPATION_STATUS = (
    ('C', 'Confirmed'),
    ('P', 'Pending'),
    ('D', 'Declined'),
)


# User Model
class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username

# Volunteer Model
class Volunteer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    availability = models.CharField(max_length=100, blank=True, null=True)
   

    def __str__(self):
        return self.name

# Event Model
class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    location = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    

    def __str__(self):
        return self.title

# Participation model
class Participation(models.Model):
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=1,
        choices=PARTICIPATION_STATUS,
        default=PARTICIPATION_STATUS[1][0]
    )
    date_participated = models.DateField()

    def __str__(self):
        return f"{self.get_status_display()} by {self.volunteer.name} for {self.event.title}"

    class Meta:
        ordering = ['-date_participated']

