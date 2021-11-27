import csv
from prettytable import PrettyTable

ASCIIART = """::::::::::: ::::::::  :::::::::   ::::::::        ::::::::  :::    ::: :::::::::: :::::::: ::::::::::: 
    :+:    :+:    :+: :+:    :+: :+:    :+:      :+:    :+: :+:    :+: :+:       :+:    :+:    :+:     
    +:+    +:+    +:+ +:+    +:+ +:+    +:+      +:+    +:+ +:+    +:+ +:+       +:+           +:+     
    +#+    +#+    +:+ +#+    +:+ +#+    +:+      +#+    +:+ +#+    +:+ +#++:++#  +#++:++#++    +#+     
    +#+    +#+    +#+ +#+    +#+ +#+    +#+      +#+  # +#+ +#+    +#+ +#+              +#+    +#+     
    #+#    #+#    #+# #+#    #+# #+#    #+#      #+#   +#+  #+#    #+# #+#       #+#    #+#    #+#     
    ###     ########  #########   ########        ###### ### ########  ########## ########     ###     """
SEPERATOR = "-------------------------------------------------------------------------------------------------------"
TICK = '\u2713'
CROSS = '\u2717'

def format_output(output):

    if output == 'in progress':
        output = CROSS
    elif output == 'completed':
        output = TICK
    else:
        pass

    return(output)

def dailies_function():
    """Test"""
    dailies_table = PrettyTable()
    dailies_table.field_names = ["Daily Quest", "Status"]

    with open("/home/benja/development/python/todoquest/quests/dailies.csv") as dailies_csv:
        data = list(csv.reader(dailies_csv))
        for line in data:
            progress = line[1]
            text = line[0]
            
            progress = format_output(progress)
            dailies_table.add_row([text, progress])
    
    print(dailies_table)

def challenges():
    
    challenges_table = PrettyTable()
    challenges_table.field_names = ["Challenge", "Status"]

    with open("/home/benja/development/python/todoquest/quests/challenges.csv") as challenges_csv:
        data = list(csv.reader(challenges_csv))
        for line in data:
            progress = line[1]
            text = line[0]
                        
            progress = format_output(progress)
            challenges_table.add_row([text, progress])

    print(challenges_table)

def long_goals():
    
    long_goals_table = PrettyTable()
    long_goals_table.field_names = ["Long Goals", "Status"]
    with open("/home/benja/development/python/todoquest/quests/long_goals.csv") as long_goals_csv:
        data = list(csv.reader(long_goals_csv))
        for line in data:
            progress = line[1]
            text = line[0]
                        
            progress = format_output(progress)
            long_goals_table.add_row([text, progress])
    
    print(long_goals_table)

print(SEPERATOR)
print(ASCIIART)
print(SEPERATOR)
dailies_function()
challenges()
long_goals()
