# -*- coding: utf-8 -*-
import subprocess
from random import random


couples = {
    'blake': 'kendra',
    'kendra': 'blake',
    'betny': 'craig',
    'craig': 'betny',
    'kim': 'mikey',
    'mikey': 'kim',
    'anush': None
}
errybody = couples.keys()


def validate(proposed):
    """Check whether a proposed mapping 
    of santas to santees meets the constraints
    we care about."""

    for santa, santee in proposed.items():

        # prevent giving to anyone you're having sex with
        if couples[santa] == santee:
            return False
        
        # prevent giving to self
        elif santa == santee:
            return False
        
        # prevent 2 people giving to each other
        if proposed[santee] == santa:
            return False

    return True


def propose():
    """Propose assignments randomly"""
    random_order = sorted(errybody, key=lambda _: random())
    return {
        santa: santee 
        for santa, santee in zip(errybody, random_order)
    }


def make_map():
    """Get a valid mapping of santas to santees"""
    proposal = propose()
    while validate(proposal) is False:
        proposal = propose()

    return proposal


applescript_tpl = """
display dialog "You got {}! Make it good." ¬
with title "{} lolsanta" ¬
with icon caution ¬
buttons {{"OK"}}
"""

if __name__ == '__main__':
    santa_map = make_map()

    while True:
        names = ', '.join(couples.keys())
        santa = raw_input('\n\nwho r u? {}\n'.format(names))
        try:
            santee = santa_map[santa.lower().strip()]
            applescript = applescript_tpl.format(santee, santa)
            subprocess.call("osascript -e '{}'".format(applescript), shell=True)
        except:
            print('no no no you idiot-- type your name')

