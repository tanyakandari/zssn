from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Survivor
from .serializer import SurvivorSerializer


class SurvivorsView(APIView):
    def get(self, _):
        query_set = Survivor.objects.all()
        return Response(
            {'data': SurvivorSerializer(
                query_set, many=True).data}, status=status.HTTP_200_OK)

    def post(self, request):
        params = request.data
        try:
            survivor = Survivor.persist(params)
            if survivor.id:
                return Response({'data': SurvivorSerializer(survivor).data}, status=status.HTTP_200_OK)
            else:
                return Response(data={'errors': 'Something bad happenened!'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(data={'errors': [e.args]}, status=status.HTTP_400_BAD_REQUEST)


class SurvivorsUpdateView(APIView):
    def put(self, request, id):
        params = request.data
        try:
            survivor = Survivor.objects.get(pk=id)
            survivor.update(params)
            return Response({'data': SurvivorSerializer(survivor).data}, status=status.HTTP_200_OK)
        except Survivor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class SurvivorsReportView(APIView):
    def get(self, _):
        percentage_of_infected_survivors = 0
        percentage_of_non_infected_survivors = 0
        total_survivors = Survivor.objects.count()
        try:
            percentage_of_non_infected_survivors = (Survivor.objects.filter(is_infected=False).count() / total_survivors) * 100
            percentage_of_infected_survivors = (Survivor.objects.filter(is_infected=True).count() / total_survivors) * 100
            return Response({'data': {'percentage_of_non_infected_survivors': percentage_of_non_infected_survivors,
                                      'percentage_of_infected_survivors': percentage_of_infected_survivors}}, status=status.HTTP_200_OK)
        except Exception:
            return Response(data={'errors': [e.args]}, status=status.HTTP_400_BAD_REQUEST)

