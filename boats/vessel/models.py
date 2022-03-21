from django.db import models


class Vessel(models.Model):
    code = models.CharField(max_length=255, unique=True, db_index=True)
    name = models.CharField(max_length=1024)
    created = models.DateTimeField(auto_created=True, auto_now=True)
    owner = models.ForeignKey(to='auth.User', on_delete=models.CASCADE,
                              null=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'{self.code}: {self.name}'


class MovementHistory(models.Model):
    vessel = models.ForeignKey(to=Vessel, on_delete=models.CASCADE)
    longitude = models.DecimalField(max_digits=10, decimal_places=8)
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    movement_datetime = models.DateTimeField()
    created = models.DateTimeField(auto_created=True, auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'{self.vessel.code}: {self.movement_datetime}'
