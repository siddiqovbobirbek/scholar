from environs import Env


env = Env()
env.read_env()

DEBUG = env.bool('DEBUG', default=False)
ENVIRONMENT = env.str('ENVIRONMENT', default='development')
if ENVIRONMENT == 'development':
    from .settings_debug import *
else:
    from .settings_release import *
