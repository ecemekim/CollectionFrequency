from cfreq.models import Operation, Bin

from django.http import JsonResponse
from django.db.models import Q

from datetime import datetime


def get_cfreqs(request):
    # First, adding some dummy data into postgres db.

    data1 = [(32.32, 32.32, 5, datetime.strptime("2021-03-17 16:21:20", '%Y-%m-%d %H:%M:%S')),
             (33.33, 33.33, 4, datetime.strptime("2021-03-17 16:21:20", '%Y-%m-%d %H:%M:%S')),
             (55.55, 55.55, 2, datetime.strptime("2021-03-17 16:21:20", '%Y-%m-%d %H:%M:%S')),
             (66.66, 66.66, 1, datetime.strptime("2021-03-17 16:21:20", '%Y-%m-%d %H:%M:%S')),
             (11.11, 11.11, 3, datetime.strptime("2021-03-17 16:21:20", '%Y-%m-%d %H:%M:%S')),
             (57.57, 57.57, 2, datetime.strptime("2021-03-17 16:21:20", '%Y-%m-%d %H:%M:%S')),
             (34.34, 34.34, 5, datetime.strptime("2021-03-17 16:21:20", '%Y-%m-%d %H:%M:%S')),
             (22.22, 22.22, 4, datetime.strptime("2021-03-17 16:21:20", '%Y-%m-%d %H:%M:%S'))]

    data2 = ["XYZ",
             "ABC",
             "KLM"]

    data3 = [(1, 2),
             (2, 3),
             (3, 1),
             (5, 2),
             (8, 3),
             (6, 1),
             (7, 2),
             (4, 3)]

    for data in data1:
        d = Bin(latitude=data[0],
                longitude=data[1],
                collection_frequency=data[2],
                last_collection=data[3])
        d.save()

    for data in data2:
        d = Operation(name=data)
        d.save()

    # Adding some dummy data to automatically created OperationBin model.
    for data in data3:
        OperationBin = Bin.operation.through
        if OperationBin.objects.filter(Q(bin_id=data[0]) | Q(operation_id=data[1])).exists():
            continue

        else:
            OperationBin.objects.bulk_create([
                OperationBin(bin_id=data[0], operation_id=data[1])
            ])

    # Second, getting all Operation-Bin Pairs.

    # pairs = Bin.objects.all().prefetch_related('operation').values()
    pairs = Bin.operation.through.objects.all().values()

    response = JsonResponse({"Bin-Operation Pairs": list(pairs)})
    return response
