from rest_framework import status
from rest_framework.views import APIView, Response
from .models import Item
from .serializers import ItemSerializer

class DumpItAPI(APIView):
    def get(self, request):
        # items = [
        #     "apple",
        #     "banana",
        #     "cherry",
        # ]
        items = Item.objects.all()
        items_data = ItemSerializer(items, many = True).data
        response_data = {"data" : items_data}
        return Response(response_data, status=status.HTTP_200_OK)

    def post(self, request):
        name = request.data.get("name")
        description = request.data.get("description")
        price = request.data.get("price")
        Item.objects.create(name = name, description = description, price = price)
        response_data = {"Response" : "Item created"}
        return Response(response_data, status=status.HTTP_200_OK)
    
    def put(self, request, id):
        name = request.data.get("name")
        description = request.data.get("description")
        price = request.data.get("price")
        item = Item.objects.filter(id = id).first()
        if item is None :
            response_data = {"Response" : "Item not found"}
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)
        item.name = name
        item.description = description
        item.price = price
        item.save()
        response_data = {"Response" : "Item updated"}
        return Response(response_data, status=status.HTTP_200_OK)
    
    def delete(self, request, id, *args, **kwargs):
        # id = request.data.get('id')
        print("check id",id)
        item = Item.objects.filter(id = id).first()
        if item is None :
            response_data = {"Response" : "Item not found"}
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)
        item.delete()
        response_data = {"Response" : "Item deleted"}
        return Response(response_data, status=status.HTTP_200_OK)