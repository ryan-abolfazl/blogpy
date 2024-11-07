from rest_framework import serializers

from blog.models import Article


# class SingleArticleSerializers(serializers.Serializer):
#     title = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=128),
#     cover = serializers.FileField(required=True, allow_null=False),
#     content = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=2048),
#     created_at = serializers.DateTimeField(required=True, allow_null=False)


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
