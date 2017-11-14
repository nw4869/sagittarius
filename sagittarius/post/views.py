from rest_framework import viewsets

from .models import *
from .serializers import *


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    ordering = （'-created', )

    def can_read_all_posts(self):
        return self.request.user.is_superuser

    def get_queryset(self):
        if self.can_read_all_posts():
            return Post.objects.all()
        else:
            return Post.public.all()
