# questions.py
# Question bank for the quiz game

quiz_data = {
    "Math": [
        {
            "question": "What is 5 + 7?",
            "options": {"a": "10", "b": "11", "c": "12", "d": "13"},
            "correct": "c",
            "explanation": "5 + 7 equals 12."
        },
        {
            "question": "What is the square root of 16?",
            "options": {"a": "2", "b": "4", "c": "6", "d": "8"},
            "correct": "b",
            "explanation": "The square root of 16 is 4 because 4 * 4 = 16."
        },
        {
            "question": "What is 9 multiplied by 8?",
            "options": {"a": "64", "b": "72", "c": "81", "d": "90"},
            "correct": "b",
            "explanation": "9 * 8 equals 72."
        },
        {
            "question": "What is 15 divided by 3?",
            "options": {"a": "3", "b": "4", "c": "5", "d": "6"},
            "correct": "c",
            "explanation": "15 divided by 3 is 5."
        },
        {
            "question": "What is 2 raised to the power of 5?",
            "options": {"a": "16", "b": "32", "c": "64", "d": "128"},
            "correct": "b",
            "explanation": "2^5 = 2 * 2 * 2 * 2 * 2 = 32."
        },
        {
            "question": "What is the value of π (pi) to two decimal places?",
            "options": {"a": "3.12", "b": "3.14", "c": "3.16", "d": "3.18"},
            "correct": "b",
            "explanation": "The value of π is approximately 3.14."
        },
        {
            "question": "What is 100 minus 37?",
            "options": {"a": "63", "b": "64", "c": "65", "d": "66"},
            "correct": "a",
            "explanation": "100 - 37 equals 63."
        },
        {
            "question": "What is the cube of 3?",
            "options": {"a": "9", "b": "18", "c": "27", "d": "36"},
            "correct": "c",
            "explanation": "3^3 = 3 * 3 * 3 = 27."
        },
        {
            "question": "What is 25% of 80?",
            "options": {"a": "15", "b": "20", "c": "25", "d": "30"},
            "correct": "b",
            "explanation": "25% of 80 is (25/100) * 80 = 20."
        },
        {
            "question": "What is the sum of angles in a triangle?",
            "options": {"a": "90°", "b": "180°", "c": "270°", "d": "360°"},
            "correct": "b",
            "explanation": "The sum of angles in a triangle is always 180°."
        },
        {
            "question": "What is 12 squared?",
            "options": {"a": "124", "b": "134", "c": "144", "d": "154"},
            "correct": "c",
            "explanation": "12^2 = 12 * 12 = 144."
        },
        {
            "question": "What is 7 times 6?",
            "options": {"a": "36", "b": "42", "c": "48", "d": "54"},
            "correct": "b",
            "explanation": "7 * 6 equals 42."
        },
        {
            "question": "What is the value of 10 factorial (10!)?",
            "options": {"a": "3,600", "b": "36,000", "c": "362,880", "d": "3,628,800"},
            "correct": "c",
            "explanation": "10! = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 = 362,880."
        }
    ],
    "Science": [
        {
            "question": "What gas do plants primarily use for photosynthesis?",
            "options": {"a": "Oxygen", "b": "Nitrogen", "c": "Carbon Dioxide", "d": "Hydrogen"},
            "correct": "c",
            "explanation": "Plants use Carbon Dioxide (CO2) during photosynthesis to produce glucose."
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": {"a": "H2O", "b": "CO2", "c": "O2", "d": "H2SO4"},
            "correct": "a",
            "explanation": "Water is represented by the chemical formula H2O."
        },
        {
            "question": "What planet is known as the Red Planet?",
            "options": {"a": "Venus", "b": "Mars", "c": "Jupiter", "d": "Saturn"},
            "correct": "b",
            "explanation": "Mars is called the Red Planet due to its reddish appearance from iron oxide (rust) on its surface."
        },
        {
            "question": "What is the primary source of energy for Earth?",
            "options": {"a": "The Moon", "b": "The Sun", "c": "Geothermal Heat", "d": "Wind"},
            "correct": "b",
            "explanation": "The Sun provides the primary energy for Earth through sunlight."
        },
        {
            "question": "What gas makes up most of Earth’s atmosphere?",
            "options": {"a": "Oxygen", "b": "Nitrogen", "c": "Carbon Dioxide", "d": "Argon"},
            "correct": "b",
            "explanation": "Nitrogen constitutes about 78% of Earth’s atmosphere."
        },
        {
            "question": "What is the boiling point of water in Celsius?",
            "options": {"a": "50°C", "b": "75°C", "c": "100°C", "d": "150°C"},
            "correct": "c",
            "explanation": "Water boils at 100°C at standard atmospheric pressure."
        },
        {
            "question": "What element is represented by the symbol Fe?",
            "options": {"a": "Fluorine", "b": "Iron", "c": "Francium", "d": "Fermium"},
            "correct": "b",
            "explanation": "Fe is the chemical symbol for Iron."
        },
        {
            "question": "What force keeps planets in orbit around the Sun?",
            "options": {"a": "Magnetism", "b": "Friction", "c": "Gravity", "d": "Tension"},
            "correct": "c",
            "explanation": "Gravity is the force that keeps planets in orbit around the Sun."
        },
        {
            "question": "What is the largest organ in the human body?",
            "options": {"a": "Liver", "b": "Brain", "c": "Skin", "d": "Heart"},
            "correct": "c",
            "explanation": "The skin is the largest organ in the human body by surface area and weight."
        },
        {
            "question": "What type of energy is stored in food?",
            "options": {"a": "Kinetic", "b": "Thermal", "c": "Chemical", "d": "Nuclear"},
            "correct": "c",
            "explanation": "Food stores chemical energy, which the body converts into usable energy."
        },
        {
            "question": "What gas do humans exhale?",
            "options": {"a": "Oxygen", "b": "Nitrogen", "c": "Carbon Dioxide", "d": "Helium"},
            "correct": "c",
            "explanation": "Humans exhale Carbon Dioxide as a byproduct of respiration."
        },
        {
            "question": "What is the hardest natural substance known?",
            "options": {"a": "Gold", "b": "Iron", "c": "Diamond", "d": "Quartz"},
            "correct": "c",
            "explanation": "Diamond is the hardest naturally occurring substance, rated 10 on the Mohs scale."
        }
    ],
    "History": [
        {
            "question": "In which year did World War II end?",
            "options": {"a": "1943", "b": "1944", "c": "1945", "d": "1946"},
            "correct": "c",
            "explanation": "World War II ended in 1945 with the surrender of Japan."
        },
        {
            "question": "Who was the first President of the United States?",
            "options": {"a": "Thomas Jefferson", "b": "George Washington", "c": "Abraham Lincoln", "d": "John Adams"},
            "correct": "b",
            "explanation": "George Washington was the first U.S. President, serving from 1789 to 1797."
        },
        {
            "question": "What ancient civilization built the pyramids of Giza?",
            "options": {"a": "Romans", "b": "Greeks", "c": "Egyptians", "d": "Mesopotamians"},
            "correct": "c",
            "explanation": "The ancient Egyptians built the pyramids of Giza around 2630 BCE."
        },
        {
            "question": "In which year did the Titanic sink?",
            "options": {"a": "1910", "b": "1912", "c": "1914", "d": "1916"},
            "correct": "b",
            "explanation": "The Titanic sank on April 15, 1912, after hitting an iceberg."
        },
        {
            "question": "Who discovered America in 1492?",
            "options": {"a": "Vasco da Gama", "b": "Christopher Columbus", "c": "Ferdinand Magellan", "d": "Marco Polo"},
            "correct": "b",
            "explanation": "Christopher Columbus reached America in 1492, though he thought it was Asia."
        },
        {
            "question": "What wall was built to keep out invaders in ancient China?",
            "options": {"a": "Berlin Wall", "b": "Hadrian’s Wall", "c": "Great Wall", "d": "Wall of Jericho"},
            "correct": "c",
            "explanation": "The Great Wall of China was built to protect against invaders."
        },
        {
            "question": "In which year did the French Revolution begin?",
            "options": {"a": "1776", "b": "1789", "c": "1804", "d": "1815"},
            "correct": "b",
            "explanation": "The French Revolution began in 1789 with the storming of the Bastille."
        },
        {
            "question": "Who was the leader of Nazi Germany during World War II?",
            "options": {"a": "Benito Mussolini", "b": "Adolf Hitler", "c": "Joseph Stalin", "d": "Winston Churchill"},
            "correct": "b",
            "explanation": "Adolf Hitler was the leader of Nazi Germany from 1933 to 1945."
        },
        {
            "question": "What empire was ruled by Julius Caesar?",
            "options": {"a": "Greek Empire", "b": "Roman Empire", "c": "Ottoman Empire", "d": "Byzantine Empire"},
            "correct": "b",
            "explanation": "Julius Caesar was a key figure in the Roman Empire."
        },
        {
            "question": "In which year did humans first land on the Moon?",
            "options": {"a": "1965", "b": "1967", "c": "1969", "d": "1971"},
            "correct": "c",
            "explanation": "Humans first landed on the Moon on July 20, 1969, during NASA’s Apollo 11 mission."
        },
        {
            "question": "What war was fought between the North and South in the U.S.?",
            "options": {"a": "Revolutionary War", "b": "Civil War", "c": "World War I", "d": "Vietnam War"},
            "correct": "b",
            "explanation": "The U.S. Civil War was fought between the northern and southern states from 1861 to 1865."
        },
        {
            "question": "Who was the first woman to fly solo across the Atlantic?",
            "options": {"a": "Amelia Earhart", "b": "Bessie Coleman", "c": "Harriet Quimby", "d": "Jacqueline Cochran"},
            "correct": "a",
            "explanation": "Amelia Earhart completed the first solo transatlantic flight by a woman in 1932."
        },
        {
            "question": "What ancient city was destroyed by a volcanic eruption in 79 CE?",
            "options": {"a": "Athens", "b": "Rome", "c": "Pompeii", "d": "Carthage"},
            "correct": "c",
            "explanation": "Pompeii was buried by the eruption of Mount Vesuvius in 79 CE."
        }
    ],
    "Geography": [
        {
            "question": "What is the capital of Brazil?",
            "options": {"a": "Rio de Janeiro", "b": "São Paulo", "c": "Brasília", "d": "Salvador"},
            "correct": "c",
            "explanation": "Brasília is the capital city of Brazil, designed specifically for that purpose."
        },
        {
            "question": "Which continent is the largest by land area?",
            "options": {"a": "Africa", "b": "Asia", "c": "Australia", "d": "Europe"},
            "correct": "b",
            "explanation": "Asia is the largest continent, covering about 44.58 million square kilometers."
        },
        {
            "question": "What is the longest river in the world?",
            "options": {"a": "Amazon", "b": "Nile", "c": "Yangtze", "d": "Mississippi"},
            "correct": "b",
            "explanation": "The Nile River is the longest, stretching over 6,650 kilometers."
        },
        {
            "question": "What mountain is the tallest in the world?",
            "options": {"a": "K2", "b": "Kangchenjunga", "c": "Everest", "d": "Lhotse"},
            "correct": "c",
            "explanation": "Mount Everest is the tallest mountain, standing at 8,848 meters."
        },
        {
            "question": "Which country has the most deserts?",
            "options": {"a": "Australia", "b": "Antarctica", "c": "Saudi Arabia", "d": "Egypt"},
            "correct": "b",
            "explanation": "Antarctica is classified as a cold desert, making it the continent with the most desert coverage by area."
        },
        {
            "question": "What is the smallest country in the world by land area?",
            "options": {"a": "Monaco", "b": "Vatican City", "c": "Liechtenstein", "d": "San Marino"},
            "correct": "b",
            "explanation": "Vatican City is the smallest country, with an area of about 44 hectares."
        },
        {
            "question": "Which ocean is the largest?",
            "options": {"a": "Atlantic", "b": "Indian", "c": "Arctic", "d": "Pacific"},
            "correct": "d",
            "explanation": "The Pacific Ocean is the largest, covering about 155.6 million square kilometers."
        },
        {
            "question": "What country is home to the Great Barrier Reef?",
            "options": {"a": "Brazil", "b": "Australia", "c": "Indonesia", "d": "Philippines"},
            "correct": "b",
            "explanation": "The Great Barrier Reef is located off the coast of Queensland, Australia."
        },
        {
            "question": "What is the capital of Japan?",
            "options": {"a": "Kyoto", "b": "Osaka", "c": "Tokyo", "d": "Hiroshima"},
            "correct": "c",
            "explanation": "Tokyo is the capital city of Japan."
        },
        {
            "question": "Which country has the most population?",
            "options": {"a": "India", "b": "China", "c": "United States", "d": "Indonesia"},
            "correct": "a",
            "explanation": "As of recent data, India has surpassed China to become the most populous country."
        },
        {
            "question": "What desert is the largest in the world?",
            "options": {"a": "Sahara", "b": "Gobi", "c": "Antarctic Desert", "d": "Kalahari"},
            "correct": "c",
            "explanation": "The Antarctic Desert is the largest desert by area, covering about 14 million square kilometers."
        },
        {
            "question": "Which river flows through Paris?",
            "options": {"a": "Thames", "b": "Seine", "c": "Danube", "d": "Rhine"},
            "correct": "b",
            "explanation": "The Seine River runs through the heart of Paris, France."
        }
    ]
}