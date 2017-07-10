from abc import ABCMeta,abstractmethod

## this is an interface which will help to get the update info when state changes.
class Observer:
    __metaclass__ = ABCMeta;

    @abstractmethod
    def update(self,arg):
        pass;
