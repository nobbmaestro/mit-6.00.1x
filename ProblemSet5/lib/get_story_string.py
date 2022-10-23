"""GetStoryString."""


# pylint: disable="C0103"
def get_story_string():
    """Return a joke in encrypted text."""
    f = open("ProblemSet5/lib/story.txt", "r")
    story = str(f.read())
    f.close()
    return story
