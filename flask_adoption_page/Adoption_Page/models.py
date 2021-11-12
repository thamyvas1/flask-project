#####################
###### MODELS ######
####################

#set up inside the __init__.py under projectfolder
from Adoption_Page import db
class Puppy(db.Model):

    ##Manual override tablename##
    __tablename__ = 'puppy'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    owner = db.relationship('Owner', backref='puppy', uselist = False)

    def __init__(self, name):
        self.name = name

    def __repr__(self): 
        if self.owner:
            return f"Puppy {self.name} has a owner called {self.owner.name}"
        else:
            return f"Puppy {self.name} has no owner yet!!"

class Owner(db.Model):

    __tablename__ = 'owners'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppy.id'))

    def __init__(self,name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id

    def __repr__(self): 
        return f"Owner name is {self.name}"