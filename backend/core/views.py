from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from core import services


class CountNumberOfWords(APIView):

    class CountNumberOfWordsSerializer(serializers.Serializer):

        text = serializers.CharField(allow_blank=False)

    def post(self, request):
        serializer = self.CountNumberOfWordsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            number_of_words = services.count_number_of_words(
                serializer.validated_data["text"])

            return Response(
                {"text": number_of_words},
                status=status.HTTP_200_OK
            )
