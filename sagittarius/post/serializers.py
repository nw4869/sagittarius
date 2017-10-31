from rest_framework import serializers

from .models import *


class PostSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='posts-detail', read_only=True)

    def __init__(self, *args, public_only=True, **kwargs):
        super(PostSerializer, self).__init__(*args, **kwargs)

        if public_only:
            # TODO
            pass

    class Meta:
        model = Post
        fields = ('url', 'id', 'title', 'content', 'created')
