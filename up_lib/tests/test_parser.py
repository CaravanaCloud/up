from up_lib.parser import parse_action

def parse(line, action):
    return parse_action(line, [action]).as_tuple()

def parse_wait(line):
    return parse_action(line, ["wait"]).as_tuple()

def test_wait_true():
    # given
    line = "wait: true"
    # when
    (action, opts, prompt) = parse_wait(line)
    # then assert actual == expected
    assert action == "wait"
    assert tuple(prompt) == ("true",)


def test_parse_simple_wait():
    # given
    line = "WAIT --timeout=42: aws sts get-caller-identity"
    # when
    (action, opts, prompt) = parse_wait(line)
    # then
    assert action == "wait"
    assert tuple(prompt) == ("aws", "sts", "get-caller-identity",)
    assert opts["timeout"] == '42'

def test_parse_vars_zero_arg():
    # given
    line = "VARS"
    # when
    (action, opts, prompt) = parse(line, "vars")
    # then
    assert action == "vars"
    assert len(prompt) == 0
    assert len(opts) == 0

def test_parse_vars_one_arg():
    # given
    line = "VARS USER"
    # when
    (action, opts, prompt) = parse(line, "vars")
    # then
    assert action == "vars"
    assert tuple(prompt) == ("USER",)
    assert len(opts) == 0

def test_parse_vars_one_arg():
    # given
    line = "VARS USER HOME"
    # when
    (action, opts, prompt) = parse(line, "vars")
    # then
    assert action == "vars"
    assert tuple(prompt) == ("USER", "HOME",)
    assert len(opts) == 0

