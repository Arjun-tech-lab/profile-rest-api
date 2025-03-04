from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """test API view"""
    def get(self,request,format=None):
        """returns a list of API featrues"""
        an_apiview=[
        'usus HTTP methods as function (get,post,put,delete)',
        'is similar to traditional Django view'
        'Gives you the most control over your application logic',
        'is mapped manually to URLs',
        ]
        return Response({'message':'Hello','an_apiview':an_apiview})
