import subprocess

from rest_framework import viewsets, mixins, status, response
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User, DataModel
from .permissions import IsUserOrReadOnly
from .serializers import CreateUserSerializer, UserSerializer, DataSerializer


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    Updates and retrieves user accounts
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsUserOrReadOnly,)


class UserCreateViewSet(mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    """
    Creates user accounts
    """
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)





class ProductViewSet(viewsets.ViewSet):
    """A ViewSet for handling product-related views.

    Attributes:
        list (function): A function to handle the GET request to retrieve a list of products.

    Returns: Response: A response object containing a serialized list of products and a success status code.
    """
    
    def list(self, request):
        """
        Retrieve a list of products.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            Response: A response object containing a serialized list of products and a success status code.
        """
        data = DataModel.objects.all()
        serializer = DataSerializer(data, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)


# class UpdateSpider(APIView):
#     """A class-based view for updating the Scrapy spider.

#     Attributes:
#         get (function): A function to handle the GET request to update the spider.

#     Returns: Response: A response object containing the output of the spider update process.
#     """

#     def get(self, request, format=None):
#         """Handle GET request to update the Scrapy spider.

#         Args:
#             request (HttpRequest): The HTTP request object.
#             format (str, optional): The format of the response data. Defaults to None.

#         Returns:
#             Response: A response object containing the output of the spider update process.
#         """
#         command = 'scrapy runspider spider/spider_files/script.py'
#         output = subprocess.check_output(command.split())
#         return Response(output.decode())
