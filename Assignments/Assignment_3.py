def run_quiz():
    score = 0

    questions = [
        {
            "q": "1) What is the output of 3 + 2?",
            "a": "a) 4",
            "b": "b) 5",
            "c": "c) 6",
            "d": "d) 32",
            "correct": "b"
        },
        {
            "q": "2) Which keyword creates a function?",
            "a": "a) func",
            "b": "b) define",
            "c": "c) def",
            "d": "d) function",
            "correct": "c"
        },
        {
            "q": "3) Which of these is a list?",
            "a": "a) (1, 2, 3)",
            "b": "b) [1, 2, 3]",
            "c": "c) {1, 2, 3}",
            "d": "d) {'a':1}",
            "correct": "b"
        },
        {
            "q": "4) What symbol starts a comment?",
            "a": "a) @",
            "b": "b) //",
            "c": "c) #",
            "d": "d) !",
            "correct": "c"
        },
        {
            "q": "5) Which data type is immutable?",
            "a": "a) list",
            "b": "b) tuple",
            "c": "c) set",
            "d": "d) dict",
            "correct": "b"
        },
        {
            "q": "6) What is the output of len('hello')?",
            "a": "a) 4",
            "b": "b) 5",
            "c": "c) 6",
            "d": "d) Error",
            "correct": "b"
        },
        {
            "q": "7) Which operator is used for exponent?",
            "a": "a) *",
            "b": "b) ^",
            "c": "c) **",
            "d": "d) //",
            "correct": "c"
        },
        {
            "q": "8) Which is a boolean value?",
            "a": "a) yes",
            "b": "b) True",
            "c": "c) 1.0",
            "d": "d) correct",
            "correct": "b"
        },
        {
            "q": "9) What is type(10)?",
            "a": "a) int",
            "b": "b) float",
            "c": "c) number",
            "d": "d) string",
            "correct": "a"
        },
        {
            "q": "10) Which function prints output?",
            "a": "a) echo()",
            "b": "b) print()",
            "c": "c) show()",
            "d": "d) display()",
            "correct": "b"
        },
        {
            "q": "11) Which loop repeats a fixed number of times?",
            "a": "a) for",
            "b": "b) while",
            "c": "c) repeat",
            "d": "d) loop",
            "correct": "a"
        },
        {
            "q": "12) Which keyword stops a loop?",
            "a": "a) exit",
            "b": "b) break",
            "c": "c) stop",
            "d": "d) end",
            "correct": "b"
        },
        {
            "q": "13) Which one is a string?",
            "a": "a) 'hello'",
            "b": "b) 100",
            "c": "c) True",
            "d": "d) 5.5",
            "correct": "a"
        },
        {
            "q": "14) Which converts text to an integer?",
            "a": "a) str()",
            "b": "b) text()",
            "c": "c) int()",
            "d": "d) number()",
            "correct": "c"
        },
        {
            "q": "15) What is the output of bool('hi')?",
            "a": "a) False",
            "b": "b) True",
            "c": "c) None",
            "d": "d) Error",
            "correct": "b"
        },
        {
            "q": "16) Which adds an item to a list?",
            "a": "a) add()",
            "b": "b) push()",
            "c": "c) append()",
            "d": "d) insert()",
            "correct": "c"
        },
        {
            "q": "17) Which of these is a dictionary?",
            "a": "a) {'a':1, 'b':2}",
            "b": "b) [1,2,3]",
            "c": "c) (1,2,3)",
            "d": "d) {1,2,3}",
            "correct": "a"
        },
        {
            "q": "18) What is 10 % 3?",
            "a": "a) 3",
            "b": "b) 1",
            "c": "c) 0",
            "d": "d) 10",
            "correct": "b"
        },
        {
            "q": "19) What does continue do?",
            "a": "a) ends loop",
            "b": "b) restarts program",
            "c": "c) skips to next iteration",
            "d": "d) exits function",
            "correct": "c"
        },
        {
            "q": "20) Which operator checks equality?",
            "a": "a) =",
            "b": "b) ==",
            "c": "c) ===",
            "d": "d) equal",
            "correct": "b"
        }
    ]

    print("Welcome to the Python Quiz!\n")

    for q in questions:
        print(q["q"])
        print(q["a"])
        print(q["b"])
        print(q["c"])
        print(q["d"])

        answer = input("Your answer (a/b/c/d): ").lower().strip()

        if answer == q["correct"]:
            print("Correct!\n")
            score += 1
        else:
            print("Wrong! Correct answer:", q["correct"], "\n")

    print("Quiz Finished!")
    print("Your final score:", score, "/", len(questions))

run_quiz()
