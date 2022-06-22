from rest_framework import serializers
from user.models import User as UserModel
from user.models import UserProfile as UserProfileModel
from user.models import Hobby as HobbyModel

from blog.serializers import ArticleSerializer, CommentSerializer


class HobbySerializer(serializers.ModelSerializer):
    same_hobby_users = serializers.SerializerMethodField()
    def get_same_hobby_users(self, obj):
        user_list = []
        for user_profile in obj.userprofile_set.all():
            user_list.append(user_profile.user.username)
        return user_list

    class Meta:
        model = HobbyModel
        fields = ["name", "same_hobby_users"]

class UserProfileSerializer(serializers.ModelSerializer):
    hobby = HobbySerializer(many=True) 
    class Meta:
        model = UserProfileModel
        fields = ["introduction", "birthday", "age", "hobby"]

class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer()
    article = ArticleSerializer(many=True, source="article_set")
    comment = CommentSerializer(many=True, source="comment_set")

    class Meta:
        model = UserModel
        fields = ["username", "email", "fullname", "join_date", "userprofile", "article", "comment"]