import csv

class Quiz:
    all_quizzes = []

    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

        Quiz.all_quizzes.append(self)


    @classmethod
    def instantiate_from_csv(cls):
        with open('practise/python/quiz/questions.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)


        for item in items:
            Quiz(
                question=item.get('question'),
                choices=item.get('choices'),
                answer=int(item.get('answer')),
            )
    
    def __repr__(self):
        return f"Item('{self.question}', {self.choices}, {self.answer})"

# To do: 
# Print each instance to the quiz interface
# Split choices into list using split method. 
# Add for loop on QuizInterface class to loop over the list.
# Add a row on csv ('result') whether a user has correctly answered a question (default on false)
# Add method on interface to take inputs from console
# Add method looping through 'result' sum(), checking how many is True/False

class QuizInterface:
    def print_quiz(self, quiz):
        print('A Quiz!')
        print('===================')

def main():
    Quiz.instantiate_from_csv()
    print(Quiz.all_quizzes)

if __name__ == "__main__":
   main()