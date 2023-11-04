from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect

class AdministratorAndLoginRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated."""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_administrator:
            return redirect("passdown:not-authorized")
        return super().dispatch(request, *args, **kwargs)