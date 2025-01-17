"""Module for creating and managing models."""
from django.db import models


class API(models.Model):
    """Model for storing project details"""

    method_status = (
        ("GET", "GET"),
        ("POST", "POST"),
    )
    project_name = models.CharField(max_length=250, blank=False, null=False)
    resource_name = models.CharField(max_length=250, blank=False, null=False)
    json_response = models.JSONField(blank=True, null=True)
    method = models.CharField(
        max_length=4, default="GET", choices=method_status, blank=False, null=False)

    class Meta:
        """Metadata of API class"""
        unique_together = ('project_name', 'resource_name', 'method', )

    def __str__(self) -> str:
        return str(self.project_name)
