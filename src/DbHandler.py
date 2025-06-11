#sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///mojabaza.db", echo=True)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)


class Result(Base):
    __tablename__ = 'results'

    id = Column(Integer, primary_key=True)
    place1_ID = Column(Integer, ForeignKey('users.id'))
    place2_ID = Column(Integer, ForeignKey('users.id'))
    place3_ID = Column(Integer, ForeignKey('users.id'), nullable= True)
    place4_ID = Column(Integer, ForeignKey('users.id'), nullable = True)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

class DbHandler:

    @staticmethod
    def login(username, password):
        all_users = session.query(User).all()
        for user in all_users:
            if user.username == username and user.password == password:
                return "zalogowany"
        return "nazwa lub hasło jest niepoprawne"

    @staticmethod
    def register(username, password): #username must be unique
        if username == "":
            return "Nazwa Wymagana"
        all_users = session.query(User).all()
        for user in all_users:
            if user.username == username:
                return "taki użytkownik już istnieje"
        session.add(User(username=username, password=password))
        session.commit()
        return "dodano uzytkownika"

    @staticmethod
    def gameRecord(players):
        result = Result(place1_ID=DbHandler.get_user_id(players[0]), place2_ID=DbHandler.get_user_id(players[0]))
        if len(players) >= 3:
            result.place3_ID = DbHandler.get_user_id(players[3])
        if len(players) >= 4:
            result.place4_ID = DbHandler.get_user_id(players[4])
        session.add(result)
        session.commit()

    @staticmethod
    def get_user_id(username):
        all_users = session.query(User).all()
        for user in all_users:
            if user.username == username:
                return user.id.integer()

    @staticmethod
    def get_scores():
        result = []
        all_users = session.query(User).all()
        all_games = session.query(Result).all()
        i = 0
        for user in all_users:
            result.append([])
            result[i].append(user.username)
            wins= 0
            looses = 0
            for game in all_games:
                if game.place1_ID == user.id:
                    wins += 1
                elif game.place2_ID == user.id or game.place3_ID == user.id or game.place4_ID == user.id:
                    looses += 1
            result[i].append(wins)
            result[i].append(looses)
            i += 1
        return result
