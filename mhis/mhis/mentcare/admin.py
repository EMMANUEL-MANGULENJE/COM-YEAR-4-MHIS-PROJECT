from django.contrib import admin
from .models import *


#Customizing the view of Models and search bar filter creation
class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'surname','gender', 'marital_status', 'home_district', 'nationality', 'name_of_next_of_kin',)
    search_fields = ('first_name', 'surname','gender',  'home_district', 'nationality',)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name','first_name','surname','email','date_of_birth','rank')
    search_fields = ('first_name','first_name','surname','email','date_of_birth','rank')


class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('patient_name','prescription')
    search_fields = ('patient_name','prescription')

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'checked_by', 'updated_at', 'updated_at',
                     'start_time', 'finish_time', 'comments', 'services')
    search_fields = ('patient_name', 'services')



class NurseNoteAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'Nurse_notes')
    search_fields = ('patient_name', 'Nurse_notes')



class DoctorNoteAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'Doctor_notes')
    search_fields = ('patient_name', 'Doctor_notes')

class DiagnosesAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'psychiatric','medical')
    search_fields = ('patient_name', 'psychiatric','medical')

class ReportAdmin(admin.ModelAdmin):
    list_display = ('ward_name', 'General_Report')
    search_fields = ('ward_name', 'General_Report')

class HIVTestAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'HIV_sero_status', 'if_reactive_when_was_tested',
                    'if_reactive_is_on_HAART', 'indication_for_HAART','how_long_on_HAART', 'if_on_HAART_when_initiated','if_on_HAART_what_is_regime' )
    search_fields = ('patient_name', 'HIV_sero_status')


#registering models
admin.site.register(Patient,PatientAdmin )
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(NurseNote, NurseNoteAdmin)
admin.site.register(MedicalPsychiatricHistorys)
admin.site.register(Exit)
admin.site.register(DoctorNote,DoctorNoteAdmin)
admin.site.register(Diagnoses, DiagnosesAdmin)
admin.site.register(Appointment,AppointmentAdmin)
admin.site.register(Male_Acute_Ward)
admin.site.register(Female_Acute_Ward)
admin.site.register(Male_Rehabilitation_Ward)
admin.site.register(Female_Rehabilitation_Ward)
admin.site.register(Paying_Ward)
admin.site.register(Districts)
admin.site.register(Education)
admin.site.register(Tribe)
admin.site.register(Marital)
admin.site.register(Religion)
admin.site.register(Gender)
admin.site.register(Employement)
admin.site.register(RefferalMode)
admin.site.register(Region)
admin.site.register(HIVTest, HIVTestAdmin)
admin.site.register(HIVStatus)
admin.site.register(HAARTIndication)
admin.site.register(HAARTDuration)
admin.site.register(HAARTRegime) 
admin.site.register(PsychiatricDiagnosis) 
admin.site.register(MedicalDiagnosis) 
admin.site.register(Prescriptions)
admin.site.register(Report, ReportAdmin)
admin.site.register(Schedules)


#Admin page customizaation
admin.site.site_header = "Mental Health Information System Admin "
admin.site.site_title = "Welcome to Mental Health info System"
admin.site.index_title = "Mental Health Information System Adminstrator"