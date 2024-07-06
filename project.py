import time
import random
score = 0
Tommy_weapon = ['sword','broom', 'knife']
weapon = random.choice(Tommy_weapon)
def adventure_story():
 score = 0
 Tommy_weapon =['sword','broom', 'knife']
 weapon = random.choice(Tommy_weapon)
 print("Tommy was an adventurous boy who loved exploring the woods near his homeOne sunny afternoon, he ventured deeper into the forest than ever before. The trees grew thicker, and soon he realized he had lost his way.As the daylight began to fade, Tommy stumbled upon an old, abandoned cabin. He had two choices:Enter the Cabin: Tommy could go inside the cabin and search for help or supplies.Continue Walking: Tommy could keep walking in the hope of finding his way back home before it got too dark.")
 time.sleep(2)
 print("what should Tommy do")
 time.sleep(2)
 print("1. enter the cabin")
 print("2. continue walking")
 choice = input("Enter choice(1/2):")
 if choice in("1"):
       score += 10
       time.sleep(2)
       print("Tommy pushed open the creaky door of the cabin and stepped inside. The air was musty, and the furniture was covered in dust. As he searched the room, he found a map on a table. The map showed a path leading out of the woods. Relieved, Tommy pocketed the map and turned to leave, but a rustling noise stopped him in his tracks.A wild animal, a raccoon, leaped at Tommy, baring its teeth. Tommy had two choices for how to defend himself:1.Use the Broom: Tommy could grab the nearby broom and use it to fight off the raccoon. 2.Throw a Blanket: Tommy could grab an old blanket from the couch and use it to shield himself from the raccoon.")
       choice = input("Enter choice(1/2):")
       if choice in("1"):
         score += 10
         time.sleep(2)
         print(f"Tommy quickly grabbed a {weapon} and swung it with all his might. After a few tense moments of fending off the raccoon, he managed to scare it away. His heart pounding, Tommy left the cabin, following the map's directions. Soon, he found his way back home, safe and sound.")

       elif choice in ("2"):
         score += 5
         print("Tommy grabbed an old blanket and threw it over the raccoon. The raccoon struggled under the blanket, but it quickly freed itself and bit Tommy. Scared and injured, Tommy ran out of the cabin without the map, and wandered aimlessly in the dark until his parents found him the next day.")  

 elif choice in("2"):
     score += 5
     time.sleep(2)
     print("Tommy decided to keep walking, relying on his instincts to guide him. As the night grew darker, he heard the howls of distant wolves. Fear gripped him, but he pressed on. Suddenly, he heard a growl close by and saw a pair of glowing eyes in the darkness. A wild dog lunged at him. Tommy had two choices for how to defend himself:1.Use a Sturdy Stick: Tommy could grab a sturdy stick from the ground and use it to fight off the wild dog.2.Climb a Tree: Tommy could try to climb a nearby tree to escape the wild dog.")

     choice = input("Enter choice(1/2):")
     if choice in("1"):
       score += 10
       time.sleep(2)
       print("Tommy quickly grabbed a sturdy stick from the ground and faced the wild dog. With courage and determination, he fought off the dog, finally managing to drive it away. Exhausted but triumphant, Tommy saw the flickering light of a lantern in the distance. It was his father, who had come searching for him. They hugged tightly, and Tommy vowed never to wander off so far again.")
       time.sleep(2)
     elif choice in("2") :
       score += 5
       print("Tommy ran to a nearby tree and started climbing as fast as he could. The wild dog jumped and barked at the base of the tree but couldn't reach him. Tommy waited until the dog lost interest and wandered away. However, he lost his balance while climbing down and fell, injuring his leg. He was found the next morning by his worried parents.")
       time.sleep(2)
 print(f"\nYour total score is: {score}")

 if score >= 20:
   print("Congratulations! You helped Tommy navigate the woods successfully.")
 else:
   print("Unfortunately, Tommy didn't make it back home safely. Better luck next time!")
while True:
    adventure_story()
    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        break