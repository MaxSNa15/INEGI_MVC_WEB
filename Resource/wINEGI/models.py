from django.db import models

class Municipality(models.Model):
    name = models.CharField(max_length=30, verbose_name="Nombre")
    region = models.CharField(max_length=35, verbose_name="Región")
    population = models.IntegerField(verbose_name="Población")

    class Meta:
        verbose_name = "Municipio"
        verbose_name_plural = "Municipios"

    def __str__(self):
        return self.name

class Locality(models.Model):
    name = models.CharField(max_length=30, verbose_name="Nombre")
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE, verbose_name="Municipio")

    class Meta:
        verbose_name = "Localidad"
        verbose_name_plural = "Localidades"

    def __str__(self):
        return self.name

class Residence(models.Model):
    adress = models.CharField(max_length=50, verbose_name="Dirección")
    type_of_residence = models.CharField(max_length=20, verbose_name="Tipo de vivienda")
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE, verbose_name="Localidad")

    class Meta:
        verbose_name = "Vivienda"
        verbose_name_plural = "Viviendas"

    def __str__(self):
        return self.adress

class Resident(models.Model):
    first_name = models.CharField(max_length=30, verbose_name="Nombre")
    last_name = models.CharField(max_length=30, verbose_name="Apellido")
    age = models.IntegerField(verbose_name="Edad")
    birthdate = models.DateField(verbose_name="Fecha de nacimiento")
    gender = models.CharField(max_length=10, verbose_name="Género")
    residence = models.ForeignKey(Residence, on_delete=models.CASCADE, verbose_name="Vivienda")

    class Meta:
        verbose_name = "Residente"
        verbose_name_plural = "Residentes"

    def __str__(self):
        return self.first_name + " " + self.last_name

class EconomicActivity(models.Model):
    name = models.CharField(max_length=30, verbose_name="Nombre")
    description = models.CharField(max_length=100, verbose_name="Descripción")
    recident = models.ManyToManyField(Resident, verbose_name="Residente")

    class Meta:
        verbose_name = "Actividad económica"
        verbose_name_plural = "Actividades económicas"

    def __str__(self):
        return self.name
