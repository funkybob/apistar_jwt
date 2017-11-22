API* JWT
========

Add JWT authentication to your API* service!


Quick Start
-----------

1. Sub-class api_start.jwt.JWTAuthentication and provide a ``get_account``
   method.

   This will be passed the decoded Token details, and is expected to return an
   object of Auth type.

2. Add settings:

   .. code-block:: python

    'AUTHENTICATION': [
        auth.JWTAuthentication(),
    ],
    'JWT': {
        'ALGORITHMS': 'RS256',
        'SECRET': SECRET,
        'EXTRA': {
            'audience': 'mysite.com',
        },
    },

   See `PyJWT` documentation for more details.

3. Start requiring Users

   .. code-block:: python

      require_login = annotate(permissions=[IsAuthenticated()])

      @require_login
      def index(user: Auth):
          return 'Hello, {.name}!'.format(user)

