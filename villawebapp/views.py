from django.shortcuts import render
from django.views.generic import TemplateView
from . models import Portfolio
from django.utils import translation
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail, get_connection, EmailMessage
# Create your views here.

##########################################################################################################################################

##########################################################################################################################################
class AboutPageView(TemplateView):
    template_name = "about.html"

##########################################################################################################################################
def index(request):
    portfolios = Portfolio.objects.all()
    return render(request, 'index.html', {
        'portfolios': portfolios,
    })
##########################################################################################################################################
class SetLanguageView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        response = super().get_redirect_url(*args, **kwargs)

        if self.request.method == 'POST':
            language = self.request.POST.get('language')
            if language:
                request = self.request
                translation.activate(language)
                request.session[translation.LANGUAGE_SESSION_KEY] = language
        return response

@method_decorator(require_POST, name='dispatch')
class SetLanguageAndRedirectView(SetLanguageView):
    def get_redirect_url(self, *args, **kwargs):
        redirect_to = self.request.POST.get('next', '/')
        return super().get_redirect_url(*args, **{'to': redirect_to})
##########################################################################################################################################


def send_contact_email(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Construct email message
            email_message = f"From: {name}\nEmail: {email}\n\n{message}"

            # Send email using Gmail SMTP
            send_mail(
                subject='Contact Form Web Page',
                message=email_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_RECEIVER],
                fail_silently=False,
            )
            return render(request, 'success.html')
    else:
        form = ContactForm()
    return render(request, 'success.html', {'form': form})



