from up_lib.parser import parse


def test_parse_simple_wait():
    # given
    line = "wait --timeout=42: aws sts get-caller-identity"
    # when
    cmd = parse(line)
    # then
    print(cmd)
    print("UALA")