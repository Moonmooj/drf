from rest_framework import serializers
from datetime import datetime

from product.models import Product as ProductModel


class  ProductSerializer(serializers.ModelSerializer):

    def validate(self, data):
        today = datetime.today().strftime("%Y-%M-%d")
        if str(data.get('post_end_date')) < today:
            raise serializers.ValidationError(
                detail={"error": "노출 일자가 지났습니다."},
                )
        return data

    def create(self, validated_data):
        today = datetime.today().strftime("%Y-%M-%d")
        validated_data['description'] += f'{today}에 등록된 상품입니다.'
        product = ProductModel(**validated_data)
        product.save()

        return product

    def update(self, instance, validated_data):
        today = datetime.today().strftime("%Y-%M-%d")
        for key, value in validated_data.items(): 
            if key == "description":
                value += f' {today}에 수정된 상품입니다.'
                continue
                
            setattr(instance, key, value)
        instance.save()   
        return instance         

    class Meta:
        model = ProductModel
        fields = "__all__"


    