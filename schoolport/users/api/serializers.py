from re import search
from rest_framework import serializers
from rest_framework.fields import NOT_READ_ONLY_WRITE_ONLY
from schoolport.users.models import User



class RegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email','username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = User(
            email = self.validated_data['email'],
            username = self.validated_data['username'],
        )
        password = self.validated_data['password']        
        password2 = self.validated_data['password2']        

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        user.set_password(password)
        user.save()
        return user

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','username']


        