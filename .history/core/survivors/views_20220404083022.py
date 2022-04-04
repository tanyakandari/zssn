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
                return Response(tatus=status.HTTP_200_OK)
            else:
                return Response(data={'errors': 'Something bad happenened!'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(data={'errors': [e.args]}, status=status.HTTP_400_BAD_REQUEST)