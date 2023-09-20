from django.db import models
from django.utils import timezone
from UserBase.models import User

class PassDown(models.Model):
    shiftList = [("Days", "Days"),
                 ("Nights", "Nights"),
                 ("Mids", "Mids")]
    shift = models.CharField(max_length=10, choices=shiftList)
    date_time = models.DateTimeField(default=timezone.now)
    notes = models.TextField()
    entered_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    #entry = models.ForeignKey(Entry, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.shift} {self.date_time}"

class Entry(models.Model):
    modex = models.IntegerField()
    discrepancy = models.CharField(max_length=50)
    text_body = models.TextField()
    passdown = models.ForeignKey(PassDown, on_delete=models.CASCADE, default=PassDown.objects.last)

    def __str__(self):
        return f"{self.modex} {self.discrepancy} {self.passdown.date_time}"
