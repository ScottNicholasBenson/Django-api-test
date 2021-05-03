from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import competitions, bids
from .serializers import competitionSerializer, buyersSerializer, sellersSerializer, bidsSerializer


@api_view(['POST'])
def uploadCompetitions(request):
    serializer = competitionSerializer(data=request.data, many=True)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)


@api_view(['POST'])
def uploadBids(request):
    serializer = bidsSerializer(data=request.data, many=True)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)


@api_view(['POST'])
def uploadSellers(request):
    serializer = sellersSerializer(data=request.data, many=True)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)


@api_view(['POST'])
def uploadBuyers(request):
    serializer = buyersSerializer(data=request.data, many=True)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)


def viewCompetitions(request):
    print(request.GET)
    bidsObj = bids.objects.all()
    context = {}
    if 'accepted_bid' in request.GET:
        if request.GET['accepted_bid'] == 'True':
            context['bidsObj'] = groupByStatus(bidsObj, True)
            context['competition_status'] = True
            return render(request, 'Competitions/view-competitions.html', context=context)
        else:
            context['bidsObj'] = groupByStatus(bidsObj, False)
            context['competition_status'] = False
            return render(request, 'Competitions/view-competitions.html', context=context)
    context['competition_status'] = 'no_data'
    return render(request, 'Competitions/view-competitions.html', context=context)


def groupByStatus(obj, status):
    """
    :param status: Bool: True or False
    :param obj: bids model object
    :return: Nested Dict grouping competitions by status
    """
    competitionsList = []
    competitionsDict = {}

    for item in obj.filter(accepted=status):
        competitionsList.append(item)

    competitionsDict[status] = competitionsList
    return competitionsDict
