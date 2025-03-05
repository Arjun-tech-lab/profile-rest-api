from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

class HelloApiView(APIView):
    """Test API view"""

    def get(self, request, format=None):
        """Returns a list of API features"""
        an_apiview = [
            'Uses HTTP methods as functions (get, post, put, delete)',
            'Is similar to traditional Django views',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]
        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        # Correctly reference the serializer
        serializer_class = serializer.HelloSerializer

        # Create an instance of the serializer with the incoming data
        serializer = serializer_class(data=request.data)

        if serializer.is_valid():
            # Retrieve the validated data and get the 'name'
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})
