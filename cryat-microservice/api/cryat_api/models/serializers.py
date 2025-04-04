# from rest_framework import serializers

# from .models import Users

# class RegistrationSerializer(serializers.Serializer):
#     username = serializers.CharField(max_length=64, required=True)
#     favorite_word = serializers.CharField(max_length=64, required=True)
#     password = serializers.CharField(max_length=64, required=True)
#     repeat_password = serializers.CharField(max_length=64, required=True)

#     def validate(self, attrs):
#         if attrs.get('password') != attrs.get('repeat_password'):
#             raise serializers.ValidationError({"repeat_password": "Passwords do not match"})
#         return attrs
    
#     def create(self, validated_data):
#         validated_data.pop('repeat_password')
#         password = validated_data.pop('password')
#         user = Users.objects.create(**validated_data)
#         user.set_password(password)
#         user.save()
#         return user
    
#     def update(self, instance, validated_data):
#         for attr, value in validated_data.items():
#             if hasattr(instance, attr):
#                 setattr(instance, attr, value)

#         if 'password' in validated_data:
#             instance.set_password(validated_data['password'])

#         instance.save()
#         return instance

# class LoginSerializer(serializers.Serializer):
#     username = serializers.CharField(max_length=64, required=True)
#     password = serializers.CharField(max_length=64, required=True)

#     def validate(self, attrs):
#         user = Users.objects.filter(username=attrs['username']).first()
#         if not user or not user.check_password(attrs['password']):
#             raise serializers.ValidationError("Invalid credentials")
#         return attrs

        
    
