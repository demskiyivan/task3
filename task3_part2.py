class CourseFactory:
    def __init__(self, name, surname, l_or_o, c_name, location, *args):
        self.t_code_n = Teacher(self)
        self.name = name
        self.surname = surname
        self.teaching = c_name
        if l_or_o == "local":
            self.c_code_n = Local(self)
        elif l_or_o == "offsite":
            self.c_code_n = Offsite(self)
        else:
            raise Exception("Please, write local or offsite if the course is local or offsite respectively")
        self.location = location
        self.c_name = c_name
        self.topics = args


class Teacher:
    def __init__(self, cf):
        self.name = cf.name
        self.surname = cf.surname
        self.teaching = cf.teaching

    def __str__(self):
        return f"{self.surname} {self.name}. Runs {self.teaching}"


class Courses:
    def __init__(self, cf):
        self.c_name = cf.c_name
        self.topics = cf.topics
        self.location = cf.location


class Local(Courses):
    def __init__(self, cf):
        super().__init__(cf)

    def __str__(self):
        return f"{self.c_name} has such topic as {self.topics} and is held in a lab {self.location}"


class Offsite(Courses):
    def __init__(self, cf):
        super().__init__(cf)

    def __str__(self):
        return f"{self.c_name} has such topic as {self.topics} and is located in city of {self.location}"
