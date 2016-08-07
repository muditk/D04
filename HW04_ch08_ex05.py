# Structure this script entirely on your own.
# See Chapter 8: Strings Exercise 5 for the task.
# Please do provide function calls that test/demonstrate your
# function.

def rotate_word(word, count):
    new_word = ""
    for n in word:
        new_word = ord(n) + count
    return new_word
    print(new_word)

rotate_word('macbook', 2)
    