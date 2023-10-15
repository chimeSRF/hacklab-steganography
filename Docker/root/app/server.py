#!/usr/bin/env python3
import os
import time
import sys
import shutil
import select

IMAGENAME = 'archive'
VIDEONAME = 'video'
SONGNAME = 'audio_hint'
MIDINAME = 'fairies'
TEXTNAME = 'text'
VIDSCRIPTNAME = 'video_script'
WHITESPNAME = 'whitespace_script'
FAIRY = 'fairy'

PICTUREPATH = f'/app/res/{IMAGENAME}.jpg'
VIDEOPATH = f'/app/res/{VIDEONAME}.mov'
SONGPATH = f'/app/res/{SONGNAME}.mp3'
MIDIPATH = f'/app/res/{MIDINAME}.mid'
TEXTPATH = f'/app/res/{TEXTNAME}.txt'
FAIRYIAMGE = f'/app/res/{FAIRY}.jpg'
# Download the video from https://vimeo.com/874505445
VIDSCRIPTPATH = f'/app/res/{VIDSCRIPTNAME}.py'
WHITESCRIPTPATH = f'/app/res/{WHITESPNAME}.py'
OUTPUT = '/opt/www/'
HOSTNAME = os.environ.get('HOSTNAME')
HOST = f'{HOSTNAME}.rdocker.vuln.land'
# shutil.copyfile(picturePath, output + 'image.jpg')
# print(f'Access here: http://localhost/image.jpg')

class TextAdventure:
    def __init__(self):
        self.game_state = 0
        self.delay = 0.02
        self.force_compartment_attempts = 0
        self.leave_first_room_tries = 0
        self.examined_bookshelfs = False
        self.found_python_script = False
        self.examined_crystal_ball = False
        self.searched_stone_door_surroundings = False
        self.searched_fairy_room_surroundings = False
        self.found_stone_door_scroll = False
        self.fourth_challenge_reached = False
        self.found_fairy_pendant = False
        self.final_room_examined = False
        self.read_final_script = False
        self.saw_stone_board = False
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def slow_print(self, text):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(self.delay)
        print()
        
    def print_link(self, text):
        length = len(text)
        border_line = '═' * (length + 8)
        padding = ' ' * ((length + 8 - len(text)) // 2)

        print(f"""
        ╔{border_line}╗
        ║{padding}{text}{padding}║
        ╚{border_line}╝
        """)

    def print_scroll(self):
        print(r"""
         _______________
    ()==(              (@==()
         '______________'|
           | whispers    |
           |      in     |
           |   the       |
           | frequen-    |
           |       cies  |
         __)_____________|
    ()==(               (@==()
         '--------------'
        """)

    def print_pendant(self):
        print(r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣤⣤⣤⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⠾⠛⠉⠉⠉⠁⠀⠀⠉⠉⠉⠉⠛⠷⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠹⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠏⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡄⠀⠀⠀⠀⠀⠀⢀⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⡀⠀⠀⠀⠀⢀⣾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣷⡀⢀⠀⢀⣾⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣗⠒⠨⢥⣾⣦⠬⠑⠒⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣸⣤⣄⣸⠏⢿⣀⣤⣴⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻lowestC=A⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⢀⣼⣁⣠⣀⣹⣄⠘⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠷⢾⣿⠿⠉⠹⢿⣿⡶⠷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠉⠁⠀
    """)

    def print_ascii_art(self):
        print(r"""
░█▀▀░█▀▀░█▀▀░█▀▄░█▀▀░▀█▀░█▀▀░░░█▀█░█▀▀░░░▀█▀░█░█░█▀▀░░░
░▀▀█░█▀▀░█░░░█▀▄░█▀▀░░█░░▀▀█░░░█░█░█▀▀░░░░█░░█▀█░█▀▀░░░
░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░░▀░░▀▀▀░░░▀▀▀░▀░░░░░░▀░░▀░▀░▀▀▀░░░  
░█▄█░█▀█░█▀▀░█▀▀░▀░█▀▀░░░█▀█░█▀▄░█▀▀░█░█░▀█▀░█░█░█▀▀
░█░█░█▀█░█░█░█▀▀░░░▀▀█░░░█▀█░█▀▄░█░░░█▀█░░█░░▀▄▀░█▀▀
░▀░▀░▀░▀░▀▀▀░▀▀▀░░░▀▀▀░░░▀░▀░▀░▀░▀▀▀░▀░▀░▀▀▀░░▀░░▀▀▀                                   
        """)
        
    def print_altar(self):
        print(r"""

  ▒▒▒▒▒▒▓▓▒▒▒▒  ▒▒▒▒▒▒░░▓▓░░░░░░▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░▒
░░░░▓▓▒▒▒░░░░▒▒░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  ▒▒░░  
  ▓▓▒▒▒▒░░   In shadows lurks a secret code,   ▒▒░░▒▒▒▒▒▒░░░
 ░░  ░░░░ Seek the path that's less bestowed.    ▒▒░░▒▒▒▒░░░░░░
  ▒▒░░░░   Between the lines, you'll find the truth,▒▒▒▒▒▒▒▒░░░░░░░
 ▒▒▒▒     In spaces unseen lies the hidden proof.  ▒▒░░░░▓▓░░░░
░░░░░░░░                                          ▒▒░░░░▓▓░░
 ░░░░▒▒░░ Not the text itself, but the gaps between, ░░░░░▒▒  ▒▒▒▒
    ░░▒▒▓▓ Are where the answer lies, yet to be seen. ░░░░▒▒▓▓░░▒▒▒▒▓░
   ░░░░░░ Read the signs they start with zero,   ▒▒▒▒▒▒▒▒░░
 ░░░░░░ You'll find the key, and be the hero.  ░░▒▒▒▒▒▒░░
   ░░▒▒░░                                          ░░░░░░▒▒
  ░░░░░░░░░░░▒▒░░░░░░▒▒░░░░▒▒▒▒░░  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░▒▒░░▒▒░░░░░░▒▒░░░░▒▒▒▒░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░  ░░░░░░░░░
░░▒▒░░▒▒░░░░▒▒▒▒  ░░▓▓░░▒▒▒▒░░░░░░░░░░    ░░░░░░░░░░░░░░░░░░░░
        """)    
    
    def print_end(self):
        print(r"""
_________          _______    _______  _        ______  
\__   __/|\     /|(  ____ \  (  ____ \( (    /|(  __  \ 
   ) (   | )   ( || (    \/  | (    \/|  \  ( || (  \  )
   | |   | (___) || (__      | (__    |   \ | || |   ) |
   | |   |  ___  ||  __)     |  __)   | (\ \) || |   | |
   | |   | (   ) || (        | (      | | \   || |   ) |
   | |   | )   ( || (____/\  | (____/\| )  \  || (__/  )
   )_(   |/     \|(_______/  (_______/|/    )_)(______/ 
                                                        
        """)
        
    def timed_input(self, prompt, timeout):
        print(prompt, end='', flush=True)
        ready, _, _ = select.select([sys.stdin], [], [], timeout)
        
        if ready:
            return sys.stdin.readline().rstrip()
        else:
            return None

    def start(self):
        self.clear_screen()
        self.print_ascii_art()
        self.game_state = 1
        self.start_screen()

    # ====================================================================== GAME START ======================================================================================= #

    def start_screen(self):
        self.slow_print("Welcome, brave adventurer, to the treacherous depths of the Mage's dungeon!")
        self.slow_print("You stand on the precipice of a perilous journey filled with mystery, danger, and untold treasures.")
        self.slow_print("Are you ready to test your mettle and face the challenges that await within?")
        print("\nOptions:")
        print("[1] Start Quest: Embark on your adventure into the depths of the dungeon.")
        print("[2] Checkpoint: Return to a previously saved checkpoint in your journey.")
        print("[3] Quit: Bid farewell to the Mage's dungeon.")
        time.sleep(0.5)
        choice = input("⊳ ")
        if choice == "1":
            self.enter_dungeon()
        if choice == "2":
            self.checkpoint_system()
        if choice == "3":
            self.quit_game()
        
    def checkpoint_system(self):
        print("\nEnter the checkpoint code:")
        checkpoint = input("⊳ ")
        if checkpoint == "painting":
            self.first_challenge()
        elif checkpoint == "image":
            self.second_challenge()
        elif checkpoint == "library":
            self.third_challenge()
        elif checkpoint == "stonedoor":
            self.audio_path_stone_door_choice()
        elif checkpoint == "audio":
            self.fourth_challenge_audio()
        elif checkpoint == "fairies":
            self.inside_portal()
        elif checkpoint == "midi":
            self.fourth_challenge_midi()
        elif checkpoint == "finalroom":
            self.enter_the_room()
        elif checkpoint == "text":
            self.fifth_challenge()
        else: 
            print("Invalid checkpoint code. Please try again.")
            self.checkpoint_system()

    # ======================================================================= STORY START ======================================================================================== #  
    
    def enter_dungeon(self):
        self.slow_print("\nYou stand at the entrance of dungeon, a sprawling labyrinth beneath Cryptoglyphia.")
        self.slow_print("As you step forward, the darkness engulfs you, and the path ahead is shrouded in mystery.")
        print("o")
        time.sleep(1)
        print("o")
        time.sleep(1)
        print("o")
        time.sleep(1)
        self.slow_print("You enter a dimly lit room, the air heavy with ancient magic.")
        self.slow_print("In the center of the room, you see an ornate frame holding a mysterious painting.")
        self.first_room_choices()
        
    def first_room_choices(self):    
        print("\nWhat would you like to do?")
        print("[1] Examine the painting")
        print("[2] Examine the room")
        if self.leave_first_room_tries == 0:
            print("[3] Leave the room")
        choice = input("⊳ ")
        if choice == "1":
            self.examine_painting()
        if choice == "2":
            self.examine_first_room()
        if self.leave_first_room_tries == 0 and choice == "3":
            self.leave_first_room()
        else:
            print("\nInvalid choice. Please try again.")
            self.first_room_choices()
    
    def examine_first_room(self):
        self.slow_print("\nYou meticulously search the room, scanning every corner for hidden treasures.")
        self.slow_print("However, apart from the painting, you find nothing of significance.")
        self.first_room_choices()
    
    def leave_first_room(self):
        self.slow_print("\nAs you approach the exit, the heavy door suddenly slams shut, blocking your way.")
        self.slow_print("You are trapped in the room, surrounded by mysterious enchantments.")
        self.leave_first_room_tries = 1
        self.first_room_choices()
   
    def examine_painting(self):
        self.slow_print("\nYou step closer to the painting, its image slowly coming into focus.")
        self.slow_print("As you gaze upon it, you notice a faint glimmer coming from behind the frame.")
        self.slow_print("Upon closer inspection, you discover a hidden compartment cleverly concealed within the frame.")
        self.slow_print("It seems there is more to this artwork than meets the eye.")
        self.examine_painting_choices()
        
    def examine_painting_choices(self):
        print("\nWhat would you like to do?")
        print("[1] Examine the compartment")
        print("[2] Try to break it open")
        choice = input("⊳ ")
        if choice == "1":
            self.examine_compartment()
        if choice == "2":
            self.try_breaking_compartment()
        else:
            print("\nInvalid choice. Please try again.")
            self.examine_painting()
    
    def try_breaking_compartment(self):
        self.force_compartment_attempts += 1
        if self.force_compartment_attempts >= 3:
            self.break_painting()
        else:
            self.slow_print("\nYou attempt to force open the compartment, but the magical seal holds strong.")
            self.examine_painting_choices()
    
    def break_painting(self):
        self.slow_print("\nAs you make another forceful attempt, the magical seal resists momentarily before shattering.")   
        self.slow_print("To your horror, the painting cracks and splinters, revealing a ruined interior.")
        self.slow_print("The secret compartment is forever lost, and you are left with the remnants of the broken painting.")
        print("\n[1] Rewind to examining the painting")
        print("[2] Restart")
        choice = input("⊳ ")
        if choice == "1":
            self.examine_painting_choices()
            self.force_compartment_attempts = 0
        elif choice == "2":
            self.begin()
        else:
            print("\nInvalid choice. Please try again.")
            self.break_painting()
    
    # ============================================================= FIRST AND SECOND CHALLENGE (IMAGE ZIP) ============================================================================== #    
    
    def examine_compartment(self):
        self.slow_print("\nWith anticipation, you reach out to open the compartment, but to your surprise, it is protected by a powerful magical seal.")
        self.slow_print("An intricate pattern of arcane symbols dances across its surface, warning of the consequences of unauthorized entry.")
        self.first_challenge()
    
    def first_challenge(self):
        print("\nCHECKPOINT 'painting' reached!")
        self.slow_print("\nFIRST CHALLENGE: Find a way to open the compartment.")
        self.slow_print("A mysterious voice speaks to you: 'Follow the link and download the file to examine it'")
        shutil.copyfile(PICTUREPATH, OUTPUT + f'{IMAGENAME}.jpg')
        self.print_link(f'http://{HOST}/{IMAGENAME}.jpg')
        print("\nWhich incantation do you use to open the hidden compartment?")
        choice = input("⊳ ")
        if choice == "unzip":   # ========================================================== CHANGE SOLUTION =========================================================================== #
            self.open_compartment()
        else:
            print("Wrong incantation. Please Try again")
            self.first_challenge()
        
    def open_compartment(self):
        self.slow_print("\nThe ancient magical seal protecting the hidden compartment shatters as you successfully unlock its secrets.")
        self.slow_print("With a satisfying click, the compartment opens, revealing a small rolled-up parchment inside.")
        self.slow_print("Gingerly, you unfurl the parchment, and before your eyes unfolds a breathtaking image.")
        self.slow_print("As you study the image, your mind races with possibilities. What secrets does this image hold?")
        self.slow_print("Might it hold the secret phrase to get you out of this tomb?")
        self.second_challenge()
        
    def second_challenge(self):
        print("\nCHECKPOINT 'image' reached!")
        self.slow_print("\nSECOND CHALLENGE: Find a secret phrase hidden in the image.")
        print("\nWhat is the phrase?")
        choice = input("⊳ ")
        if choice == "th4t_w4s_e4sy": # ========================================================== CHANGE SOLUTION ================================================================================ #
            self.first_room_solved()
        else:
            print("Wrong Phrase. Please Try again")
            self.second_challenge()
    
    # ======================================================================= STORY ====================================================================================================== #
    
    def first_room_solved(self):
        self.slow_print("\nAs the magical seal yields to your efforts, the door creaks open, revealing a hidden passage that leads deeper into the depths of the dungeon.")
        self.slow_print("With each step you take, the air grows colder, and the sound of your own footsteps echoes through the winding corridors.")
        self.slow_print("Torch in hand, you press forward, navigating the labyrinthine tunnels and treacherous chambers until you find yourself before a door.")
        self.slow_print("\nYou enter the library feeling a soft, ethereal glow illuminating the space.")
        self.slow_print("The air feels charged with mystical energy, and a sense of anticipation fills the atmosphere.")
        self.slow_print("In the center of the room, resting upon an intricately carved pedestal, you behold a magnificent crystal ball.")
        self.library_choices()
        
    def library_choices(self):
        print("\nWhat would you like to do?")
        print("[1] Examine the crystal ball")
        if not self.found_python_script:
            print("[2] Examine the room")
        if not self.examined_bookshelfs:
            print("[3] Examine the bookshelfs")
        choice = input("⊳ ")
        if choice == "1":
            self.examine_crystal_ball()
        if not self.found_python_script and choice == "2":
            self.examine_library()
        if not self.examined_bookshelfs and choice == "3":
            self.examine_bookshelfs()
        else:
            print("\nInvalid choice. Please try again.")
            self.library_choices()        
        
    def examine_bookshelfs(self):
        self.examined_bookshelfs = True
        self.slow_print("\nAs you approach the bookshelves, you notice that the books are written in a language unknown to you.")
        self.slow_print("Strange symbols and intricate glyphs adorn their covers, leaving you perplexed and unable to decipher their contents.")
        self.slow_print("It seems these books hold knowledge beyond your current understanding, locked away in a language known only to the mage.")
        self.slow_print("Curiously, you spot the numbers 1346 and 673 carved into the wood of one of the bookshelves. Maybe they help solving the riddle.")
        self.library_choices()
    
    def examine_library(self):
        self.found_python_script = True
        self.slow_print("\nAs you meticulously search through the labyrinthine library, your fingers brush against dusty tomes and ancient manuscripts.")
        self.slow_print("After what feels like an eternity, your gaze falls upon a half-destroyed tome tucked away in a neglected corner.")
        self.slow_print("The book appears weathered and worn, its pages yellowed with age.")
        self.slow_print("You carefully retrieve the tome from its resting place, feeling a sense of anticipation as you examine its contents.")
        self.slow_print("Inside, you find a script, the ink faded and some of the pages torn.")
        self.slow_print("It seems to be a fragment of a larger work, with sections missing and sentences abruptly cut off.")
        shutil.copyfile(VIDSCRIPTPATH, OUTPUT + 'video_script.py')
        self.print_link(f'http://{HOST}/video_script.py')
        self.library_choices()
    
    # =================================================================== THIRD CHALLENGE (VIDEO) =========================================================================================== #
    
    def examine_crystal_ball(self):
        if self.examined_crystal_ball: 
            self.slow_print("\nAs you return to the radiant crystal ball, its vibrant glow captivates your attention once more.")
            self.slow_print("The dancing light within beckons you, as if urging you to delve deeper into its mystical depths.")
        else: 
            self.slow_print("\nAs you examine the crystal ball, you notice a faint pulsating glow emanating from within.")
            self.slow_print("Intrigued, you focus your attention on the crystal's surface, and to your surprise, the glow intensifies, revealing moving images within its depths.")
        if self.found_python_script and self.examined_bookshelfs:
            self.slow_print("As you cautiously approach the crystal ball, the glow emanating from within intensifies, growing brighter and more vibrant.")
            self.slow_print("The ethereal light pulses and dances, responding to your presence and the tome you hold in your hand.")
            self.third_challenge()
        else:
            self.slow_print("As you peer into the depths of the crystal ball, the moving images within present a bewildering display.")
            self.slow_print("The scenes shift and twist, each one more perplexing than the last.")
            self.slow_print("Colors meld together in a kaleidoscope of confusion, and the shapes and forms seem to defy logic.")
            self.slow_print("Maybe you find something in the library to decipher the moving images.")
            self.examined_crystal_ball = True
            self.library_choices()
    
    def third_challenge(self):
        print("\nCHECKPOINT 'library' reached!")
        self.slow_print("\nTHIRD CHALLENGE: Find a secret hidden in the video with the use of the script.")
        self.slow_print("The mysterious voice speaks to you again:")
        self.slow_print("Gaze upon the video and decipher its secret using the script.")
        shutil.copyfile(VIDEOPATH, OUTPUT + 'video.mov')
        self.print_link(f'http://{HOST}/video.mov')
        print("\nWhat is the solution?")
        choice = input("⊳ ")
        if choice == "candle": # =========================================================== CHANGE SOLUTION =============================================================================== #
            self.second_room_solved()
        else:
            print("Wrong Phrase. Please Try again")
            self.third_challenge()
    
    # ====================================================================== STORY SPLIT (AUDIO VS MUSIC) ================================================================================ #
    
    def second_room_solved(self):
        self.slow_print("\nAs you successfully decipher the secrets hidden within the crystal ball's radiant glow, a resounding energy fills the room.")
        self.slow_print("The air crackles with arcane power, and the ground trembles beneath your feet.")
        self.slow_print("Suddenly, the once-still crystal ball levitates in the air, its glow intensifying to an blinding brilliance.")
        self.slow_print("As you watch in awe, a portal begins to materialize before you.")
        self.portal_choice()
    
    def portal_choice(self):
        print("\nWhat do you do?")
        print("[1] Hold onto a shelf")
        print("[2] Step in the portal")
        print("[3] Cover behind pedestal")

        choice = self.timed_input('⊳ ', 8)
        print("\n") 
        if choice == "1":
            self.slow_print("\nAs the portal's powerful pull intensifies, threatening to consume you, your instincts kick in.")
            self.slow_print("Desperately, you lunge towards a nearby shelf, gripping it with all your might.")
            self.slow_print("With an unexpected surge of resistance, you summon all your strength and manage to hold firm against the relentless pull of the portal.")
            self.portal_closes_without_you()
        if choice == "2":
            self.slow_print("\nWith a surge of courage, you leap into the portal, ready to face the challenges ahead.")
            self.inside_portal()
        else:
            self.slow_print("\nIt draws you closer, its unseen force tugging at your very being.")
            self.slow_print("Before you can react, you are helplessly engulfed by its power, inexorably pulled into the unknown depths of the portal's realm.")
            self.inside_portal()

    # ======================================================================== STORY (OUTSIDE PORTAL) ===================================================================================== #

    def portal_closes_without_you(self):
        self.slow_print("\nThe portal shudders, its vibrant energy waning, until finally, with a resounding thud, it closes shut.")
        self.slow_print("The room returns to its eerie stillness, and you find yourself released from the grasp of the portal's magnetic pull.")
        self.slow_print("As the portal's mysterious energy dissipates, it leaves behind an enigmatic hole in the ground, beckoning you to explore its depths.")
        self.slow_print("Without hesitation, you steel yourself and descend into the depths, the dim light of the dungeon above fading behind you.")
        self.slow_print("Fueled by curiosity and the desire for adventure, you venture forth, prepared to face the challenges that await within the depths of the earth.")
        self.audio_path_chosen()
    
    def audio_path_chosen(self):
        self.slow_print("\nYou find yourself in a dark, labyrinthine passage.")
        self.slow_print("As you cautiously navigate the winding tunnels, your senses heighten, alert to any hidden dangers lurking in the shadows.")
        self.slow_print("Suddenly, you come upon a colossal stone door, adorned with intricate engravings and arcane symbols.")
        print("\nCHECKPOINT 'stonedoor' reached!")
        self.audio_path_stone_door_choice()

    def audio_path_stone_door_choice(self):
        print("\nWhat would you like to do?")
        print("[1] Try breaking the door down")
        if not self.found_stone_door_scroll:
            print("[2] Check the surroundings")
        print("[3] Examine the Engravings")

        choice = input("⊳ ")
        if choice == "1":
            self.try_breaking_stone_door()
        if not self.found_stone_door_scroll and choice == "2":
            self.examine_stone_door_surroundings()
        if choice == "3":
            self.examine_stone_door_engravings()
        else:
            print("\nInvalid choice. Please try again.")
            self.audio_path_stone_door_choice()

    def try_breaking_stone_door(self):
        self.slow_print("\nDriven by frustration and a sense of urgency, you muster all your strength and deliver mighty blows to the unyielding surface.")
        print("o")
        time.sleep(1)
        self.slow_print("Each strike reverberates through the air, sending echoes that seem to challenge the very depths of the dungeon.")
        print("o")
        time.sleep(1)
        print("o")
        time.sleep(1)
        self.slow_print("Yet, despite your valiant efforts, the door remains steadfast, unmoved by your physical assault.")
        self.slow_print("As you catch your breath, you come to realize that brute force alone will not grant you access to the secrets that lie beyond.")
        self.audio_path_stone_door_choice()

    def examine_stone_door_surroundings(self):
        if not self.searched_stone_door_surroundings:
            self.slow_print("\nPerplexed, you explore the surroundings and stumble upon an old, weathered scroll lying on the ground.")
        self.searched_stone_door_surroundings = True
        print("\nWhat would you like to do?")
        if not self.fourth_challenge_reached:
            print("[1] Ignore the scroll")
        print("[2] Examine the scroll")
        
        choice = input("⊳ ") 
        if not self.fourth_challenge_reached and choice == "1":
            self.slow_print("\nYou search the surrounding stonewalls for clues but there is nothing to find but cold granite.")
            self.audio_path_stone_door_choice()
        if choice == "2":
            self.slow_print("\nWith a sense of curiosity, you reach down and pick it up, unfurling the delicate parchment.")
            self.read_stone_door_scroll()
        else:
            print("\nInvalid choice. Please try again.")
            self.examine_stone_door_surroundings()

    def examine_stone_door_engravings(self):
        self.slow_print("\nYou lean in, studying the intricate engravings and arcane symbols etched upon its surface.")
        self.slow_print("Your fingers trace the lines, feeling the weathered texture beneath your touch.")
        self.slow_print("Suddenly, your eyes catch a glimpse of something peculiar — a small, concealed hole nestled within the intricate design.")
        print("\nWhat would you like to do?")
        print("[1] Examine further")
        print("[2] Reach inside")

        choice = input("⊳ ") 
        if choice == "1":
            self.slow_print("\nThe engravings are written in a language unfamiliar to your eyes—a cryptic script known only to the Mage, the enigmatic architect of this labyrinthine dungeon.")
            self.audio_path_stone_door_choice()
        if choice == "2":
            self.slow_print("\nIntrigued, you reach into your pack and retrieve a small object—a crystal resonator.")
            print("\nCHECKPOINT 'audio' reached!")
            self.fourth_challenge_audio()
        else:
            print("\nInvalid choice. Please try again.")
            self.examine_stone_door_engravings()

    def read_stone_door_scroll(self):
        self.found_stone_door_scroll = True
        self.slow_print("\nThe scroll reveals faded ink, its fragile surface hinting at the passage of time.")
        self.print_scroll()
        self.slow_print("The scroll might be of use")
        if self.fourth_challenge_reached:
            self.fourth_challenge_audio()
        else:
            self.audio_path_stone_door_choice()

    # ================================================================== FOURTH CHALLENGE (AUDIO) ======================================================================================== #

    def fourth_challenge_audio(self):
        self.fourth_challenge_reached = True
        if not self.found_stone_door_scroll:
            self.slow_print("Maybe theres a hint hidden in the surroundings. Want to check them?")
            print("[1] Check out surroundings")
            choice1 = input("⊳ ")
            if choice1 == "1":
                self.examine_stone_door_surroundings()
            else: 
                print("\nInvalid choice. Please try again.")
                self.fourth_challenge_audio()
        else:
            self.slow_print("\nFOURTH CHALLENGE: Find a secret phrase hidden in the audio file.")
            self.slow_print("The mysterious voice speaks to you once more:")
            self.slow_print("Listen to the sound and find the message engraved in it.")
            shutil.copyfile(SONGPATH, OUTPUT + 'song.mp3')
            self.print_link(f'http://{HOST}/song.mp3')
            print("\nWhat is the phrase?")
            choice2 = input("⊳ ")
            if choice2 == "h1dd3n 1n fr3qu3nc13s": # =========================================================== CHANGE SOLUTION =============================================================================== #
                self.stone_door_solved()
            else:
                print("Wrong Phrase. Please Try again")
                self.fourth_challenge_audio()

    def stone_door_solved(self):
        self.slow_print("\nAs the final notes of the audio riddle fade away, a profound silence settles in the chamber.")
        self.slow_print("The intricate melody and harmonies have revealed their secrets to you, guiding your mind through the labyrinth of sounds.")
        self.slow_print("With a surge of satisfaction, you witness the massive stone door groaning and creaking, its ancient mechanisms responding to the unraveling of the audio puzzle.")
        self.final_room_hallway()

    # ======================================================================= STORY (INSIDE PORTAL) ======================================================================================= #

    def inside_portal(self):
        print("\nCHECKPOINT 'fairies' reached!")
        self.slow_print("\nAs you are pulled deeper into the portal, you find yourself in an eerie room filled with lush greenery.")
        self.slow_print("The air is thick with a sweet fragrance, and soft melodies sung by fairies fill the space.")
        self.slow_print("The room seems enchanted, with magical lights flickering around you.")
        self.slow_print("In front of you stands a door, intricately carved with mystical symbols.")
        shutil.copyfile(FAIRYIAMGE, OUTPUT + 'fairy.jpg')
        self.print_link(f'http://{HOST}/fairy.jpg')
        self.fairy_room_choice()

    def fairy_room_choice(self):
        print("\nWhat would you like to do?")
        print("[1] Examine the door")
        print("[2] Interact with the fairies")
        if not self.found_fairy_pendant:
            print("[3] Search your surroundings")

        choice = input("⊳ ")
        if choice == "1":
            self.examine_fairy_door()
        if choice == "2":
            self.interact_with_fairies()
        if not self.found_fairy_pendant and choice == "3":
            self.search_fairy_room_surroundings()
        else:
            print("\nInvalid choice. Please try again.")
            self.fairy_room_choice()

    def search_fairy_room_surroundings(self):
        if not self.searched_fairy_room_surroundings:
            self.slow_print("\nAs you search the room for clues, your eyes catch a glimmer of light.")
            self.slow_print("You follow the source and discover a small, shimmering object tucked among the leaves of a nearby plant.")
            self.slow_print("Carefully, you retrieve it and realize it's a tiny pendant.")
        self.searched_fairy_room_surroundings = True
        print("\nWhat would you like to do?")
        print("[1] Examine the pendant")
        print("[2] Ignore the pendant")

        choice = input("⊳ ")
        if choice == "1":
            self.slow_print("\nWith a sense of curiosity, you reach down and pick it up, unfurling the delicate parchment.")
            self.examine_fairy_pendant()
        if choice == "2":
            self.slow_print("\nYou search the surrounding plants for clues but there is nothing more to find...")
            self.fairy_room_choice()
        else:
            print("\nInvalid choice. Please try again.")
            self.search_fairy_room_surroundings()
    
    def examine_fairy_pendant(self):
        self.found_fairy_pendant = True
        self.slow_print("\nExamining the backside of the pendant reveals small engravings indicating a cipher.")
        self.print_pendant()
        self.slow_print("This clue might be of use to solve the riddle")
        self.fairy_room_choice()

    def interact_with_fairies(self):
        self.slow_print("\nAs you cautiously approach the fairies, their melodies grow louder and more alluring.")
        self.slow_print("The ethereal beings flit and dance around you, their enchanting voices beckoning you to come closer.")
        self.slow_print("Their melody growing louder and louder, but you can't resist to get closer.")
        self.slow_print("You reach your hand out to touch one of them but the melody overwhelmes you and knocks you out.")
        print("o")
        time.sleep(1)
        print("o")
        time.sleep(1)
        print("o")
        time.sleep(1)
        print("o")
        time.sleep(1)
        print("o")
        time.sleep(1)
        print("o")
        time.sleep(1)
        self.slow_print("You slowly get back on your feet you still find yourself trapped inside their realm.")
        self.fairy_room_choice()

    def examine_fairy_door(self):
        self.slow_print("\nIt appears to be locked shut, blocking your path to the next stage of your journey.")
        if self.found_fairy_pendant:
            print("\nCHECKPOINT 'midi' reached!")
            self.fourth_challenge_midi()
        else:
            self.fairy_room_choice()

    # ================================================================== FIFTH CHALLENGE (MUSIC) ========================================================================================== #

    def fourth_challenge_midi(self):
        self.slow_print("\nFOURTH CHALLENGE: Find a secret phrase hidden in the midi file.")
        self.slow_print("The mysterious voice speaks to you once more:")
        self.slow_print("The melody is cryptic. Maybe the pendants code helps deciphering it.")
        shutil.copyfile(MIDIPATH, OUTPUT + 'midi.mid')
        self.print_link(f'http://{HOST}/midi.mid')
        print("\nWhat is the phrase?")
        choice = input("⊳ ")
        if choice == "fairies sing awfully": # =========================================================== CHANGE SOLUTION =============================================================================== #
            self.slow_print("\nAs the fairies' song reaches a crescendo, the final letter falls into place, and the hidden message is revealed.")
            self.fairy_room_solved()
        else:
            print("\nWrong Phrase. Please Try again")
            self.fourth_challenge_midi()
    
    def fairy_room_solved(self):
        self.slow_print("\nArmed with the knowledge gained from deciphering the melody, you approach the locked door with confidence.")
        self.slow_print("You insert the key, formed by the fairies' enchanting song, into the lock.")
        self.slow_print("With a soft click, the door unlocks, revealing the path that lies ahead.")
        self.final_room_hallway()

    # ========================================================================== STORY (FINAL ROOM) ========================================================================================= #

    def final_room_hallway(self):
        self.slow_print("\nThe air grows heavier with anticipation as you step into the corridor, your every footfall echoing softly against the stone walls.")
        self.slow_print("The flickering torches cast dancing shadows, playing tricks on your senses and heightening the suspense that hangs in the air.")
        self.slow_print("With each step, the anticipation builds, as you know that the end of your quest lies just beyond the threshold of the final room.")
        self.slow_print("Finally, at the end of the hallway, the passage opens up into a vast chamber—a sacred space where the culmination of your journey unfolds.")
        self.enter_final_chamber()
    
    def enter_final_chamber(self):
        self.slow_print("\nThe door opens slowly, revealing the long-awaited glimpse of the final room of the dungeon.")
        self.slow_print("A soft, ethereal light spills into the chamber, illuminating the scene before you.")
        print("\nWhat would you like to do?")
        print("[1] Quit and return to the surface, never knowing the secret which hides in this chamber.")
        print("[2] Enter the room to reveal the Mage's evil secret")

        choice = input("⊳ ")
        if choice == "1":
            self.slow_print("\nYou retrace your steps through the winding halls filled with shame.")
            self.the_end()
        if choice == "2":
            self.slow_print("\nYou step forward, crossing the threshold into the heart of the dungeon, eager to uncover the Mage's ultimate secrets.")
            print("\nCHECKPOINT 'finalroom' reached!")
            self.enter_the_room()
    
    def enter_the_room(self):
        self.slow_print("\nThe room is vast and eerily silent, bathed in an unnatural darkness that your torches barely penetrate.")
        self.slow_print("The air is thick with the stench of decay and the oppressive weight of ancient secrets.")
        self.slow_print("As your eyes adjust to the darkness, you notice that the walls of the chamber are composed of massive stone blocks, each covered in a complex web of writings and symbols.")
        self.slow_print("In the center of the room, an altar made of black obsidian stands ominously.")
        self.final_room_choice()
    
    def final_room_choice(self):
        print("\nWhat would you like to do?")
        if not self.final_room_examined:
            print("[1] Examine the room")
        print("[2] Examine the altar")
        if not self.read_final_script:
            print("[3] Read through the tome from the library")
        
        choice = input("⊳ ")
        if not self.final_room_examined and choice == "1":
            self.examine_the_room()
        if choice == "2":
            self.examine_the_stoneboard()
        if not self.read_final_script and choice == "3":
            self.read_through_the_tome_from_library()
        else:
            print("\nInvalid choice. Please try again.")
            self.final_room_choice()
    
    def examine_the_room(self):
        self.final_room_examined = True
        self.slow_print("\nThe room is shrouded in darkness, with cobwebs hanging from its corners, a testament to the centuries that have passed since its last inhabitant.")
        self.slow_print("In the vast chamber, there is nothing but the obsidian altar, standing in the center, hinting at its significance.")
        self.slow_print("The silence is almost palpable, making it clear that this forsaken space holds a powerful secret, awaiting discovery by those daring enough to venture within.")
        self.final_room_choice()
    
    def examine_the_stoneboard(self):
        self.slow_print("\nAs you come closer to the altar to notice it being filled with text.")
        self.slow_print("The lines are etched deep into the stone, glowing faintly with an eerie, eldritch light.")
        self.slow_print("As you examine the obsidian altar more closely, you notice a beautifully crafted shield mounted above the puzzling text.")
        self.print_altar()
        self.stone_board_choice()
        
    def stone_board_choice(self):
        self.saw_stone_board = True
        print("\nWhat would you like to do?")
        print("[1] Examine the text")
        if not self.read_final_script:
            print("[2] Read through the tome from the library")
        
        choice = input("⊳ ")
        if choice == "1":
            self.examine_the_text()
        if not self.read_final_script and choice == "2":
            self.read_through_the_tome_from_library()
        else:
            print("\nInvalid choice. Please try again.")
            self.stone_board_choice()
            
    def read_through_the_tome_from_library(self):
        self.read_final_script = True
        self.slow_print("\nYour eyes are drawn to a section of the tome that appears to be more worn than the rest, as if it has been frequently referenced.")
        self.slow_print("The pages detail a powerful incantation which might be the key to reveal the secrets.")
        shutil.copyfile(WHITESCRIPTPATH, OUTPUT + 'text_script.py')
        self.print_link(f'http://{HOST}/text_script.py')
        if self.saw_stone_board:
            self.fifth_challenge()
        else:
            self.final_room_choice()
           
    def examine_the_text(self):
        self.slow_print("\nAs you begin to read the text, you take note of the hint provided by the shield, keeping in mind the importance of the spaces between the lines.")
        if self.read_final_script:
            self.fifth_challenge()
        else:
            self.slow_print("Realizing that you haven't yet discovered the full magical formula, your grab the tome from the library to hopefully find a scripture.")
            self.stone_board_choice()

    # ================================================================== SIXTH CHALLENGE (TEXT) ============================================================================================ #

    def fifth_challenge(self):
        print("\nCHECKPOINT 'text' reached!")
        self.slow_print("\nFIFTH CHALLENGE: Find a secret hidden in the text file.")
        self.slow_print("The mysterious voice speaks to you one last time:")
        self.slow_print("Read the text with the hint in mind.")
        shutil.copyfile(TEXTPATH, OUTPUT + 'text.txt')
        self.print_link(f'http://{HOST}/text.txt')
        print("\nFound the secret?")
        print("[1] Yes")
        print("[2] No, I need a hint")
        choice = input("⊳ ")
        if choice == "1":
            self.end_scene()
        if choice == "2":
            self.fifth_challenge_hint()
        else:
            print("\nInvalid choice. Please try again.")
            self.fifth_challenge()
    
    def fifth_challenge_hint(self):
        self.slow_print("\nThe mysterious voice speaks to you:")
        print("\nWhat do you like to do?")
        print("[1] Take another look at the rhyme")
        print("[2] I need a hint")
        print("[3] Back to the challenge")
        choice = input("⊳ ")
        if choice == "1":
            self.print_altar()
            self.fifth_challenge()
        if choice == "2":
            self.slow_print("\nThe mysterious voice whispers to you: Look at the whitespaces in the text.")
            self.slow_print("The first one is interpreted as as 0.")
            self.fifth_challenge()
        if choice == "3":
            self.fifth_challenge()
        else:
            print("\nInvalid choice. Please try again.")
            self.fifth_challenge_hint()
    
    # =============================================================================== STORY =============================================================================================== #

    def end_scene(self):
        self.clear_screen()
        self.slow_print("\nWith the secrets of the Mage's dungeon unraveled and the artifact in your possession, you feel a sense of triumph and accomplishment.")
        self.slow_print("The weight of the ancient knowledge and the power you have acquired is both exhilarating and humbling.")
        self.slow_print("As you stand in the final chamber, basking in the glow of your success, you know that it is time to leave the depths of this treacherous dungeon and return to the world beyond.")
        self.the_end()

    def the_end(self):
        self.print_end()
        print("Enter x to leave.")
        choice = input("⊳ ")
        if choice == "x":
            self.quit_game()
        else:
            self.the_end()

    def play(self):
        self.start()

    def quit_game(self):
        self.clear_screen()
        self.print_ascii_art()
        print("\nThank you for playing! Farewell, adventurer.")
        sys.exit()

if __name__ == '__main__':
    game = TextAdventure()
    game.play()


