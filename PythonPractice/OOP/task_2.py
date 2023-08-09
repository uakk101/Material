def count_vowels(sentence): 
    vowels = "aeiouAEIOU"
    vowel_count = 0

    for char in sentence:
        if char in vowels:
            vowel_count +=1

    return vowel_count


user_sentence = input("Enter a sentence: ")
vowel_count = count_vowels(user_sentence) # usman
print("Total number of vowels in the sentence:", vowel_count)




# def main():
    

# if __name__ == "__main__":
#     main()
