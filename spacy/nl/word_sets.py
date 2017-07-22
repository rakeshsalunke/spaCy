# coding: utf8
from __future__ import unicode_literals


# Stop words are retrieved from http://www.damienvanholten.com/downloads/dutch-stop-words.txt

STOP_WORDS = set("""
aan af al alles als altijd andere

ben bij

daar dan dat de der deze die dit doch doen door dus

een eens en er

ge geen geweest

haar had heb hebben heeft hem het hier hij hoe hun

iemand iets ik in is

ja je

kan kon kunnen

maar me meer men met mij mijn moet

na naar niet niets nog nu

of om omdat ons ook op over

reeds

te tegen toch toen tot

u uit uw

van veel voor

want waren was wat we wel werd wezen wie wij wil worden

zal ze zei zelf zich zij zijn zo zonder zou
""".split())


# Number words

NUM_WORDS = set("""
nul een één twee drie vier vijf zes zeven acht negen tien elf twaalf dertien
veertien twintig dertig veertig vijftig zestig zeventig tachtig negentig honderd
duizend miljoen miljard biljoen biljard triljoen triljard
""".split())


# Ordinal words

ORDINAL_WORDS = set("""
eerste tweede derde vierde vijfde zesde zevende achtste negende tiende elfde
twaalfde dertiende veertiende twintigste dertigste veertigste vijftigste
zestigste zeventigste tachtigste negentigste honderdste duizendste miljoenste
miljardste biljoenste biljardste triljoenste triljardste
""".split())