import sqlite3


class User():

    def __init__(self, first_name, last_name, email, username):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__username = username

    def get_full_name(self):
        return "{} {}".format(self.__first_name, self.__last_name)

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_email(self):
        return self.__email

    def get_username(self):
        return self.__username

    def get_dogs(self):
        pass