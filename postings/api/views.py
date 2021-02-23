from django.db.models import Q
from rest_framework import generics, mixins
from postings.models import BlogPost
from .serializers import BlogPostSerializer


class BlogPostAPIView(mixins.CreateModelMixin, generics.ListAPIView):  # Detail View
    lookup_field = 'pk'   # default in rest framework
    serializer_class = BlogPostSerializer

    def get_queryset(self):
        qs = BlogPost.objects.all()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query)
            ).distinct()
        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BlogPostRudView(generics.RetrieveUpdateDestroyAPIView):  # Detail View
    lookup_field = 'pk'   # default in rest framework
    serializer_class = BlogPostSerializer

    def get_queryset(self):
        return BlogPost.objects.all()

    # def get_object(self):
    #     pk = self.kwargs.get('pk')
    #     return BlogPost.objects.get(pk=pk)
