from django.db import models
from django.conf import settings

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    genre = models.CharField(max_length=255)
    imdb = models.CharField(max_length=255)
    description = models.TextField()
    poster = models.URLField()  # URL to the movie poster

    def __str__(self):
        return self.title

class Showtime(models.Model):
    date = models.DateField()
    time = models.TimeField()
    seats_available = models.IntegerField(default=25)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='showtimes')

    def __str__(self):
        return f"{self.movie.title} - {self.date} {self.time}"


class Seat(models.Model):
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE, related_name='seats')
    seat_number = models.CharField(max_length=10)
    is_booked = models.BooleanField(default=True)

    def __str__(self):
        return f"Seat {self.seat_number} for {self.showtime}"


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,  # Use the AUTH_USER_MODEL setting correctly
        on_delete=models.CASCADE,
        related_name='bookings')
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE, related_name='bookings')
    seats = models.ManyToManyField(Seat, related_name='bookings')
    payment = models.OneToOneField('Payment', on_delete=models.CASCADE, related_name='booking', null=True, blank=True)

    def __str__(self):
        return f"Booking by {self.user.username} for {self.showtime}"


class Payment(models.Model):
    amount = models.FloatField()
    payment_method = models.CharField(max_length=50)
    transaction_id = models.CharField(max_length=100)

    def __str__(self):
        return f"Payment {self.transaction_id} - {self.amount}"
