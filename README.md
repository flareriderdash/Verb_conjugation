# Verb_conjugation
The script written in python uses cPickle to access and store python dictonaries for conjugation tables for french or spanish
or what ever other latin language(I havent tested it on languages other than ones that are based off of latin and I dont plan to)

To use the script just do a chmod 755 on the two scripts (addtable.py and verb_conjugations.py) then run addtable.py with the infinitive
and conjugation tables in the order of (i,you(informal),he/she or you,we,you(formal),they) and then the english at the end with quotes

Ex. ./addtable leer leo lees lee leemos leeis leen "To Read"
This will add a table like the one below to the pickle file

                leer
             yo         leo
             tu         lees
     el/ella/UD         lee
       nosotros         leemos
       vosotros         leeis
ellos/ellas/Uds         leen

And at the same time will add to the .Words file 

leer    English: To Read

so when you run ./verb_conjugations.py 
you will see this output below telling the opitons
(I've added more so you can see my point)

Avalible Searches

gustar		English: to like
beber		  English: to drink
disculpar	English: Excuse Me
leer		  English: to read
escribir	English: To Write
hablar		English: To Speak/To Talk
ser		    English: To Be
comer		  English: To Eat
hacer		  English: To Do,To Make

If you run ./verb_conjugations.py gustar it will give you the 
congjugation table for that infinative

                gustar
             yo         gusto
             tu         gustas
     el/ella/UD         gusta
       nosotros         gustamos
       vosotros         gustais
ellos/ellas/Uds         gustan

Now if you put in a word wrong or screw up the order of the conjugations you can run addtable.py --remove-key ${word}
it will remove the word and its table from the pickle file and remove the word frome the .Word file keeping accurate 
records

There are some spanish words all ready in the files ready for you to test the program for yourself
