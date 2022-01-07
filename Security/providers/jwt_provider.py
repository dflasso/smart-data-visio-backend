from datetime import timedelta, datetime 
import calendar
import jwt

SECRET_JWT = "55Jpc3SM0Eu6Kza"
TIME_MIN_LIFE_JWT_DEFAUL= 30


def jwt_provider_from_user(user, time_life_jwt = TIME_MIN_LIFE_JWT_DEFAUL):
    """Función que provee los JWT a los usuarios autenticados"""

    """Calculo de fecha de creación y fecha de expiración"""
    now = datetime.now()

    period_time_jwt = timedelta(minutes=time_life_jwt)

    exp = now + period_time_jwt

    _profile = "0"
    if user.id_profile is not None:
        _profile = user.id_profile

    claims = {
        "sub": user.id,
        "nickname": f'{user.first_name} {user.last_name}',
        "profile": _profile,
        "iat": calendar.timegm(now.utctimetuple()) ,
        "exp": calendar.timegm(exp.utctimetuple())
    }

    return jwt.encode(claims, SECRET_JWT, algorithm="HS256")


