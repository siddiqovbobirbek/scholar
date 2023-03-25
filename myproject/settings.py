from environs import Env


env = Env()
env.read_env()

debug = env.bool('DEBUG', default=False)
DEBUG = debug
if debug:
    from .settings_debug import *
else:
    from .settings_release import *
