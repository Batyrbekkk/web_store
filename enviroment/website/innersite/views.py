from .models import Person
# получаем все объекты

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
 
try:
    tom = Person.objects.get(name="Tom")    # MultipleObjectsReturned
    alex = Person.objects.get(name="Alex")  # ObjectDoesNotExist
except ObjectDoesNotExist:
    print("Объект не сушествует")
except MultipleObjectsReturned:
    print("Найдено более одного объекта")