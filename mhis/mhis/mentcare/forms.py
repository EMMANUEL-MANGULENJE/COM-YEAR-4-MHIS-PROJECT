from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views
from .models import *
from django.forms.widgets import *
from django.forms.fields import *


gender_slecet = ('male', 'female')

class DateInput(forms.DateInput):
    input_type = "date"


#registration form
class UserRegForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model= User
        fields = ['username', 'email', 'password1','password2']



#Nurses notes data entry form
class NurseNotesForm(forms.ModelForm):
    class Meta:
        model = NurseNote
        fields =['patient_name', 'Nurse_notes']



#Doctors notes data entry form
class DoctorNotesForm(forms.ModelForm):
    class Meta:
        model = DoctorNote
        fields =['patient_name', 'Doctor_notes']



#patient details add form
class PatientAddForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields =  ['first_name','surname','gender','home_district','home_TA', 'date_of_birth','religion',
                'employment', 'Education_level', 'nationality', 'marital_status', 'tribe','phone_number',
                'name_of_next_of_kin','phone_of_guardian','history_of_consultation']
        widgets = {
            "date_of_birth":DateInput(attrs={'type': 'date'}),
        }

                


#Discharge Form
class DischargeForm(forms.ModelForm):
    class Meta:
        model = Exit
        fields = '__all__'

        widgets = {
            "date_of_exit":DateInput(attrs={'type': 'date'}),
        }



#Appointment form
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
        widgets = {
            "updated_at":DateInput(attrs={'type': 'date'}),
            "start_time":TimeInput(attrs={'type': 'time'}),
            "finish_time":TimeInput(attrs={'type': 'time'}),
        }



#Hiv stastus data entry form
class HIVStatusForm(forms.ModelForm):
    class Meta:
        model = HIVTest
        fields = '__all__'
        widgets = {
            "if_reactive_when_was_tested":DateInput(attrs={'type': 'date'}),
            "if_on_HAART_when_initiated":DateInput(attrs={'type': 'date'}),
        }
         


class DiagnosisForm(forms.ModelForm):
    class Meta:
        model = Diagnoses
        fields = '__all__'


class MedicalPsychiatricHistoryForm(forms.ModelForm):
    class Meta:
        model = MedicalPsychiatricHistorys
        fields = '__all__'

        widgets = {
            "date_of_OPD_review":DateInput(attrs={'type': 'date'}),
            "date_of_OPD_exit":DateInput(attrs={'type': 'date'}),
        }


class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescriptions
        fields = '__all__'


class ReportsForm(forms.ModelForm):
    class Meta:
        model  = Report
        fields ='__all__'

         widgets = {
            "date":DateInput(attrs={'type': 'date'}),
        }