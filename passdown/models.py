from django.db import models
from django.utils import timezone
from UserBase.models import User

class PassDown(models.Model):
    shiftList = [("Days", "Days"),
                 ("Nights", "Nights"),
                 ("Mids", "Mids")]
    
    shift = models.CharField(max_length=10, choices=shiftList)
    date_time = models.DateTimeField(default=timezone.now)
    date = models.DateField(default=timezone.now)
    notes = models.TextField(help_text="This section is for general notes. Once submitted, you can create A/C entries on the next page.")
    entered_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ["date_time"]
    #entry = models.ForeignKey(Entry, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.shift} {self.date_time}"

class Entry(models.Model):
    jobStatus = [
        ("M1", "M1"),
        ("M3", "M3"),
        ("M4", "M4"),
        ("M5", "M5"),
        ("M7", "M7"),
        ("M8", "M8"),
        ("J/C", "J/C"),
        ("S/O", "S/O"),
    ]
    modex = models.IntegerField()
    discrepancy = models.CharField(max_length=50)
    text_body = models.TextField()
    passdown = models.ForeignKey(PassDown, on_delete=models.CASCADE, default=PassDown.objects.last)
    job_status = models.CharField(max_length=3, choices=jobStatus, null=True, blank=True)
    cdi = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.modex} {self.discrepancy} {self.passdown.date_time}"
    
    
class Organization(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"
    

class WorkCenter(models.Model):
    name = models.CharField(max_length=20)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)