from database import Database
from user import User

Database.initialise(user="postgres",
                    password="1234",
                    database="learn",
                    host="localhost")

# saving to DB
my_user = User('mika@na.na', 'mika', 'schwarz', None)
my_user.save_to_db()

# loading from DB
my_user = User.load_from_db_by_email('mika@na.na')

print my_user

# from database import Database
#
# databse_one = Database()
# databse_two = Database()
#
# print database_one.connection_pool
#
# databse_one.initialise()
#
# print database_two.connection_pool
