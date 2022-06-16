from django.shortcuts import render

from django.http import HttpResponse, HttpResponseBadRequest

from AppCoder.models import Familia

def familia(self):
    familia1 = Familia(nombre = "Donavon", edad = 17, nacimiento = "2004-09-08")
    familia1.save()
    familia2 = Familia(nombre = "Ellsworth", edad = 50, nacimiento = "1972-04-02")
    familia2.save()
    familia3 = Familia(nombre = "Samson", edad = 22, nacimiento = "2000-05-29")
    familia3.save()
    documento = [f"Estos son mis parientes: {familia1.nombre} tiene {familia1.edad} y nació {familia1.nacimiento}. {familia2.nombre} tiene {familia2.edad} y nació {familia2.nacimiento}. {familia3.nombre} tiene {familia3.edad} y nació {familia3.nacimiento}."]
    return HttpResponse(documento)