''' Anagram Problem '''

def checkAnagram(word1, word2):
    if len(word1) != len(word2): # if words are diff lengths, we know they can't be anagrams
        print(word1, " & ", word2, "These two words are not of matching length!")
    # check each letter
    foundMatch = 0    
    for letter in word1:
        for letter2 in word2:
             if letter2 == letter:
                foundMatch = foundMatch + 1
                break
    if foundMatch == len(word1):
         print(word1, " & ", word2, "These two words are an anagram!")
    else:
        print(word1, " & ", word2, "These two words are not an anagram!")
        
checkAnagram("undertale", "deltarune")
checkAnagram("table", "bleat")
checkAnagram("eat", "tea")
checkAnagram("table", "tbajk")
checkAnagram("race", "care")
