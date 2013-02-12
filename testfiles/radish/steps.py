# -*- coding: utf-8 -*-

from radish import step, world
from time import sleep


@step(r'I have the number ([+0-9-]+)')
def have_the_number(step, number):
    if int(number) < 0:
        step.ValidationError("The number cannot be nagative")
        return

    world.number = 0
    if not step.is_dry_run():
        world.number = int(number)
        sleep(1)


@step(r'I compute its factorial')
def compute_its_factorial(step):
    if not step.is_dry_run():
        world.number = factorial(world.number)
        sleep(1)


@step(r'I see the number (\d+)')
def check_number(step, expected):
    if not step.is_dry_run():
        expected = int(expected)
        sleep(1)
        assert world.number == expected, "Got %d" % world.number


@step(r'(dfg)+')
def dfg(step, dfg):
    if not step.is_dry_run():
        sleep(1)


def factorial(number):
    return -1
