from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Classroom
from .forms import ClassroomForm
from Booking.models import Booking


@login_required()
def view_classroom(request):
    classroom = Classroom.objects.all()
    return render(request, 'Classroom/ViewClassroom.html', {'classroom': classroom})


@staff_member_required
def add_classroom(request):
    if request.method == 'POST':
        form = ClassroomForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('View-Classroom')
            except:
                pass
    else:
        form = ClassroomForm()
    return render(request, 'Classroom/AddClassroom.html', {'form': form})


@staff_member_required
def edit_classroom(request, id):
    classroom = Classroom.objects.get(classroom_identity=id)
    return render(request, 'Classroom/EditClassroom.html', {'classroom': classroom})


@staff_member_required
def update_classroom(request, id):
    classroom = Classroom.objects.get(classroom_identity=id)
    form = ClassroomForm(request.POST, instance=classroom)
    print(id, classroom.classroom_name, classroom.classroom_capacity, classroom.classroom_status)

    if form.is_valid():
        try:
            form.save()
            return redirect('View-Classroom')
        except:
            pass
    else:
        print('Error : Failed to Update')
        print(form.errors)

    return render(request, 'Classroom/EditClassroom.html', {'classroom': classroom})


@staff_member_required
def delete_classroom(request, id):
    classroom = Classroom.objects.get(classroom_identity=id)
    classroom.delete()
    return redirect('View-Classroom')


@login_required
def classroom_booking_list(request, id):
    booking = Booking.objects.filter(booking_classroom_identity=id)

    return render(request, 'Classroom/ClassroomBookingList.html', {'booking': booking})