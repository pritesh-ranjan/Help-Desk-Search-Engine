# Create your tests here.
from django.test import TestCase
from django.contrib.auth import get_user_model

from search import models
from search.documents import HelpdeskDocument

User = get_user_model()


class UserTestCase(TestCase):
    def setUp(self):
        self.user_password = "test_password"
        user_a = User(username='phil')
        user_a.is_staff = True
        user_a.is_superuser = False
        user_a.set_password(self.user_password)
        user_a.save()
        print(user_a.id)

    def test_user_count(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 1)

    def test_user_exists(self):
        user_account = User.objects.filter(username__exact="phil")
        user_exists = user_account.exists() and user_account.count() == 1
        self.assertTrue(user_exists)

    def test_user_password(self):
        user_a = User.objects.get(username="phil")
        self.assertTrue(user_a.check_password(self.user_password))


SearchData = models.HelpdeskModel


class SearchTestCase(TestCase):
    def setUp(self) -> None:
        search_a = SearchData(title="Computer error", details="New error", owner="Test name")
        search_a.save()
        search_b = SearchData(title="Software error", details="build error", owner="Test name")
        search_b.save()

    def test_search_capability(self):
        query = "error"
        s = HelpdeskDocument.search().query("match", title=query).query("match", details=query)
        qs = s.to_queryset()
        result_count = qs.count()
        # print(f"ttt {result_count} results found")
        self.assertEqual(result_count, 2)



