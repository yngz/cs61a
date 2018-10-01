# All cards available in a standard deck.
from classes import *

# TAs

albert = TACard('Albert, Lethargy Incarnate', 1000, 2000)
alex = TACard('President Lieutenant Stennet for Senate', 1400, 2000)
annie = TACard('Annie, the Annihilator of Water', 1700, 1500)
audrey = TACard('Audrey, Tree Whisperer', 2400, 1000)
brandon = TACard('The Wrong Fong ', 1000, 2300)
charles = TACard('Charles "Charles Hong" Hong', 1700, 1600)
chris_a = TACard('Chris, Caller of Men', 1800, 1600)
derek = TACard('Derek, The Wan and Only', 2000, 1000)
ellen = TACard('Ellen, Taker of Ls', 1500, 1900)
gibbes = TACard('Gibbes, Free Energy Mage', 1100, 2100)
jason = TACard('zhou.json', 1500, 1600)
jennifer = TACard('Jennifer, je pense, donc jtsui', 1500, 1900)
kartik = TACard('Karctic the Polar Bear Kapur', 2100, 1200)
kavi = TACard('Kavi Gupta', 2100, 1000)
keon = TACard('Keon, Slifer the Sky Dragon', 1100, 2300)
kevin_w = TACard('Kevin W, One of the Four', 1100, 2100)
lillian = TACard('Lillian, Linda', 1100, 2100)
nancy = TACard('Nancy, The Sheep in the Jeep', 1100, 2100)
neil = TACard('Neil Before Me', 2300, 1000)
nick = TACard('Nick, Theatrical Teeter Totter of Terror', 2300, 1100)
paul = TACard('Better Call Paul', 2100, 1200)
ryan = TACard('Ryan, Master Python Tamer', 1000, 2100)
samee = TACard('Samee the Brave', 2000, 1300)
shea = TACard('Shea Butter', 1600, 1700)
shreya = TACard('Shreya', 2100, 1300)
tim = TACard('Tim the Forester ', 1000, 2000)
yannan = TACard('Yannan, Consumer of Anthocyanin', 1500, 1900)
yichen = TACard('Yichen, Drinker of Boba', 1800, 1500)

# Tutors

aaron = TutorCard('Aaron the Baron', 2300, 1100)
abhinav = TutorCard('Abhinav, Fan of Durant', 1300, 2000)
amy = TutorCard('Amy, not a Composer', 1700, 1700)
anirvin = TutorCard('Supreme Lord of the Universe: Anirvin Sikha', 1600, 1800)
christopher_z = TutorCard('Christopher the Redeemer', 2200, 1100)
evan = TutorCard('Ev-Bot, A Lean Mean Python Machine ', 1600, 1700)
jack = TutorCard('Jack Wack aka Coyle the Boyle', 1500, 1900)
jade = TutorCard('Jade, Singher of Songs', 1700, 1500)
jemmy = TutorCard('Jemmy, The Zhou-ker', 1200, 2200)
julianna = TutorCard('Julianna, Lover of Gushers', 1000, 2400)
katherine = TutorCard('Katherine, She Who Never Liu-ses', 2300, 1100)
kevin_y = TutorCard('Kevin, The Hanzo Main', 2200, 1200)
lauren = TutorCard('Explorin\' Lauren', 1600, 1700)
lucas = TutorCard('Lucas, Mad Scientist Hououin Kyouma', 1600, 1700)
rachel = TutorCard('Rachel \'Genes of Jeans\' De Jaen', 1700, 1700)
shayna = TutorCard('Shayna, The Indecisive', 1100, 2300)
varun = TutorCard('Varun "what\'s your last name again?" Jhunjhunwalla ', 2100, 1300)

# Professors
denero = ProfessorCard('John DeNero, Protector of Abstraction Barriers', 5000, 5000)

# A standard deck contains all standard cards.
standard_cards = [albert, alex, annie, audrey, brandon, charles, chris_a, derek, ellen, gibbes, jason, jennifer, 
				  kartik, kavi, keon, kevin_w, lillian, nancy, neil, nick, paul, ryan, samee, shea, shreya, tim, 
				  yannan, yichen, aaron, abhinav, amy, anirvin, christopher_z, evan, jack, jade, jemmy, julianna, 
				  katherine, kevin_y, lauren, lucas, rachel, shayna, varun, denero]
standard_deck = Deck(standard_cards)

# The player and opponent's decks are the standard deck by default.
player_deck = standard_deck.copy()
opponent_deck = standard_deck.copy()