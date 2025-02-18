from datetime import date

from django.contrib.auth.models import User, Group
from news.models import Article, Reporter
from rest_framework import serializers

class ReporterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporter
        fields = ['full_name']

class ArticleSerializer(serializers.ModelSerializer):
    reporter_id = serializers.PrimaryKeyRelatedField(
        queryset=Reporter.objects.all(),
        source='reporter',  # 🔹 실제 모델 필드는 `reporter`지만, 입력은 `reporter_id`로 받음
        write_only=True  # 🔹 GET 응답에는 포함되지 않고, POST 요청에서만 사용됨
    )

    reporter = ReporterSerializer(read_only=True)  # 🔹 기존 SerializerMethodField() 제거
    pub_date = serializers.DateField(default=date.today)

    class Meta:
        model = Article
        fields = ['id', 'headline', 'pub_date', 'reporter', 'content', 'reporter_id']
        read_only_fields = ['pub_date', 'reporter']