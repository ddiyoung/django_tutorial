from django.test import TestCase

import pytest
from rest_framework.test import APIClient
from news.models import Article, Reporter


# Create your tests here.

@pytest.fixture
def reporter():
    return Reporter.objects.create(full_name="Django PyTester")

@pytest.mark.django_db
def test_create_article(client, reporter):
    response = client.post("/articles/create/", {
        "headline": "Django RestFramework Test",
        "reporter_id": reporter.id,
        "content": "Django's RestFramework is Easy!"
    }, format="json")

    assert response.status_code == 201
    assert Article.objects.count() == 1


@pytest.mark.django_db
def test_get_article_detail(client, reporter):
    article = Article.objects.create(
        headline="Testing with pytest",
        reporter_id=reporter.id,
        content="This is a test article."
    )

    # 🟢 GET 요청 (Article 조회)
    response = client.get(f"/articles/{article.id}/")

    assert response.status_code == 200
    assert response.data["headline"] == "Testing with pytest"
