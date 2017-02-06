import sqlite3


class Registrar():

    def register_user(self, user):
        with sqlite3.connect("dogwalking.db") as doge:
            cursor = doge.cursor()

            try: 
                cursor.execute("SELECT * FROM User")
                users = cursor.fetchall()
            except sqlite3.OperationalError:
                cursor.execute("""
                CREATE TABLE `User`
                    (
                        user_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        first_name TEXT NOT NULL,
                        last_name TEXT NOT NULL,
                        email TEXT NOT NULL,
                        username TEXT NOT NULL
                    )
                """)

            cursor.execute("""
            INSERT INTO User VALUES (null, '{}', '{}', '{}', '{}')
            """.format(
                        user.get_first_name(), 
                        user.get_last_name(), 
                        user.get_email(), 
                        user.get_username()))
        

    def user_is_registered(self, user):
        with sqlite3.connect("dogwalking.db") as doge:
            cursor = doge.cursor()

            try:
                cursor.execute("""
                    SELECT * FROM User 
                    WHERE first_name='{}'
                    AND last_name='{}'
                    AND email='{}'
                    AND username='{}'
                """.format(user.get_first_name(), 
                            user.get_last_name(), 
                            user.get_email(), 
                            user.get_username()))
            except sqlite3.OperationalError:
                return False

            selected_user = cursor.fetchall()
            return len(selected_user) == 1

        

    def register_dog(self, user, dog):
        pass