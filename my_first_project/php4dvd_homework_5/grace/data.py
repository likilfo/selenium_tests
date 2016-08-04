class User(object):

    def __init__(self, username="", password=""):
        self.username = username
        self.password = password

    @classmethod
    def Admin(cls):
        return cls(username='admin', password='admin')


class Movie(object):
    def __init__(self, title="", year=""):
        self.title = title
        self.year = year

    @classmethod
    def Movie(cls):
        return cls(title="Mission Impossible", year='2004')

    @classmethod
    def NoMovie(cls):
        return cls(title="NoSuchMovie", year="")

    @classmethod
    def Movie_for_delete(cls):
        return cls(title="BoringMovie", year="2016")