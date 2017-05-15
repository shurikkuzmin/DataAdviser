# -*- coding: utf-8 -*-
from alchemyapi import AlchemyAPI
import json

if __name__ == "__main__":
    text = u'Artist tackles Chicago\'s pesky pothole problem _ by filling annoying craters with mosaics\r\n\r\nCHICAGO \u2013  The perfect pothole might not exist for many people \u2014 but for mosaic artist Jim Bachor, it\'s one with a nice oval shape. Bachor began filling those potholes a little more than a year ago, after one in front of his house became a hassle.\r\n\r\nBachor doesn\'t just fill them with cement, though. He\'s turned pothole-filling into a public art project \u2014 one with a sense of humor. He fills them with mosaics.\r\n\r\n"I just think it\'s fun to add that little bit of spark into (an) issue that people moan about," says the Chicago resident, whose work also hangs in galleries. He was first drawn to the ancient art form because of its ability to last.\r\n\r\nWith orange cones and vests displaying his last name, Bachor and his helpers look official enough to shut down a street section to work on filling a pothole.\r\n\r\nBachor uses the Chicago city flag design in his pothole art. Some versions hold phone numbers to local auto repair shops, while others simply read "POTHOLE." His most recent installment north of downtown Chicago \u2014 "#21914" \u2014 pokes fun at the huge number of potholes that exist in the city.\r\n\r\nWhile his mosaic art isn\'t a permanent solution to the city\'s pothole problem, it\'s at least a small fix, he says. The city hasn\'t shut down his project, and some community members have expressed gratitude.\r\n\r\nAfter his first project, one neighbor stopped to thank him. "And then 15 minutes later, he came back with a coffee and a Danish for me," Bachor says, "and so I thought that was really cool."\r\n\r\nGerry Shaheen, a resident of Peoria, Illinois, recently stopped to ask Bachor about his work, as the artist installed a mosaic. He says Bachor and his crew are welcome anytime to fill potholes in his city, one of many hit with an especially large number of the annoying craters after a hard winter.\r\n\r\n"I\'ll pave the way for them," Shaheen said with smirk. "No pun intended."'

    #text = u'''When three Chicago financial trading firms traveled to Washington, D.C., for a crucial meeting with federal regulators, they didn\'t go alone. They brought a man schooled in the ways of the capital who had recently received $182,000 in political contributions from them: Mayor Rahm Emanuel. At stake was a proposal that would have cut into the firms\' bottom lines by making them hold large cash reserves to protect against volatility in the fledgling, high-frequency trading market they had helped pioneer. Public officials of Emanuel\'s stature rarely show up at the arcane rule-making meetings of the Commodity Futures Trading Commission. But the newly elected mayor delivered a message in the windowless conference room that day, about the important role the trading firms and others like them play in Chicago\'s economy. When regulators drafted the final rules months after the September 2011 meeting, Chicago\'s trading firms got the break they wanted. Since the Washington meeting, the three firms — DRW Trading Group, Chicago Trading Co. and Infinium Capital — have donated an additional $187,800 to Emanuel\'s campaign funds, bringing their total support of the mayor to nearly $370,000. Two other Chicago firms that stood to benefit from the rule, PEAK6 and Chopper Trading, have given an additional $334,000 to Emanuel. All the trading firms but Infinium are among an elite corps of roughly 100 donors Emanuel turned to when he first ran for mayor and is relying on again for his re-election effort. Those donors, consisting of individuals, couples, business partners and firms, are responsible for more than $14 million of the $30.5 million he has raised since fall 2010. More than half of those loyal donors have received a tangible benefit from the mayor or his administration, ranging from city contracts to help with regulators, according to a Tribune analysis. In a monthslong examination of Emanuel\'s fundraising machine, the Tribune documented his connections to investment house executives, corporate CEOs and Washington insiders who sustain him with cash even though their interests lie far beyond the policy decisions issued from the mayor\'s fifth-floor office at City Hall. Emanuel declined to be interviewed for this story. His spokeswoman said his trip to Washington in September 2011 was focused on helping the city but declined to discuss what he did on behalf of the key donors. "The mayor had a series of meetings with federal officials in Washington, as he routinely does, to advocate for Chicago priorities — including federal funding for Chicago — and regarding matters critical to our city\'s interest,\" Kelley Quinn, Emanuel\'s communications director, said in a statement. \"In these meetings he discussed federal funding to invest in housing for low-income Chicagoans, funding to invest in Chicago parkland and open space, a potential national park designation for the historic Pullman neighborhood (on) the South Side, and issues impacting Chicago\'s trading industry that employs more than 33,000 people in the city." Those Washington meetings — among more than 100 he has had during more than 30 trips as mayor — are the result of years of cultivating relationships with fellow national leaders. Emanuel\'s resume is unmatched by any mayor in the country: senior adviser to then-President Bill Clinton, top-ranking Democratic congressman from Chicago and first White House chief of staff to President Barack Obama. Add to that years as a top strategist and fundraiser for the national Democratic Party and a two-year stint as an investment banker.'''
    text = text.encode('ascii','ignore')
    
    alchemyapi = AlchemyAPI()

    response = alchemyapi.keywords('text',text,{'sentiment':1,'maxRetrieve':20,'keywordExtractMode':'strict'})

    if response['status'] == "OK":
        print(json.dumps(response, indent = 4))

        for keyword in response['keywords']:
            print('Keyword text:',keyword['text'].encode('utf-8'))
            print('Keyword relevance:',keyword['relevance'])
    print("**********")
    response = alchemyapi.concepts('text',text,{'maxRetrieve':10})

    if response['status'] == "OK":
        #print(json.dumps(response, indent = 4)) 
        keywords = [(concept['text'].encode('ascii'),float(concept['relevance'])) for concept in response['concepts'] ]
    
        for concept in response['concepts']:
            print('Concept text:',concept['text'].encode('utf-8'))
            print('Concept relevance:',concept['relevance'])

        print keywords

    print("**********")
    response = alchemyapi.entities('text',text,{'maxRetrieve': 200})
    if response['status'] == "OK":
        print(json.dumps(response, indent = 4))
        
        for entity in response['entities']:
            print("Entity text",entity['text'])
            print("Entity type",entity['type'])
            
        persons = [ent['text']  for ent in response['entities'] if ent['type']=='Person']

        print("All persons:",persons)
