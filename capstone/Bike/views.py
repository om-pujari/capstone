from django.http import JsonResponse
from django.shortcuts import render,reverse
from django.views.generic import ListView,CreateView,DetailView, View, FormView
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect,get_object_or_404
from .models import Bike
from TestDrive.models import TestDrive
from .models import Maintenance
from .forms import MaintenanceForm
from django.urls import reverse_lazy
from .models import Bike, Comparison, Review
from .forms import ComparisonForm
from django import forms
from django.shortcuts import redirect
import logging
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required



logger = logging.getLogger(__name__)
# Create your views here.
class Bike_List(ListView):
    context_object_name = "prod"
    model = models.Bike


class Bike_Detail(DetailView):
    context_object_name = 'dets'
    model = models.Bike


class BookTestDriveView(LoginRequiredMixin, View):
    def post(self, request, pk):
        # Add explicit logging
        logger.info(f"Test drive booking request received. Headers: {request.headers}")
        logger.info(f"Is AJAX: {request.headers.get('X-Requested-With') == 'XMLHttpRequest'}")

        try:
            bike = Bike.objects.get(pk=pk)
            test_drive_date = request.POST.get('test_drive_date')

            logger.info(f"Booking details - Bike: {bike}, Date: {test_drive_date}")

            # Check if test drive already exists
            existing_test_drive = TestDrive.objects.filter(
                user=request.user,
                bike=bike,
                test_drive_date=test_drive_date
            ).exists()

            if existing_test_drive:
                logger.warning("Duplicate test drive booking attempt")
                return JsonResponse({
                    'success': False,
                    'error': 'You have already booked a test drive for this bike on this date.'
                }, status=400)

            # Create test drive
            TestDrive.objects.create(
                user=request.user,
                bike=bike,
                test_drive_date=test_drive_date
            )

            logger.info("Test drive booked successfully")
            return JsonResponse({
                'success': True,
                'message': 'Test drive booked successfully!'
            })

        except Bike.DoesNotExist:
            logger.error(f"Bike with pk {pk} not found")
            return JsonResponse({
                'success': False,
                'error': 'Bike not found.'
            }, status=404)

        except Exception as e:
            logger.exception("Unexpected error in test drive booking")
            return JsonResponse({
                'success': False,
                'error': str(e)
            }, status=500)

class MaintenanceView(LoginRequiredMixin, CreateView):
    model = Maintenance
    form_class = MaintenanceForm  # Fix typo (was "forms_class")
    template_name = "Bike/maintenance.html"
    success_url = reverse_lazy('User:profile')  # Redirect after booking

    def form_valid(self, form):
        form.instance.user = self.request.user  # Assign logged-in user
        return super().form_valid(form)




class CompareBikesView(FormView):
    template_name = "Bike/compare.html"
    form_class = ComparisonForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Check for bikes in GET parameters or form submission
        bike_one_id = self.request.GET.get('bike_one') or self.request.GET.get('form-bike_one')
        bike_two_id = self.request.GET.get('bike_two') or self.request.GET.get('form-bike_two')

        # Fetch bikes if IDs are provided
        if bike_one_id:
            context['bike_one'] = get_object_or_404(Bike, id=bike_one_id)

        if bike_two_id:
            context['bike_two'] = get_object_or_404(Bike, id=bike_two_id)

        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()

        # Pass GET parameters to form for initial data
        kwargs['initial'] = {
            'bike_one': self.request.GET.get('bike_one'),
            'bike_two': self.request.GET.get('bike_two')
        }

        return kwargs

    def form_valid(self, form):
        # Redirect to comparison page with selected bikes
        return redirect(
            reverse('Bikes:compare') +
            f'?bike_one={form.cleaned_data["bike_one"].id}&bike_two={form.cleaned_data["bike_two"].id}'
        )

@login_required
@require_http_methods(["POST"])
def add_review(request):
    try:
        bike_id = request.POST.get('bike_id')
        rating = request.POST.get('rating')
        review_text = request.POST.get('review_text')

        # Validate inputs
        if not all([bike_id, rating, review_text]):
            return JsonResponse({
                'success': False,
                'error': 'All fields are required.'
            }, status=400)

        bike = Bike.objects.get(pk=bike_id)

        # Create review
        Review.objects.create(
            bike=bike,
            user=request.user,
            rating=int(rating),
            text=review_text
        )

        return JsonResponse({
            'success': True,
            'message': 'Review added successfully!'
        })

    except Bike.DoesNotExist:
        return JsonResponse({
            'success': False,
            'error': 'Bike not found.'
        }, status=404)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)

def get_reviews(request, bike_id):
    try:
        bike = Bike.objects.get(pk=bike_id)
        reviews = Review.objects.filter(bike=bike).order_by('-date')

        review_list = [{
            'rating': review.rating,
            'text': review.text,
            'date': review.date.isoformat(),
            'username': review.user.username
        } for review in reviews]

        return JsonResponse({
            'success': True,
            'reviews': review_list
        })

    except Bike.DoesNotExist:
        return JsonResponse({
            'success': False,
            'error': 'Bike not found.'
        }, status=404)



