from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'home/index.html'

class SignUpView(TemplateView):
    template_name = "home/sign-up-form.html"
