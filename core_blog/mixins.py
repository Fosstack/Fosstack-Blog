from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin


class IsStaffUserMixin(LoginRequiredMixin):
    def handle_no_permission(self):
        raise Http404


class PageTitleMixin:
    page_title = ""

    def get_page_title(self):
        return self.page_title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.get_page_title()
        return context
