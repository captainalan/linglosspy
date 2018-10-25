import unittest
from lingloss import Lingloss


"""Test inputs"""
# Inputs as lists
a = Lingloss(['hola', 'amigos', 'mios'],
             ['hello', 'friends', '1SG-GEN'],
             "Hello, my friends!", listsGiven=True)

# Inputs as strings
b = Lingloss("tomodachi he konnichiwa", "friends toward hello", 
        "Hello, my friends")

# Non-ASCII input
c = Lingloss("你好 网友 好久不见", "hello internet-friends long-time-no-see",
        "Greetings netizens; it's been a while")


"""Unit tests"""
class TestLinglossMethods(unittest.TestCase):

    def testListsGivenTrue(self):
        self.assertEqual(a.getHTML(),"""<table>
    <tr><td>hola</td><td>amigos</td><td>mios</td></tr>
    <tr><td>hello</td><td>friends</td><td>1SG-GEN</td></tr>
    <tr><td colspan=3>Hello, my friends!</td></tr>
</table>""")

    def testListsGivenFalse(self):
        self.assertEqual(b.getHTML(),"""<table>
    <tr><td>tomodachi</td><td>he</td><td>konnichiwa</td></tr>
    <tr><td>friends</td><td>toward</td><td>hello</td></tr>
    <tr><td colspan=3>Hello, my friends</td></tr>
</table>""")

    def testNonASCII(self):
        self.assertEqual(c.getHTML(),"""<table>
    <tr><td>你好</td><td>网友</td><td>好久不见</td></tr>
    <tr><td>hello</td><td>internet-friends</td><td>long-time-no-see</td></tr>
    <tr><td colspan=3>Greetings netizens; it's been a while</td></tr>
</table>""")


if __name__ == '__main__':
    unittest.main()
