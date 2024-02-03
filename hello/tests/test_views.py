from django.test import TestCase, Client
from django.urls import reverse
from hello.models import LogMessage
from django.utils.timezone import now

class LogMessageViewTests(TestCase):

    def setUp(self):
        # Create a sample log message to delete
        self.message = LogMessage.objects.create(message="Test Message", log_date=now())
        self.client = Client()

    def test_delete_message(self):
        # Ensure the message exists
        self.assertEqual(LogMessage.objects.count(), 1)
        
        # Send a POST request to delete the message
        response = self.client.post(reverse('delete_message', args=[self.message.id]))
        
        # Check that the response redirects as expected
        self.assertRedirects(response, reverse('home'))
        
        # Check the message has been deleted
        self.assertEqual(LogMessage.objects.count(), 0)

class LogMessageViewTest(TestCase):
    def test_create_logmessage_via_form(self):
        # Simulate a POST request to the view that handles form submission
        response = self.client.post(reverse('log'), {'message': 'Test Message'})
        # Assert the form submission is successful and redirects as expected
        self.assertEqual(response.status_code, 302)  # Assuming the view redirects after successful submission

        # Optionally, verify the LogMessage was created
        self.assertEqual(LogMessage.objects.count(), 1)
        self.assertEqual(LogMessage.objects.first().message, 'Test Message')