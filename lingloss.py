import argparse

class Lingloss:
    """Class representing linguistic glosses."""

    def __init__(self, original_words, gloss_words, free_translation, 
            original_sentence='', listsGiven=False):
        """
        Args: 
            original_words: an array of words
            gloss_words: a list of words, glossing the original words
            free_translation: a string that freely translates the original
                sentence
            orginal_sentence: optional, the original sentence possibly rendered
                in its native orthography
            listsGiven: specifies whether arguments are given as strings which
                must be parsed as lists or if they are already given as lists.
        """

        if not listsGiven:
            self.original_words = original_words.split()
            self.gloss_words = gloss_words.split()
        else:
            self.original_words = original_words
            self.gloss_words = gloss_words

        if len(self.original_words) != len(self.gloss_words):
            raise ValueError("Lengths or original words (1st argument) and \
                glossed words (2nd argument) must be equal")

        self.free_translation = free_translation
        self.original_sentence = original_sentence

    def getHTML(self):
        """ Since what I'm doing here is pretty simple (so far), I'll just write
        HTML directly. Using some more sophisticated library may be a good idea
        for adding more sophisticated features.
        """
        return """<table>
    <tr>""" + ''.join(map((lambda x: "<td>{}</td>".format(x)), 
            self.original_words)) \
            + """</tr>
    <tr>""" + ''.join(map((lambda x: "<td>{}</td>".format(x)), 
            self.gloss_words)) \
            + """</tr>
    <tr><td colspan=""" + str(len(self.original_words)) \
        + ">" + self.free_translation + """</td></tr>
</table>"""


if __name__ == '__main__':
    pass
