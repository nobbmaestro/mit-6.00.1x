def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("ProblemSet5/lib/given_data/story.txt", "r")
    story = str(f.read())
    f.close()
    return story