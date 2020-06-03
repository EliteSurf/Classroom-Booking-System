from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from Classroom.models import Classroom
from .forms import BookingForm
from .models import Booking


# @user_passes_test(lambda u: u.is_superuser)
@login_required
def user_view_booking(request):
    user_id = request.user.id
    print(user_id)
    booking = Booking.objects.filter(booking_user_identity=user_id)

    return render(request, 'Booking/UserViewBooking.html', {'booking': booking})


@staff_member_required
def admin_view_booking(request):
    # booking = Booking.objects.filter(booking_status='Pending')
    booking = Booking.objects.all()

    return render(request, 'Booking/AdminViewBooking.html', {'booking': booking})


@staff_member_required
def admin_view_booking_detail(request, id):
    booking = Booking.objects.get(booking_identity=id)
    return render(request, 'Booking/AdminViewBookingDetail.html', {'booking': booking})


@staff_member_required
def admin_update_booking_status(request, id):
    booking = Booking.objects.get(booking_identity=id)

    print(booking.booking_classroom_identity_id, booking.booking_date, booking.booking_time, booking.booking_status)
    check_booking = Booking.objects.filter(booking_classroom_identity=booking.booking_classroom_identity_id,
                                           booking_date=booking.booking_date, booking_time=booking.booking_time,
                                           booking_status='Approve')
    print('Count:', check_booking.count())
    if request.method == 'POST':
        if request.POST.get('Approve'):
            if check_booking.count() == 0:
                status = 'Approve'
            else:
                messages.error(request, 'This Time Slot Had Already Been Occupied')
                return render(request, 'Booking/AdminViewBookingDetail.html', {'booking': booking})
        elif request.POST.get('Reject'):
            status = 'Reject'
        else:
            status = 'Verifying'

        Booking.objects.filter(booking_identity=id).update(booking_status=status)
        return redirect('Admin-View-Booking')
    else:
        return render(request, 'Booking/AdminViewBookingDetail.html', {'booking': booking})


@login_required  # Redirect if NOT logged in
def add_booking(request):
    if request.method == 'POST':
        booking_user_identity = User.objects.get(id=request.user.id)
        booking_classroom_identity = Classroom.objects.get(classroom_identity=request.POST.get('booking_classroom_identity'))
        booking_date = request.POST.get('booking_date')
        booking_time = request.POST.get('booking_time')
        booking_category = request.POST.get('booking_category')
        booking_reason = request.POST.get('booking_reason')

        # Check Duplicate
        check_booking = Booking.objects.filter(booking_classroom_identity=booking_classroom_identity,
                                               booking_date=booking_date, booking_time=booking_time,
                                               booking_status='Approve')
        if check_booking.count() == 0:
            booking_object = Booking.objects.create(booking_user_identity=booking_user_identity,
                                                    booking_classroom_identity=booking_classroom_identity,
                                                    booking_date=booking_date, booking_time=booking_time,
                                                    booking_category=booking_category, booking_reason=booking_reason)
            booking_object.save()
            return redirect('User-View-Booking')
        else:
            messages.error(request, 'Duplicate Booking !')
            classroom = Classroom.objects.all()
            form = BookingForm()
    else:
        classroom = Classroom.objects.all()
        form = BookingForm()

    context = {'form': form, 'classroom': classroom}
    return render(request, 'Booking/AddBooking.html', context)
