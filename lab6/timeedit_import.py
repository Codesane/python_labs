from urllib.request import urlopen
from datetime import datetime
from datatyper import *
from bokningar import *

# Returns an url where the dictionarie DATA been appended to the string SITE.
# Example: generate_url('index.html', {'ett': 'två', 'tre': 'fyra'}) =>
# 'index.html?ett=två&tre=fyra'.
def generate_url(site, data):
    url = site
    if data:
        url += '?'
        for key in data:
            url += key+'='+data[key]+'&'
    return url[:-1]

# Returns the content of the page URL as a string.
def get_page_content(url):
    return str(urlopen(url).read(), 'utf8', 'ignore')

# Returns the first object id found in the list to the left when searching
# on timeedit with the parameters wv_type = CATEGORY_ID and
# wv_search = PATTERN.
def timeedit_get_object_id(category_id, pattern):
    page = 'http://timeedit.liu.se/4DACTION/WebShowSearch/5/1-0'
    data = {'wv_type': category_id,
            'wv_search': pattern}
    url = generate_url(page, data)
    content = get_page_content(url)
    looking_for = 'javascript:addObject('
    index_start = content.find(looking_for)+len(looking_for)
    index_stop = content.find(')', index_start)
    return content[index_start:index_stop]

# Returns the ical-file for given OBJECT_ID and time.
def timeedit_get_ical(object_id, year=0, start_week=0, stop_week=0):
    now = datetime.now()
    current_week = now.isocalendar()[1]
    if year == 0:
        year = now.year;
    if start_week == 0:
        start_week = current_week
    if stop_week == 0:
         stop_week = 27 if current_week < 26 else 52
    
    page = 'http://timeedit.liu.se/4DACTION/iCal_downloadReservations/timeedit.ics'
    year = (year % 1000)*100 # Replace 2 last digits with zeros.
    data = {'id1': object_id,
            'from': str(year+start_week),
            'to': str(year+stop_week),
            'branch': '5'}
    return get_page_content(generate_url(page, data))

def ical_to_årsalmanacka(ical):
    
    # Unescape escaped chars
    ical = ical.replace('\,', ',')
    
    årsalma = skapa_årsalmanacka()
    
    months = { 1: 'januari',
               2: 'februari',
               3: 'mars',
               4: 'april',
               5: 'maj',
               6: 'juni',
               7: 'juli',
               8: 'augusti',
               9: 'september',
              10: 'oktober',
              11: 'november',
              12: 'december'}
    
    lines = ical.split('\r\n')
    start = ''
    end = ''
    summary = ''
    location = ''
    
    while lines:
        
        line = lines.pop(0)
        
        if 1 < len(line):
            
            if line == 'BEGIN:VEVENT':
                
                start = {}
                end = {}
                summary = ''
                location = ''
                
            elif line == 'END:VEVENT':
                
                dag = skapa_dag(start['day'])
                mån = skapa_månad(months[start['month']])
                start = skapa_klockslag(
                            skapa_timme(start['hour']),
                            skapa_minut(start['minute']))
                slut = skapa_klockslag(
                            skapa_timme(end['hour']),
                            skapa_minut(end['minute']))
                möte = skapa_möte(summary + ', ' + location)
                årsalma = boka_möte(årsalma, dag, mån, start, slut, möte)
                
            else:
                
                key, value = line.split(':')
                
                if key == 'DTSTART;TZID=Europe/Stockholm':
                    
                    start['year'] = int(value[0:4])
                    start['month'] = int(value[4:6])
                    start['day'] = int(value[6:8])
                    start['hour'] = int(value[9:11])
                    start['minute'] = int(value[11:13])
                    
                elif key == 'DTEND;TZID=Europe/Stockholm':
                    
                    end['year'] = int(value[0:4])
                    end['month'] = int(value[4:6])
                    end['day'] = int(value[6:8])
                    end['hour'] = int(value[9:11])
                    end['minute'] = int(value[11:13])
                    
                elif key == 'SUMMARY':
                    
                    summary = value
                    
                elif key == 'LOCATION':
                    
                    location = value
                
    return årsalma

def importera_schema_för_kurs(course_code, year=0, start_week=0, stop_week=0):
    return ical_to_årsalmanacka(timeedit_get_ical(
                                    timeedit_get_object_id('6', course_code),
                                    year, start_week, stop_week))

def importera_schema_för_grupp(group_name, year=0, start_week=0, stop_week=0):
    return ical_to_årsalmanacka(timeedit_get_ical(
                                    timeedit_get_object_id('8', group_name), year,
                                    start_week, stop_week))

def importera_schema_för_lärare(liu_id, year=0, start_week=0, stop_week=0):
    return ical_to_årsalmanacka(timeedit_get_ical(
                                    timeedit_get_object_id('9', liu_id),
                                    year, start_week, stop_week))