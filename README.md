# Linglosspy

This Python program produces linguistic glosses in the form of HTML tables.

Before creating this program, I used to use monospace fonts to give linguistic
examples like this (Japanese to English):

    Kare  wa     ningen  desu
    He    TOPIC  human   COPULA
    "He is a human"

This program provides a function to produce tables like this: 

<table>
    <tr><td>kare</td><td>wa</td><td>ningen</td><td>desu</td></tr>
    <tr><td>He</td><td>TOPIC</td><td>human</td><td>COPULA</td></tr>
    <tr><td colspan=4>He is a human</td></tr>
</table>

...which you can style using CSS, embed in your webpages, etc.

## Usage

This program was made using `pipenv`. To install dependencies from Pipfile, do:

```
$ pipenv install
```

Then, start the virtual environment:

```
$ pipenv shell
```

Example usage (Japanese to English):

```bash
$ python -i __init__.py
```

```python
>>> my_sentence = Lingloss("tanoshimi no moto", "fun GEN source", "source of fun")
>>> print(my_sentence.getHTML())
<table>
    <tr><td>tanoshimi</td><td>no</td><td>moto</td></tr>
    <tr><td>fun</td><td>GEN</td><td>source</td></tr>
    <tr><td colspan=3>source of fun</td></tr>
</table>
```


## Other Notes

Roughly, I'm following the guidelines of 
[Structuring Your Project](https://docs.python-guide.org/writing/structure/)
to set up this project. 

