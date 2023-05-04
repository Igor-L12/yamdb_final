from django.core.validators import (MaxLengthValidator, MinLengthValidator,
                                    RegexValidator)
from rest_framework import serializers, status
from rest_framework.validators import UniqueValidator
from reviews.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role',
        )

    def validate_username(self, value):
        min_length = 5
        max_length = 150
        validators = [
            MinLengthValidator(min_length),
            MaxLengthValidator(max_length),
            # Добавляем проверку на соответствие паттерну
            RegexValidator(
                regex=r'^[\w.@+-]+\Z',
                message=('Логин содержит недопустимые символы'),
            ),
        ]

        # Применяем все валидаторы к значению поля username
        for validator in validators:
            validator(value)

        return value


class RegistrationSerializer(serializers.ModelSerializer):
    username = serializers.RegexField(
        r'^[\w.@+-]+',
        max_length=150,
        min_length=None,
        allow_blank=False,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    email = serializers.EmailField(
        max_length=254,
        min_length=None,
        allow_blank=False,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model = User
        fields = ('username', 'email')

    def validate_email(self, email):
        """Проверка уникальности email."""
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                'Такой email уже существует.'
            )
        return email

    def validate_username(self, username):
        """Проверка на создание пользователя ME."""
        if username.lower() == 'me':
            raise serializers.ValidationError(
                'Пользователя с username=me нельзя создавать.',
                code=status.HTTP_400_BAD_REQUEST
            )
        return username


class VerificationSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    confirmation_code = serializers.CharField(max_length=250)
