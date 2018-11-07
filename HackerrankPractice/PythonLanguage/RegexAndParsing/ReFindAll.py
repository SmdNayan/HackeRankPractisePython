import re
if __name__ == "__main__":
    s = '[bcdfghjklmnpqrstvwxyz]'
    ss = re.findall('(?<=' + s +')([aeiou]{2,})' + s, input(), re.I)
    print('\n'.join(ss or ['-1']))