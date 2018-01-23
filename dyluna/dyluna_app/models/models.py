from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    diet = models.ForeignKey('Diet', on_delete="CASCADE", null=True)
    user_role = models.ForeignKey('User_Role', on_delete="CASCADE")

    def __str__(self):
        return self.name + " " + self.last_name



class User_Role(models.Model):
    id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=255)

    def __str__(self):
        return self.role_name


class Diet(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.name + " - " + "".join(self.description.split(" ")[0:7])


class Workshop(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    user = models.ForeignKey('User', on_delete="CASCADE") # TODO: to jest prowadzący, zmienic nazwe odpowiednio
    type = models.ForeignKey('Type', on_delete="CASCADE")
    description = models.CharField(max_length=1000, blank=True)
    equipment = models.ForeignKey('Equipment', on_delete="CASCADE", null=True)

    def __str__(self):
        return "[{0}] {1} - {2}".format( str(self.id), self.name, str(self.type) )


class Type(models.Model): # czego to Type? :D TODO: zmienic nazwe na Workshop_Type
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name + " - ".join(self.description.split(" ")[0:7])

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

    def __str__(self):
        return self.name + " ".join(self.description.split(" ")[0:7])


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

# class przykladowa_osoba(models.Model):
#     idOsoby = models.IntegerField()
#     imieOsoby = models.CharField(max_length=240)
#
#     def __str__(self):
#         return 'Osoba: ' + self.imieOsoby
#
#     class Meta:
#         verbose_name_plural = "Obywatelki"

