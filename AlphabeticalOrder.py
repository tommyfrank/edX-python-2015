s = raw_input('Enter a string: ')
currentChar = 0
longest = ''
longestLength = -1
viewedChar = 0
previousViewedChar = 0
viewedSequence = ''
for currentChar in range(0, len(s)-2):
    viewedChar = currentChar + 1
    previousViewedChar = currentChar
    viewedSequence = list(s[previousViewedChar] + s[viewedChar])
    while sorted(viewedSequence) == viewedSequence:
        viewedChar += 1
        previousViewedChar += 1
        if viewedChar < len(s):
            viewedSequence = list(s[previousViewedChar] + s[viewedChar])
        else:
            break
    if previousViewedChar - currentChar > longestLength:
        longest = s[currentChar]
        longestLength = previousViewedChar - currentChar
        while longestLength > 0:
            longest += s[previousViewedChar - longestLength + 1]
            longestLength -= 1
        longestLength = previousViewedChar - currentChar
print('Longest substring in alphabetical order is: ' + longest)