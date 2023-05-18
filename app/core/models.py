from django.db import models


PERIOD_TYPE = (
    ('M', 'Mensal'),
    ('Q', 'Trimestral'),
    ('S', 'Semestral'),
    ('A', 'Anual')
)


class Program(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Indicator(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=500)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class DataElement(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=500)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class OrganizationUnit(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
