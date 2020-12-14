"""mhis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mentcare.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


#url patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name ='home'),
    path('register/', register, name = 'register'),
    path('support/', support, name = 'support'),
    
    
    #discharge urls
    path('Discharge/', Discharge, name = 'Discharge'),
    path('dischargeDetail/', DischargeDetail, name='dischargeDetails'),
    path('update_discharge(?p<int:pk>)', DischargeUpdate, name='update_discharge'),
    path('delete_discharge(?p<int:pid>)', DeleteDischarge, name='delete_discharge'),


    #appiontment urls
    path('MakeAppointment/', MakeAppointment, name = 'MakeAppointment'),
    path('appointmentDetail/', AppointmentDetail, name='appointmentDetails'),
    path('update_appointment(?p<int:pk>)', AppointmentUpdate, name='update_appointment'),
    path('delete_appointment(?p<int:pid>)', DeleteAppointment, name='delete_appointment'),


    #General Reports
    path('Reports/', Reports, name = 'Reports'),
    path('Rdetail/', Rdetail, name = 'Rdetail'),
    path('update_Reports(?p<int:pk>)', ReportsUpdate, name='update_Reports'),
    path('delete_Reports(?p<int:pid>)', DeleteReports, name='delete_Reports'),



    #schedule url
    path('Cschedule/', Cschedule, name = 'Cschedule'),
    # path('Schedule/',Schedule, name = 'Schedule'),
    


    #diagnosis urls
    path('Diagnosis/', Diagnosis, name = 'Diagnosis'),
    path('update_diagnosis(?p<int:pk>)', DiagnosisUpdate, name='update_diagnosis'),
    path('delete_diagnosis(?p<int:pid>)', DeleteDiagnosis, name='delete_diagnosis'),
    path('diagnosisDetail/', DiagnosisDetail, name='diagnosisDetails'),


    path('HIVSeroStatus/', HIVSeroStatus, name = 'HIVSeroStatus'),
    path('HIVDetail/', HIVDetail, name = 'HIVDetail'),
    path('update_HIVSeroStatus(?p<int:pk>)', HIVStatusUpdate, name='update_HIVSeroStatus'), 
    path('delete_HIVSeroStatus(?p<int:pid>)', DeleteHIVStatus, name='delete_HIVSeroStatus'),
    

    #nurses notes irls
    path('NurseNotes/', NurseNotes, name = 'NurseNotes'),
    path('nurseDetail/', NurseDetail, name='nurseDetails'),
    path('update_NurseNotes(?p<int:pk>)', NnotesUpdate, name='update_NurseNotes'), 
    path('delete_NurseNotes(?p<int:pid>)', DeleteNnotes, name='delete_NurseNotes'),


    #doctor notes urls
    path('DoctorNotes/', DoctorNotes, name = 'DoctorNotes'),
    path('doctorDetail/', DoctorDetail, name='doctorDetails'),
    path('update_DoctorNotes(?p<int:pk>)', DNotesUpdate, name='update_DoctorNotes'), 
    path('delete_DoctorNotes(?p<int:pid>)', DeleteDnotes, name='delete_DoctorNotes'),

    #prescription urls
    path('Prescription/', Prescription, name = 'Prescription'),
    path('prescriptionDetails/', prescriptionDetails, name = 'prescriptionDetails'),
    path('update_prescription(?p<int:pk>)', PrescriptionUpdate, name='update_prescription'),
    path('delete_prescription(?p<int:pid>)', DeletePrescription, name='delete_prescription'),
    

    #patient history details
    path('MedicalPsychiatricHistory/', MedicalPsychiatricHistory, name = 'MedicalPsychiatricHistory'),
    path('HistoryDetail/', HistoryDetail, name = 'HistoryDetail'),


    #patients urls
    path('PatientAdd/', PatientAdd, name = 'PatientAdd'),
    path('patientDetail/', patientDetail, name = 'patientDetail'),
    path('update_patient(?p<int:pk>)', PatientUpdate, name='update_patient'),
    path('delete_patient(?p<int:pid>)', DeletePatient, name='delete_patient'),

    #ward urls
    path('ward/', ward, name = 'ward'),
    path('MRward/', MRward, name = 'MRward'),
    path('FRward/', FRward, name = 'FRward'),
    path('FAward/', FAward, name = 'FAward'),
    path('Pward/', Pward, name = 'Pward'),

    #logout in and logout urls
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),#login route
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),#logout route
    
    
    #password reset and changing password urls
    path('change_password/', auth_views.PasswordChangeView.as_view(template_name = 'password_change.html'), name = "change_password"),
    path('change_password_sent/', auth_views.PasswordChangeDoneView.as_view(template_name = 'password_change_done.html'), name ="password_change_done"),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name = 'password_reset.html'), name = "reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = 'password_reset_sent.html'), name ="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name = 'password_reset_confirm.html'), name = "password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'password_reset_complete.html'), name = "password_reset_complete"),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)