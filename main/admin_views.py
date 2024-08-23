from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from .models import Attendance, LeaveRequest
from datetime import datetime
from django.db.models import Count, Q
from django.contrib import messages

@staff_member_required
def admin_dashboard(request):
    users = User.objects.all()
    return render(request, 'admin_dashboard.html', {'users': users})

@staff_member_required
def view_user_attendance(request, user_id):
    user = User.objects.get(id=user_id)
    attendance_records = Attendance.objects.filter(user=user)
    return render(request, 'view_user_attendance.html', {'attendance_records': attendance_records, 'user': user})

@staff_member_required
def edit_attendance(request, attendance_id):
    attendance = Attendance.objects.get(id=attendance_id)
    if request.method == 'POST':
        attendance.present = request.POST.get('present') == 'on'
        attendance.save()
        return redirect('view_user_attendance', user_id=attendance.user.id)
    return render(request, 'edit_attendance.html', {'attendance': attendance})

@staff_member_required
def delete_attendance(request, attendance_id):
    attendance = Attendance.objects.get(id=attendance_id)
    user_id = attendance.user.id
    attendance.delete()
    return redirect('view_user_attendance', user_id=user_id)

@staff_member_required
def leave_approval(request):
    leave_requests = LeaveRequest.objects.all()
    if request.method == 'POST':
        leave_id = request.POST.get('leave_id')
        action = request.POST.get('action')
        leave_request = LeaveRequest.objects.get(id=leave_id)
        if action == 'approve':
            leave_request.approved = True
        elif action == 'reject':
            leave_request.delete()
        leave_request.save()
    return render(request, 'leave_approval.html', {'leave_requests': leave_requests})

@staff_member_required
def system_report(request):
    if request.method == 'POST':
        from_date = request.POST.get('from_date')
        to_date = request.POST.get('to_date')
        messages.warning(request, "there is no record")
    #     return render(request, 'system_report.html', {'attendances': attendances, 'from_date': from_date, 'to_date': to_date})
        
        attendances = Attendance.objects.filter(date__range=[from_date, to_date])
        user_attendance_count = attendances.values('user__username').annotate(
            
            presents=Count('id', filter=Q(present=True)),
            # leaves=Count('id', filter=Q(leave=True)),
            absents=Count('id', filter=Q(present=False))
            
        )
        grades = {
            'A': 26,
            'B': 20,
            'C': 15,
            'D': 10,
        }

        def get_grade(present_days):
            for grade, days in grades.items():
                if present_days >= days:
                    return grade
            return 'F'

        for user_attendance in user_attendance_count:
            user_attendance['grade'] = get_grade(user_attendance['presents'])

        context = {
            'attendances': attendances,
            'user_attendance_count': user_attendance_count,
            'from_date': from_date,
            'to_date': to_date,
        }

        return render(request, 'system_report.html', context, )

    return render(request, 'system_report.html')