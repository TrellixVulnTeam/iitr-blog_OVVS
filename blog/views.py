from blog.models import Blog, Tag
from blog.serializer import BlogSerializer, TagSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics


# Create your views here.

# class BlogList(APIView):
#
#     def get(self, request):
#         blogs = Blog.objects.all()
#         serializer = BlogSerializer(blogs, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = BlogSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class BlogDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Blog.objects.get(pk=pk)
#         except Blog.DoesnotExists:
#             raise Http404
#
#     def get(self, request, pk):
#         blog = self.get_object(pk)
#         serializer = BlogSerializer(blog, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def put(self, request, pk):
#         blog = self.get_object(pk)
#         serializer = BlogSerializer(blog, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         blog = self.get_object(pk)
#         blog.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class BlogList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class TagList(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
