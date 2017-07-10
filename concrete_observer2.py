"""
Implement the observer to keep its state updated.
"""
from observer import Observer

class Concrete_ob2(Observer):

    def update(self,arg):
        print("observer2:",arg);
        self._observer_state = arg;