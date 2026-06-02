import configparser


class Config:

    def __init__(self, filename):
        self.filename = filename
        self.config = configparser.ConfigParser()

    def load_config(self):
        self.config.read(self.filename)


class DatabaseConfig(Config):

    def load_database_settings(self):

        self.load_config()

        required_keys = ["host", "port", "user", "password"]

        for key in required_keys:
            if key not in self.config["DATABASE"]:
                print(f"Missing key: {key}")
                return

        print("Database Configuration")
        print(f"Host: {self.config['DATABASE']['host']}")
        print(f"Port: {self.config['DATABASE']['port']}")
        print(f"User: {self.config['DATABASE']['user']}")
        print(f"Password: {self.config['DATABASE']['password']}")


db = DatabaseConfig("db.ini")

db.load_database_settings()