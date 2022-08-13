from typing import Any, Dict
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from smtplib import SMTPException

from ratelimit.decorators import ratelimit

from .models import PortfolioProject
from .forms import ContactForm

# Create your views here.


def ratelimited_error(request, exception):
    """
    Handle RateLimited exception
    """
    return HttpResponse(status=429)


def page_not_found_view(request, exception):
    """
    Handle 404 status code
    """
    return render(request, 'portfolio/404.html', status=404)


class IndexView(ListView):
    """
    GET: returns paginated list of PortfolioProject
         ordered by `id` in descending order
    """
    template_name = 'portfolio/index.html'
    model = PortfolioProject
    ordering = ['-id']
    context_object_name = 'all_projects'
    paginate_by = 6

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        # page name to use in CSS
        context['page'] = 'index'
        return context


def project_details(request, slug):
    """
    GET: returns a single PortfolioProject
    """
    project = get_object_or_404(PortfolioProject, slug=slug)

    return render(request, 'portfolio/project-details.html', {
        'project': project,
    })


def about(request):
    """
    GET: returns About page template
    """
    return render(request, 'portfolio/about.html', {'page': 'about'})


@ratelimit(key='ip', rate='5/m', method='POST', block=True)
def contact(request):
    """
    GET: returns Contact page template and forms.ContactForm
    POST: checks if form is valid 
          saves form model to database
          uses django.core.mail.send_mail to send an email
    POST requests are ratelimitet based on IP
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            email_subject = f'New contact {form.cleaned_data["name"]}: {form.cleaned_data["email"]}'
            email_message = form.cleaned_data['message']
            try:
                send_mail(email_subject, email_message,
                          settings.DJANGO_CONTACT_EMAIL, settings.DJANGO_ADMIN_EMAILS)
            except SMTPException as e:          # It will catch other errors related to SMTP.
                print('There was an error sending an email.' + e)
            except:                             # It will catch All other possible errors.
                print("Mail Sending Failed!")
            return render(request, 'portfolio/contact_success.html')
    else:
        form = ContactForm()

    return render(request, 'portfolio/contact.html', {
        'form': form,
        'page': 'contact'
    })


# def download_cv(request):
#     filename = 'cv.pdf'
#     # Define the full file path
#     filepath = settings.MEDIA_ROOT + '/' + filename
#     # Open the file for reading content
#     path = open(filepath, 'rb')
#     # Set the return value of the HttpResponse
#     response = HttpResponse(path, content_type='application/pdf')
#     # Set the HTTP header for sending to browser
#     response['Content-Disposition'] = f"attachment; filename={filename}"
#     # Return the response value
#     return response
