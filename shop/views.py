from urllib import response
from rest_framework.views import APIView
from shop.serializers import RegisterSerializer, LoginSerializer


# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response(serializer.data, )

class LoginView(APIView):
    def post(self, request):
        pass
