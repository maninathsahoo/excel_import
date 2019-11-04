from django.shortcuts import render
from .resources import PersonResource
from .models import Person
from tablib import Dataset

from datetime import datetime
import datetime
import radar
from django.db.models import Q

def simple_upload(request):
    if request.method == 'POST':
        person_resource = PersonResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']
        imported_data = dataset.load(new_persons.read())
        for i in imported_data:
            if len(str(i[2]))==10 and "@" in i[1]:
                name = i[0]
                email_id = i[1]
                phone_number= i[2]
                start_date = radar.random_datetime(
                        start=datetime.date(day=1, month=1,year=1975),
                        stop=datetime.date(day=1, month=3,year=2015)
                    )
                age=datetime.datetime.today().year-start_date.year
                data = Person(name=name, email_id=email_id, phone_number=phone_number, age = age)
                data.save()
        return render(request,'simple_upload.html',{})
    else:
        return render(request, 'simple_upload.html', {})






def searchdata(request):
    if request.method == 'GET':
        query = request.GET.get('q')


        if query is not None:
            lookups = Q(name__icontains=query) | Q(email_id__exact=query)
            results = Person.objects.filter(lookups).distinct()

            context = {'results': results}

            return render(request, 'search.html', context)

        else:
            return render(request, 'search.html')

    else:
        return render(request, 'search.html')





