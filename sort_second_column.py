from docx import Document

def get_table_data(table):
    data = []
    for row in table.rows:
        row_data = [cell.text.strip() for cell in row.cells]
        data.append(row_data)
    return data

def sort_table_by_column(table_data, column_index):
    sorted_data = sorted(table_data, key=lambda row: row[column_index])
    return sorted_data

def find_duplicates(data, column_index):
    duplicates = []
    counts = {}
    for row in data:
        # print(row, column_index)
        cell_value = row[column_index]
        try:
            word = cell_value.split()[0]  # Assuming the first word is used for comparison

            counts[word] = counts.get(word, 0) + 1
            if counts[word] > 1:
                duplicates.append(cell_value)
        except:
            None
    return duplicates

# Load the Word document
doc = Document('wordFiles\\MainEnglish - backup 28.06.2023.docx')

# Assuming the table is the first table in the document
table = doc.tables[0]

# Extract table data
table_data = get_table_data(table)

# Sort the table by the second column (index 1)
sorted_table_data = sort_table_by_column(table_data, 1)

# Find cells where the first word repeats more than once
duplicates = find_duplicates(sorted_table_data, 1)  # Assuming the first column (index 0) contains the cells to compare

# Print the duplicate cells
for cell in duplicates:
    print(cell)

"""Arm chair -
At least [æt list]-
Back  /bæk/-
Back bone /ˈbækˌbəʊn/ - the series of vertebrae extending from the skull to the pelvis; a metaphor for strength or support.
Bed /bɛd/ -
Blood /blʌd/ - the red liquid that circulates in the arteries and veins of humans and other vertebrate animals, carrying oxygen to and carbon dioxide from the tissues of the body.
Boil /bɔɪl/- the process of liquid turning into vapor due to high temperatures;
Bone /bəʊn/ - the hard, rigid connective tissue forming the skeleton of vertebrates.
Butter  /ˈbʌtər/ - a dairy product made from cream or milk, often used as a spread or in cooking and baking.Catch the bus /kætʃ/ /ðə/ /bʌs/ - to get on a bus before it departs from a station or stop.
Chicken  /ˈtʃɪkɪn/ - a domesticated bird kept for its eggs or meat, often used in a variety of dishes.      
Cold  /kəʊld/ -
Daily /ˈdeɪli/ - occurring every day or happening once a day.
Dry  /draɪ/-
Eat local dishes  /it ˈloʊkəl ˈdɪʃɪz/ -to try or enjoy the traditional cuisine of a particular region or culture;
Expensive  /ɪkˈspɛnsɪv/ -costing a lot of money;
Fail  /feɪl/- to be unsuccessful in achieving one's goal or to fall short of expectations;
Foggy  /ˈfɒɡi/ -characterized by the presence of fog.
Full price  /fʊl praɪs/- the regular or non discounted price of a product or service;
Guess  /ɡɛs/- to form an opinion or estimate without certain knowledge;
Hang out  /hæŋ/ /aʊt/ - to spend time with someone or in a particular place, especially for social purposes.Hot  /hɒt-
I bet [aɪ bɛt] -
In front  /ɪn/ /frʌnt/-
Kind -
Oil /ɔɪl/ - A viscous liquid derived from petroleum, used as fuel, lubricant, and many other purposes.      
Polite  /pəˈlaɪt/-
Rice  /raɪs/ - a cereal grain that is a staple food in many parts of the world, often served as a side dish.Rude /ruːd/ - Rude refers to behavior that is impolite or disrespectful, while kind refers to behavior that 
is considerate and compassionate. Polite refers to behavior that is courteous and respectful.
Shelf /ʃɛlf/ - A flat, horizontal surface used for storing or displaying items.
Short /ʃɔːt/ -
Star  /stɑr/- a luminous celestial body consisting of a mass of gas held together by its own gravity;       
Sun /sʌn/ the star at the centre of the solar system;
Sun rise /sʌn raɪz/ -
Sun set  /sʌn sɛt/ -
To be afraid [tuː bi əˈfreɪd]-
To be in a mood /tuː biː ɪn ə muːd/ - This is a phrase used to describe someone who is feeling a particular 
emotion or attitude at a given moment.
To mean  /tuː miːn/ - These are phrasal verbs used to indicate the intention of someone's words or actions, 
or to describe someone who is unkind or unpleasant.
Together  /təˈɡɛðər/- in company or in association with others;
Twenty five-
Twenty four-
Twenty nine-
Twenty one-
Twenty seven-
Twenty six-
Twenty three-
Twenty two-
Vegetables / fruits  /ˈvɛdʒtəbəlz/ /fruːts/ - Vegetables are plants that are consumed as food and fruits are the sweet and fleshy product of a tree or other plant that contains seed and can be eaten as food.
Warm -
Weak / strong /wiːk / strɒŋ/ - lacking in strength or power / having or showing great strength or power;    
Wet  /wɛt/ - Covered or saturated with water or another liquid.
always -
answer /ˈænsər/ ,  answered-
any  -
around  -
aunt -
aunt [ænt] -
believe /bəˈliv/ ,  believed-
brother -
busy [ˈbɪzi] -
buy /baɪ/ ,  bought-
can I -
change /tʃeɪndʒ/ ,  changed-
course  -
create /kriˈeɪt/ ,  created-
daughter -
day  -
day  [deɪ] -
done  -
eight thousand-
enough  -
ever  -
every -
everybody  [ˈɛvrɪˌbɑdi] -
everything -
expect /ɪkˈspɛkt/ ,  expected-
expect [ɪkˈspɛkt] -
false /fɔːls/ -
father, dad  -
fine  -
first -
five thousand-
follow /ˈfɑloʊ/ ,  followed-
four thousand-
god  -
goodbye [ɡʊdˈbaɪ] -
granddaughter -
grandfather -
grandmother -
grandson -
great  -
grow /ɡroʊ/ ,  grew-
guy, guys  -
hear /hɪr/ ,  heard-
hell  [hɛl] -
hello  -
help  -
help /hɛlp/ ,  helped-
his, her, its  [hɪz, hɜr, ɪts] -
if  [ɪf] -
imagine [ɪˈmæʤɪn] -
into  -
it sounds [ɪt saʊndz] -
last  -
later /ˈleɪtər/ -
lead /lid/ ,  led-
learn /lɜrn/ ,  learned-
learn /lɜrn/ ,  learned-
leave  -
leave /liv/ ,  left-
left  -
life  -
like /laɪk/ ,  liked-
little  -
love  -
love /lʌv/ ,  loved-
man, men  [mæn, mɛn] -
may I  -
meet /mit/ ,  met-
might  -
money  -
mother, mum -
mr.  -
must  -
name  -
never  -
new  -
night -
night -
nine thousand-
nobody [ˈnoʊˌbɒdi] -
not ready  [nɑt ˈrɛdi] -
nothing  -
off  -
old -
one thousand-
only  -
other  -
our -
out -
over  -
paid [peɪd] -
people  -
pick /pɪk/ ,  picked-
place  -
please  -
right -
right -
right -
right -
run /rʌn/ ,  ran-
serious, seriously [ˈsɪəriəs] -
seven thousand-
sir  -
sister -
sister -
six thousand-
someone  -
someone -
something -
something -
son -
sorry  -
speak /spik/ ,  spoke-
start /stɑrt/ ,  started-
still  -
sure  -
thank  -
their -
this -
three thousand-
to sort  [tuː sɔrt] -
today  -
tomorrow -
train [treɪn] -
train station [treɪn ˈsteɪʃən] -
two thousand-
uncle -
uncle [ˈʌŋkl̩] -
under -
wait  -
wait /weɪt/ ,  waited-
want /wɑnt/ ,  wanted-
woman, women -
world  -
wrong  -
yesterday -
you are -"""
