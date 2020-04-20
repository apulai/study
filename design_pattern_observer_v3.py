# https://www.youtube.com/watch?v=87MNuBgeg34&list=PLTbTIHxH9yV4hWlSVsYisRprP78fhGFKx&index=2&t=0s
# Observers
class Subscriber:
    def __init__(self, name):
        self.name=name
    def update(self, message):
        print('{} got message "{}"'.format(self.name, message))


# Observable class
class Publisher:
    # Dictionary comprehension
    #Minden létrehoz egy dict-et, úgy hogy minden esemény mellé belerak egy üres dict-et
    def __init__(self, events):
        self.subscribers = { event: dict()
                          for event in events }

    #Visszadja, hogy az adott eventre, ki fizetett elő
    def get_subscribers(self, event):
        return self.subscribers[event]

    def register(self, event, who, callback=None):
        if callback is None:
            callback = getattr(who, 'update')
        # A fenti segedfüggvény, szerintem itt egy bonyolult
        # szintaktikat segit egyszerusíteni
        self.get_subscribers(event)[who] = callback
    def unregister(self, event , who):
        del self.get_subscribers(event)[who]
    def dispatch(self,event, message):
        for subsciber, callback in self.get_subscribers(event).items():
            callback(message)

pub = Publisher(['lunch','dinner'])

bob = Subscriber('Bob')
alice = Subscriber('Alice')
john= Subscriber('John')

pub.register('lunch',bob)
pub.register('lunch',alice)
pub.register('lunch',john)

pub.register('dinner',bob)
pub.register('dinner',alice)


pub.dispatch('lunch',"It's lunchtime")
pub.dispatch('dinner',"Dinner is served")

