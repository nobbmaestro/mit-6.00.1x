# Problem Set 5, Problem 4 - Decrypt a Story
#
# For this problem, the graders will use our implementation of the Message, PlaintextMessage, and CiphertextMessage classes, 
# so don't worry if you did not get the previous parts correct.
#
# Now that you have all the pieces to the puzzle, please use them to decode the file story.txt. The file ps6.py contains a 
# helper function get_story_string() that returns the encrypted version of the story as a string. Create a CiphertextMessage 
# object using the story string and use decrypt_message to return the appropriate shift value and unencrypted story string.
#
# Paste your function decrypt_story() in the box below.

from ProblemSet5 import get_story_string, CiphertextMessage

def decrypt_story(story_text = get_story_string()):
    return CiphertextMessage(story_text).decrypt_message()

def main():
    msg = "Story decrypted at shift: {shift} \n\nThe story is: {story}"
    result = decrypt_story()
    print(msg.format(shift=result[0], story=result[1]))

if __name__ == '__main__':
    main()