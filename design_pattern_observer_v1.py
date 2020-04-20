# https://www.youtube.com/watch?v=87MNuBgeg34&list=PLTbTIHxH9yV4hWlSVsYisRprP78fhGFKx&index=2&t=0s
# Observers
class Subscriber:
    def __init__(self, name):
        self.name=name
    def update(self, message):
        print('{} got message "{}"'.format(self.name, message))

# Observerable class
class Publisher:
    def __init__(self,events):
        self.subscribers = set ()
    def register(self, who):
        self.subscribers.add(who)
    def unregister(self,who):
        self.subscribers.discard(who)
    def dispatch(self,message):
        for subsciber in self.subscribers:
            subsciber.update(message)

pub = Publisher()

bob = Subscriber('Bob')
alice = Subscriber('Alice')
john= Subscriber('John')

pub.register(bob)
pub.register(alice)
pub.register(john)

pub.dispatch("It's lunch time")
pub.unregister(john)
pub.dispatch("It's dinner")
