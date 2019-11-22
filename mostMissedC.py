class MostMissedCls:
    def __init__(self):
        self.numQuestions = ""
        self.questions = []
        self.missedQuestion = 0
        self.mostMissed = 0
        self.numMostMissed = 0
        self.errLst = []

    def getQuestions(self):
        while True:
            # Getting the number of questions on the given assignment
            try:
                self.numQuestions = int(input("How many questions were there: "))
                if self.numQuestions != 0:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("That wasn't a valid option.")

        # Appending to list
        self.questions += self.numQuestions * [0]

    def missedQuestions(self):
        # In a loop so any errors restart it for user to try again
        while True:
            # Getting Question Number
            self.missedQuestion = str.lower(input("Type the number of the question(s) missed, separated by a space "
                                                  "for multiple questions, or type 'results' to see the results: "))
            self.missedQuestion = self.missedQuestion.split(" ")

            # Testing if user wants results
            if "results" in self.missedQuestion:
                break

            """This is some janky code that tests if it is a number, and then converts all usable data to int"""
            # Finding all non-int characters
            for i in self.missedQuestion:
                try:
                    int(i)
                except ValueError:
                    self.errLst.append(i)
                    print(f"{i} is not a valid question number"
                          f"")

            # Removing bad values
            for i in self.errLst:
                self.missedQuestion.remove(i)

            # Converting to int and defining new list
            self.missedQuestion = [int(x) for x in self.missedQuestion]
            """End Jankyness"""

            # Adding one to the missed question counter, unless number isn't a question
            for i in self.missedQuestion:
                try:
                    if self.missedQuestion != 0:
                        self.questions[i - 1] += 1
                    else:
                        raise IndexError
                except IndexError:
                    print(f"{i} is not a valid question number.")
                    continue

        return self.questions

    def results(self, lst):
        # Takes the list and finds the most missed question and the question number
        # TODO Show all results that are equal to the max value, For loop?
        self.numMostMissed = max(lst)
        self.mostMissed = lst.index(self.numMostMissed) + 1
        print(f"The most missed question(s) was: {self.mostMissed}, being missed {self.numMostMissed} times.")
