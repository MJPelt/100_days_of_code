print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

step_1 = input("You start your adventure at a river. Do you 'look' around or do you 'swim' across?")
if step_1 == "look":
    step_2 = input("You look around and see a boat. Do you want to take the 'boat' across the water or you choose to 'walk' along shore?")
    if step_2 == "boat":
        step_3 = input("You paddle across the river and make it to the other side safely. On the other side of the river you see lights and smoke coming from a town in the distance, do you want to walk toward the 'town' or do you choose to enter the 'woods' and explore?")
        if step_3 == "town":
            step_4 = input("In the town you see 3 buildings. One made of 'straw', one made of 'sticks', and the third made of 'brick'. Which house do you enter?")
            if step_4 == "brick":
                step_5 = input("You enter the brick house. A big bad wolf comes by and huffs and puffs but is unable to blow the house down. You are safe. There is a trap door in the floor do you wish to 'open' the door or 'wait'?")
                if step_5 == "open":
                    print('''
                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.|uuu|.-'    __/ \__ |
              |==== .'.'^'.'.====|
          jgs |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
                    You open the trap door and find a pile of treasure. You are happy. You have treasure. You have succeeded.''')
                elif step_5 == "wait":
                    print('''
                         .-""-._
                        / ___/  \         _&_
                  _.--""|/    `\|        // \\
                .'      ( ^/ ^  )'.     / / \ \
               /         | _   |   \   // / \ \\
               |        _\____/    |  /_/_/_\_\_\
               |      .' \____/-._ |     .-"-.
               |     /            `;    /#    \
               |    /  /     _|_.---\   |     |
               |.-.;   :--.-(_/.____/.-""\___/"-.
               /    \ / ~~/   /\   \{"=.______.="}
              /--. ; /___/_~~/ ; .--\"=...__...="}
             /    \-/  `\______|/    \-.______..-;
             |    /`|   |       \    |   ||||   ||
             |   /_ |   |_______/    |   ||||   ||
             |   \_/|   |-------'    |--'||'--._||
             |      |   |            |   ||     |>
             |______|   |____________|._ || _..-;|
             |      [___]            |  `||()   ||
             |______ |\/|____________|jgs||     ()
              (__)   \__/        (__)    ()
              You wait and wait and wait. You live a long life but eventually die without the treasure.''')
            elif step_4 == "straw":
                print('''
                
                               __
                             .d$$b
                           .' TO$;\
                          /  : TP._;
                         / _.;  :Tb|
                        /   /   ;j$j
                    _.-"       d$$$$
                  .' ..       d$$$$;
                 /  /P'      d$$$$P. |\
                /   "      .d$$$P' |\^"l
              .'           `T$P^"""""  :
          ._.'      _.'                ;
       `-.-".-'-' ._.       _.-"    .-"
     `.-" _____  ._              .-"
    -(.g$$$$$$$b.              .'
      ""^^T$$$P^)            .(:
        _/  -"  /.'         /:/;
     ._.'-'`-'  ")/         /;/;
  `-.-"..--""   " /         /  ;
 .-" ..--""        -'          :
 ..--""--.-"         (\      .-(\
   ..--""              `-\(\/;`
     _.                      :
                             ;`-
                            :\
                            ;  
                            You enter the straw house. A big bad wolf comes by and huffs and puffs and blows the house down. He then eats you. Game Over.''')
            elif step_4 == "sticks":
                print('''
                                __
                             .d$$b
                           .' TO$;\
                          /  : TP._;
                         / _.;  :Tb|
                        /   /   ;j$j
                    _.-"       d$$$$
                  .' ..       d$$$$;
                 /  /P'      d$$$$P. |\
                /   "      .d$$$P' |\^"l
              .'           `T$P^"""""  :
          ._.'      _.'                ;
       `-.-".-'-' ._.       _.-"    .-"
     `.-" _____  ._              .-"
    -(.g$$$$$$$b.              .'
      ""^^T$$$P^)            .(:
        _/  -"  /.'         /:/;
     ._.'-'`-'  ")/         /;/;
  `-.-"..--""   " /         /  ;
 .-" ..--""        -'          :
 ..--""--.-"         (\      .-(\
   ..--""              `-\(\/;`
     _.                      :
                             ;`-
                            :\
                            ;  
                            You enter the sticks house. A big bad wolf comes by and huffs and puffs and blows the house down. He then eats you. Game Over.''')
        elif step_3 == "woods":
            print('''
           ____                      ,
          /---.'.__             ____//
               '--.\           /.---'
          _______  \\         //
        /.------.\  \|      .'/  ______
       //  ___  \ \ ||/|\  //  _/_----.\__
      |/  /.-.\  \ \:|< >|// _/.'..\   '--'
         //   \'. | \'.|.'/ /_/ /  \\
        //     \ \_\/" ' ~\-'.-'    \\
       //       '-._| :H: |'-.__     \\
      //           (/'==='\)'-._\     ||
      ||                        \\    \|
      ||                         \\    '
      |/                          \\
                                   ||
                                   ||
                                   \\
                                    '
            as you are exploring the woods you stumble into a large spider web. You are stuck. A giant spider is coming. There is nothing you can do. You wait and watch as the spider comes closer. You are doomed. Game Over.''')
    elif step_2 == "walk":
        print('''
                     _.---._     .---.
            __...---' .---. `---'-.   `.
        .-''__.--' _.'( | )`.  `.  `._ :
      .'__-'_ .--'' ._`---'_.-.  `.   `-`.
             ~ -._ -._``---. -.    `-._   `.
                  ~ -.._ _ _ _ ..-_ `.  `-._``--.._
                               -~ -._  `-.  -. `-._``--.._.--''.
                                    ~ ~-.__     -._  `-.__   `. `.
                                          ~~ ~---...__ _    ._ .` `.
                                                      ~  ~--.....--~`
        As you walk along the shore, a crocodile emerges from the water and eats you. Game over.''')

elif step_1 == "swim":
    print('''
     .-''-''-.    
 ('    '  '0)-/)
 '..____..:    \._
   u  u (        '-..------._
   |     /      :   '.        '--.
  .nn_nn/ (      :   '            '|
 ( '' '' /      ;     .             |
  ''----' "\          :            : '.
         .'/                           '.
        / /                             '.
       /_|       )                     .\|
         |      /\                     . '
         '--.__|  '--._  ,            /
                      /'-,          .'
                     /   |        _.' 
                    (____\       /    
                          \      \    
                           '-'-'-'    
     
    As you swim a hippo appears and eats you. Game over''')
