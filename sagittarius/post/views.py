from rest_framework import viewsets, filters

from .models import *
from .serializers import *


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    ordering = ('-updated', )
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    ordering_fields = ('updated', 'created')
    search_fields = ('title', 'content')

    def can_read_all_posts(self):
        return self.request.user.is_superuser

    def get_queryset(self):
        if self.can_read_all_posts():
            return Post.objects.all()
        else:
            return Post.public.all()
