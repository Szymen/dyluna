from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    diet = models.ForeignKey('Diet', on_delete="CASCADE")

class User_Role(models.Model):
    user = models.OneToOneField(
        'User',
        on_delete=models.CASCADE,
        primary_key=True,
    )
    role_name = models.CharField(max_length=255)

class Diet(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000, blank=True)

class Workshop(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    user = models.ForeignKey('User', on_delete="CASCADE")
    type = models.ForeignKey('Type', on_delete="CASCADE")
    description = models.CharField(max_length=1000, blank=True)
    equipment = models.ForeignKey('Equipment', on_delete="CASCADE", null=True)

class Type(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)

class Workshop_Schedule(models.Model):
    id = models.AutoField(primary_key=True)
    workshop = models.ForeignKey('Workshop', on_delete="CASCADE")
    time = models.DateTimeField()
    place = models.ForeignKey('Place', on_delete="CASCADE")

class Equipment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000, blank=True)
    quantity = models.IntegerField()

class Place(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)

class Meal(models.Model):
    id = models.AutoField(primary_key=True)
    menu = models.CharField(max_length=255)

class Meal_Time(models.Model):
    meal = models.OneToOneField(
        'Meal',
        on_delete=models.CASCADE,
        primary_key=True,
    )
    meal_time = models.DateTimeField()

class Preferences(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', on_delete="CASCADE")
    workshop = models.ForeignKey('Workshop', on_delete="CASCADE")

class przykladowa_osoba(models.Model):
    idOsoby = models.IntegerField()
    imieOsoby = models.CharField(max_length=240)

    def __str__(self):
        return 'Osoba: ' + self.imieOsoby

    class Meta:
        verbose_name_plural = "Obywatelki"