from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from match_pair_check.views import *
from homepage.views import *
# test views here

from django.db.utils import ConnectionRouter
from django.test import TestCase
from match_all_check.models import MatchAllCheck
from account.models import STAFF


class AccountRouterTest(TestCase):
    def test_default_db(self):
        router = ConnectionRouter()

        # Test the db used for read of some model
        self.assertEqual(router.db_for_read(MatchAllCheck), "default")

        # Test the db used for write of some model
        self.assertEqual(router.db_for_write(MatchAllCheck), "default")

        # Test if relation is allowed between two instances
        self.assertTrue(router.allow_relation(MatchAllCheck(), MatchAllCheck()))

        # Test if some model is allowed to be migrated to some database
        self.assertTrue(router.allow_migrate_model("default", MatchAllCheck))

    def test_shire_db(self):
        router = ConnectionRouter()

        # Test the db used for read of some model
        self.assertEqual(router.db_for_read(STAFF), "Shire_Data")

        # Test the db used for write of some model
        self.assertEqual(router.db_for_write(STAFF), "default")

        # Test if relation is allowed between two instances
        self.assertFalse(router.allow_relation(STAFF(), STAFF()))
        self.assertFalse(router.allow_relation(STAFF(), MatchAllCheck()))

        # Test if some model is allowed to be migrated to some database
        self.assertFalse(router.allow_migrate_model("Shire_Data", STAFF))
        self.assertFalse(router.allow_migrate_model("default", STAFF))
