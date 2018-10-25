# Linglosspy

Produce linguistic glosses...

Before, I used monospace fonts to do things like this:

    Kare  wa     ningen  desu
    He    TOPIC  human   COPULA
    "He is a human"

Using either command line arguments, JSON, or your immagination, you can now
produce similar output as HTML tables, like this:

<table>
    <tr><td>kare</td><td>wa</td><td>ningen</td><td>desu</td></tr>
    <tr><td>He</td><td>TOPIC</td><td>human</td><td>COPULA</td></tr>
    <tr><td colspan=4>He is a human</td></tr>
</table>

## Other Notes

Roughly, I'm following the guidelines of 
[Structuring Your Project](https://docs.python-guide.org/writing/structure/)
to set up this project. 

