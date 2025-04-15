import random
import time
import os
import requests

# Pokémon List (Full List)
pokemon_list = ['abomasnow','abra','absol','accelgor','aegislash','aerodactyl','aggron','aipom',
                'alakazam','alcremie','alomomola','altaria','amaura','ambipom','amoonguss','ampharos',
                'annhilape','anorith','appletun','applin','araquanid','arbok','arboliva','arcanine',
                'arceus','archaludon','archen','archeops','arctibax','arctovish','arctozolt','ariados',
                'armaldo','armarouge','aromatisse','aron','arrokuda','articuno','audino','aurorus','avalugg',
                'axew','azelf','azumarill','azurill','bagon','baltoy','banette','barbaracle','barboach',
                'barraskewda','basculegion','basculin','bastiodon','baxcalibur','bayleef','beartic',
                'beautifly','beedril','beheeyem','beldum','bellibolt','bellossom','bellsprout','bergmite',
                'bewear','bibarel','bidoof','binacle','bisharp','blacephalon','blastoise','blaziken',
                'blipbug','blissey','blitzle','boldore','boltund','bombirdier','bonsly','bouffalant',
                'bounsweet','braixen','brambleghast','bramblin','braviary','breloom','brionne','bronzong',
                'bronzor','brute-bonnet','bruxish','budew','buizel','bulbasaur','buneary','bunnelby',
                'burmy','butterfree','buzzwole','cacnea','cacturne','calyrex','camerupt','capsakid',
                'carbink','carkol','carnivine','carracosta','carvanha','cascoon','caterpie','celebi',
                'celesteela','centiskorch','ceruledge','cetitan','cetoddle','chandelure','chansey',
                'charcadet','charizard','charjabug','charmannder','charmeleon','chatot','cherrim',
                'cherubi','chesnaught','chespin','chewtle','chi-yu','chien-pao','chikorita','chimchar',
                'chimecho','chinchou','chingling','cinccino','cinderace','clamperl','clauncher',
                'clawtizer','claydol','cleffable','clefairy','cleffa','clobbopus','clodsire','cloyster',
                'coalossal','cobalion','cofagrigus','combee','combusken','comfey','conkeldurr',
                'copperajah','corphish','corsola','corviknight','corvisquire','cosmoem','cosmog',
                'cottonee','crabominable','cradily','cramorant','cranidos','crawdaunt','cressela',
                'croagunk','crobat','crocalor','croconaw','crustle','cryogonal','cubchoo','cubone',
                'cufant','cursola','cutiefly','cyclizar','cyndaquil','dachsbun','darkrai','darmanitan',
                'dartrix','darumaka','decidueye','dedenne','deerling','deino','delcatty','delibird',
                'delphox','deoxys','dewgong','dewott','dewpider','dhelmise','dialga','diancie',
                'diggersby','diglett','dipplin','ditto','dodrio','doduo','dolliv','dondozo','donphan',
                'dottler','doublade','dracovish','dracozolt','dragalge','dragapult','dragonair','dragonite',
                'drakloak','drampa','drapion','dratini','drednaw','dreepy','drifblim','drifloon','drilbur',
                'drizzile','drowzee','druddigon','dubwool','ducklett','dudunsparce','dugtrio','dunsparce',
                'duosion','duralodon','durant','dusclops','dusknoir','duskull','dustox','dwebble','eelektrik',
                'eelektross','eevee','eiscue','ekans','eldegross','electabuzz','electrike','electrode',
                'elekid','elgyem','emboar','emolga','empoleon','enamorus-incarnate','entei','escavalier','espathra',
                'espurr','eternatus','excadrill','exeggcute','exeggutor','exploud','falinks',"farfetchd",
                'farigiraf','fearow','feebas','fennekin','feraligatr','ferroseed','ferrothorn','fezandipiti',
                'fidough','finizen','finneon','flaffy','flabebe','flamigo','flapple','flareon','fletchinder',
                'fletchling','flittle','floatzel','floatte','florogato','florges','flutter-mane','flygon',
                'fomantis','foongus','forretress','fraxure','fligibax','frillish','froakie','frogadier',
                'froslass','frosmoth','fuecoco','furfrou','furret','gabite','gallade','galvantula','garbodor',
                'garchomp','gardevoir','garganacl','gastly','gastrodon','genesect','gengar','geodude','gholdengo',
                'gible','gigalith','gimmighoul','girafarig','giratina','glaceon','glalie','glameow','glastrier',
                'gligar','glimmet','glimmora','gliscor','gogoat','golbat','goldeen','golduck','golem','golett',
                'golisopod','golurk','goodra','goomy','gorebryss','gossilfleur','gothita','gothitelle',
                'gothorita','gouging-fire','gourgeist','grafaiai','granbull','grapploct','graveler',
                'great-tusk','greavard','greedent','greninja','grimer','grimmsnarl','grookey','grotle',
                'groudon','grovyle','growlithe','grubbin','grumpig','gulpin','gumshoos','gurdurr','guzzlord',
                'gyarados','hakamo-o','happiny','hariyama','hatenna','hatterene','hattrem','haunter','hawlucha',
                'haxorus','heatmor','heatran','heliolisk','helioptile','heracross','herdier','hippopatas',
                'hippowdon','hitmonchan','hitmonlee','hitmontop','ho-oh','honchkrow','honedge','hoopa', 'hoothoot',
                'hoppip','horsea','houndoom','houndour','houndstone','huntail','hydrapple','hydreigon','hypno',
                'igglybuff','illumise','impidimp','incineroar','indeedee','infernape','inkay','inteleon',
                'iron-boulder', 'iron-bundle','iron-crown','iron-hands','iron-jugulis','iron-leaves','iron-moth',
                'iron-thorns','iron-treads','iron-valiant','ivysaur','jangmo-o','jellicent','jigglypuff','jirachi',
                'jolteon','joltik','jumpluff','jynx','kabuto','kabutops','kadabra','kakuna','kangaskhan',
                'karrablast','kartana','kecleon','keldeo','kilowattrel','kingambit','kingdra','kingler','kirlia',
                'klang','klawf','kleavor','klefki','klink','klinklang','koffing','komala','kommo-o','koraidon',
                'krabby','kricketot','kricketune','krokorok','krookodile','kubfu','kyogre','kyurem','lairon',
                'lampent','landorus','lanturn','lapras','larvesta','larvitar','latias','latios','leafeon',
                'leavanny','lechonk','ledian','ledyba','lickilicky','lickitung','liepard','lileep','lilligant',
                'lillipup','linoone','litleo','litten','litwick','lokix','lombre','lopunny','lotad','loudred',
                'lucario','ludicolo','lugia','lumineon','lunala','lunatone','lurantis','luvdisc','luxio',
                'luxray','lycanroc','mabosstiff','machamp','machoke','machop','magby','magcargo','magearna',
                'magikarp','magmar','magmortar','magnemite','magneton','magnezone','makuhita','malamar',
                'mamoswine','manaphy','mandibuzz','manectric','mankey','mantine','mantyke','maractus',
                'mareanie','mareep','marill','marowak','marshadow','marshtomp','maschiff','masquerain',
                'maushold','mawile','medicham','meditite','meganium','melmetal','meloetta','meltan',
                'meowscarada','meowstic','meowth','mesprit','metagross','metang','metapod','mew','mewtwo',
                'mienfoo','mienshoo','mightyena','milcery','milotik','miltank','mime-jr','mimikyu','minccino',
                'minior','minum','miraidon','misdreavus','mismagius','moltres','monferno','morelull',
                'morgrem','morpeko','mothim','mr-mime','mr-rime','mudbray','mudkip','mudsdale','muk',
                'Munchlax','munkidori','munna','murkrow','musharna','nacli','naclstack','naganadel','natu',
                'necrozma','nickit','nidoking','nidoqueen','nidoran','nidorina','nidorino','nihilego',
                'nincada','ninetails','ninjask','noctowl','noibat','noivern','nosepass','numel','nuzleaf',
                'nymble','obstagoon','octillery','oddish','ogerpon','oinkologne','okidogi','omanyte','omastar',
                'onix','oranguru','orbeetle','oricorio','orthworm','oshawott','overqwil','pachirisu','palafin',
                'palkia','palossand','palpitoad','pancham','pangoro','panpour','pansage','pansear','paras',
                'parasect','passimian','patrat','pawmi','pawmo','pawmot','pawniard','pecharunt','pelipper',
                'perrserker','persian','petilil','phanpy','phantump','pheromosa','phione','pichu','pidgeot',
                'pidgeotto','pidgey','pidove','pignite','pikachu','pikipek','piloswine','pincurchin','pineco',
                'pinsir','piplup','plusle','poipole','politoed','poliwag','poliwhirl','poliwrath','poltchageist',
                'polteageist','ponyta','poochyena','popplio','porygon-z','porygon2','primarina','primeape',
                'prinplup','probopass','psyduck','pumpkaboo','pupitar','purrloin','purugly','pyroar','pyukumuku',
                'quagsire','quaquaval','quaxly','quaxwell','quilava','quilladin','qwilfish','raboot','rabsca',
                'raging-bolt','raichu','raikou','ralts','ramparados','rapidash','raticate','rattata','rayquaza',
                'regice','regidrago','regieleki','regigigas','regirock','registeel','relicanth','rellor','remoraid',
                'reshiram','reuniclus','revavroom','rhydon','rhyhorn','rhyperior','ribombee','rillaboom','riolu',
                'roaring-moon','rockruff','roggenrola','rolycoly','rookidee','roselia','roserade','rotom','rowlet',
                'rufflet','runerigus','sableye','salamence','salandit','salazzle','samurott','sandaconda','sandile',
                'sandshrew','sandlslash','sandy shocks','sandygast','sawk','sawsbuck','scatterbug','sceptile','scizor',
                'scolipede','scorbunny','scovillain','scrafty','scraggy','scream-tail','seadra','seaking','sealeo',
                'seedot','seel','seismitoad','sentret','serperior','servine','seviper','sewaddle','sharpedo',
                'shaymin','shedinja','shelgon','shellder','shellos','shelmet','sheildon','shiftry','shiinotic','shinx',
                'shroodle','shroomish','shuckle','shuppet','sigilyph','silcoon','silicobra','silvally','simipour',
                'simisage','simisear','sinistcha','sinistea',"sirfetchd",'sizzlipede','skarmory','skeledirge','skiddo',
                'skiploom','skitty','skorupi','skrelp','skuntank','skwovet','slaking','slakoth','sliggoo','slither-wing',
                'slowbro','slowking','slowpoke','slugma','slurpuff','smeargle','smoliv','smoochum','sneasel','sneaseler',
                'snivy','snom','snorlax','snorunt','snover','snubbull','sobble','solgaleo','solosis','solrock','spearow',
                'spectrier','spewpa','spheal','spidops','spinarak','spinda','spiritomb','spoink','spigatito','spritzee',
                'squawkabilly','squirtle','stakataka','stantler','staraptor','staravia','starly','starmie','staryu',
                'steelix','steenee','stonjourner','stoutland','stufful','stunfisk','stunky','sudowoodo','suicune',
                'sunflora','surskit','swablu','swadloon','swalot','swampert','swanna','swellow','swirlix','swoobat',
                'sylveon','tadbulb','tailow','talonflame','tandemaus','tangela','tangrowth','tapu-bulu','tapu-fini',
                'tapu-koko','tapu-lele','tarountula','tatsugiri','tauros','teddiursa','tentacool','tentacruel','tepig',
                'terapagos','terrakion','thievul','throh','thundurus','thwackey','timburr','ting-lu','tinkatink','tinkaton',
                'tinkatuff','tirtouga','toedscool','toedscruel','togedemaru','togekiss','togepi','togetic','torchic',
                'torkoal','tornadus','torracat','torterra','totodile','toucannon','toxapex','toxel','toxicroak',
                'toxtricity','tranquill','trapinch','treecko','trevenant','tropius','trubbish','trumbeak','tsareena',
                'turtonator','turtwig','tympole','tynamo','typhlosion','tyranitar','tyrantrum','tyrogue','tyrunt',
                'umbreon','unfezant','unown','ursaluna','ursaring','urshifu','uxie','vanillish','vanillite',
                'vanilluxe','vaporeon','varoom','veluza','venipede','venomoth','venonat','venusaur','vespiqueen',
                'vibrava','victini','victreebel','vigoroth','vikavolt','vileplume','virizion','vivillon','volbeat',
                'volcanion','volcarona','voltorb','vullaby','vulpix','wailmer','wailord','walking-wake','walrein',
                'wartortle','watchdog','wattrel','weavile','weedle','weepinbell','weezing','whimsicott','whirlpede',
                'whiscash','whismur','wigglytuff','wiglett','wimpod','wingull','wishiwashi','wo-chien','wobbuffet',
                'woobat','wooloo','wooper','wormadam','wugtrio','wurmple','wynaut','wyrdeer','xatu','xerneas',
                'xurkitree','yamask','yamper','yanma','yanmega','yungoos','yvenltal','zacian','zamazenta',
                'zangoos','zapdos','zarude','zebstrika','zekrom','zeraora','zigzagoon','zoroark','zorua','zubat',
                'zweilous','zygarde']

game_list = pokemon_list.copy()
base_url = "https://pokeapi.co/api/v2/"



def pok_search(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        pok_data = response.json()
        return pok_data
    else:
        print(f"Failed to retrieve data {response.status_code}")
        
def dex_search(dex_number):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{dex_number}/")
    if response.status_code == 200:
        data = response.json()
        print(f"Name: {data['name']}")
        print(f"Dex Number: {data['id']}")
    else:
        print("Pokémon not found.")    
        
def pok_moves(list):
    selected_pok = random.sample(pokemon_list,1)
    pokemon_moves = []
    
    for pokemon in selected_pok:
        response = requests.get(f"{base_url}/pokemon/{pokemon.lower()}")
        if response.status_code == 200:
            data = response.json()
            moves = data['moves']
            
            random_moves = random.sample(moves, min(4,len(moves)))
            move_names = [move['move']['name'] for move in random_moves]
            
            pokemon_moves.append({
                'moves': move_names

            })
        else:
            print(f"Failed to retrieve data for {pokemon}")
    print("\nYour Pokémon moves are: ")

    return pokemon_moves
# Functions
def random_pok(num):
    if num > len(pokemon_list):
        return "Error: Not enough Pokemon in the list to generate that many"
    return random.sample(pokemon_list, num)


def find_pokemon(pok):
    if pok in pokemon_list:
        return "Yes, this Pokémon is in the list."
    else:
        return "No, this Pokémon is not in the list."
    
def create_team(game_list):
    total_list = []
    for i in range(6):
        team_list = random.sample(game_list,3)
        print(team_list)
        picker = int(input("Which one do you want to choose (1), (2), (3): "))
        if picker == 1:
            total_list.append(team_list[0])
            game_list.remove(team_list[0])
        elif picker == 2:
            total_list.append(team_list[1])
            game_list.remove(team_list[1])
        elif picker == 3:
            total_list.append(team_list[2])
            game_list.remove(team_list[2])
        else:
            auto_r = random.choice(team_list)
            print("Invalid choice. Please try again.")
            total_list.append(auto_r)
            game_list.remove(auto_r)
            break
    time.sleep(1)
    print("\nYour Pokémon team is:")
    for pokemon in total_list:
        print(pokemon)
    return total_list 

 

def dex_num_gen(pokemon_list, num):
    # Select 'num' random Pokémon from the list (with safety checks)
    selected_pok = random.sample(pokemon_list, min(num, len(pokemon_list)))
    dex_numbers = []
    
    for pokemon in selected_pok:
        response = requests.get(f"{base_url}/pokemon/{pokemon.lower()}")
        if response.status_code == 200:
            data = response.json()
            dex_numbers.append({
                'dex_number': data['id']  # Directly get the Dex number
            })
        else:
            print(f"Failed to retrieve data for {pokemon}")
    
    print(f"\nYour {len(dex_numbers)} Dex IDs are:")
    print(dex_numbers)
    

def chain_game(game_list):  # Take game_list as argument
    score = 0
    used_pok = []
    current_letter = None

    available_pokemon = game_list.copy()  # Local copy to modify
    if not available_pokemon:
        print("No Pokemon available for the chain game.")
        return 0

    current_pok = random.choice(available_pokemon).lower()
    available_pokemon.remove(current_pok)
    used_pok.append(current_pok)
    print(f"Starting Pokémon: {current_pok}")

    while True:
        current_letter = current_pok[-1].lower()
        print(f"\nNext Pokémon must start with: {current_letter.upper()}")
        user_input = input().lower()

        # Conditions
        if not user_input:
            print("Game ended by user!")
            break

        if user_input in used_pok:
            print(f"{user_input.title()} has already been used")
            print(f"You final score is {score}")
            break

        if user_input not in pokemon_list:
            print(f"{user_input.title()} is not a valid Pokemon")
            break

        if user_input[0].lower() != current_letter:
            print(f"{user_input.title()} doesn't start with {current_letter.upper()}")
            print(f"You final score is {score}")
            break

        # Valid Guesses
        score += 1
        available_pokemon.remove(user_input)
        used_pok.append(user_input)
        current_pok = user_input

        # Check remaining moves
        remaining = [p for p in available_pokemon if p.lower().startswith(current_letter)]
        if not remaining:
            print("No more possible Pokemon")
            print(f"You final score is {score}")
            break

    print(f"\nGame Over! Final score: {score}")
    return score


def first_letter(letter):
    correct_pok = []
    for pok in pokemon_list:
        if pok[0].lower() == letter:
            correct_pok.append(pok)
    print(correct_pok)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def save_high_score(score):
    with open("high_score.txt", "w") as file:
        file.write(str(score))


def chooser(high_score, total_games):  # Pass high_score and total_games
    # GUI
    print("(1) Random mode: Randomly selects a Pokémon from the list.")
    time.sleep(0.5)
    print("(2) Game mode: Play a special game with the names of the Pokemon")
    time.sleep(0.5)
    print("(3) Find mode: Find if a Pokemon exists in the list")
    time.sleep(0.5)
    print("(4) Team mode: Choose a team of 6 Pokemon for battle")
    time.sleep(0.5)
    while True:
        try:
            mode_c = int(input("Which mode do you want to play: "))
            break  # Exit the loop if input is valid
        except ValueError:
            print("Invalid input. Please enter a number (1, 2, 3 or 4).")
            time.sleep(1)  # Short delay to allow the user to see the error
            continue  # Go back to the beginning of the loop

    if mode_c == 1:
        print("(1) Pokemon mode: Generate a random number of Pokemon")
        time.sleep(0.5)
        print("(2) Ability mode: Generate a random ability of a Pokemon")
        time.sleep(0.5)
        print("(3) Moves mode: Generate 4 random moves for your Pokemon")
        time.sleep(0.5)
        print("(4) Dex mode: Generate a number of random Dex IDs")
        time.sleep(0.5)
        while True:
            try:
                mode_f = int(input("Which mode do you want to use: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
                time.sleep(2)  # Short delay to allow the user to see the error
                continue  # Go back to the beginning of the loop
        if mode_f == 1:
            num = int(input("How many pokemon do you want to generate? "))
            print(random_pok(num))
        elif mode_f == 2:
            print("(1) Single mode: Generate one ability for 1 Pokemon")
            time.sleep(0.5)
            print("(2) Multiple mode: Generate mulitple abilities at once")
            time.sleep(0.5)
            mode_g = int(input("Which mode do you want to use? "))
            if mode_g == 1:
                ability_name = pok_search(random.choice(pokemon_list))['abilities'][0]['ability']['name']
                print(ability_name)
            elif mode_g == 2:
                num = int(input("How many do you want to generate: "))
                selected_pok = random.sample(pokemon_list, num)
                for pok in selected_pok:
                    data = pok_search(pok)
                    if data and 'abilities' in data:
                        ability_name = data['abilities'][0]['ability']['name']
                        print(f"{ability_name}")
                    else:
                        print(f"Unable to fetch for {pok}")
            else:
                print("Invalid mode choice.")
        elif mode_f == 3:
            print(pok_moves(random.choice(pokemon_list)))
        elif mode_f == 4:
            print("(1) Single mode: Generate one Dex ID")
            time.sleep(0.5)
            print("(2) Triple mode: Generate 3 Dex ID")
            time.sleep(0.5)
            print("(3) Pentacle mode: Generate 5 Dex ID")
            time.sleep(0.5)
            print("(4) Chooser mode: Generate how many you want Dex ID")
            time.sleep(0.5)
            mode_b = int(input("Which mode do you want to use: "))
            if mode_b == 1:
                dex_num_gen(pokemon_list,1)
            elif mode_b == 2:
                dex_num_gen(pokemon_list,3)
            elif mode_b == 3:
                dex_num_gen(pokemon_list,5)
            elif mode_b == 4:
                dex_num = int(input("How many Dex IDs do you want to generate: "))
                dex_num_gen(pokemon_list,dex_num)
            else:
                print("Wrong choice selected")

    elif mode_c == 2:
        total_games += 1
        score = chain_game(game_list.copy())
        if score > high_score:
            high_score = score
            save_high_score(high_score)
            print("Congratulations! New High Score:", high_score)
        else:
            print(f"The Current High Score is {high_score}, better luck next time!")


    elif mode_c == 3:
        print("(1) Name mode: Find Pokemon by name")
        time.sleep(0.5)
        print("(2) First letter mode: Find Pokemon by the first letter")
        time.sleep(0.5)
        print("(3) Dex mode: Find Pokemon by its Dex ID")
        time.sleep(0.5)
        while True:
            try:
                waver = int(input("Which mode do you want to use: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number (1,2 or 3).")
                time.sleep(1)  # Short delay to allow the user to see the error
                continue  # Go back to the beginning of the loop
        if waver == 1:
            pok_to_find = input("Enter the name of a Pokémon:").lower()
            print(find_pokemon(pok_to_find))
        elif waver == 2:
            first_letter_to_find = input("Enter the first letter of a Pokémon:").lower()
            first_letter(first_letter_to_find)
        elif waver == 3:
            d_id = int(input("What Dex number do you want to search: "))
            dex_search(d_id)
    elif mode_c == 4:
        create_team(game_list)
    else:
        print("Invalid mode choice.")
    return high_score, total_games


def main():
    total_games = 0
    high_score = get_high_score()

    while True:
        clear_screen()
        print("\nWelcome to Pokémon Master!")
        print("High Score:", high_score)
        print("Total Games Played:", total_games)

        while True:
            try:
                choice = int(input("\n(1) Play\n(2) Exit\nEnter your choice: "))
                break  # Exit the loop if input is valid
            except ValueError:
                print("Invalid input. Please enter a number (1 or 2).")
                time.sleep(1)  # Short delay to allow the user to see the error
                continue  # Go back to the beginning of the loop

        if choice == 1:
            clear_screen()
            high_score, total_games = chooser(high_score, total_games)  # capture returned values
            #print("The Current High Score is:", high_score)

            print("\nPress Enter to continue")
            input()

        elif choice == 2:
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice. Please try again.")
            time.sleep(1)  # Short delay to allow the user to see the error

def get_high_score():
    try:
        with open('high_score.txt', 'r') as file:
            high_score = int(file.read())
            return high_score
    except (FileNotFoundError, IOError, ValueError):
        return 0

if __name__ == '__main__':
    main()
