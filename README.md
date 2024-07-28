# pig-latin-translator

A group of Vatican City police officers are planning a trip to Canada.
Since they only speak Pig Latin, they will need to translate a lot of English phrases. Write
a simple program to perform basic English to Pig Latin translation

Translation rules
1. Separate each word into two parts. The first part is called the prefix and
extends from the beginning of the word up to, but not including, the first
vowel. (The letter y will be considered a vowel.) The rest of the word is called
the stem.
2. The Pig Latin text is formed by reversing the order of the prefix and stem and
adding the letters ay to the end. For example, sandwich is composed of s +
andwich + ay. and would translate to andwichsay.
3. If the word begins with a vowel (AEIOUY), let the prefix be empty and the
word be the stem. The word ending should be yay instead of merely ay. For
example, I would be Iyay, and ultimate would be ultimateyay.
4. All punctuation should be preserved (only need to worry about periods,
commas, exclamation and question marks).
5. If the word begins with a capital letter, then the translated word should too.
6. Any word that does not have letters in it should not be translated (so a
number like 14, for example, should be left as it is).
