from  rest_framework.response import Response
from rest_framework.views import APIView
from URL import func
from .seriaalizers import URLSerializer


class URLView(APIView):

    def get(self, request, url):
        output = func.URL(url)

        serializer_for_request = URLSerializer(instance=output)

        return Response(serializer_for_request)