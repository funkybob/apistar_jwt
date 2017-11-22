import logging
from typing import Union, Mapping

import jwt

from apistar import http
from apistar.interfaces import Auth
from apistar import Settings


log = logging.getLogger(__name__)


class JWTAuthentication:

    def authenticate(self,
                     authorization: http.Header,
                     settings: Settings
                     ) -> Union[Auth, None]:
        if authorization is None:
            return None

        if not authorization.startswith('Bearer '):
            return None

        bearer = authorization.split(' ', 1)[1].strip()

        try:
            token = jwt.decode(
                bearer,
                algorithms=settings['JWT'].get('ALGORITHMS', ['EC256']),
                secret=settings['JWT'].get('SECRET', ''),
                **settings['JWT'].get('EXTRA', {}),
            )
        except jwt.MissingRequiredClaimError as ex:
            log.warning('JWT Missing claim: %s', ex.claim)
            return None
        except jwt.InvalidTokenError as ex:
            log.exception('JWT Invalid Token: %s', ex.__class__.__name__)
            return None

        return self.get_account(token)

    def get_account(self, token: Mapping) -> Auth:
        raise NotImplementedError
