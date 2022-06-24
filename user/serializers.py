from pkg_resources import require
from rest_framework import serializers
from user.models import User as UserModel
from user.models import UserProfile as UserProfileModel
from user.models import Hobby as HobbyModel

from blog.serializers import ArticleSerializer, CommentSerializer


class HobbySerializer(serializers.ModelSerializer):
    same_hobby_users = serializers.SerializerMethodField()  # * serializerMethod는 검증안함 
    def get_same_hobby_users(self, obj):
        user_list = []
        for user_profile in obj.userprofile_set.all():
            user_list.append(user_profile.user.username)
        return user_list

    class Meta:
        model = HobbyModel
        fields = ["name", "same_hobby_users"]

class UserProfileSerializer(serializers.ModelSerializer):
    hobby = HobbySerializer(many=True,read_only=True) 
    get_hobbys = serializers.ListField(required=False)

    class Meta:
        model = UserProfileModel
        fields = ["introduction", "birthday", "age", "hobby", "get_hobbys"]

class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer()      
    article = ArticleSerializer(many=True, source="article_set",read_only=True)
    comment = CommentSerializer(many=True, source="comment_set",read_only=True)
    
    def validate(self, data):
        if not data.get('email','').endswith('@naver.com'):
            raise serializers.ValidationError(detail={'error':'네이버 이메일만 가입할 수 있습니다.'})

        return data

    def create(self, validated_data):
        user_profile = validated_data.pop('userprofile')
        password =validated_data.pop('password')
        get_hobbys = user_profile.pop("get_hobbys", [])

        user = UserModel(**validated_data)
        user.set_password(password)
        user.save()

        user_profile = UserProfileModel.objects.create(user=user,**user_profile)

        user_profile.hobby.add(*get_hobbys)
        
        return user

    def update(self, instance, validated_data):
        # instance에는 입력된 object가 담긴다.
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
                continue
            
            setattr(instance, key, value)
        instance.save()
        return instance

    class Meta:
        model = UserModel
        fields = ["username", "password","email", "fullname", "join_date",
                    "userprofile", "article", "comment"]
        
        # 각 필드에 해당하는 다양한 옵션 지정
        extra_kwargs = {
            # write_only : 해당 필드를 쓰기 전용으로 만들어 준다.
            # 쓰기 전용으로 설정 된 필드는 직렬화 된 데이터에서 보여지지 않는다.
            'password': {'write_only': True}, # default : False
            'email': {
                # error_messages : 에러 메세지를 자유롭게 설정 할 수 있다.
                'error_messages': {
                    # required : 값이 입력되지 않았을 때 보여지는 메세지
                    'required': '이메일을 입력해주세요.',
                    # invalid : 값의 포맷이 맞지 않을 때 보여지는 메세지
                    'invalid': '알맞은 형식의 이메일을 입력해주세요.'
                    },
                    # required : validator에서 해당 값의 필요 여부를 판단한다.
                    'required': False # default : True
                    },
            }