class InvalidPasswordException(Exception):
    """
    InvalidPasswordException is raised when an invalid password is entered.
    You can use InvalidPasswordException as is, you do not need to
    modify/add any code.
    """
    def __str__(self):
        return "Invalid password was entered!"

class edx(object):
    def __init__(self, courses):
        self.myCourses = []
        for course in courses:
            self.myCourses.append(courseInfo(course))

    def setGrade(self, grade, course="6.01x", password=None):
        """  
        grade: integer greater than or equal to 0 and less than or equal to 100
        course: string 
        password: string

        This method sets the grade in the courseInfo object named by `course`, depending on
        if the proper password is supplied.

        The password must match the default teacher's password.

        If the password is omitted, a "Password Required" message should be returned.

        If the password is incorrect, an `InvalidPasswordException` should be raised.

        If `course` was not part of the initialization, then no grade is set, and no
        error is thrown.

        The method does not return a value, unless the password is omitted, then a "Password Required"
        message is returned.
        """
        #   fill in code to set the grade
        pass

    def getGrade(self, course="6.02x", password=None):
        """
        course: string 
        password: string

        This method gets the grade in the the courseInfo object named by `course`, depending on
        if the proper password is supplied.

        The password must match the default student's password.

        If the password is omitted, a "Password Required" message should be returned.

        If the password is incorrect, an `InvalidPasswordException` should be raised.

        returns: the integer grade for `course`. 
        If `course` was not part of the initialization, returns -1.
        If the password is omitted, returns "Password Required".
        """
        #   fill in code to get the grade
        pass

    def setPset(self, pset, score, course="6.00x"):
        """
        pset: a string or a number
        score: an integer between 0 and 100
        course: string

        The `score` of the specified `pset` is set for the
        given `course` using the courseInfo object.

        If `course` is not part of the initialization, then no pset score is set,
        and no error is thrown.
        """
        #   fill in code to set the pset
        pass

    def getPset(self, pset, course="6.00x"):
        """
        pset: a string or a number
        score: an integer between 0 and 100
        course: string        

        returns: The score of the specified `pset` of the given
        `course` using the courseInfo object.
        If `course` was not part of the initialization, returns -1.
        """
        #   fill in code to get the pset
        pass
