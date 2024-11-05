from server.server import Server
from dotenv import dotenv_values

def main():
    env = dotenv_values(".env")
    server = Server(env["IP"], int(env["PORT"]))
    server.start()

if __name__ == "__main__":
    main()