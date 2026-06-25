import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random  
import time

# quiz questions and answers
quizzes = [
    # World Knowledge
    {"question": "What is the capital of Japan?", "answers": ["Tokyo", "Seoul", "Beijing", "Bangkok"], "correct": "Tokyo"},
    {"question": "Which country is known as the Land of the Rising Sun?", "answers": ["Japan", "China", "India", "South Korea"], "correct": "Japan"},
    {"question": "What is the largest country in the world by land area?", "answers": ["Russia", "Canada", "China", "United States"], "correct": "Russia"},
    {"question": "Which country is famous for having the Eiffel Tower?", "answers": ["France", "Italy", "Spain", "Germany"], "correct": "France"},
    {"question": "Which South American country is known for its Amazon Rainforest?", "answers": ["Brazil", "Argentina", "Peru", "Colombia"], "correct": "Brazil"},
    {"question": "What is the smallest country in the world by land area?", "answers": ["Vatican City", "Monaco", "San Marino", "Liechtenstein"], "correct": "Vatican City"},
    {"question": "Which country is home to the Great Barrier Reef?", "answers": ["Australia", "Indonesia", "Malaysia", "Philippines"], "correct": "Australia"},
    {"question": "In which country can you find the Taj Mahal?", "answers": ["India", "Pakistan", "Bangladesh", "Nepal"], "correct": "India"},
    {"question": "Which country is known for its tulips and windmills?", "answers": ["Netherlands", "Belgium", "Denmark", "Sweden"], "correct": "Netherlands"},
    {"question": "Which country is famous for its pyramids and the Sphinx?", "answers": ["Egypt", "Greece", "Italy", "Turkey"], "correct": "Egypt"},
    {"question": "Which country is known as the 'Land of Ice and Fire'?", "answers": ["Iceland", "Norway", "Sweden", "Finland"], "correct": "Iceland"},
    {"question": "What is the capital of Canada?", "answers": ["Ottawa", "Toronto", "Vancouver", "Montreal"], "correct": "Ottawa"},
    {"question": "Which country is known for the ancient city of Petra?", "answers": ["Jordan", "Lebanon", "Syria", "Egypt"], "correct": "Jordan"},
    {"question": "Which country has the longest coastline in the world?", "answers": ["Canada", "Russia", "Australia", "United States"], "correct": "Canada"},
    {"question": "What is the capital city of Australia?", "answers": ["Canberra", "Sydney", "Melbourne", "Brisbane"], "correct": "Canberra"},
    {"question": "Which country is known for its traditional Samurai warriors?", "answers": ["Japan", "China", "Korea", "Mongolia"], "correct": "Japan"},
    {"question": "Which country is known for the pyramids of Giza?", "answers": ["Egypt", "Sudan", "Morocco", "Saudi Arabia"], "correct": "Egypt"},
    {"question": "What is the longest river in the world?", "answers": ["Amazon", "Nile", "Yangtze", "Mississippi"], "correct": "Nile"},
    {"question": "Which country has the largest population?", "answers": ["China", "India", "United States", "Indonesia"], "correct": "China"},
    {"question": "Which city is famous for the landmark Big Ben?", "answers": ["London", "Paris", "Berlin", "Rome"], "correct": "London"},
    {"question": "What is the capital of Germany?", "answers": ["Berlin", "Munich", "Hamburg", "Frankfurt"], "correct": "Berlin"},
    {"question": "Which country is home to the historical site Machu Picchu?", "answers": ["Peru", "Chile", "Argentina", "Ecuador"], "correct": "Peru"},
    {"question": "In which country can you find the Great Wall?", "answers": ["China", "Japan", "India", "Vietnam"], "correct": "China"},
    {"question": "Which desert is the largest in the world?", "answers": ["Sahara", "Arabian", "Gobi", "Kalahari"], "correct": "Sahara"},
    {"question": "Which ocean is the largest?", "answers": ["Pacific", "Atlantic", "Indian", "Arctic"], "correct": "Pacific"},
    {"question": "Which city is known as 'The Eternal City'?", "answers": ["Rome", "Athens", "Cairo", "Jerusalem"], "correct": "Rome"},

    # Entertainment
    {"question": "Who directed the film 'Inception'?", "answers": ["Christopher Nolan", "Steven Spielberg", "Martin Scorsese", "Quentin Tarantino"], "correct": "Christopher Nolan"},
    {"question": "Which movie won the Academy Award for Best Picture in 1994?", "answers": ["Forrest Gump", "Pulp Fiction", "The Shawshank Redemption", "Braveheart"], "correct": "Forrest Gump"},
    {"question": "What is the name of the fictional wizarding school in the 'Harry Potter' series?", "answers": ["Hogwarts", "Beauxbatons", "Durmstrang", "Ilvermorny"], "correct": "Hogwarts"},
    {"question": "Who starred as Jack Dawson in the film 'Titanic'?", "answers": ["Leonardo DiCaprio", "Brad Pitt", "Tom Cruise", "Johnny Depp"], "correct": "Leonardo DiCaprio"},
    {"question": "Which TV show features a coffee shop called Central Perk?", "answers": ["Friends", "How I Met Your Mother", "Seinfeld", "The Big Bang Theory"], "correct": "Friends"},
    {"question": "What is the title of the first 'Star Wars' film released in 1977?", "answers": ["A New Hope", "The Empire Strikes Back", "Return of the Jedi", "Phantom Menace"], "correct": "A New Hope"},
    {"question": "Which singer is known as the 'Queen of Pop'?", "answers": ["Madonna", "Lady Gaga", "Beyoncé", "Taylor Swift"], "correct": "Madonna"},
    {"question": "Who played the role of Iron Man in the Marvel Cinematic Universe?", "answers": ["Robert Downey Jr.", "Chris Evans", "Mark Ruffalo", "Tom Holland"], "correct": "Robert Downey Jr."},
    {"question": "Which animated film features a character named Woody?", "answers": ["Toy Story", "Finding Nemo", "The Lion King", "Frozen"], "correct": "Toy Story"},
    {"question": "What genre of music is Elvis Presley most associated with?", "answers": ["Rock and Roll", "Jazz", "Classical", "Pop"], "correct": "Rock and Roll"},
    {"question": "Who voiced the character of Simba in 'The Lion King' (1994)?", "answers": ["Matthew Broderick", "Robin Williams", "Mufasa", "James Earl Jones"], "correct": "Matthew Broderick"},
    {"question": "Which movie features a character named Luke Skywalker?", "answers": ["Star Wars", "The Matrix", "Indiana Jones", "Back to the Future"], "correct": "Star Wars"},
    {"question": "Which actor played the role of Captain Jack Sparrow?", "answers": ["Johnny Depp", "Orlando Bloom", "Leonardo DiCaprio", "Brad Pitt"], "correct": "Johnny Depp"},
    {"question": "In which movie does the phrase 'May the Force be with you' come from?", "answers": ["Star Wars", "The Matrix", "Avengers", "Jurassic Park"], "correct": "Star Wars"},
    {"question": "Who is known as the King of Pop?", "answers": ["Michael Jackson", "Prince", "Elvis Presley", "Beyoncé"], "correct": "Michael Jackson"},
    {"question": "Which animated movie features a character named Elsa?", "answers": ["Frozen", "Moana", "Tangled", "The Lion King"], "correct": "Frozen"},
    {"question": "Who directed the movie 'Avatar'?", "answers": ["James Cameron", "Steven Spielberg", "Christopher Nolan", "Peter Jackson"], "correct": "James Cameron"},
    {"question": "Which 90s TV show featured a character named Ross Geller?", "answers": ["Friends", "Seinfeld", "The Office", "How I Met Your Mother"], "correct": "Friends"},
    {"question": "What was the title of the first James Bond film?", "answers": ["Dr. No", "Goldfinger", "Casino Royale", "Skyfall"], "correct": "Dr. No"},
    {"question": "Who starred as the Joker in the 2008 film 'The Dark Knight'?", "answers": ["Heath Ledger", "Jack Nicholson", "Jared Leto", "Joaquin Phoenix"], "correct": "Heath Ledger"},

    # Sports
    {"question": "Which country won the FIFA World Cup in 2018?", "answers": ["France", "Croatia", "Germany", "Argentina"], "correct": "France"},
    {"question": "Which sport is known as 'the beautiful game'?", "answers": ["Soccer", "Basketball", "Tennis", "Golf"], "correct": "Soccer"},
    {"question": "Who holds the record for the most home runs in a single MLB season?", "answers": ["Barry Bonds", "Hank Aaron", "Babe Ruth", "Mark McGwire"], "correct": "Barry Bonds"},
    {"question": "What is the maximum break possible in snooker?", "answers": ["147", "155", "150", "140"], "correct": "147"},
    {"question": "Which city hosted the Summer Olympics in 2020?", "answers": ["Tokyo", "Beijing", "London", "Rio de Janeiro"], "correct": "Tokyo"},
    {"question": "Which tennis Grand Slam is played on grass courts?", "answers": ["Wimbledon", "US Open", "French Open", "Australian Open"], "correct": "Wimbledon"},
    {"question": "Which swimmer has won the most Olympic gold medals?", "answers": ["Michael Phelps", "Usain Bolt", "Carl Lewis", "Mark Spitz"], "correct": "Michael Phelps"},
    {"question": "Which country has won the most Rugby World Cups?", "answers": ["New Zealand", "Australia", "South Africa", "England"], "correct": "New Zealand"},
    {"question": "Who is the all-time top scorer in the NBA?", "answers": ["Kareem Abdul-Jabbar", "LeBron James", "Michael Jordan", "Karl Malone"], "correct": "Kareem Abdul-Jabbar"},
    {"question": "Which country won the 2019 Cricket World Cup?", "answers": ["England", "India", "Australia", "New Zealand"], "correct": "England"},
    {"question": "Which country won the FIFA World Cup in 2014?", "answers": ["Germany", "Brazil", "Argentina", "Netherlands"], "correct": "Germany"},
    {"question": "Who holds the record for the most goals in World Cup history?", "answers": ["Marta", "Ronaldo", "Miroslav Klose", "Pele"], "correct": "Miroslav Klose"},
    {"question": "Which team won the NBA Championship in 2016?", "answers": ["Cleveland Cavaliers", "Golden State Warriors", "Miami Heat", "Los Angeles Lakers"], "correct": "Cleveland Cavaliers"},
    {"question": "Who won the first ever gold medal in Olympic history?", "answers": ["James Connolly", "Michael Phelps", "Usain Bolt", "Larisa Latynina"], "correct": "James Connolly"},
    {"question": "Which team won the most Super Bowl championships?", "answers": ["New England Patriots", "Dallas Cowboys", "Pittsburgh Steelers", "San Francisco 49ers"], "correct": "New England Patriots"},
    {"question": "What is the highest possible score in a game of bowling?", "answers": ["300", "250", "400", "500"], "correct": "300"},
    {"question": "Which country hosted the 2012 Summer Olympics?", "answers": ["United Kingdom", "China", "Greece", "Australia"], "correct": "United Kingdom"},
    {"question": "Who is the most decorated Olympian of all time?", "answers": ["Michael Phelps", "Usain Bolt", "Larisa Latynina", "Mark Spitz"], "correct": "Michael Phelps"},
    {"question": "Which country won the first Rugby World Cup?", "answers": ["New Zealand", "South Africa", "England", "Australia"], "correct": "New Zealand"},
    {"question": "Which country has the most Tour de France wins?", "answers": ["France", "Belgium", "Italy", "Spain"], "correct": "France"},

    # Religions
    {"question": "What is the holy book of Islam?", "answers": ["Quran", "Bible", "Vedas", "Torah"], "correct": "Quran"},
    {"question": "Which religion follows the teachings of Buddha?", "answers": ["Buddhism", "Hinduism", "Islam", "Christianity"], "correct": "Buddhism"},
    {"question": "In which city is the Vatican located?", "answers": ["Rome", "Paris", "Jerusalem", "Athens"], "correct": "Rome"},
    {"question": "Which religion is known for the practice of meditation and yoga?", "answers": ["Hinduism", "Islam", "Judaism", "Sikhism"], "correct": "Hinduism"},
    {"question": "Who is considered the founder of Christianity?", "answers": ["Jesus Christ", "Muhammad", "Buddha", "Moses"], "correct": "Jesus Christ"},
    {"question": "What is the name of the Jewish day of rest?", "answers": ["Sabbath", "Ramadan", "Eid", "Diwali"], "correct": "Sabbath"},
    {"question": "Which Hindu festival is known as the 'Festival of Lights'?", "answers": ["Diwali", "Holi", "Navratri", "Raksha Bandhan"], "correct": "Diwali"},
    {"question": "Which religious leader is known for his teachings on non-violence and civil rights?", "answers": ["Mahatma Gandhi", "Nelson Mandela", "Martin Luther King Jr.", "Dalai Lama"], "correct": "Mahatma Gandhi"},
    {"question": "What is the primary language of the Bible's Old Testament?", "answers": ["Hebrew", "Greek", "Aramaic", "Latin"], "correct": "Hebrew"},
    {"question": "Which religion is associated with the practice of meditation?", "answers": ["Buddhism", "Christianity", "Islam", "Judaism"], "correct": "Buddhism"},
    {"question": "What is the name of the Jewish New Year?", "answers": ["Rosh Hashanah", "Yom Kippur", "Hanukkah", "Passover"], "correct": "Rosh Hashanah"},
    {"question": "Which religion believes in the concept of Karma?", "answers": ["Hinduism", "Buddhism", "Christianity", "Judaism"], "correct": "Hinduism"},
    {"question": "What is the holy book of Christians?", "answers": ["Bible", "Quran", "Vedas", "Talmud"], "correct": "Bible"},
    {"question": "Which festival is celebrated by the Jewish community with the lighting of a menorah?", "answers": ["Hanukkah", "Passover", "Yom Kippur", "Purim"], "correct": "Hanukkah"},
    {"question": "In Islam, which city is considered the holiest?", "answers": ["Mecca", "Medina", "Jerusalem", "Cairo"], "correct": "Mecca"},
    {"question": "Which religion celebrates Diwali, the Festival of Lights?", "answers": ["Hinduism", "Sikhism", "Buddhism", "Jainism"], "correct": "Hinduism"},
    {"question": "What is the name of the Muslim place of worship?", "answers": ["Mosque", "Temple", "Church", "Synagogue"], "correct": "Mosque"},
    {"question": "Who is the central figure of Christianity?", "answers": ["Jesus Christ", "Muhammad", "Buddha", "Abraham"], "correct": "Jesus Christ"},
    {"question": "Which Hindu god is known as the Destroyer in the Holy Trinity?", "answers": ["Shiva", "Vishnu", "Brahma", "Ganesh"], "correct": "Shiva"},

]
current_question_index = 0
correct_answers = 0
incorrect_answers = 0
timer_seconds = 30  # 30 seconds 
time_left = timer_seconds
timer_running = False

def start_quiz():
    global current_question_index, correct_answers, incorrect_answers, timer_running, time_left
    current_question_index = 0
    correct_answers = 0
    incorrect_answers = 0
    random.shuffle(quizzes)  
    timer_running = False
    time_left = timer_seconds  
    open_quiz_window()

def open_quiz_window():
    global current_question_index, correct_answers, incorrect_answers, timer_running, time_left

    if current_question_index >= len(quizzes):
        messagebox.showinfo("Quiz Completed", f"You have completed the quiz!\nCorrect Answers: {correct_answers}\nIncorrect Answers: {incorrect_answers}")
        return

    quiz_window = tk.Toplevel(root)
    quiz_window.title("Quiz")
    quiz_window.geometry("700x700")  # Adjust window size
    quiz_window.configure(bg="#e0e0e0")

    quiz_frame = tk.Frame(quiz_window, padx=20, pady=20, bg="#ffffff", borderwidth=2, relief="groove")
    quiz_frame.pack(expand=True, fill="both", padx=10, pady=10)

    stats_frame = tk.Frame(quiz_window, padx=10, pady=10, bg="#e0e0e0")
    stats_frame.pack(side="top", anchor="ne")

    global correct_label, incorrect_label, timer_label
    correct_label = tk.Label(stats_frame, text=f"Correct Answers: {correct_answers}", font=("Arial", 12), bg="#e0e0e0")
    incorrect_label = tk.Label(stats_frame, text=f"Incorrect Answers: {incorrect_answers}", font=("Arial", 12), bg="#e0e0e0")
    timer_label = tk.Label(stats_frame, text=f"Time Left: {time_left}s", font=("Arial", 12), bg="#e0e0e0")
    
     # timer_label with red color and bold font
    timer_label = tk.Label(stats_frame, text=f"Time Left: {time_left}s", font=("Arial", 14, "bold"), fg="red", bg="#e0e0e0")

    correct_label.pack(anchor="ne")
    incorrect_label.pack(anchor="ne")
    timer_label.pack(anchor="ne")

    quiz = quizzes[current_question_index]

    question_label = tk.Label(quiz_frame, text=quiz['question'], font=("Arial", 16), bg="#dbe9f4", anchor="w", wraplength=650, padx=10, pady=10, relief="flat")
    question_label.pack(pady=(10, 5), anchor="w")

    selected_option = tk.StringVar()

    for idx, answer in enumerate(quiz["answers"]):
        option_label = chr(65 + idx)
        tk.Radiobutton(quiz_frame, text=f"Option {option_label}: {answer}", variable=selected_option, value=answer, font=("Arial", 12), bg="#f4f4f4", anchor="w", padx=10, pady=5, relief="flat").pack(anchor="w")

    submit_button = tk.Button(quiz_frame, text="Submit", command=lambda: check_answer(selected_option.get(), quiz_window), font=("Arial", 14), bg="#4CAF50", fg="#ffffff", relief="raised")
    submit_button.pack(pady=20, side="bottom")

    # Start the timer countdown
    start_timer(quiz_window)

def start_timer(quiz_window):
    global timer_running, time_left

    if timer_running:
        return  

    timer_running = True
    def countdown():
        global time_left, timer_running
        if time_left > 0:
            time_left -= 1
            timer_label.config(text=f"Time Left: {time_left}s")
            quiz_window.after(1000, countdown)  
        else:
            # Time is up, automatically move to the next question
            messagebox.showinfo("Time's Up!", "Time is up! Moving to the next question.")
            check_answer("", quiz_window)  #
    countdown()

def check_answer(selected_answer, quiz_window):
    global current_question_index, correct_answers, incorrect_answers, timer_running, time_left

    correct_answer = quizzes[current_question_index]['correct']

    # Check if the selected answer is correct
    if selected_answer == correct_answer:
        messagebox.showinfo("Correct!", "Your answer is correct.")
        correct_answers += 1
    else:
        messagebox.showinfo("Incorrect", "Your answer is incorrect.")
        incorrect_answers += 1

    current_question_index += 1
    timer_running = False  # Stop the timer when the question is answered
    time_left = timer_seconds  # Reset the timer for the next question
    quiz_window.destroy()  # Close the current question window
    open_quiz_window()  # Open the next question window

root = tk.Tk()
root.title("Quiz Game")
root.geometry("700x700")
root.configure(bg="#198dbc")

icon = ImageTk.PhotoImage(file="Path to your image") # Download the image and enter it's path here 
root.iconphoto(False, icon)

frame = tk.Frame(root, padx=20, pady=20, bg="#198dbc")
frame.pack(expand=True, fill="both")

logo_image = Image.open("Path to your image") # Download the image and enter it's path here 
logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = tk.Label(frame, image=logo_photo, bg="#198dbc")
logo_label.image = logo_photo
logo_label.pack(pady=(0, 20))

title_label = tk.Label(frame, text="Welcome to the Quiz Game", font=("Arial", 18, "bold"), bg="#198dbc", fg="#FFFFFF")
title_label.pack(pady=(0, 20))

instructions = """
Test your knowledge with our fun and challenging quiz.
Click the button below to get started!
"""
instructions_label = tk.Label(frame, text=instructions, font=("Arial Rounded MT Bold", 18), justify="center", bg="#198dbc", fg="#FFFFFF")
instructions_label.pack(pady=(10, 20))

start_button = tk.Button(frame, text="Start Quiz", font=("Arial", 14), command=start_quiz)
start_button.pack(pady=20)

root.mainloop()
