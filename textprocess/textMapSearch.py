#!/usr/bin/env python

import sys
from topia.termextract import extract
import urllib,urllib2
from bs4 import BeautifulSoup
from django.utils.html import mark_safe
from alchemyapi_python.alchemyapi import AlchemyAPI

city_names = {'EDM':'Edmonton',
              'CGO':'Chicago',
              'NYC':'New York City',
              'SFO':'San Francisco',
              'BOS':'Boston',
              'MTL':'Montreal',
             }

def find_keywords(text,citycode):
    text=text.encode('ascii','ignore')
    ###extractor = extract.TermExtractor()
    ###keywords = extractor(text)

    ###s1 = sorted(keywords,key=lambda term: term[1])
    ###s1.reverse()
    ###s2 = sorted(keywords,key=lambda term: term[2])
    ###s2.reverse()
    
    ###maxkw = 3
    ###s1 = [(kw[0],kw[1]) for kw in s1[0:maxkw] ]
    ###s2 = [(kw[0],kw[2]) for kw in s2[0:maxkw] ]
    
    ###kw = s1
    ###for k in s2:
    ###    if k not in kw:
    ###        kw.append(k)
    ###kw = sorted(kw,key=lambda term: term[1])
    ###kw.reverse()
    
    #kw = set(s1+s2)
    alchemyapi = AlchemyAPI()
    ###response = alchemyapi.keywords('text',text,{'sentiment':1,'maxRetrieve':5})
    response = alchemyapi.concepts('text',text,{'maxRetrieve':5})

    kw = []
    if response['status'] == "OK":
        #kw = [(keyword['text'].encode('ascii'),float(keyword['relevance'])) for keyword in response['keywords']]
        kw = [(concept['text'].encode('ascii'),float(concept['relevance'])) for concept in response['concepts']]
    print kw

    results = {}

    isFirst = True

    # all data?
    # opendata.socrata.com/browse
    dataSetQueryURLs = {'EDM':         'https://data.edmonton.ca/browse?limitTo=maps&sortBy=relevance&q=%s',
                        'CGO':   'https://data.cityofchicago.org/browse?limitTo=maps&sortBy=relevance&q=%s',
                        'NYC':  'https://nycopendata.socrata.com/browse?limitTo=maps&sortBy=relevance&q=%s',
                        'SFO':           'https://data.sfgov.org/browse?limitTo=maps&sortBy=relevance&q=%s',
                        'BOS':    'https://data.cityofboston.gov/browse?limitTo=maps&sortBy=relevance&q=%s',
                        'MTL':'https://montreal.demo.socrata.com/browse?limitTo=maps&sortBy=relevance&q=%s',
                       }
    dataSetQueryURL = dataSetQueryURLs[citycode]
    
    linkclasses = {'EDM':'nameLink',
                   'CGO':'name',
                   'NYC':'nameLink',
                   'SFO':'nameLink',
                   'BOS':'name',
                   'MTL':'nameLink',}
    linkclass = linkclasses[citycode]
    
    for key in kw:
        text = key[0]
        score = key[1]
        
        # save score somewhere?
        
        url = dataSetQueryURL % urllib.quote(text)

        content = urllib2.urlopen(url).read()
        soup = BeautifulSoup(content)
        links = soup.find_all("a",class_=linkclass)
        links = links[0:3]
        if len(links) > 0:
            results[text] = []
            for link in links:
                results[text].append(link['href'])
                if isFirst:
                    content = urllib2.urlopen(results[text][0]).read()
                    soup = BeautifulSoup(content)
                    embed = soup.find(id="embed_code")
                    embed = str(embed.contents[0])
                    embed = embed.replace('_width_px','646')
                    embed = embed.replace('_height_px','760')
                    results['the_featured_embed_'] = mark_safe(embed)
                    isFirst = False
                    
    return results


