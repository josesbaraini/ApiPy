from rest_framework import serializers
from client.models import Client
from emails.serializers import EmailSerializer
from phone.serializers import PhoneSerializer

class ClientModelSerializer(serializers.ModelSerializer):
    emails = EmailSerializer(many=True, read_only=True)
    phones = PhoneSerializer(many=True, read_only=True)
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Client
        fields= "__all__"

    def get_rate(self, obj):
        reviews = obj.reviews.all()
        if reviews:
            sum_reviews = 0
            for review in reviews:
                sum_reviews += review.stars
            return round(sum_reviews / reviews.count(), 1)
        

        return None