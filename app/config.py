
from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
LOG_PATH = env.str("LOG_PATH")