
spellings = {}
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
  # see how many hundreds there are
  hundreds = 0
  while n > 100:
    n -= 100
    hundreds += 1
  # count the hundreds
  letters += spellings[hundreds]
  letters += spellings[100]

  # next, see how many tens there are above twenty
    hundreds = i - (i % 100)
    letters += hundreds
# add one thousand
letters += spellings[1]
letters += spellings[1000]
