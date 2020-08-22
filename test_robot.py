import pytest

from robot import Robot, Direction, IllegalMoveException


@pytest.fixture
def robot():
    return Robot()


def test_constructor(robot):
    state = robot.state()

    assert state['direction'] == Direction.NORTH
    assert state['row'] == 10
    assert state['col'] == 1


def test_turn(robot):
    robot.turn()

    state = robot.state()
    assert state['direction'] == Direction.EAST

    robot.turn()
    state=robot.state()
    assert state['direction'] == Direction.SOUTH

    robot.turn()
    state = robot.state()
    assert state['direction'] == Direction.WEST

    robot.turn()
    state = robot.state()
    assert state['direction'] == Direction.NORTH

def test_illegal_move(robot):
    robot.turn()
    robot.turn()
    #move South
    with pytest.raises(IllegalMoveException):
        robot.move()
    robot.turn()
    #move_West
    with pytest.raises(IllegalMoveException):
        robot.move()
    robot.turn()
    #move_NOURTH
    with pytest.raises(IllegalMoveException):
        for i in range(11):
            robot.move()
    #move_EAST
    with pytest.raises(IllegalMoveException):
        robot.move()

def test_move(robot):
    robot.move()
    state = robot.state()
    assert state['row'] == 9
    assert state['col'] == 1

    robot.turn()
    robot.move()
    state = robot.state()
    assert state['row'] == 9
    assert state['col'] == 2
    robot.turn()
    robot.move()
    state = robot.state()
    assert state['row'] == 10
    assert state['col'] == 2
    robot.turn()
    robot.move()
    state = robot.state()
    assert state['row'] == 10
    assert state['col'] == 1

def test_back_track_without_history(robot):
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 10
    assert state['col'] == 1

def test_back_after_a_moving(robot):
    robot.move()
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 10
    assert state['col'] == 1

def test_back_after_a_turn(robot):
    robot.turn()
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 10
    assert state['col'] == 1

def test_back_after_2_turn(robot):
    robot.move()
    robot.move()
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 9
    assert state['col'] == 1

def test_back_after_multiple(robot):
    robot.move()
    robot.move()
    robot.back_track()
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 10
    assert state['col'] == 1