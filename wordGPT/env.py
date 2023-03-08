env_dict = dict()

def loadEnv(path=".env"):
    global env_dict

    with open(".env", "r") as env:
        for line in env:
            env_item = line.strip().split("=")
            env_dict[env_item[0]] = env_item[1]

def getEnv(key):
    return env_dict.get(key)