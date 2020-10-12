text_from_user = input("Please type/paste your text here: ")
vowels_lower_case = 0
vowels_upper_case = 0
consonants_lower_case = 0
consonants_upper_case = 0
romanian_diacritics_lower_case = 0
romanian_diacritics_upper_case = 0
punctuation_marks = 0
special_characters = 0
_empty_space = 0
_numbers = 0

for every_character in text_from_user:
	if every_character=="a" or every_character=="e" or every_character=="i" or every_character=="o" or every_character=="u":
		vowels_lower_case += 1
	elif every_character=="A" or every_character=="E" or every_character=="I" or every_character=="O" or every_character=="U":
		vowels_upper_case += 1
	elif every_character=="b" or every_character=="c" or every_character=="d" or every_character=="f" or every_character=="g" or every_character=="h" or every_character=="j" or every_character=="k" or every_character=="l" or every_character=="m" or every_character=="n" or every_character=="p" or every_character=="q" or every_character=="r" or every_character=="s" or every_character=="t" or every_character=="v" or every_character=="w" or every_character=="x" or every_character=="y" or every_character=="z":
		consonants_lower_case += 1
	elif every_character=="B" or every_character=="C" or every_character=="D" or every_character=="F" or every_character=="G" or every_character=="H" or every_character=="J" or every_character=="K" or every_character=="L" or every_character=="M" or every_character=="N" or every_character=="P" or every_character=="Q" or every_character=="R" or every_character=="S" or every_character=="T" or every_character=="V" or every_character=="W" or every_character=="X" or every_character=="Y" or every_character=="Z":
		consonants_upper_case += 1
	elif every_character=="ă" or every_character=="î" or every_character=="ș" or every_character=="ț"  or every_character=="â":
		romanian_diacritics_lower_case += 1
	elif every_character=="Ă" or every_character=="Î" or every_character=="Ș" or every_character=="Ț" or every_character=="Â":
		romanian_diacritics_upper_case += 1
	elif every_character=="\'" or every_character=="\"" or every_character==";" or every_character==":" or every_character=="," or every_character=="." or every_character=="/" or every_character=="?" or every_character=="!" or every_character=="-":
		punctuation_marks += 1
	elif every_character=="\\" or every_character=="|" or every_character=="<" or every_character==">" or every_character=="[" or every_character=="]" or every_character=="{" or every_character=="}" or every_character=="~" or every_character=="!" or every_character=="@" or every_character=="#" or every_character=="$" or every_character=="%" or every_character=="^" or every_character=="&" or every_character=="*" or every_character=="(" or every_character==")" or every_character=="_" or every_character=="+" or every_character=="=" or ((every_character>=chr(128) and every_character<=chr(254))):
		special_characters += 1 																																																																																																																															#ASCII CHARACTER NOTATION FROM 128 - 255
	elif every_character==" ":
		_empty_space += 1
	elif str(every_character<=chr(48)) and str(every_character<=chr(57)):
		_numbers += 1
total_number_of_vowels = vowels_lower_case + vowels_upper_case
total_number_of_consonants = consonants_lower_case + consonants_upper_case
total_number_of_romanian_diacritics = romanian_diacritics_lower_case + romanian_diacritics_upper_case
total_number_of_special_characters_spaces_and_punctuation_marks = punctuation_marks + special_characters + _empty_space
length_of_text = len(text_from_user)

print(f"\t\t\t\n SUMMARY ")
print(f"Number of vowels in lowercase: {vowels_lower_case} ")
print(f"Number of vowels in uppercase: {vowels_upper_case} ")
print(f"Number of consonants in lowercase: {consonants_lower_case} ")
print(f"Number of consonants in uppercase: {consonants_upper_case} ")
print(f"Number of romanian diacritics in lowercase: {romanian_diacritics_lower_case} ")
print(f"Number of romanian diacritics in uppercase: {romanian_diacritics_upper_case} ")
print(f"Number of punctuation marks: {punctuation_marks} ")
print(f"Number of empty spaces: {_empty_space} ")
print(f"Number of special characters: {special_characters} ")
print(f"\n\nThe total number of vowels: {total_number_of_vowels} ")
print(f"The total number of consonants: {total_number_of_consonants}")
print(f"The total number of romanian diacritics: {total_number_of_romanian_diacritics}")
print(f"The total number of special characters, punctuation marks and empty spaces: {total_number_of_special_characters_spaces_and_punctuation_marks}")
print(f"The total number of numerals: {_numbers}")
print(f"The total number of characters in text: {length_of_text}")

