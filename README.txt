Observer pattern implemented in python using the set()
using the set, we can remove the duplicates observers.

observer.py -> is abstract file, with which we can force users to implement certain methods which are needed for the observers.
concrete_observer1.py -> first observer which is implemented by importing observer.py. this observer is intrested in changes in subject state.
concrete_observer2.py -> second observer which is implemented by importing observer.py. this observer is intrested in changes in subject state.
subject.py -> the subject is the one who notifies all the observers when there is change in state.