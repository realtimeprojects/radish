# -*- coding: utf-8 -*-

from radish import step, world
from time import sleep


@step(r'I have the number ([+0-9-]+)', metric_indicators=['a', 'c'])
def have_the_number(step, number):
    if int(number) < 0:
        step.ValidationError("The number cannot be nagative")
        return

    world.number = 0
    if not step.is_dry_run():
        world.number = int(number)
        sleep(1)


@step(r'I compute its factorial', metric_indicators=['b', 'c'])
def compute_its_factorial(step):
    if not step.is_dry_run():
        world.number = factorial(world.number)
        sleep(1)


@step(r'I see the number (\d+)', metric_indicators=['a', 'b', 'c'])
def check_number(step, expected):
    if not step.is_dry_run():
        expected = int(expected)
        sleep(1)
        assert world.number == expected, "Got %d" % world.number


@step(r'(dfg)+')
def dfg(step, dfg):
    if not step.is_dry_run():
        sleep(1)

@step(r'I fail after (\d+) times')
def fail_after_times(step, times):
    times = int(times)
    if world.fail_after_times_count >= times:
        assert False, "Sorry, but it's the %d time" % times
    print world.fail_after_times_count
    world.fail_after_times_count += 1


def factorial(number):
    return -1
