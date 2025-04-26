


forma nativa:

import csv


def export_csv(request):
    queryset = modelo.objcets.all()

    options = modelo._meta

    # generamos una lista con los campos de 
    fields = [field.name for field in options.fields]

    #Construir response:
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'atachment; filename="nombre.csv"'

    # generar csv
    writer = csv.writer(response)
    
    #Writing header
    writer.writerow([options.get_field(field).verbose_name for field in fields])

    # writing data
    for obj in queryset:
        writer.writerow([getattr(obj,field) for field in fields])
    
    return response
