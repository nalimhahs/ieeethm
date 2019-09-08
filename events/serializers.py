from rest_framework import serializers

from .models import Event, Catagory, Organizer


class CatagorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Catagory
        fields = (
            'name',
        )


class OrganizerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organizer
        fields = (
            'name',
            'phone',
            'email'
        )



class EventSerializer(serializers.ModelSerializer):

    organizer_1 = OrganizerSerializer(read_only=True)
    organizer_2 = OrganizerSerializer(read_only=True)
    catagory = CatagorySerializer(read_only=True)

    class Meta:
        model = Event
        fields = (
            'event_id',
            'name',
            'desc',
            'price',
            'organizer_1',
            'organizer_2',
            'event_start',
            'event_end',
            'banner_url',
            'card_image_url',
            'catagory',
        )

