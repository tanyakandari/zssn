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
            return Response({'data': SurvivorSerializer(survivor).data},status=status.HTTP_200_OK)
        except Survivor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
