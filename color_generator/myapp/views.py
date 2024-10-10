import random
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Colours
from .serializers import ColoursSerializer
 
 

@api_view(['POST'])
def create_colour_scheme(request):
    user_name = request.data.get('user_name')
 
    if not user_name:
        return Response({"error": "User name is required"}, status=status.HTTP_400_BAD_REQUEST)

    
    colours = request.data.get('colours')
    
   
    colour_data = {'user_name': user_name, 'colours': colours}

     
    serializer = ColoursSerializer(data=colour_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_colour_schemes_and_name(request):
    data = Colours.objects.all()
    serializer = ColoursSerializer(data, many=True)
    
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
def update_colour_scheme(request, pk):
    try:
        colour_scheme = Colours.objects.get(pk=pk)
    except Colours.DoesNotExist:
        return Response({"error": "Colour scheme not found"}, status=status.HTTP_404_NOT_FOUND)

    # Create a serializer instance with the existing instance and the new data
    serializer = ColoursSerializer(colour_scheme, data=request.data, partial=True)  # Use partial=True for optional fields

    if serializer.is_valid():
        serializer.save()  # Save the updated instance
        return Response(serializer.data, status=status.HTTP_200_OK)  # Return updated data
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return validation errors


@api_view(['DELETE'])
def delete_colour_scheme(request, pk):
    try:
        colour_scheme = Colours.objects.get(pk=pk)
        colour_scheme.delete()  # Delete the instance
        return Response({"message": "Colour scheme deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    except Colours.DoesNotExist:
        return Response({"error": "Colour scheme not found"}, status=status.HTTP_404_NOT_FOUND)

    
    