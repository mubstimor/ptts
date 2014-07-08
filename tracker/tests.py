import datetime

from django.utils import timezone
from django.test import TestCase

from tracker.models import Buse

class BusMethodTests(TestCase):

    def test_false_if_not_added_recently(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Buse(date_added=time)
        self.assertEqual(future_question.was_added_recently(), False)

    def test_true_if_was_added_recently(self):
        time = timezone.now()
        future_question = Buse(date_added=time)
        self.assertEqual(future_question.was_added_recently(), True)
