import random
import tkinter as tk
from tkinter import messagebox

# Quiz questions and answers
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["A. Berlin", "B. Paris", "C. London", "D. Rome"],
        "correct_answer": "B"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "choices": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
        "correct_answer": "C"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "choices": ["A. Michelangelo", "B. Vincent van Gogh", "C. Leonardo da Vinci", "D. Pablo Picasso"],
        "correct_answer": "C"
    },
    {
        "question": "Which country is known as the Land of the Rising Sun?",
        "choices": ["A. China", "B. Japan", "C. South Korea", "D. Vietnam"],
        "correct_answer": "B"
    },
    {
        "question": "What is the currency of Germany?",
        "choices": ["A. Pound", "B. Euro", "C. Yen", "D. Dollar"],
        "correct_answer": "B"
    },
    {
        "question": "Which river is the longest in the world?",
        "choices": ["A. Amazon River", "B. Nile River", "C. Mississippi River", "D. Yangtze River"],
        "correct_answer": "B"
    },

]

def load_quiz_questions():
    # You can add more questions here or load them from an external file/database.
    return quiz_questions

def evaluate_answer(user_answer, correct_answer):
    if user_answer.lower() == correct_answer.lower():
        return True
    return False

class QuizApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("General Knowledge Quiz")
        self.geometry("400x300")
        self.configure(bg="#f0f0f0")  # Set the background color to light grey

        self.quiz_questions = load_quiz_questions()
        self.current_question = 0
        self.score = 0

        self.create_widgets()
        self.display_question()

    def create_widgets(self):
        self.question_label = tk.Label(self, text="", wraplength=350, font=("Arial", 14), bg="#f0f0f0")
        self.question_label.pack(pady=20)

        self.choice_var = tk.StringVar()
        self.choices_radiobuttons = []
        for i in range(4):
            choice_radio = tk.Radiobutton(self, text="", variable=self.choice_var, value="", font=("Arial", 12), bg="#f0f0f0", command=self.on_answer_select)
            choice_radio.pack(anchor=tk.W)
            self.choices_radiobuttons.append(choice_radio)

        self.submit_button = tk.Button(self, text="Submit", font=("Arial", 12), command=self.on_submit)
        self.submit_button.pack(pady=10)

        self.result_label = tk.Label(self, text="", font=("Arial", 16), bg="#f0f0f0")
        self.result_label.pack(pady=10)


    def display_question(self):
        question_data = self.quiz_questions[self.current_question]
        self.question_label.config(text=question_data["question"])

        choices = question_data["choices"]
        for i in range(4):
            self.choices_radiobuttons[i].config(text=choices[i], value=choices[i][0])

        self.choice_var.set("")

    def on_answer_select(self):
        pass

    def on_submit(self):
        user_answer = self.choice_var.get()
        correct_answer = self.quiz_questions[self.current_question]["correct_answer"]
        if evaluate_answer(user_answer, correct_answer):
            self.score += 1

        self.current_question += 1
        if self.current_question < len(self.quiz_questions):
            self.display_question()
        else:
            self.show_final_results()

    def show_final_results(self):
        self.question_label.pack_forget()
        for radio_button in self.choices_radiobuttons:
            radio_button.pack_forget()
        self.submit_button.pack_forget()

        final_score = f"Your final score is: {self.score}/{len(self.quiz_questions)}"
        if self.score == len(self.quiz_questions):
            performance_message = "Congratulations! You got a perfect score!"
        elif self.score >= len(self.quiz_questions) / 2:
            performance_message = "Great job! You know quite a bit!"
        else:
            performance_message = "Keep practicing to improve your knowledge."

        self.result_label.config(text=f"{final_score}\n{performance_message}")
        self.result_label.pack(pady=50)

        # Ask if the user wants to play again
        play_again = messagebox.askyesno("Play Again?", "Do you want to play again?")
        if play_again:
            self.destroy()  # Destroy the current window
            self.__init__()  # Re-initialize the QuizApp
        else:
            self.quit()


if __name__ == "__main__":
    app = QuizApp()
    app.mainloop()
