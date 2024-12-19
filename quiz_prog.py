#python quiz program
questions=("who is the father of the computer ?",
           "what is the full form of the email ?",
           "In the virtual world www stands for __________",
           "what do you call a person who uses the internet to explore and communicate ?",
           "who invented the compact Disc ?")
options=(("A.charles babbage" ,"B.Thomas Edison" ,"C.Albert Einstein" ,"D.Isaac Newton "),
         ("A.Electric Mail" ,"B.Exchange Mail" ,"C.Electronic Mail" ,"D.Engagement Mail"),
         ("A.World Without Windows", "B.World Wide Web" ,"C.World Wide Web Applications" ,"D.World Wide Warehouse"),
         ("A.Citizen", "B.Resident" ,"C.Cybernaut" ,"D.None of the above"),
         ("A.James T.Russell" ,"B.Fujio Musuako" ,"C.Thomas Edison", "D. Martin Cooper"))
answers=("A", "C","B","C","A")
guesss=[]
score=0
question_num=0
print("Each question carry one mark")
for question in questions:
    print(question)
    for option in options[question_num]:
        print(option)
    guess=input("Enter (A,B,C,D): ").upper()
    if guess==answers[question_num]:
        score+=1
        print("Correct")
    else:
        print("Incorrect")
        print(f"{answers[question_num]} is the correct answer")
    question_num+=1
    print("______________________________________________________________________")
print("The total score is:",score)
    
        
        
