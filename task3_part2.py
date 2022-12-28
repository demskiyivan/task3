from abc import ABC, abstractmethod


class ITeacher(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class ICourses(ABC):
    @abstractmethod
    def __init__(self):
        pass


class ILocal(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class IOffsite(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class CourseFactory(ICourses):
    def __init__(self, name, surname, c_name, location, *args):
        self.name = name
        self.surname = surname
        self.c_name = c_name
        self.location = location
        self.topics = args


class Teacher(ITeacher):
    def __init__(self, cf):
        self.name = cf.name
        self.surname = cf.surname
        self.teaching = cf.c_name

    def __str__(self):
        return f"{self.surname} {self.name}. Runs {self.teaching}"


class Courses(ICourses):
    def __init__(self, cf):
        self.c_name = cf.c_name
        self.topics = cf.topics
        self.location = cf.location


class Local(Courses, ILocal):
    def __init__(self, cf):
        super().__init__(cf)

    def __str__(self):
        return f"{self.c_name} has such topic as {self.topics} and is held in a lab {self.location}"


class Offsite(Courses, IOffsite):
    def __init__(self, cf):
        super().__init__(cf)

    def __str__(self):
        return f"{self.c_name} has such topic as {self.topics} and is located in city of {self.location}"


factory = CourseFactory("Ivan", "Ivanov", "rand", "lab2", "random numbers")
x1 = Teacher(factory)
x2 = Local(factory)
print(x1)
print(x2)
