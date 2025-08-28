from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import TravelOption, Booking
from .forms import UserRegisterForm, BookingForm, ProfileEditForm
from django.contrib.auth.forms import UserChangeForm

@login_required
def profile(request):
    return render(request, 'booking/profile.html')

@login_required
def profile_edit(request):
    if request.method == "POST":
        form = ProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileEditForm(instance=request.user)
    
    return render(request, 'booking/profile_edit.html', {'form': form})

def home(request):
    travels = TravelOption.objects.all()
    return render(request, 'booking/home.html', {'travels': travels})

def travel_options(request):
    travels = TravelOption.objects.all()

    t_type = request.GET.get('type')
    src = request.GET.get('source')
    dest = request.GET.get('destination')
    date = request.GET.get('date')

    if t_type:
        travels = travels.filter(type=t_type)
    if src:
        travels = travels.filter(source=src)
    if dest:
        travels = travels.filter(destination=dest)
    if date:
        travels = travels.filter(date_time__date=date)

    return render(request, 'booking/travel_options.html', {'travels': travels})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'booking/register.html', {'form': form})


@login_required
def book_ticket(request, travel_id):
    travel = get_object_or_404(TravelOption, travel_id=travel_id)

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            if booking.number_of_seats > travel.available_seats:
                form.add_error('number_of_seats', "Not enough seats available.")
            else:
                booking.user = request.user
                booking.travel_option = travel
                booking.total_price = booking.number_of_seats * travel.price
                booking.save()
                travel.available_seats -= booking.number_of_seats
                travel.save()
                return redirect('my_bookings')
    else:
        # 👈 For GET request (when you first click "Book Now")
        form = BookingForm()

    # 👈 Always return a response
    return render(request, 'booking/book_ticket.html', {'form': form, 'travel': travel})
    
@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking/my_bookings.html', {'bookings': bookings})

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id, user=request.user)
    booking.status = 'Cancelled'
    booking.travel_option.available_seats += booking.number_of_seats
    booking.travel_option.save()
    booking.save()
    return redirect('my_bookings')