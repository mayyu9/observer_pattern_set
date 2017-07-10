from observer import Observer
from subject import Subject
from concrete_observer1 import Concrete_ob1
from concrete_observer2 import Concrete_ob2

def main():
    sub = Subject();
    ob1 = Concrete_ob1();
    ob2 = Concrete_ob2();
    sub.attach(ob1);
    sub.attach(ob2);
    sub.subject_state = 123;

if __name__ == '__main__':
    main();