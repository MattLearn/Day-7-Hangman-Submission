import random
import hangman_art as art
import wordlist


def game_setup():
  life = 6
  display_list=[]
  chosen_word = random.choice(wordlist.word_list)
  for letter in chosen_word:
    display_list.append('_')
  print(art.logo)
  game_loop(life,chosen_word,display_list)

def game_loop(lives,answer,display):
  #print(answer)
  print(art.stages[lives])
  print(f"Tries left: {lives}")
  print(display)

  while answer not in display:
  
    guess = input("Guess a letter: ").lower()

    if guess in display:
      print("you already entered this letter")
    
    elif guess in answer:
      print("You Found one!")
      for index, letter in enumerate(answer):
        if guess == letter:
          display[index] = guess
    
    else:
      print("This letter isn't in the word!")
      lives -=1
      if lives == 0:
        print("You Lose!")
        break
  
    if answer in ''.join(display):
      print("You win")
      break
    
    print(art.stages[lives])
    print(f"Tries left: {lives}")
    print(display)
      
game_setup()
if(input("would you like to play again? (Y or N)").lower() == "y"):
  game_setup()