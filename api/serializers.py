#HBW/api/serializers.py

from rest_framework import serializers
from login import models
from django.contrib.auth.models import User

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(view_name='user-detail', queryset = User.objects.all(), required=False, allow_null=True)
    user_info = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = models.Student
        fields = ('url', 'user_info', 'user', 'std_year', 'is_paid', 'A4_count',
                'today_A4', 'month_A4', 'is_attend')



class UserSerializer(serializers.ModelSerializer):
    user_data = StudentSerializer(read_only=True)

    class Meta:
        model = User
        fields = ( 'url', 'id', 'username', 'last_name', 'first_name', 'user_data')
        write_only_fields = ('password',)
        



class UnbrellaSerializer(serializers.ModelSerializer):
    borrowed_by = serializers.HyperlinkedRelatedField(view_name='student-detail', queryset=models.Student.objects.all(), required=False, allow_null = True)

    class Meta:
        model = models.Unbrella
        fields = ('url', 'number',  'borrowed_by', 'borrowed_time', 'is_reserved', 'is_borrowed', 'status')


class BatterySerializer(serializers.ModelSerializer):
    borrowed_by = serializers.HyperlinkedRelatedField(view_name='student-detail', queryset=models.Student.objects.all(), required=False, allow_null = True)

    class Meta:
        model = models.Battery
        fields = ('url', 'number',  'borrowed_by', 'borrowed_time', 'is_reserved', 'is_borrowed', 'status')


class LanSerializer(serializers.ModelSerializer):
    borrowed_by = serializers.HyperlinkedRelatedField(view_name='student-detail', queryset=models.Student.objects.all(), required=False, allow_null = True)

    class Meta:
        model = models.Lan
        fields = ('url', 'number',  'borrowed_by', 'borrowed_time', 'is_reserved', 'is_borrowed', 'status')


class StudyTableSerializer(serializers.ModelSerializer):
    lender = serializers.HyperlinkedRelatedField( view_name='student-detail', queryset=models.Student.objects.all(), required=False, allow_null=True)

    class Meta:
        model = models.StudyTable
        fields = ('url', 'number', 'is_borrowed', 'start_time', 'end_time', 'lender')

class ComplainSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Complain
        fields = ('url', 'number', 'username', 'updated_text',)