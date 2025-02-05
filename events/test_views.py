from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CommentForm
from .models import Event

class TestEventsViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.event = Event(title="Event title", author=self.user,
                         slug="event-title", category=2, 
                         excerpt="Event excerpt", date="2025-03-15 20:00", 
                         location="Event location", description="Event description", 
                         status=1)
        self.event.save()

    def test_render_event_detail_page_with_comment_form(self):
        response = self.client.get(reverse(
            'event_detail', args=['event-title']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Event title", response.content)
        self.assertIn(b"Event description", response.content)
        self.assertIsInstance(
            response.context['comment_form'], CommentForm)

    def test_successful_comment_submission(self):
        """Test for posting a comment on an event"""
        self.client.login(
            username="myUsername", password="myPassword")
        post_data = {
            'content': 'This is a test comment.'
        }
        response = self.client.post(reverse(
            'event_detail', args=['event-title']), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Comment submitted and awaiting approval',
            response.content
        )