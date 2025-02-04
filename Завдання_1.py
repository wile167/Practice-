def process_string(input_str):
 vowels = "aeiouAEIOU"
 vowel_list = []
 for char in input_str:
     if char in vowels:
         vowel_list.append(char)
 sorted_vowels = sorted(vowel_list)
 vowel_str = "".join(sorted_vowels)
 vowel_count = len(vowel_str)
 
 consonant_list = []
 for char in input_str:
     if char not in vowels:
         consonant_list.append(char)
 sorted_consonants = sorted(consonant_list)
 consonant_str = "".join(sorted_consonants)
 
 return vowel_str, vowel_count, consonant_str

input_str = "abcdefg"
result = process_string(input_str)
print(f"({result[0]}, {result[1]}, {result[2]})")
