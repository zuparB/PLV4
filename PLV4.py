# MIT License
# 
# Copyright (c) 2025 zuparb
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

irregular = {"child": "children",
             "bus": "buses",
             "shrimp": "shrimp",
             "fish": "fish",
             "mouse": "mice",
             "man": "men",
             "woman": "women",
             "deer": "deer",
             "species": "species",
             "person": "people",
             "knife": "knives",
             "sheep": "sheep",
             "ox": "oxen",
             "moose": "moose",
             "virus": "viruses",
             "giraffe": "giraffes",
             "chief": "chiefs",
             "roof": "roofs",
             "photo": "photos",
             "piano": "pianos",
             "manatee": "manatees",
             "human": "humans",
             "goose": "geese",
             "tooth": "teeth",
             "mantis": "mantises",
             "reef": "reefs",
             "die": "dice",
             "index": "indeces",
             "chef": "chefs",
             "soprano": "sopranos",
             "cello": "cellos",
             "dynamo": "dynamos",
             "kilo": "kilos",
             "auto": "autos",
             "avocado": "avocados",
             "video": "videos",
             "studio": "studios",
             "concerto": "concertos",
             "radio": "radios",
             "quiz": "quizzes",
             "trout": "trout",
             "salmon": "salmon",
             "series": "series",
             "cod": "cod",
             "pro": "pros",
             "rice": "rice",
             "louse": "lice", # Offtopic who knew this?? The animal that eats your dandruff isnt a lice its a god damn louse??
             "banana": "bananas",
             "drama": "dramas",
             "umbrella": "umbrellas",
             "zebra": "zebras",
             "iron": "irons",
             "spoon": "spoons",
             "drum": "drums",
             "wagon": "wagons",
             "mix": "mixes",
             "lexix": "lexicon",
             "scissors": "scissor",
             "dragon": "dragons",
             "lion": "lions",
             "pizza": "pizzas",
             "camera": "cameras",
             "gondola": "gondolas",
             "saga": "sagas",
             "manual": "manuals",
             "plaza": "plazas",
             "pizza": "pizzas",
             "idea": "ideas"}

us_to_i = {
    "alumnus",    # alumni
    "bacillus",   # bacilli
    "cactus",     # cacti
    "focus",      # foci
    "fungus",     # fungi
    "locus",      # loci
    "nucleus",    # nuclei
    "radius",     # radii
    "stimulus",   # stimuli
    "syllabus",   # syllabi
    "terminus",   # termini
    "uterus",     # uteri
    "octopus",     # octopi (octopuses is also valid but come on i dont need more special cases man)
    "apparatus"
}
vowels = {"a", "e", "i", "o", "u"}
consonants = {"b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"}

def makepl(word):
    word = word.lower()  
    plural = word + "s"
    
    if word in irregular:  
        plural = irregular[word]
    elif word.endswith(("oo", "ff")):
        plural = word + "s"
    elif word in us_to_i:
        plural = word[:-2] + "i"
    elif word.endswith("y") and word[-2] in consonants:
        plural = word[:-1] + "ies"
    elif word.endswith(("is")):
        plural = word[:-2] + "es"
    elif word.endswith(("ix", "ex")):
        plural = word[:-2] +"ices"
    elif word.endswith(("sh","o","ch", "x", "z")):
        plural = word + "es"
    elif word.endswith("fe"):
        plural = word[:-2] + "ves"
    elif word.endswith("f"):
        plural = word[:-1] + "ves"
    elif word.endswith("a"):
        plural = word + "e"
    elif word.endswith("s"):
        plural = word + "es"
    elif "woman" in word :
        plural = word.replace("woman", "women")
    elif "man" in word[:-3]:
        plural = word + "es"
    elif "man" in word :
        plural = word.replace("man", "men")
    elif word.endswith(("tion", "mon", "ion")):
        plural = word + "s"
    elif word.endswith(("um", "on")):
        plural = word[:-2] + "a"
    return plural
             
while True:
    print("Use singular form.. (V4 model)")
    wish = input("Please enter the word(s) you wish to pluralize: ").split()
    
    if wish and wish[0].lower() == "quit":
        break
    
    plural_form = [makepl(word) for word in wish]
    print("Pluralized word(s):", " ".join(plural_form))
    print(" ")
    
#CHECK OUT MY GITHUB: zuparB :)