
from unicodedata import category
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from blog.models import Article as ArticleModel

from ai.permissions import RegistedMoretThanThreeUser


# Create your views here.


class ArticleView(APIView): # CBV 방식
    # 로그인 한 사용자의 게시글 목록 return
    permission_classes = [RegistedMoretThanThreeUser]

    def get(self, request):
        user = request.user

        articles = ArticleModel.objects.filter(author=user)
        titles = []

        for article in articles:
            titles.append(article.title)
        
        return Response ({"article_list": titles})

    def post(self, request):
        user = request.user
        title = request.data.get('title','')
        categorys = request.data.pop('category')
        contents = request.data.get('contents','')

        if len(title) <= 5 :
            return Response({"error":"title이 5자 이하라면 게시글을 작성할 수 없습니다."})
        if len(contents) <= 20 :
            return Response({"error":"contents가 20자 이하라면 게시글을 작성할 수 없습니다."})
        if not category :
            return Response({"error":"카테고리가 지정되지 않았다면 카테고리를 지정해주세요"})


        article = ArticleModel(
            author = user,
            title = title,
            contents = contents
        )

        article.save()
        article.category.add(*categorys)

        return Response({"message":"작성 완료!"})