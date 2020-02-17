import pickle

 

class Film:

    title = ""

    direction = ""

    music = ""

    caste = ""

    year  = -1

    video = None

 

    def __init__(self, title, direction, music, cast, video):

        self.title      = title

        self.direction  = direction

        self.music      = music

        self.cast       = cast

        self.video      = None

   

    def identify(self):

        print("Movie title:%s"%(self.title))

        print("Directed by:%s"%(self.direction))

        print("Music:%s"%(self.music))

        print("Cast:%s"%(self.cast))

        print("Video Buffer:%s"%(self.video))

 

# Create a film instance

film = Film("Sound Of Music",

            "Robert Wise",

            ["Julie Andrews", "Christopher Plummer"],

            1965,

            None)

 

# Print the film info

film.identify()

 

# Pickle the python object

pickledObject = pickle.dumps(film)

 

# pickledObject can be written to a file, to a binary stream and so on

print(pickledObject)