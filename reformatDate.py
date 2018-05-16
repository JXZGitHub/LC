# Complete the reformatDate function below.
# 20th Oct 2052 → 2052-10-20
# 6th Jun 1933 → 1933-06-06
def reformatDate(dates):
    #dates is a list of str, eg ['20th Oct 2052', '6th Jun 1933'],
    # return a list of strings in the converted format: ['2052-10-20','1933-06-06']
    months = {'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06', 'Jul':'07', 'Aug':'08', 'Sep':'09',
             'Oct':'10', 'Nov':'11','Dec':'12'}
    res = []
    for raw_d in dates:
        d = raw_d.split()
        converted = []
        year,month,day = d[2],d[1],d[0]
        converted.append(year)
        converted.append(months[month])
        converted.append('%02d' % int(day[:-2]))
        converted = '-'.join(converted)
        res.append(converted)
    return res