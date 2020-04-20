# https://www.youtube.com/watch?v=87MNuBgeg34&list=PLTbTIHxH9yV4hWlSVsYisRprP78fhGFKx&index=2&t=0s
# Observers
class SubscriberOne:
    def __init__(self, name):
        self.name=name
    def update(self, message):
        print('{} got message "{}"'.format(self.name, message))

class SubscriberTwo:
    def __init__(self, name):
        self.name=name
    def receive(self, message):
        print('{} got message "{}"'.format(self.name, message))


# Observable class
class Publisher:
    def __init__(self):
        self.subscribers = dict()
    def register(self, who, callback=None):
        if callback is None:
            callback = getattr(who, 'update')
        self.subscribers[who] = callback
    def unregister(self,who):
        del self.subscribers[who]
    def dispatch(self,message):
        for subsciber, callback in self.subscribers.items():
            callback(message)

pub = Publisher()

bob = SubscriberOne('Bob')
alice = SubscriberTwo('Alice')
john= SubscriberOne('John')

pub.register(bob)
pub.register(alice, alice.receive)
pub.register(john, john.update)

pub.dispatch("It's lunch time")
pub.unregister(john)
pub.dispatch("It's dinner")
