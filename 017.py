# Project Euler
# Problem 17
#
# Number letter counts

spellings = {}
spellings[0]    = ''
spellings[1]    = 'one'
spellings[2]    = 'two'
spellings[3]    = 'three'
spellings[4]    = 'four'
spellings[5]    = 'five'
spellings[6]    = 'six'
spellings[7]    = 'seven'
spellings[8]    = 'eight'
spellings[9]    = 'nine'
#
spellings[10]   = 'ten'
spellings[11]   = 'eleven'
spellings[12]   = 'twelve'
spellings[13]   = 'thirteen'
spellings[14]   = 'fourteen'
spellings[15]   = 'fifteen'
spellings[16]   = 'sixteen'
spellings[17]   = 'seventeen'
spellings[18]   = 'eighteen'
spellings[19]   = 'nineteen'
#
spellings[20]   = 'twenty'
spellings[30]   = 'thirty'
spellings[40]   = 'forty'
spellings[50]   = 'fifty'
spellings[60]   = 'sixty'
spellings[70]   = 'seventy'
spellings[80]   = 'eighty'
spellings[90]   = 'ninety'
spellings[100]  = 'hundred'
spellings[1000] = 'thousand'

letters = 0

for i in range(1,1000):

  n = i

  # count the hundreds
  hundreds = 0
  if n > 99:
    while n > 99:
      n -= 100
      hundreds += 1
    letters += len(spellings[hundreds])
    letters += len(spellings[100])
    if n != 0: letters += len('and')

  # tens
  tens = 0
  if n < 20:
    letters += len(spellings[n])
    ns += spellings[n] + ' '
    n = 0
  else:
    while n > 9:
      n -= 10
      tens += 1
  letters += len(spellings[tens * 10])

  # add the ones
  letters += len(spellings[n])
    
# add one thousand
letters += len(spellings[1])
letters += len(spellings[1000])

print letters
