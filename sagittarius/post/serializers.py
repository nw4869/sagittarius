from rest_framework import serializers

from .models import *


class PostSerializer(serializers.ModelSerializer):
    def __init__(self, public_only=True, *args, **kwargs):
        super(PostSerializer, self).__init__(*args, **kwargs)

        if public_only:
            # TODO
            pass

    class Meat:
        model = Post
        fields = '__all__'
