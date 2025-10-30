import time


resources = []
familysaved = []
days_passed = 0
force_break_loop = 0
consumables = 3




def introduction():
    print("Welcome to the 60 Seconds Nuke Survival Game!")
    time.sleep(2)
    print("You have 60 seconds to prepare for a nuclear disaster.")
    time.sleep(2)
    print("The countdown begins now...")
    time.sleep(1)
   




def gather_supplies():
    print("You frantically gather supplies for your fallout shelter.")
    time.sleep(2)
    print("You find 5 supplies but can only carry 2. Make your pick.")
    time.sleep(2)
    supplies = ["Rifle", "BoyScout Book", "Axe", "Bug Spray", "Med Kit"]
    print("Choose 2 supplies from the following list:")
    for i, supply in enumerate(supplies, 1):
        print(f"{i}. {supply}")
    choices = []
    for _ in range(2):
        choice = int(input("Enter the number of the supply you want to grab: "))
        choices.append(supplies[choice - 1])
        resources.append(supplies[choice - 1])
    print(f"You grab {choices[0]} and {choices[1]} and head to your shelter.")




def gather_family():
    print("You remember about your family. Grab two of your family members and drop them in your fallout shelter.")
    time.sleep(2)
    family = ["Dolores (Wife)", "Mary Jane (Daughter)", "Timmy (Son)"]
    print("Choose 2 of your Family Members:")
    for i, member in enumerate(family, 1):
        print(f"{i}. {member}")
    choices = []
    for _ in range(2):
        choice = int(input("Enter the number of the family member you want to grab: "))
        choices.append(family[choice - 1])
        familysaved.append(family[choice - 1])
    print(f"You grab {choices[0]} and {choices[1]} and head to your shelter.")
    remaining_member = set(family) - set(choices)
    print(f"How could you forget {remaining_member.pop()}? Terrible Father!")




def gather_neccesities():
    global food_amount, water_amount
    print("Starving and Dehydration do not sound pleasent at all. Grab some of the neccesities and hurry up! ")
    time.sleep(2)
    neccesities = ["Food", "Water"]
    print("You have 48 available spaces, choose how to divide them.")
    food_amount = 0
    while True:
        try:
            food_amount = int(input("Please enter how many cans of food you would like to grab: "))
            break
        except ValueError:
            print("Please enter a valid number.")
   
    print("You grabbed", food_amount, "cans of food")
    water_amount = 48 - food_amount
    print("You grabbed", water_amount, "bottles of water")
   
def gather_utility_items():
    print("You remember the utility items you might need for your shelter.")
    time.sleep(2)
    utility_items = ["Radio", "Flashlight", "Gas Mask"]
    print("You have 3 utility items available, choose one to grab:")
    for i, item in enumerate(utility_items, 1):
        print(f"{i}. {item}")
    choice = int(input("Enter the number of the utility item you want to grab: "))
    if choice == 1:
        choice = 0
    elif choice == 2:
        choice = 1
    elif choice == 3:
        choice = 2
    chosen_item = utility_items[choice]
    resources.append(chosen_item)
    print(f"You grab the {chosen_item} and take it with you to your shelter.")




def gather_passtimes():
    print("It'll be a long time you stay down in that bunker... you should grab a few games to pass the time")
    time.sleep(2)
    passtimes = ["Chess", "Cards", "Checkers"]
    print("You have 3 pastimes available, choose one to grab:")
    for i, item in enumerate(passtimes, 1):
        print(f"{i}. {item}")
    choice = int(input("Enter the number of the game item you want to grab: "))
    chosen_item = passtimes[choice - 1]
    resources.append(chosen_item)
    print(f"You grab the {chosen_item} and take it with you to your shelter.")




from random import randint


selected_supplies = []
selected_family = []
selected_utility = []
selected_food = 0
selected_water = 0
allies = ["Eugene", "DaSilva"]
ops = ["Mohammed", "Velmurugan"]
other_bunkers = []








def trader():
    print("trade offer")
   
def ally():
    print("u make friends")




def scavenge():
    print("u find food")




def fight():




    if "rifle" in selected_supplies:
        print("u have a gun")
        if randint(1,10) <= 9:
            print("ur safe")
        else:
            print("ur cooked")
    else:
        print("u dont have gun")
        if randint(1,10) <= 1:
            print("ur safe")
        else:
            print("ur cooked")




def invasion():
    print("Do you trust the invaders? Or do you think they're here to kill you?")
    print("you can...")
    print("1. trust")
    print("2. attack")
    decision = input("enter your decision here: ")




    if decision == "trust":
        if randint(1,10) <= 6:
            print("ur safe")
        else:
            print("ur cooked")
    elif decision == "attack":
        fight()




def food_ration():
    print("u eat")




def insanity():
    print("u r insane")




def invade(familyName):
    print("Do you trust the inhabitants? Or do you think they're going to defend their bunker?")
    print("you can...")
    print("1. trust")
    print("2. attack")
    decision = input("enter your decision here:")




    if decision == "trust":
        if randint(1,10) <= 6:
            print("ur safe")
        else:
            print("ur cooked")
    elif decision == "attack":
        fight()








def main():
    introduction()
    time_left = 60
    while time_left > 0:
        if time_left == 50:
            gather_supplies()
        if time_left == 40:
            gather_family()
        if time_left == 30:
            gather_neccesities()
        if time_left == 20:
            gather_utility_items()
        if time_left == 10:
            gather_passtimes()
        if time_left == 3:
            print("GET TO THE BUNKER!")
        print(f"{time_left}...")
        time.sleep(1)
        time_left -= 1




normal_diary = []
nonnormal_diary = []












if __name__ == "__main__":
    main()




    print("you are now in bunker")








    for i in range (30):
        print("Day " , i+1 )
        food_amount = food_amount - consumables
        water_amount = water_amount - consumables


        if food_amount <= 0 or water_amount <= 0:
            print("There was not enough consumables, the family has died.")
            break
       
        normal_diary.append("Another day in this post-apocalyptic world. The sun rose, painting the sky with hues of orange and pink, reminding us of the days before everything went wrong. Our little shelter still stands, a beacon of hope in a desolate world. Today the family consumed another 3 food and water which brings our total to " + str(food_amount) + " food and " + str(water_amount) + " water. Our other resources are " + str(resources)) # type: ignore
        normal_diary.append("This morning, we felt the inevitable pinch of survival. As usual, our rations had to be adjusted. We used up 3 cans of food and 3 bottles of water. It's a harsh reality we face every day, but there's no escaping it. Our water amount is " + str(water_amount) + " and our food amount is " + str(food_amount) + ". Our supplies are dwindling faster than we hoped. We must be more cautious and resourceful if we're to see another sunrise. Our supplies are " + str(resources))
        normal_diary.append("We woke up to another quiet morning. We consumed another 3 cans of food and 3 bottles of water. It’s unsettling how quickly supplies dwindle.. Today, we talked a lot about the past, reminiscing about better days. It helps to keep our spirits up, though sometimes it feels like we're clinging to ghosts. Our water amount is " + str(water_amount) + " and our food amount is " + str(food_amount) + ". Our supplies are dwindling faster than we hoped. We must be more cautious and resourceful if we're to see another sunrise. Our supplies are " + str(resources))
        normal_diary.append("Rations are becoming a routine – 3 cans of food, 3 bottles of water. The predictability is oddly comforting. We spent the day playing card games and telling stories. It's essential to keep our minds sharp and our morale high. The nights are getting colder. We bundled up together, grateful for every bit of warmth we can share. Tomorrow, we’ll need to find ways to insulate the bunker better. Our water amount is " + str(water_amount) + " and our food amount is " + str(food_amount) + ". Our supplies are dwindling faster than we hoped. We must be more cautious and resourceful if we're to see another sunrise. Our supplies are " + str(resources))
        normal_diary.append("Today was a quiet day. We stuck to our ration plan and tried to conserve as much energy as possible. We spent hours discussing what we miss most from the outside world. Simple things like fresh air and sunlight feel like distant dreams. The bonds we're forming in this small space are growing stronger, though. It's comforting to know we’re not facing this alone.We lost another 3 food and water. Our water amount is " + str(water_amount) + " and our food amount is " + str(food_amount) + ". Our supplies are dwindling faster than we hoped. We must be more cautious and resourceful if we're to see another sunrise. Our supplies are " + str(resources))
        normal_diary.append("Another day in the bunker. Another 3 cans of food, 3 bottles of water. We're getting used to the rhythm of life here. We decided to take turns keeping watch, even though we know it's unlikely anyone will come. It’s more for our peace of mind. We’ve also started writing letters to ourselves, a way to process everything we’re going through. Our water amount is " + str(water_amount) + " and our food amount is " + str(food_amount) + ". Our supplies are dwindling faster than we hoped. We must be more cautious and resourceful if we're to see another sunrise. Our supplies are " + str(resources))
        normal_diary.append("Every new day in the bunker feels like a milestone. We celebrated with the luxury of eating and drinking. We spent the day reminiscing and planning for the future. If we ever get out, what will we do first? These dreams keep us going, giving us a reason to push through each day. Tonight, we’ll try to get a good night’s sleep, hopeful for better days ahead. We lost another 3 food and water. Our water amount is " + str(water_amount) + " and our food amount is " + str(food_amount) + ". Our supplies are dwindling faster than we hoped. We must be more cautious and resourceful if we're to see another sunrise. Our supplies are " + str(resources))
        normal_diary.append("Routine is our lifeline. Breakfast, discussions, games, dinner, sleep. It's all so repetitive, but it's our new normal. We consumed another 3 cans of food and 3 bottles of water today. We talked about ways to stretch our supplies further. Maybe skipping a meal every few days? It’s a tough decision, but survival requires hard choices. We’ll see how we feel about it tomorrow. Our water amount is " + str(water_amount) + " and our food amount is " + str(food_amount) + ". Our supplies are dwindling faster than we hoped. We must be more cautious and resourceful if we're to see another sunrise. Our supplies are " + str(resources))
        normal_diary.append("Today was uneventful, but uneventful is good. It means we’re still safe. We talked a lot about the future today, imagining what life might be like when we finally leave the bunker. It’s important to keep hope alive, even in small ways. Rations are still holding out, but the dwindling numbers are always in the back of our minds. We must stay strong and focused. We lost another 3 food and water. Our water amount is " + str(water_amount) + " and our food amount is " + str(food_amount) + ". Our supplies are dwindling faster than we hoped. We must be more cautious and resourceful if we're to see another sunrise. Our supplies are " + str(resources))
        normal_diary.append("Another day of the same routine. It’s comforting in a way. We ate our usual rations and spent the day sharing stories. The bunker feels a little smaller every day, but we’re making it work. We’ve started a small journal where we each write a daily entry. It’s a way to document our experiences and keep our minds occupied. Tomorrow, we’ll try to come up with new activities to keep our spirits up. We lost another 3 food and water. Our water amount is " + str(water_amount) + " and our food amount is " + str(food_amount) + ". Our supplies are dwindling faster than we hoped. We must be more cautious and resourceful if we're to see another sunrise. Our supplies are " + str(resources))
        normal_diary.append("The days blend into each other down here. Today was no different. We rationed our food and water, trying to make it last as long as possible. We spent time discussing strategies for the future and reminiscing about the past. It’s hard not to think about what we’ve lost, but we’re trying to stay positive. We need to stay focused and take it one day at a time. We lost another 3 food and water. Our water amount is " + str(water_amount) + " and our food amount is " + str(food_amount) + ". Our supplies are dwindling faster than we hoped. We must be more cautious and resourceful if we're to see another sunrise. Our supplies are " + str(resources))
        normal_diary.append("Another day in the bunker. It’s becoming routine, but that’s not necessarily a bad thing. We consumed our rations and spent the day talking about our hopes and dreams. It’s important to keep hope alive, even when things seem bleak. We’re trying to stay positive and support each other as best we can. Every day is a step closer to the end of this ordeal. We lost another 3 food and water. Our water amount is " + str(water_amount) + " and our food amount is " + str(food_amount) + ". Our supplies are dwindling faster than we hoped. We must be more cautious and resourceful if we're to see another sunrise. Our supplies are " + str(resources))
        normal_diary.append("Today felt particularly long. We rationed our food and water as usual, but the monotony is starting to wear on us. We tried to distract ourselves with games and stories, but it’s hard to shake the feeling of being trapped. We’re doing our best to stay positive and keep each other motivated. Tomorrow is another day, and we’ll face it together. We lost another 3 food and water. Our water amount is " + str(water_amount) + " and our food amount is " + str(food_amount) + ". Our supplies are dwindling faster than we hoped. We must be more cautious and resourceful if we're to see another sunrise. Our supplies are " + str(resources))
        normal_diary.append("This bunker will never end. We’re sticking to our rations and trying to make the best of our situation. We’ve been talking about ways to stay sane and keep our spirits up. It’s important to stay hopeful, even when things seem bleak. We’re all in this together, and we’ll get through it together. We lost another 3 food and water. Our water amount is " + str(water_amount) + " and our food amount is " + str(food_amount) + ". Our supplies are dwindling faster than we hoped. We must be more cautious and resourceful if we're to see another sunrise. Our supplies are " + str(resources))
        normal_diary.append("Another day, another 3 cans of food and 3 bottles of water. The routine is comforting in its own way, but it’s hard not to feel restless. We spent the day discussing our plans for the future and trying to keep our spirits up. It’s important to stay positive and support each other. We’re all in this together, and we’ll get through it together. Our water amount is " + str(water_amount) + " and our food amount is " + str(food_amount) + ". Our supplies are dwindling faster than we hoped. We must be more cautious and resourceful if we're to see another sunrise. Our supplies are " + str(resources))
        normal_diary.append("Today was much like the others. We rationed our food and water and spent the day talking and playing games. It’s important to keep our minds occupied and our spirits high. We’re trying to stay positive and support each other as best we can. Every day is a step closer to the end of this ordeal. We lost another 3 food and water. Our water amount is " + str(water_amount) + " and our food amount is " + str(food_amount) + ". Our supplies are dwindling faster than we hoped. We must be more cautious and resourceful if we're to see another sunrise. Our supplies are " + str(resources))
        normal_diary.append("The days are starting to blur together. We rationed our food and water and spent the day talking about our hopes and dreams. It’s important to keep hope alive, even when things seem bleak. We’re trying to stay positive and support each other as best we can. Tomorrow is another day, and we’ll face it together. We lost another 3 food and water. Our water amount is " + str(water_amount) + " and our food amount is " + str(food_amount) + ". Our supplies are dwindling faster than we hoped. We must be more cautious and resourceful if we're to see another sunrise. Our supplies are " + str(resources))
        normal_diary.append("Another day in the bunker. It’s becoming routine, but that’s not necessarily a bad thing. We consumed our rations and spent the day talking about our hopes and dreams. It’s important to keep hope alive, even when things seem bleak. We’re trying to stay positive and support each other as best we can. Every day is a step closer to the end of this ordeal. We lost another 3 food and water. Our water amount is " + str(water_amount) + " and our food amount is " + str(food_amount) + ". Our supplies are dwindling faster than we hoped. We must be more cautious and resourceful if we're to see another sunrise. Our supplies are " + str(resources))
        normal_diary.append("Today felt particularly long. We rationed our food and water as usual, but the monotony is starting to wear on us. We tried to distract ourselves with games and stories, but it’s hard to shake the feeling of being trapped. We’re doing our best to stay positive and keep each other motivated. Tomorrow is another day, and we’ll face it together. We lost another 3 food and water. Our water amount is " + str(water_amount) + " and our food amount is " + str(food_amount) + ". Our supplies are dwindling faster than we hoped. We must be more cautious and resourceful if we're to see another sunrise. Our supplies are " + str(resources))
        normal_diary.append("Twenty days in the bunker. It feels like a milestone, though it’s hard to celebrate. We’re sticking to our rations and trying to make the best of our situation. We’ve been talking about ways to stay sane and keep our spirits up. It’s important to stay hopeful, even when things seem bleak. We’re all in this together, and we’ll get through it together. We lost another 3 food and water. Our water amount is " + str(water_amount) + " and our food amount is " + str(food_amount) + ". Our supplies are dwindling faster than we hoped. We must be more cautious and resourceful if we're to see another sunrise. Our supplies are " + str(resources))
        normal_diary.append("Another day, another 3 cans of food and 3 bottles of water. The routine is comforting in its own way, but it’s hard not to feel restless. We spent the day discussing our plans for the future and trying to keep our spirits up. It’s important to stay positive and support each other. We’re all in this together, and we’ll get through it together. Our water amount is " + str(water_amount) + " and our food amount is " + str(food_amount) + ". Our supplies are dwindling faster than we hoped. We must be more cautious and resourceful if we're to see another sunrise. Our supplies are " + str(resources))
        normal_diary.append("Today was much like the others. We rationed our food and water and spent the day talking and playing games. It’s important to keep our minds occupied and our spirits high. We’re trying to stay positive and support each other as best we can. Every day is a step closer to the end of this ordeal. We lost another 3 food and water. Our water amount is " + str(water_amount) + " and our food amount is " + str(food_amount) + ". Our supplies are dwindling faster than we hoped. We must be more cautious and resourceful if we're to see another sunrise. Our supplies are " + str(resources))
        normal_diary.append("The days are starting to blur together. We rationed our food and water and spent the day talking about our hopes and dreams. It’s important to keep hope alive, even when things seem bleak. We’re trying to stay positive and support each other as best we can. Tomorrow is another day, and we’ll face it together. We lost another 3 food and water. Our water amount is " + str(water_amount) + " and our food amount is " + str(food_amount) + ". Our supplies are dwindling faster than we hoped. We must be more cautious and resourceful if we're to see another sunrise. Our supplies are " + str(resources))
        normal_diary.append("Another day in the bunker. It’s becoming routine, but that’s not necessarily a bad thing. We consumed our rations and spent the day talking about our hopes and dreams. It’s important to keep hope alive, even when things seem bleak. We’re trying to stay positive and support each other as best we can. Every day is a step closer to the end of this ordeal. We lost another 3 food and water. Our water amount is " + str(water_amount) + " and our food amount is " + str(food_amount) + ". Our supplies are dwindling faster than we hoped. We must be more cautious and resourceful if we're to see another sunrise. Our supplies are " + str(resources))
        normal_diary.append("Today felt particularly long. We rationed our food and water as usual, but the monotony is starting to wear on us. We tried to distract ourselves with games and stories, but it’s hard to shake the feeling of being trapped. We’re doing our best to stay positive and keep each other motivated. Tomorrow is another day, and we’ll face it together. We lost another 3 food and water. Our water amount is " + str(water_amount) + " and our food amount is " + str(food_amount) + ". Our supplies are dwindling faster than we hoped. We must be more cautious and resourceful if we're to see another sunrise. Our supplies are " + str(resources))
        normal_diary.append("Today, We’re sticking to our rations and trying to make the best of our situation. We’ve been talking about ways to stay sane and keep our spirits up. It’s important to stay hopeful, even when things seem bleak. We’re all in this together, and we’ll get through it together. We lost another 3 food and water. Our water amount is " + str(water_amount) + " and our food amount is " + str(food_amount) + ". Our supplies are dwindling faster than we hoped. We must be more cautious and resourceful if we're to see another sunrise. Our supplies are " + str(resources))
        normal_diary.append("Another day, another 3 cans of food and 3 bottles of water. The routine is comforting in its own way, but it’s hard not to feel restless. We spent the day discussing our plans for the future and trying to keep our spirits up. It’s important to stay positive and support each other. We’re all in this together, and we’ll get through it together. Our water amount is " + str(water_amount) + " and our food amount is " + str(food_amount) + ". Our supplies are dwindling faster than we hoped. We must be more cautious and resourceful if we're to see another sunrise. Our supplies are " + str(resources))
        normal_diary.append("Today was much like the others. We rationed our food and water and spent the day talking and playing games. It’s important to keep our minds occupied and our spirits high. We’re trying to stay positive and support each other as best we can. Every day is a step closer to the end of this ordeal. We lost another 3 food and water. Our water amount is " + str(water_amount) + " and our food amount is " + str(food_amount) + ". Our supplies are dwindling faster than we hoped. We must be more cautious and resourceful if we're to see another sunrise. Our supplies are " + str(resources))
        normal_diary.append("The days are starting to blur together. We rationed our food and water and spent the day talking about our hopes and dreams. It’s important to keep hope alive, even when things seem bleak. We’re trying to stay positive and support each other as best we can. Tomorrow is another day, and we’ll face it together.We lost another 3 food and water. Our water amount is " + str(water_amount) + " and our food amount is " + str(food_amount) + ". Our supplies are dwindling faster than we hoped. We must be more cautious and resourceful if we're to see another sunrise. Our supplies are " + str(resources))
        normal_diary.append("This bunker feels like eternity. We’re sticking to our rations and trying to make the best of our situation. We’ve been talking about ways to stay sane and keep our spirits up. It’s important to stay hopeful, even when things seem bleak. We’re all in this together, and we’ll get through it together. We lost another 3 food and water. Our water amount is " + str(water_amount) + " and our food amount is " + str(food_amount) + ". Our supplies are dwindling faster than we hoped. We must be more cautious and resourceful if we're to see another sunrise. Our supplies are " + str(resources))
       
        if randint(1,10) <= 3:
            enter = input(normal_diary[i] + " press enter to continue.")
        else:
            non_normal_day = randint(1,4)
            if non_normal_day == 1:
                if familysaved:
                    for i, member in enumerate(familysaved, 1):
                        print(f"{i}. {member}")
                    choice = input("The day is rainy, send someone out to collect water: ")
                    if familysaved[int(choice)-1] == "Dolores (Wife)":
                        random = randint(1,10)
                        if random <= 6:
                            water_gathered = randint(3,6)
                            water_amount += water_gathered
                            print(familysaved[int(choice)-1] + " brought back " + str(water_gathered) + " water")
                        elif random == 7 or randint(1,10) == 8:
                            print(familysaved[int(choice)-1] + " dropped all the water coming back")
                        else:
                            print(familysaved[int(choice)-1] + " slipped on the slippery steps and died")
                            consumables -= 1
                            del familysaved[int(choice)-1]
                    elif familysaved[int(choice)-1] == "Mary Jane (Daughter)":
                        random = randint(1,10)
                        if random <= 4:
                            water_gathered = randint(5,8)
                            water_amount += water_gathered
                            print(familysaved[int(choice)-1] + " brought back " + str(water_gathered) + " water")
                        elif random <= 6:
                            water_gathered = randint(2,4)
                            water_amount += water_gathered
                            print(familysaved[int(choice)-1] + " brought back " + str(water_gathered) + " water")
                        else:
                            consumables -= 1
                            print(familysaved[int(choice)-1] + " saw a colorful frog and tried petting it. The frog ate her.")
                            del familysaved[int(choice)-1]
                    elif familysaved[int(choice)-1] == "Timmy (Son)":
                        random = randint(1,10)
                        if random <= 5:
                            water_gathered = 5
                            water_amount += water_gathered
                            print(familysaved[int(choice)-1] + " brought back " + str(water_gathered) + " water")
                        elif random <= 9:
                            print(familysaved[int(choice)-1] + " was pretty thirsty so he drank all of it on the way back")
                        else:
                            print(familysaved[int(choice)-1] + " drank too much  on the way back that he blew up.")
                            consumables -= 1
                            del familysaved[int(choice)-1]
                else:
                    enter = input("The day is rainy and you're by yourself. You decided to go fetch some water. Press enter to continue")
                    random = randint(1,10)
                    if random <= 7:
                        water_gathered = randint(3,6)
                        water_amount += water_gathered
                        print(familysaved[int(choice)-1] + " brought back " + str(water_gathered) + " water")
                    else:
                        print("You decided that it wasn't worth living by yourself anymore, so you decided the best way to go out is to go swim in the radioactive lake with the fishes. You died.")
                        force_break_loop = 1
                        break
            elif non_normal_day == 2:
                if familysaved:
                    for i, member in enumerate(familysaved, 1):
                        print(f"{i}. {member}")
                    choice = input("The day is sunny, send someone to get food")
                    if familysaved[int(choice)-1] == "Dolores (Wife)":
                        random = randint(1,10)
                        if random <= 6:
                            food_gathered = randint(3,6)
                            food_amount += food_gathered
                            print(familysaved[int(choice)-1] + " brought back " + str(food_gathered) + " food")
                        elif random == 7:
                            print(familysaved[int(choice)-1] + " got attacked by monkeys and got her food gathered stolen")
                        else:
                            print(familysaved[int(choice)-1] + " had a sun stroke and died.")
                            consumables -= 1
                            del familysaved[int(choice)-1]
                    elif familysaved[int(choice)-1] == "Mary Jane (Daughter)":
                        random = randint(1,10)
                        if random <= 4:
                            food_gathered = randint(6,9)
                            food_amount += food_gathered
                            print(familysaved[int(choice)-1] + " brought back " + str(food_gathered) + " food")
                        elif random <= 6:
                            food_gathered = randint(2,4)
                            food_amount += food_gathered
                            print(familysaved[int(choice)-1] + " brought back " + str(food_gathered) + " food")
                        elif random <= 8:
                            print(familysaved[int(choice)-1] + " was to picky with the perfect ripeness of fruits that it became night time and had to run back")
                        else:
                            print(familysaved[int(choice)-1] + " got sleepy and decided to take a nap. Vultures came and ate her.")
                            consumables -= 1
                            del familysaved[int(choice)-1]
                    elif familysaved[int(choice)-1] == "Timmy (Son)":
                        random = randint(1,10)
                        if random <= 7:
                            food_gathered = randint(7,10)
                            food_amount += food_gathered
                            print(familysaved[int(choice)-1] + " brought back " + str(food_gathered) + " food")
                        else:
                            print(familysaved[int(choice)-1] + " fought with lions for the food. It was admirable but still stupid. He of coursed died.")
                            consumables -= 1
                            del familysaved[int(choice)-1]
                else:
                    print("The day is sunny and you're by yourself. You decided to go fetch some food")
                    random = randint(1,10)
                    if random <= 6:
                        food_gathered = randint(3,6)
                        food_amount += food_gathered
                        print("You brought back " + str(food_gathered) + " food")
                    else:
                        print("You developed an immunity to the radiation and you met with monkeys. You decided it would be better living with monkey than by yourself.")
                        force_break_loop = 1
                        break      
            elif non_normal_day == 3:
                choice = input("You hear knockings on the door. What do you do? \n 1. Ignore \n 2. Answer")
                if choice == 1:
                    random = randint(1,100)
                    if random <= 33:
                        print("After a while the bangings stop. Wonder that could've been.")
                    elif random <= 50:
                        water_gathered = randint(2,5)
                        print("Flying fishes busted through the door and saw the stored water. They swam in it and contaminated " + str(water_gathered) + " water")
                        water_amount -= water_gathered
                    elif random <= 80:
                        if familysaved:
                            for i, member in enumerate(familysaved, 1):
                                print(f"{i}. {member}")
                            fchoice = input("An intruder barged in ready to fight. Who do you send to resolve the situation")
                            if familysaved[int(choice)-1] == "Dolores (Wife)":
                                for i, x in enumerate(resources, 1):
                                    print(f"{i}. {x}")
                                choice = input("What do you want " + familysaved[int(fchoice) - 1] + " to use? ")
                                if resources[int(choice) - 1] == "Bug Spray":
                                    random2 = randint(1,10)
                                    if random2 <= 4:
                                        print(familysaved[int(fchoice)-1] + " sprayed bug spray into the intruder's eyes. The intruder ran away.")
                                    elif random2 <= 7:
                                        print(familysaved[int(fchoice)-1] + " sprayed bug spray. The intruder really liked the bug spray so he stole it and ran away.")
                                        resources.remove("Bug Spray")
                                    else:
                                        print("The intruder didn't like the idea of bus spray in his face. He kidnapped " + familysaved[int(fchoice)-1] + " and ran away")
                                        consumables -= 1
                                        del familysaved[int(fchoice) - 1]
                                elif resources[int(choice) - 1] == "Medkit":
                                    random2 = randint(1,10)
                                    if random2 <= 5:
                                        print(familysaved[int(fchoice)-1] + " gave the medkit away. The intruder appreciated that and in return gave the family 3 food.")
                                        resources.remove("Medkit")
                                        food_amount += 3
                                    else:
                                        print("The intruder just stole the medkit and ran away")
                                        resources.remove("Medkit")
                                elif resources[int(choice) - 1] == "Flashlight":
                                    random2 = randint(1,10)
                                    if random2 <= 3:
                                        print(familysaved[int(fchoice)-1] + " flashed the intruder's eyes and blinded him. He ran away crying.")
                                    else:
                                        print("The intruder was confused what just happened and got annoyed at " + familysaved[int(fchoice) - 1] + " and stole the flashlight.")
                                        resources.remove("Flashlight")
                                elif resources[int(choice) - 1] == "Rifle":
                                    random2 = randint(1,10)
                                    if random2 <= 7:
                                        print(familysaved[int(fchoice) - 1] + " used the rifle and killed the intruder")
                                    else:
                                        print(familysaved[int(fchoice) - 1] + " used the rifle and killed the intruder. However, the rifle blew up.")
                                        del resources[int(choice) - 1]
                                elif resources[int(choice) - 1] == "Axe":
                                    random2 = randint(1,10)
                                    if random2 <= 9:
                                        print(familysaved[int(fchoice) - 1] + " used the axe and killed the intruder")
                                    else:
                                        print(familysaved[int(fchoice) - 1] + " used the axe and killed the intruder. However, she swung so hard that she killed herself too.")
                                        del familysaved[int(fchoice) - 1]
                                else:
                                    print(familysaved[int(fchoice)-1] + " used " + resources[int(choice) - 1] + " to resolve the situtation. The intruder stole " + resources[int(choice) - 1] + " and ran away")
                                    del resources[int(choice)-1]
                            elif familysaved[int(choice)-1] == "Mary Jane (Daughter)":
                                for i, x in enumerate(resources, 1):
                                    print(f"{i}. {x}")
                                choice = input("What do you want " + familysaved[int(fchoice) - 1] + " to use? ")
                                if resources[int(choice) - 1] == "Bug Spray":
                                    random2 = randint(1,10)
                                    if random2 <= 4:
                                        print(familysaved[int(fchoice)-1] + " sprayed bug spray into the intruder's eyes. The intruder ran away.")
                                    elif random2 <= 9:
                                        print(familysaved[int(fchoice)-1] + " sprayed bug spray. The intruder really liked the bug spray so he stole it and ran away.")
                                        resources.remove("Bug Spray")
                                    else:
                                        print("The intruder didn't like the idea of bus spray in his face. He kidnapped " + familysaved[int(fchoice)-1] + " and ran away")
                                        consumables -= 1
                                        del familysaved[int(fchoice) - 1]
                                elif resources[int(choice) - 1] == "Medkit":
                                    random2 = randint(1,10)
                                    if random2 <= 8:
                                        print(familysaved[int(fchoice)-1] + " gave the medkit away. The intruder appreciated that and in return gave the family 5 food.")
                                        resources.remove("Medkit")
                                        food_amount += 5
                                    else:
                                        print("The intruder just stole the medkit and ran away")
                                        resources.remove("Medkit")
                                elif resources[int(choice) - 1] == "Flashlight":
                                    random2 = randint(1,10)
                                    if random2 <= 3:
                                        print(familysaved[int(fchoice)-1] + " flashed the intruder's eyes and blinded him. He ran away crying.")
                                    else:
                                        print("The intruder was confused what just happened and got annoyed at " + familysaved[int(fchoice) - 1] + " and stole the flashlight.")
                                        resources.remove("Flashlight")
                                elif resources[int(choice) - 1] == "Rifle":
                                    random2 = randint(1,10)
                                    if random2 <= 5:
                                        print(familysaved[int(fchoice) - 1] + " used the rifle and killed the intruder")
                                    else:
                                        print(familysaved[int(fchoice) - 1] + " used the rifle and killed the intruder. However, the rifle blew up.")
                                        del resources[int(choice) - 1]
                                elif resources[int(choice) - 1] == "Axe":
                                    random2 = randint(1,10)
                                    if random2 <= 7:
                                        print(familysaved[int(fchoice) - 1] + " used the axe and killed the intruder")
                                    else:
                                        print(familysaved[int(fchoice) - 1] + " used the axe and killed the intruder. However, she swung so hard that she killed herself too.")
                                        del familysaved[int(fchoice) - 1]
                                else:
                                    print(familysaved[int(fchoice)-1] + " used " + resources[int(choice) - 1] + " to resolve the situtation. The intruder stole " + resources[int(choice) - 1] + " and ran away")
                                    del resources[int(choice)-1]
                            elif familysaved[int(choice)-1] == "Timmy (Son)":
                                for i, x in enumerate(resources, 1):
                                    print(f"{i}. {x}")
                                choice = input("What do you want " + familysaved[int(fchoice) - 1] + " to use? ")
                                if resources[int(choice) - 1] == "Bug Spray":
                                    random2 = randint(1,10)
                                    if random2 <= 4:
                                        print(familysaved[int(fchoice)-1] + " sprayed bug spray into the intruder's eyes. The intruder ran away.")
                                    elif random2 <= 6:
                                        print(familysaved[int(fchoice)-1] + " sprayed bug spray. The intruder really liked the bug spray so he stole it and ran away.")
                                        resources.remove("Bug Spray")
                                    else:
                                        print("The intruder didn't like the idea of bus spray in his face. He kidnapped " + familysaved[int(fchoice)-1] + " and ran away")
                                        consumables -= 1
                                        del familysaved[int(fchoice) - 1]
                                elif resources[int(choice) - 1] == "Medkit":
                                    random2 = randint(1,10)
                                    if random2 <= 5:
                                        print(familysaved[int(fchoice)-1] + " gave the medkit away. The intruder appreciated that and in return gave the family 3 food.")
                                        resources.remove("Medkit")
                                        food_amount += 3
                                    else:
                                        print("The intruder just stole the medkit and ran away")
                                        resources.remove("Medkit")
                                elif resources[int(choice) - 1] == "Flashlight":
                                    random2 = randint(1,10)
                                    if random2 <= 3:
                                        print(familysaved[int(fchoice)-1] + " flashed the intruder's eyes and blinded him. He ran away crying.")
                                    else:
                                        print("The intruder was confused what just happened and got annoyed at " + familysaved[int(fchoice) - 1] + " and stole the flashlight.")
                                        resources.remove("Flashlight")
                                elif resources[int(choice) - 1] == "Rifle":
                                    random2 = randint(1,10)
                                    if random2 <= 9:
                                        print(familysaved[int(fchoice) - 1] + " used the rifle and killed the intruder")
                                    else:
                                        print(familysaved[int(fchoice) - 1] + " used the rifle and killed the intruder. However, the rifle blew up.")
                                        del resources[int(choice) - 1]
                                elif resources[int(choice) - 1] == "Axe":
                                    random2 = randint(1,10)
                                    if random2 <= 9:
                                        print(familysaved[int(fchoice) - 1] + " used the axe and killed the intruder")
                                    else:
                                        print(familysaved[int(fchoice) - 1] + " used the axe and killed the intruder. However, she swung so hard that she killed herself too.")
                                        del familysaved[int(fchoice) - 1]
                                else:
                                    print(familysaved[int(fchoice)-1] + " used " + resources[int(choice) - 1] + " to resolve the situtation. The intruder stole " + resources[int(choice) - 1] + " and ran away")
                                    del resources[int(choice)-1]
                        else:
                            for i, x in enumerate(resources, 1):
                                    print(f"{i}. {x}")
                            choice = input("What do you want " + familysaved[int(fchoice) - 1] + " to use? ")
                            if resources[int(choice) - 1] == "Bug Spray":
                                    random2 = randint(1,10)
                                    if random2 <= 4:
                                        print(familysaved[int(fchoice)-1] + " sprayed bug spray into the intruder's eyes. The intruder ran away.")
                                    elif random2 <= 6:
                                        print(familysaved[int(fchoice)-1] + " sprayed bug spray. The intruder really liked the bug spray so he stole it and ran away.")
                                        resources.remove("Bug Spray")
                                    else:
                                        print("The intruder didn't like the idea of bus spray in his face. He kidnapped " + familysaved[int(fchoice)-1] + " and ran away")
                                        consumables -= 1
                                        force_break_loop = 1
                            elif resources[int(choice) - 1] == "Medkit":
                                    random2 = randint(1,10)
                                    if random2 <= 5:
                                        print(familysaved[int(fchoice)-1] + " gave the medkit away. The intruder appreciated that and in return gave the family 3 food.")
                                        resources.remove("Medkit")
                                        food_amount += 3
                                    else:
                                        print("The intruder just stole the medkit and ran away")
                                        resources.remove("Medkit")
                            elif resources[int(choice) - 1] == "Flashlight":
                                    random2 = randint(1,10)
                                    if random2 <= 3:
                                        print(familysaved[int(fchoice)-1] + " flashed the intruder's eyes and blinded him. He ran away crying.")
                                    else:
                                        print("The intruder was confused what just happened and got annoyed at " + familysaved[int(fchoice) - 1] + " and stole the flashlight.")
                                        resources.remove("Flashlight")
                            elif resources[int(choice) - 1] == "Rifle":
                                    random2 = randint(1,10)
                                    if random2 <= 9:
                                        print(familysaved[int(fchoice) - 1] + " used the rifle and killed the intruder")
                                    else:
                                        print(familysaved[int(fchoice) - 1] + " used the rifle and killed the intruder. However, the rifle blew up.")
                                        del resources[int(choice) - 1]
                            elif resources[int(choice) - 1] == "Axe":
                                    random2 = randint(1,10)
                                    if random2 <= 9:
                                        print(familysaved[int(fchoice) - 1] + " used the axe and killed the intruder")
                                    else:
                                        print(familysaved[int(fchoice) - 1] + " used the axe and killed the intruder. However, she swung so hard that she killed herself too.")
                                        force_break_loop = 1
                            elif resources[int(choice) - 1] == "Gas Mask":
                                print("You decided to wear your Gas mask and go on an adeventure with the intruder.")
                                force_break_loop = 1
                            else:
                                print("You were about to do something but you decided it was no longer worth the trouble so you let the intruder kill you")
                                force_break_loop = 1
            elif non_normal_day == 4:
                random_family = randint(1,len(familysaved))
               
                if familysaved[random_family-1] == "Dolores (Wife)":
                    choice = input(familysaved[random_family-1] + " is scratching her scalp rapidly. What do you want to do? \n1: Give her a game \n2: Calm her down \n3: Let it be\n")
                   
                    if int(choice) == 1:
                        if "Chess" in resources:
                           
                            random = randint(1,10)
                           
                            if random <= 4:
                                print(familysaved[random_family-1] + " tried playing the game but didn't understand how castling worked. She killed herself out of confusion")
                                del familysaved[random_family-1]
                            elif random <= 8:
                                print(familysaved[random_family-1] + " really liked the game and became great at it.")
                            elif random == 9:
                                print(familysaved[random_family-1] + " got really mad when she lost to her son that she broke the game.")
                            elif random == 10:
                                print(familysaved[random_family-1] + " was apparently really huungry and she just ate the board. She did not survive that.")
                                del familysaved[random_family-1]
                                resources.remove("Chess")
                        elif "Checkers" in resources:
                           
                            random = randint(1,10)
                           
                            if random <= 2:
                                print(familysaved[random_family-1] + " tried playing the game but didn't understand Checkers. She killed herself out of confusion")
                                del familysaved[random_family-1]
                            elif random <= 8:
                                print(familysaved[random_family-1] + " really liked the game and became great at it.")
                            elif random == 9:
                                print(familysaved[random_family-1] + " got really mad when she lost to her son that she broke the game.")
                            elif random == 10:
                                print(familysaved[random_family-1] + " was apparently really huungry and she just ate the board. She did not survive that.")
                                del familysaved[random_family-1]
                                resources.remove("Checkers")
                        elif "Cards" in resources:
                           
                            random = randint(1,10)
                           
                            if random <= 2:
                                print(familysaved[random_family-1] + " tried playing the game but didn't understand Cards. She killed herself out of confusion")
                                del familysaved[random_family-1]
                            elif random <= 8:
                                print(familysaved[random_family-1] + " really liked the game and became great at it.")
                            elif random == 9:
                                print(familysaved[random_family-1] + " got really mad when she lost to her son that she broke the game.")
                            elif random == 10:
                                print(familysaved[random_family-1] + " was apparently really huungry and she just ate the board. She did not survive that.")
                                del familysaved[random_family-1]
                                resources.remove("Cards")
                        else:
                            print("You were trying to find a game " + familysaved[random_family-1] + " could play, but you couldn't. She killed herself")
                            del familysaved[random_family-1]
                    elif int(choice) == 2:
                        random = randint(1,10)
                       
                        if random <= 4:
                            print("You sand a lullaby and she went to sleep")
                        else:
                            print("She whacked your daughter as she was trying to sleep and killed her")
                            familysaved.remove("Mary Jane (Daughter)")
                    elif int(choice) == 3:
                        print("She killed herself.")
                        del familysaved[random_family-1]
                       
                       


                           
                           
                       
        if force_break_loop:
            break
        else:
            days_passed += 1


        normal_diary.clear()
       
    if days_passed == 30:
        print("Congratulations, you won the game!")          
    else:
        print("Your entire family died. You have lost")



