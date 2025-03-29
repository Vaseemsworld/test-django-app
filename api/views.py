from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET','POST'])
def hello_world(request):
    if request.method == 'POST':
        name = request.data.get('name','').strip()
        if not name:
            return Response({'error':'Name is required'}, status=400)
        message = f"Hello {name} success, You are in.!"
        return Response({'message':message}, status=200)
    elif request.method == 'GET':
        return Response({'message':'Salamwalekum, You are getting data.......!'}, status=200)
