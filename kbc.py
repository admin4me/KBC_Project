''' I am going to create a project on "KAUN BANEGA CAROREPATI" in this you will get 15 questions for 1 crore prize money, 
for each correct answer your prize money will increase you will be out of game on wrong answer. At the end at the end you will see your amount you are taking home, 
after deducting any taxes liable on winning amount. Play the game and have fun!'''
name = input("Enter your name : ")
print(name, "Welcome to KBC!\nAnswer these 15 Questions and stand a chance to win 1 crore.\n")
Questions = ["1. What is the capital of India?", "2. Who wrote the national anthem of India?", "3. Which planet is known as the ‘Red Planet’?", "4.  What is the full form of CPU in computers?", "5. Who is known as the ‘Missile Man of India’?", "6. How many colors are there in a rainbow", "7. The famous ‘Mona Lisa’ painting was made by which artist?", "8. What is the chemical symbol for water?", "9. Which festival is called the ‘Festival of Lights’ in India?" ,"10. Who was the first Prime Minister of India?", "11. What is the largest mammal in the world?", "12. Which is the smallest planet in our solar system?", "13. What is the capital city of Japan?", "14. In which year did India gain independence from British rule?", "15. Who is the author of the famous book ‘Harry Potter and the Sorcerer’s Stone’?"]
Options = ["A) Mumbai", "B) Kolkata", "C) New Delhi", "D) Chennai\n", "A) Rabindranath Tagore", "B) Bankim Chandra Chattopadhyay", "C) Sarojini Naidu", "D) Mahatma Gandhi\n", "A) Venus", "B) Mars", "C) Jupiter", "D) Saturn\n", "A) Central Processing Unit", "B) Central Program Unit", "C) Control Processing Unit", "D) Central Power Unit\n", "A) C.V. Raman", "B) Homi Bhabha", "C) A.P.J. Abdul Kalam", "D) Vikram Sarabhai\n", "A) 5", "B) 6", "C) 7", "D) 8\n", "A) Leonardo da Vinci", "B) Pablo Picasso", "C) Vincent van Gogh", "D) Michelangelo\n", "A) H2O", "B) O2", "C) CO2", "D) HO\n", "A) Holi", "B) Diwali", "C) Eid", "D) Christmas\n", "A) Sardar Patel", "B) Jawaharlal Nehru", "C) Mahatma Gandhi", "D) Dr. B.R. Ambedkar", "A) Elephant", "B) Blue Whale", "C) Giraffe", "D) Rhinoceros", "A) Earth", "B) Mercury", "C) Mars", "D) Pluto", "A) Beijing", "B) Tokyo", "C) Seoul", "D) Bangkok", "A) 1942", "B) 1947", "C) 1950", "D) 1960", "A) J.R.R. Tolkien", "B) J.K. Rowling", "C) Suzanne Collins", "D) George R.R. Martin"]
answer = ["C", "A", "B", "A", "C", "C", "A", "A", "B", "B", "B", "B", "B", "B", "B"]
cans = 0
for i in Questions:
    print(i)
    for j in Options[Questions.index(i)*4:(Questions.index(i)+1)*4]:
        print(j)
    userans = input("type A, B, C or D for your corrosponding answer : ").upper().strip()
    if answer[Questions.index(i)] == userans:
        print("\nCongratulations!, It was a correct answer\n")
        cans = cans+1
    else:
        print("\nSorry!, you missed it.\n")
        break
print("\nfrom total of 15 Question you had", cans, "Correct Answers\n")
prizemoney = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]
total = prizemoney[cans-1]
print("Congratulations! You won total of ", total)
print("\nThe prize money from KBC falls under section 194B of the income Tax Act, which covers winning from game shows, lotteries and similar competitions.\nFlat 30% TDS is deducted at the source before the contestant receives the money.\nAdditionay 4% of Cess is applied on tax, making effective deduction 31.2%\n")
print("you will receive ", total-total*0.312)