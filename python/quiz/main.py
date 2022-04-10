import csv

class Quiz:
    all_quizzes = []

    def __init__(self, question, choices, answer):
        # implement assert

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
                answer=item.get('answer'),
                # change to answer=int(item.get('answer')) after sorting out bug
            )
    
    def __repr__(self):
        return f"Item('{self.question}', {self.choices}, {self.answer})"


class QuizInterface:
    def print_quiz(self, quiz):
        print('A Quiz!')
        print('===================')

def main():
    Quiz.instantiate_from_csv()
    print(Quiz.all_quizzes)

if __name__ == "__main__":
   main()