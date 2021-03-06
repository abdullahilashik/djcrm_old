from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import render, redirect


class OrganizationLoginRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated."""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_organization:
            return redirect('leads:lead-list')
            # return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
