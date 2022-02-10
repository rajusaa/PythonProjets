import tkinter
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class UserInterface():


    def __init__(self,quiz_brain : QuizBrain ):
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        #self.window.minsize(400,750)
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        #self.window.config(highlightthickness=0)

        self.score = 0

        self.label = tkinter.Label(text=f"Score: {self.score}", bg = THEME_COLOR, fg='white')
        self.label.grid(column=1, row=0)

        self.canvas = tkinter.Canvas(height=250, width=300, bg='white', highlightthickness=0)
        self.create_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="test",
            fill='black',
            font=('Arial', 20, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=10)

        self.right_img = tkinter.PhotoImage(file="./images/true.png",)
        self.button_right = tkinter.Button(image=self.right_img, command=self.verify_true_answer)
        self.button_right.grid(column=0, row=2)

        self.wrong_img = tkinter.PhotoImage(file="./images/false.png",)
        self.button_wrong = tkinter.Button(image=self.wrong_img, command=self.verify_false_answer)
        self.button_wrong.grid(column=1, row=2)

        self.next_question()
        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg='white')
        self.label.config(text=f"Score:{self.score}")
        question = self.quiz.next_question()
        self.canvas.itemconfig(self.create_text, text=question)

    def verify_true_answer(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def verify_false_answer(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
            self.score+=1
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.next_question)