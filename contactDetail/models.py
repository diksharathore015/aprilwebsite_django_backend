from django.db import models

class ContactDetail(models.Model):
    """
    A single model to manage multiple contact details like phone numbers, social media links, and YouTube links.
    """
    TYPE_CHOICES = [
        ('Phone', 'Phone'),
        ('SocialMedia', 'Social Media'),
        ('YouTube', 'YouTube'),
        ('Instagram', 'Instagram'),
        ('facebook', 'Facebook'),
    ]

    contact_type = models.CharField(max_length=20, choices=TYPE_CHOICES, help_text="Type of contact detail.")
    value = models.CharField(max_length=255, help_text="Phone number, social media link, or YouTube link.")
    label = models.CharField(max_length=50, blank=True, null=True, help_text="Optional label (e.g., Home, Work, Facebook, etc.).")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.contact_type} - {self.label or 'No Label'}: {self.value}"
