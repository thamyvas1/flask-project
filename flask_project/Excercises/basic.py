from setup import db,Puppy,Owner,Toy


##CREATES ALL THE TABLES Model --> Db Table
db.create_all()

hazel = Puppy('Hazel', 1,'fluffy')
sam = Puppy('Sammy', 5, 'fluffy')

db.session.add_all([hazel,sam])
db.session.commit()

print(Puppy.query.all())

hazel = Puppy.query.filter_by(name='Hazel').first()

##Create owner object

thamy = Owner('Thamyres', hazel.id)

##Give some toys

toy1 = Toy('Chew Toy', hazel.id)
toy2 = Toy('Ball', hazel.id)

db.session.add_all([thamy,toy1,toy2])
db.session.commit()

#Grab Hazel after those additions

hazel = Puppy.query.filter_by(name='Hazel').first()
print(hazel)
hazel.report_toys()