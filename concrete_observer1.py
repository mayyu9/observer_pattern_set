"""
Implement the observer to keep its state updated.
"""
from observer import Observer

class Concrete_ob1(Observer):

    def update(self,arg):
        print("concrete observer",arg);
        self._observer_state = arg;