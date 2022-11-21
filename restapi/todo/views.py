from django.shortcuts import render
from django.http.response import Http404
from rest_framework.views import APIView
from .models import Todo
from .serializer import TodoSerializer
from rest_framework.response import Response

# Create your views here.
class TodoAPIView(APIView):

    def get_object(self, pk):
        try:
            print("run")
            return Todo.objects.get(pk = pk)
        except Todo.DoesNotExist:
            print("get error")
            raise Http404

    def get_object1(self, value):
        try:
            print("run")
            return Todo.objects.filter(title = value).values()
        except Todo.DoesNotExist:
            print("get error")
            raise Http404

    def get(self, request, pk = None, format = None):
        if pk:
            print("hello")
            data = self.get_object(pk)
            print(data)
            serializer = TodoSerializer(data)
            
            return Response(serializer.data)

        elif request.data:
            print(request.data)
            value = request.data["value"]

            data = self.get_object1(value)
            
            return Response(data)

        else:
            print("else")
            data = Todo.objects.all()
            serializer = TodoSerializer(data, many = True)

            return Response(serializer.data)
    

    def post(self, request, format = None):
        data = request.data
        # data1 = request.GET["name"]
        print(data)
        # print(data1)
        serializer = TodoSerializer(data = data)

        serializer.is_valid(raise_exception = True)

        serializer.save()

        response = Response()

        response.data = {
            "message": "Todo Create Successfully",
            "data": serializer.data
        }
        print("run successfully")

        return response

    
    def put(self, request, pk = None, format=  None):

        todo_to_update = Todo.objects.get(pk = pk)

        serializer = TodoSerializer(instance = todo_to_update, data = request.data, partial = True)

        serializer.is_valid(raise_exception = True)
        serializer.save()

        response = Response()
        print("run")

        response.data = {
            "message" : "Todo Updated Successfully",
            "data": serializer.data
        }

        return response

    def delete(self, request, pk = None, format = None):
        print("start")
        todo_to_delete = Todo.objects.get(pk = pk)
        print(todo_to_delete)

        todo_to_delete.delete()

        return Response({
            "message": "Todo Delete Successfully"
        })

    def patch(self, request, pk = None):
        print("start")
        todo_update_value = Todo.objects.get(pk = pk)
        serializer = TodoSerializer(instance = todo_update_value, data = request.data, partial = True)

        serializer.is_valid(raise_exception = True)
        serializer.save()

        response = Response()
        print("run")

        response.data = {
            "message" : "Todo Updated Successfully",
            "data": serializer.data
        }

        return response