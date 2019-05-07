{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "from __future__ import division  # Python 2 users only\n",
    "import nltk, re, pprint\n",
    "from nltk import word_tokenize"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "unicode"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import urllib2\n",
    "url = \"http://www.gutenberg.org/files/2554/2554-0.txt\"\n",
    "response = urllib2.urlopen(url)\n",
    "raw = response.read().decode('utf8')\n",
    "type(raw)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1176965"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(raw)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "u'\\ufeffThe Project Gutenberg EBook of Crime and Punishment, by Fyodor Dostoevsky\\r'"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "raw[:75]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "list"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tokens = word_tokenize(raw)\n",
    "type(tokens)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "257726"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(tokens)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[u'\\ufeffThe',\n",
       " u'Project',\n",
       " u'Gutenberg',\n",
       " u'EBook',\n",
       " u'of',\n",
       " u'Crime',\n",
       " u'and',\n",
       " u'Punishment',\n",
       " u',',\n",
       " u'by']"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tokens[:10]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "nltk.text.Text"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "text = nltk.Text(tokens)\n",
    "type(text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[u'an',\n",
       " u'exceptionally',\n",
       " u'hot',\n",
       " u'evening',\n",
       " u'early',\n",
       " u'in',\n",
       " u'July',\n",
       " u'a',\n",
       " u'young',\n",
       " u'man',\n",
       " u'came',\n",
       " u'out',\n",
       " u'of',\n",
       " u'the',\n",
       " u'garret',\n",
       " u'in',\n",
       " u'which',\n",
       " u'he',\n",
       " u'lodged',\n",
       " u'in',\n",
       " u'S.',\n",
       " u'Place',\n",
       " u'and',\n",
       " u'walked',\n",
       " u'slowly',\n",
       " u',',\n",
       " u'as',\n",
       " u'though',\n",
       " u'in',\n",
       " u'hesitation',\n",
       " u',',\n",
       " u'towards',\n",
       " u'K.',\n",
       " u'bridge',\n",
       " u'.',\n",
       " u'He',\n",
       " u'had',\n",
       " u'successfully']"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "text[1024:1062]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Katerina Ivanovna; Pyotr Petrovitch; Pulcheria Alexandrovna; Avdotya\n",
      "Romanovna; Rodion Romanovitch; Marfa Petrovna; Sofya Semyonovna; old\n",
      "woman; Project Gutenberg-tm; Porfiry Petrovitch; Amalia Ivanovna;\n",
      "great deal; young man; Nikodim Fomitch; Ilya Petrovitch; Project\n",
      "Gutenberg; Andrey Semyonovitch; Hay Market; Dmitri Prokofitch; Good\n",
      "heavens\n"
     ]
    }
   ],
   "source": [
    "text.collocations()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5336"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "raw.find(\"PART I\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1157810"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "raw.rfind(\"End of Project Gutenberg\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "195767"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "raw = raw[5338:1157743]\n",
    "raw.find(\"PART I\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "u'<!doctype html public \"-//W3C//DTD HTML 4.0 Transitional//EN'"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "url = \"http://news.bbc.co.uk/2/hi/health/2284783.stm\"\n",
    "html = urllib2.urlopen(url).read().decode('utf8')\n",
    "html[:60]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/Users/Charon/anaconda2/lib/python2.7/site-packages/bs4/__init__.py:181: UserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system (\"lxml\"). This usually isn't a problem, but if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.\n",
      "\n",
      "The code that caused this warning is on line 174 of the file /Users/Charon/anaconda2/lib/python2.7/runpy.py. To get rid of this warning, change code that looks like this:\n",
      "\n",
      " BeautifulSoup(YOUR_MARKUP})\n",
      "\n",
      "to this:\n",
      "\n",
      " BeautifulSoup(YOUR_MARKUP, \"lxml\")\n",
      "\n",
      "  markup_type=markup_type))\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "[u'BBC',\n",
       " u'NEWS',\n",
       " u'|',\n",
       " u'Health',\n",
       " u'|',\n",
       " u'Blondes',\n",
       " u\"'to\",\n",
       " u'die',\n",
       " u'out',\n",
       " u'in',\n",
       " u'200',\n",
       " u\"years'\",\n",
       " u'NEWS',\n",
       " u'SPORT',\n",
       " u'WEATHER',\n",
       " u'WORLD',\n",
       " u'SERVICE',\n",
       " u'A-Z',\n",
       " u'INDEX',\n",
       " u'SEARCH',\n",
       " u'You',\n",
       " u'are',\n",
       " u'in',\n",
       " u':',\n",
       " u'Health',\n",
       " u'News',\n",
       " u'Front',\n",
       " u'Page',\n",
       " u'Africa',\n",
       " u'Americas',\n",
       " u'Asia-Pacific',\n",
       " u'Europe',\n",
       " u'Middle',\n",
       " u'East',\n",
       " u'South',\n",
       " u'Asia',\n",
       " u'UK',\n",
       " u'Business',\n",
       " u'Entertainment',\n",
       " u'Science/Nature',\n",
       " u'Technology',\n",
       " u'Health',\n",
       " u'Medical',\n",
       " u'notes',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'-',\n",
       " u'Talking',\n",
       " u'Point',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'-',\n",
       " u'Country',\n",
       " u'Profiles',\n",
       " u'In',\n",
       " u'Depth',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'-',\n",
       " u'Programmes',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'-',\n",
       " u'SERVICES',\n",
       " u'Daily',\n",
       " u'E-mail',\n",
       " u'News',\n",
       " u'Ticker',\n",
       " u'Mobile/PDAs',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'-',\n",
       " u'Text',\n",
       " u'Only',\n",
       " u'Feedback',\n",
       " u'Help',\n",
       " u'EDITIONS',\n",
       " u'Change',\n",
       " u'to',\n",
       " u'UK',\n",
       " u'Friday',\n",
       " u',',\n",
       " u'27',\n",
       " u'September',\n",
       " u',',\n",
       " u'2002',\n",
       " u',',\n",
       " u'11:51',\n",
       " u'GMT',\n",
       " u'12:51',\n",
       " u'UK',\n",
       " u'Blondes',\n",
       " u\"'to\",\n",
       " u'die',\n",
       " u'out',\n",
       " u'in',\n",
       " u'200',\n",
       " u\"years'\",\n",
       " u'Scientists',\n",
       " u'believe',\n",
       " u'the',\n",
       " u'last',\n",
       " u'blondes',\n",
       " u'will',\n",
       " u'be',\n",
       " u'in',\n",
       " u'Finland',\n",
       " u'The',\n",
       " u'last',\n",
       " u'natural',\n",
       " u'blondes',\n",
       " u'will',\n",
       " u'die',\n",
       " u'out',\n",
       " u'within',\n",
       " u'200',\n",
       " u'years',\n",
       " u',',\n",
       " u'scientists',\n",
       " u'believe',\n",
       " u'.',\n",
       " u'A',\n",
       " u'study',\n",
       " u'by',\n",
       " u'experts',\n",
       " u'in',\n",
       " u'Germany',\n",
       " u'suggests',\n",
       " u'people',\n",
       " u'with',\n",
       " u'blonde',\n",
       " u'hair',\n",
       " u'are',\n",
       " u'an',\n",
       " u'endangered',\n",
       " u'species',\n",
       " u'and',\n",
       " u'will',\n",
       " u'become',\n",
       " u'extinct',\n",
       " u'by',\n",
       " u'2202',\n",
       " u'.',\n",
       " u'Researchers',\n",
       " u'predict',\n",
       " u'the',\n",
       " u'last',\n",
       " u'truly',\n",
       " u'natural',\n",
       " u'blonde',\n",
       " u'will',\n",
       " u'be',\n",
       " u'born',\n",
       " u'in',\n",
       " u'Finland',\n",
       " u'-',\n",
       " u'the',\n",
       " u'country',\n",
       " u'with',\n",
       " u'the',\n",
       " u'highest',\n",
       " u'proportion',\n",
       " u'of',\n",
       " u'blondes',\n",
       " u'.',\n",
       " u'The',\n",
       " u'frequency',\n",
       " u'of',\n",
       " u'blondes',\n",
       " u'may',\n",
       " u'drop',\n",
       " u'but',\n",
       " u'they',\n",
       " u'wo',\n",
       " u\"n't\",\n",
       " u'disappear',\n",
       " u'Prof',\n",
       " u'Jonathan',\n",
       " u'Rees',\n",
       " u',',\n",
       " u'University',\n",
       " u'of',\n",
       " u'Edinburgh',\n",
       " u'But',\n",
       " u'they',\n",
       " u'say',\n",
       " u'too',\n",
       " u'few',\n",
       " u'people',\n",
       " u'now',\n",
       " u'carry',\n",
       " u'the',\n",
       " u'gene',\n",
       " u'for',\n",
       " u'blondes',\n",
       " u'to',\n",
       " u'last',\n",
       " u'beyond',\n",
       " u'the',\n",
       " u'next',\n",
       " u'two',\n",
       " u'centuries',\n",
       " u'.',\n",
       " u'The',\n",
       " u'problem',\n",
       " u'is',\n",
       " u'that',\n",
       " u'blonde',\n",
       " u'hair',\n",
       " u'is',\n",
       " u'caused',\n",
       " u'by',\n",
       " u'a',\n",
       " u'recessive',\n",
       " u'gene',\n",
       " u'.',\n",
       " u'In',\n",
       " u'order',\n",
       " u'for',\n",
       " u'a',\n",
       " u'child',\n",
       " u'to',\n",
       " u'have',\n",
       " u'blonde',\n",
       " u'hair',\n",
       " u',',\n",
       " u'it',\n",
       " u'must',\n",
       " u'have',\n",
       " u'the',\n",
       " u'gene',\n",
       " u'on',\n",
       " u'both',\n",
       " u'sides',\n",
       " u'of',\n",
       " u'the',\n",
       " u'family',\n",
       " u'in',\n",
       " u'the',\n",
       " u'grandparents',\n",
       " u\"'\",\n",
       " u'generation',\n",
       " u'.',\n",
       " u'Dyed',\n",
       " u'rivals',\n",
       " u'The',\n",
       " u'researchers',\n",
       " u'also',\n",
       " u'believe',\n",
       " u'that',\n",
       " u'so-called',\n",
       " u'bottle',\n",
       " u'blondes',\n",
       " u'may',\n",
       " u'be',\n",
       " u'to',\n",
       " u'blame',\n",
       " u'for',\n",
       " u'the',\n",
       " u'demise',\n",
       " u'of',\n",
       " u'their',\n",
       " u'natural',\n",
       " u'rivals',\n",
       " u'.',\n",
       " u'They',\n",
       " u'suggest',\n",
       " u'that',\n",
       " u'dyed-blondes',\n",
       " u'are',\n",
       " u'more',\n",
       " u'attractive',\n",
       " u'to',\n",
       " u'men',\n",
       " u'who',\n",
       " u'choose',\n",
       " u'them',\n",
       " u'as',\n",
       " u'partners',\n",
       " u'over',\n",
       " u'true',\n",
       " u'blondes',\n",
       " u'.',\n",
       " u'Bottle-blondes',\n",
       " u'like',\n",
       " u'Ann',\n",
       " u'Widdecombe',\n",
       " u'may',\n",
       " u'be',\n",
       " u'to',\n",
       " u'blame',\n",
       " u'But',\n",
       " u'Jonathan',\n",
       " u'Rees',\n",
       " u',',\n",
       " u'professor',\n",
       " u'of',\n",
       " u'dermatology',\n",
       " u'at',\n",
       " u'the',\n",
       " u'University',\n",
       " u'of',\n",
       " u'Edinburgh',\n",
       " u'said',\n",
       " u'it',\n",
       " u'was',\n",
       " u'unlikely',\n",
       " u'blondes',\n",
       " u'would',\n",
       " u'die',\n",
       " u'out',\n",
       " u'completely',\n",
       " u'.',\n",
       " u'``',\n",
       " u'Genes',\n",
       " u'do',\n",
       " u\"n't\",\n",
       " u'die',\n",
       " u'out',\n",
       " u'unless',\n",
       " u'there',\n",
       " u'is',\n",
       " u'a',\n",
       " u'disadvantage',\n",
       " u'of',\n",
       " u'having',\n",
       " u'that',\n",
       " u'gene',\n",
       " u'or',\n",
       " u'by',\n",
       " u'chance',\n",
       " u'.',\n",
       " u'They',\n",
       " u'do',\n",
       " u\"n't\",\n",
       " u'disappear',\n",
       " u',',\n",
       " u\"''\",\n",
       " u'he',\n",
       " u'told',\n",
       " u'BBC',\n",
       " u'News',\n",
       " u'Online',\n",
       " u'.',\n",
       " u'``',\n",
       " u'The',\n",
       " u'only',\n",
       " u'reason',\n",
       " u'blondes',\n",
       " u'would',\n",
       " u'disappear',\n",
       " u'is',\n",
       " u'if',\n",
       " u'having',\n",
       " u'the',\n",
       " u'gene',\n",
       " u'was',\n",
       " u'a',\n",
       " u'disadvantage',\n",
       " u'and',\n",
       " u'I',\n",
       " u'do',\n",
       " u'not',\n",
       " u'think',\n",
       " u'that',\n",
       " u'is',\n",
       " u'the',\n",
       " u'case',\n",
       " u'.',\n",
       " u'``',\n",
       " u'The',\n",
       " u'frequency',\n",
       " u'of',\n",
       " u'blondes',\n",
       " u'may',\n",
       " u'drop',\n",
       " u'but',\n",
       " u'they',\n",
       " u'wo',\n",
       " u\"n't\",\n",
       " u'disappear',\n",
       " u'.',\n",
       " u\"''\",\n",
       " u'See',\n",
       " u'also',\n",
       " u':',\n",
       " u'28',\n",
       " u'Mar',\n",
       " u'01',\n",
       " u'|',\n",
       " u'Education',\n",
       " u'What',\n",
       " u'is',\n",
       " u'it',\n",
       " u'about',\n",
       " u'blondes',\n",
       " u'?',\n",
       " u'09',\n",
       " u'Apr',\n",
       " u'99',\n",
       " u'|',\n",
       " u'Health',\n",
       " u'Platinum',\n",
       " u'blondes',\n",
       " u'are',\n",
       " u'labelled',\n",
       " u'as',\n",
       " u'dumb',\n",
       " u'17',\n",
       " u'Apr',\n",
       " u'02',\n",
       " u'|',\n",
       " u'Health',\n",
       " u'Hair',\n",
       " u'dye',\n",
       " u'cancer',\n",
       " u'alert',\n",
       " u'Internet',\n",
       " u'links',\n",
       " u':',\n",
       " u'University',\n",
       " u'of',\n",
       " u'Edinburgh',\n",
       " u'The',\n",
       " u'BBC',\n",
       " u'is',\n",
       " u'not',\n",
       " u'responsible',\n",
       " u'for',\n",
       " u'the',\n",
       " u'content',\n",
       " u'of',\n",
       " u'external',\n",
       " u'internet',\n",
       " u'sites',\n",
       " u'Top',\n",
       " u'Health',\n",
       " u'stories',\n",
       " u'now',\n",
       " u':',\n",
       " u'Heart',\n",
       " u'risk',\n",
       " u'link',\n",
       " u'to',\n",
       " u'big',\n",
       " u'families',\n",
       " u'Back',\n",
       " u'pain',\n",
       " u'drug',\n",
       " u\"'may\",\n",
       " u'aid',\n",
       " u\"diabetics'\",\n",
       " u'Congo',\n",
       " u'Ebola',\n",
       " u'outbreak',\n",
       " u'confirmed',\n",
       " u'Vegetables',\n",
       " u'ward',\n",
       " u'off',\n",
       " u\"Alzheimer's\",\n",
       " u'Polio',\n",
       " u'campaign',\n",
       " u'launched',\n",
       " u'in',\n",
       " u'Iraq',\n",
       " u'Gene',\n",
       " u'defect',\n",
       " u'explains',\n",
       " u'high',\n",
       " u'blood',\n",
       " u'pressure',\n",
       " u'Botox',\n",
       " u\"'may\",\n",
       " u'cause',\n",
       " u'new',\n",
       " u\"wrinkles'\",\n",
       " u'Alien',\n",
       " u\"'abductees\",\n",
       " u\"'\",\n",
       " u'show',\n",
       " u'real',\n",
       " u'symptoms',\n",
       " u'Links',\n",
       " u'to',\n",
       " u'more',\n",
       " u'Health',\n",
       " u'stories',\n",
       " u'are',\n",
       " u'at',\n",
       " u'the',\n",
       " u'foot',\n",
       " u'of',\n",
       " u'the',\n",
       " u'page',\n",
       " u'.',\n",
       " u'E-mail',\n",
       " u'this',\n",
       " u'story',\n",
       " u'to',\n",
       " u'a',\n",
       " u'friend',\n",
       " u'Links',\n",
       " u'to',\n",
       " u'more',\n",
       " u'Health',\n",
       " u'stories',\n",
       " u'In',\n",
       " u'This',\n",
       " u'Section',\n",
       " u'Heart',\n",
       " u'risk',\n",
       " u'link',\n",
       " u'to',\n",
       " u'big',\n",
       " u'families',\n",
       " u'Back',\n",
       " u'pain',\n",
       " u'drug',\n",
       " u\"'may\",\n",
       " u'aid',\n",
       " u\"diabetics'\",\n",
       " u'Congo',\n",
       " u'Ebola',\n",
       " u'outbreak',\n",
       " u'confirmed',\n",
       " u'Vegetables',\n",
       " u'ward',\n",
       " u'off',\n",
       " u\"Alzheimer's\",\n",
       " u'Polio',\n",
       " u'campaign',\n",
       " u'launched',\n",
       " u'in',\n",
       " u'Iraq',\n",
       " u'Gene',\n",
       " u'defect',\n",
       " u'explains',\n",
       " u'high',\n",
       " u'blood',\n",
       " u'pressure',\n",
       " u'Botox',\n",
       " u\"'may\",\n",
       " u'cause',\n",
       " u'new',\n",
       " u\"wrinkles'\",\n",
       " u'Alien',\n",
       " u\"'abductees\",\n",
       " u\"'\",\n",
       " u'show',\n",
       " u'real',\n",
       " u'symptoms',\n",
       " u'How',\n",
       " u'sperm',\n",
       " u'wriggle',\n",
       " u'Bollywood',\n",
       " u'told',\n",
       " u'to',\n",
       " u'stub',\n",
       " u'it',\n",
       " u'out',\n",
       " u'Fears',\n",
       " u'over',\n",
       " u'tuna',\n",
       " u'health',\n",
       " u'risk',\n",
       " u'to',\n",
       " u'babies',\n",
       " u'Public',\n",
       " u'can',\n",
       " u'be',\n",
       " u'taught',\n",
       " u'to',\n",
       " u'spot',\n",
       " u'strokes',\n",
       " u'^^',\n",
       " u'Back',\n",
       " u'to',\n",
       " u'top',\n",
       " u'News',\n",
       " u'Front',\n",
       " u'Page',\n",
       " u'|',\n",
       " u'Africa',\n",
       " u'|',\n",
       " u'Americas',\n",
       " u'|',\n",
       " u'Asia-Pacific',\n",
       " u'|',\n",
       " u'Europe',\n",
       " u'|',\n",
       " u'Middle',\n",
       " u'East',\n",
       " u'|',\n",
       " u'South',\n",
       " u'Asia',\n",
       " u'|',\n",
       " u'UK',\n",
       " u'|',\n",
       " u'Business',\n",
       " u'|',\n",
       " u'Entertainment',\n",
       " u'|',\n",
       " u'Science/Nature',\n",
       " u'|',\n",
       " u'Technology',\n",
       " u'|',\n",
       " u'Health',\n",
       " u'|',\n",
       " u'Talking',\n",
       " u'Point',\n",
       " u'|',\n",
       " u'Country',\n",
       " u'Profiles',\n",
       " u'|',\n",
       " u'In',\n",
       " u'Depth',\n",
       " u'|',\n",
       " u'Programmes',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'To',\n",
       " u'BBC',\n",
       " u'Sport',\n",
       " u'>',\n",
       " u'>',\n",
       " u'|',\n",
       " u'To',\n",
       " u'BBC',\n",
       " u'Weather',\n",
       " u'>',\n",
       " u'>',\n",
       " u'|',\n",
       " u'To',\n",
       " u'BBC',\n",
       " u'World',\n",
       " u'Service',\n",
       " u'>',\n",
       " u'>',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'--',\n",
       " u'\\xa9',\n",
       " u'MMIII',\n",
       " u'|',\n",
       " u'News',\n",
       " u'Sources',\n",
       " u'|',\n",
       " u'Privacy',\n",
       " u'<',\n",
       " u'!',\n",
       " u'--',\n",
       " u'var',\n",
       " u'pCid=',\n",
       " u\"''\",\n",
       " u'uk_bbc_0',\n",
       " u\"''\",\n",
       " u';',\n",
       " u'var',\n",
       " u'w0=1',\n",
       " u';',\n",
       " u'var',\n",
       " u'refR=escape',\n",
       " u'(',\n",
       " u'document.referrer',\n",
       " u')',\n",
       " u';',\n",
       " u'if',\n",
       " u'(',\n",
       " u'refR.length',\n",
       " u'>',\n",
       " u'=252',\n",
       " u')',\n",
       " u'refR=refR.substring',\n",
       " u'(',\n",
       " u'0,252',\n",
       " u')',\n",
       " u'+',\n",
       " u\"''\",\n",
       " u'...',\n",
       " u\"''\",\n",
       " u';',\n",
       " u'//',\n",
       " u'--',\n",
       " u'>',\n",
       " u'<',\n",
       " u'!',\n",
       " u'--',\n",
       " u'var',\n",
       " u'w0=0',\n",
       " u';',\n",
       " u'//',\n",
       " u'--',\n",
       " u'>',\n",
       " u'<',\n",
       " u'!',\n",
       " u'--',\n",
       " u'if',\n",
       " u'(',\n",
       " u'w0',\n",
       " u')',\n",
       " u'{',\n",
       " u'var',\n",
       " u'imgN=',\n",
       " u\"'\",\n",
       " u'<',\n",
       " u'img',\n",
       " u'src=',\n",
       " u\"''\",\n",
       " u'http',\n",
       " u':',\n",
       " u'//server-uk.imrworldwide.com/cgi-bin/count',\n",
       " u'?',\n",
       " u\"ref='+\",\n",
       " u'refR+',\n",
       " u\"'\",\n",
       " u'&',\n",
       " u\"cid='+pCid+\",\n",
       " u\"'\",\n",
       " u\"''\",\n",
       " u'width=1',\n",
       " u'height=1',\n",
       " u'>',\n",
       " u\"'\",\n",
       " u';',\n",
       " u'if',\n",
       " u'(',\n",
       " u'navigator.userAgent.indexOf',\n",
       " u'(',\n",
       " u\"'Mac\",\n",
       " u\"'\",\n",
       " u')',\n",
       " u'!',\n",
       " u'=-1',\n",
       " u')',\n",
       " u'{',\n",
       " u'document.write',\n",
       " u'(',\n",
       " u'imgN',\n",
       " u')',\n",
       " u';',\n",
       " u'}',\n",
       " u'else',\n",
       " u'{',\n",
       " u'document.write',\n",
       " u'(',\n",
       " u\"'\",\n",
       " u'<',\n",
       " u'applet',\n",
       " u'code=',\n",
       " u\"''\",\n",
       " u'Measure.class',\n",
       " u\"''\",\n",
       " u\"'+\",\n",
       " u\"'codebase=\",\n",
       " u\"''\",\n",
       " u'http',\n",
       " u':',\n",
       " u'//server-uk.imrworldwide.com/',\n",
       " u\"''\",\n",
       " u\"'+'width=1\",\n",
       " u'height=2',\n",
       " u'>',\n",
       " u\"'+\",\n",
       " u\"'\",\n",
       " u'<',\n",
       " u'param',\n",
       " u'name=',\n",
       " u\"''\",\n",
       " u'ref',\n",
       " u\"''\",\n",
       " u'value=',\n",
       " u\"''\",\n",
       " u\"'+refR+\",\n",
       " u\"'\",\n",
       " u\"''\",\n",
       " u'>',\n",
       " u\"'+\",\n",
       " u\"'\",\n",
       " u'<',\n",
       " u'param',\n",
       " u'name=',\n",
       " u\"''\",\n",
       " u'cid',\n",
       " u\"''\",\n",
       " u'value=',\n",
       " u\"''\",\n",
       " u\"'+pCid+\",\n",
       " u\"'\",\n",
       " u\"''\",\n",
       " u'>',\n",
       " u'<',\n",
       " u'textflow',\n",
       " u'>',\n",
       " u\"'+imgN+\",\n",
       " u\"'\",\n",
       " u'<',\n",
       " u'/textflow',\n",
       " u'>',\n",
       " u'<',\n",
       " u'/applet',\n",
       " u'>',\n",
       " u\"'\",\n",
       " u')',\n",
       " u';',\n",
       " u'}',\n",
       " u'}',\n",
       " u'document.write',\n",
       " u'(',\n",
       " u'``',\n",
       " u'<',\n",
       " u'COMMENT',\n",
       " u'>',\n",
       " u\"''\",\n",
       " u')',\n",
       " u';',\n",
       " u'//',\n",
       " u'--',\n",
       " u'>',\n",
       " u'var',\n",
       " u'si',\n",
       " u'=',\n",
       " u'document.location+',\n",
       " u\"''\",\n",
       " u\"''\",\n",
       " u';',\n",
       " u'var',\n",
       " u'tsi',\n",
       " u'=',\n",
       " u'si.replace',\n",
       " u'(',\n",
       " u'``',\n",
       " u'.stm',\n",
       " u\"''\",\n",
       " u',',\n",
       " u\"''\",\n",
       " u\"''\",\n",
       " u')',\n",
       " u'.substr',\n",
       " u'(',\n",
       " u'si.length-11',\n",
       " u',',\n",
       " u'si.length',\n",
       " u')',\n",
       " u';',\n",
       " u'if',\n",
       " u'(',\n",
       " u'!',\n",
       " u'tsi.match',\n",
       " u'(',\n",
       " u'/\\\\d\\\\d\\\\d\\\\d\\\\d\\\\d\\\\d/',\n",
       " u')',\n",
       " u')',\n",
       " u'{',\n",
       " u'tsi',\n",
       " u'=',\n",
       " u'0',\n",
       " u';',\n",
       " u'}',\n",
       " u'document.write',\n",
       " u'(',\n",
       " u\"'\",\n",
       " u'<',\n",
       " u'img',\n",
       " u'src=',\n",
       " u\"''\",\n",
       " u'http',\n",
       " u':',\n",
       " u'//stats.bbc.co.uk/o.gif',\n",
       " u'?',\n",
       " u'~RS~s~RS~News~RS~t~RS~HighWeb_Legacy~RS~i~RS~',\n",
       " u\"'\",\n",
       " u'+',\n",
       " u'tsi',\n",
       " u'+',\n",
       " u\"'~RS~p~RS~0~RS~u~RS~/2/hi/health/2284783.stm~RS~r~RS~\",\n",
       " u'(',\n",
       " u'none',\n",
       " u')',\n",
       " u'~RS~a~RS~International~RS~q~RS~~RS~z~RS~37~RS~',\n",
       " u\"''\",\n",
       " u'>',\n",
       " u\"'\",\n",
       " u')',\n",
       " u';']"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from bs4 import BeautifulSoup\n",
    "raw = BeautifulSoup(html).get_text()\n",
    "tokens = word_tokenize(raw)\n",
    "tokens"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Displaying 5 of 5 matches:\n",
      "hey say too few people now carry the gene for blondes to last beyond the next \n",
      "blonde hair is caused by a recessive gene . In order for a child to have blond\n",
      " have blonde hair , it must have the gene on both sides of the family in the g\n",
      "ere is a disadvantage of having that gene or by chance . They do n't disappear\n",
      "des would disappear is if having the gene was a disadvantage and I do not thin\n"
     ]
    }
   ],
   "source": [
    "tokens = tokens[110:390]\n",
    "text = nltk.Text(tokens)\n",
    "text.concordance('gene')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "u'Language Log'"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import feedparser\n",
    "llog = feedparser.parse(\"http://languagelog.ldc.upenn.edu/nll/?feed=atom\")\n",
    "llog['feed']['title']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "13"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(llog.entries)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "u'The Bureau of Linguistical Reality'"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "post = llog.entries[2]\n",
    "post.title"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "u'<p>No, <a href=\"https://bureauoflinguisticalreality.com/\">The Bureau o'"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "content = post.content[0].value\n",
    "content[:70]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[u'No',\n",
       " u',',\n",
       " u'The',\n",
       " u'Bureau',\n",
       " u'of',\n",
       " u'Linguistical',\n",
       " u'Reality',\n",
       " u'is',\n",
       " u'not',\n",
       " u'something',\n",
       " u'dreamed',\n",
       " u'up',\n",
       " u'by',\n",
       " u'Borges',\n",
       " u',',\n",
       " u'or',\n",
       " u'the',\n",
       " u'Firesign',\n",
       " u'Theatre',\n",
       " u'.',\n",
       " u'It',\n",
       " u'actually',\n",
       " u'exists',\n",
       " u',',\n",
       " u'or',\n",
       " u'at',\n",
       " u'least',\n",
       " u'it',\n",
       " u'exists',\n",
       " u'in',\n",
       " u'the',\n",
       " u'same',\n",
       " u'state',\n",
       " u'of',\n",
       " u'electronic',\n",
       " u'virtual',\n",
       " u'actuality',\n",
       " u'as',\n",
       " u'Language',\n",
       " u'Log',\n",
       " u',',\n",
       " u'YouTube',\n",
       " u',',\n",
       " u'and',\n",
       " u'the',\n",
       " u'Wayback',\n",
       " u'Machine',\n",
       " u'.',\n",
       " u'The',\n",
       " u'Bureau',\n",
       " u'of',\n",
       " u'Linguistical',\n",
       " u'Reality',\n",
       " u'was',\n",
       " u'established',\n",
       " u'on',\n",
       " u'October',\n",
       " u'28',\n",
       " u',',\n",
       " u'2014',\n",
       " u'for',\n",
       " u'the',\n",
       " u'purpose',\n",
       " u'of',\n",
       " u'collecting',\n",
       " u',',\n",
       " u'translating',\n",
       " u'and',\n",
       " u'creating',\n",
       " u'a',\n",
       " u'new',\n",
       " u'vocabulary',\n",
       " u'for',\n",
       " u'the',\n",
       " u'Anthropocene',\n",
       " u'.',\n",
       " u'Our',\n",
       " u'species',\n",
       " u'(',\n",
       " u'Homo',\n",
       " u'Sapien',\n",
       " u')',\n",
       " u'is',\n",
       " u'experiencing',\n",
       " u'a',\n",
       " u'collective',\n",
       " u'\\u201c',\n",
       " u'loss',\n",
       " u'of',\n",
       " u'words',\n",
       " u'\\u201d',\n",
       " u'as',\n",
       " u'our',\n",
       " u'lexicon',\n",
       " u'fails',\n",
       " u'to',\n",
       " u'represent',\n",
       " u'the',\n",
       " u'emotions',\n",
       " u'and',\n",
       " u'experiences',\n",
       " u'we',\n",
       " u'are',\n",
       " u'undergoing',\n",
       " u'as',\n",
       " u'our',\n",
       " u'habitat',\n",
       " u'(',\n",
       " u'earth',\n",
       " u')',\n",
       " u'rapidly',\n",
       " u'changes',\n",
       " u'due',\n",
       " u'to',\n",
       " u'climate',\n",
       " u'change',\n",
       " u'and',\n",
       " u'other',\n",
       " u'unprecedented',\n",
       " u'events',\n",
       " u'.',\n",
       " u'To',\n",
       " u'this',\n",
       " u'end',\n",
       " u'the',\n",
       " u'The',\n",
       " u'Bureau',\n",
       " u'of',\n",
       " u'Linguistical',\n",
       " u'Reality',\n",
       " u'is',\n",
       " u'solemnly',\n",
       " u'tasked',\n",
       " u'generating',\n",
       " u'linguistic',\n",
       " u'tools',\n",
       " u'to',\n",
       " u'express',\n",
       " u'these',\n",
       " u'changes',\n",
       " u'at',\n",
       " u'the',\n",
       " u'personal',\n",
       " u'and',\n",
       " u'collective',\n",
       " u'level',\n",
       " u'.',\n",
       " u'Cartographers',\n",
       " u'are',\n",
       " u'redrawing',\n",
       " u'maps',\n",
       " u'to',\n",
       " u'accommodate',\n",
       " u'rising',\n",
       " u'seas',\n",
       " u',',\n",
       " u'psychologists',\n",
       " u'are',\n",
       " u'beginning',\n",
       " u'to',\n",
       " u'council',\n",
       " u'people',\n",
       " u'on',\n",
       " u'climate',\n",
       " u'change',\n",
       " u'related',\n",
       " u'stress',\n",
       " u',',\n",
       " u'scientists',\n",
       " u'are',\n",
       " u'defining',\n",
       " u'this',\n",
       " u'as',\n",
       " u'a',\n",
       " u'new',\n",
       " u'age',\n",
       " u'or',\n",
       " u'epoch',\n",
       " u'.',\n",
       " u'The',\n",
       " u'Bureau',\n",
       " u'was',\n",
       " u'thus',\n",
       " u'established',\n",
       " u',',\n",
       " u'as',\n",
       " u'an',\n",
       " u'interactive',\n",
       " u'conceptual',\n",
       " u'artwork',\n",
       " u'to',\n",
       " u'help',\n",
       " u'to',\n",
       " u'fill',\n",
       " u'the',\n",
       " u'linguistical',\n",
       " u'void',\n",
       " u'in',\n",
       " u'our',\n",
       " u'rapidly',\n",
       " u'changing',\n",
       " u'world',\n",
       " u'.',\n",
       " u'Some',\n",
       " u'of',\n",
       " u'the',\n",
       " u'neologisms',\n",
       " u'that',\n",
       " u'have',\n",
       " u'been',\n",
       " u'submitted',\n",
       " u'are',\n",
       " u'cutesy',\n",
       " u'blends',\n",
       " u'of',\n",
       " u'the',\n",
       " u'kind',\n",
       " u'that',\n",
       " u'you',\n",
       " u'\\u2019',\n",
       " u've',\n",
       " u'no',\n",
       " u'doubt',\n",
       " u'seen',\n",
       " u'before',\n",
       " u':',\n",
       " u'gwilt',\n",
       " u'To',\n",
       " u'cause',\n",
       " u'wilting',\n",
       " u'in',\n",
       " u'plants',\n",
       " u'by',\n",
       " u'not',\n",
       " u'providing',\n",
       " u'proper',\n",
       " u'horticultural',\n",
       " u'care',\n",
       " u'out',\n",
       " u'of',\n",
       " u'concern',\n",
       " u'for',\n",
       " u'water',\n",
       " u'consumption',\n",
       " u',',\n",
       " u'especially',\n",
       " u'during',\n",
       " u'a',\n",
       " u'time',\n",
       " u'of',\n",
       " u'drought',\n",
       " u'.',\n",
       " u'The',\n",
       " u'feeling',\n",
       " u'of',\n",
       " u'regret',\n",
       " u'and',\n",
       " u'responsibility',\n",
       " u'for',\n",
       " u'its',\n",
       " u'wilting',\n",
       " u'.',\n",
       " u'The',\n",
       " u'accompanying',\n",
       " u'compensatory',\n",
       " u'feeling',\n",
       " u'caused',\n",
       " u'by',\n",
       " u'watering',\n",
       " u'said',\n",
       " u'plants',\n",
       " u'and',\n",
       " u'experiencing',\n",
       " u'further',\n",
       " u'gwilt',\n",
       " u'for',\n",
       " u'not',\n",
       " u'practicing',\n",
       " u'water',\n",
       " u'conservation',\n",
       " u'.',\n",
       " u'This',\n",
       " u'is',\n",
       " u'a',\n",
       " u'form',\n",
       " u'of',\n",
       " u'a',\n",
       " u'Double',\n",
       " u'Bind',\n",
       " u'But',\n",
       " u'others',\n",
       " u'are',\n",
       " u'wittier',\n",
       " u'(',\n",
       " u'if',\n",
       " u'gallows',\n",
       " u'humor',\n",
       " u'can',\n",
       " u'be',\n",
       " u'thought',\n",
       " u'of',\n",
       " u'as',\n",
       " u'witty',\n",
       " u')',\n",
       " u':',\n",
       " u'pre-traumatic',\n",
       " u'stress',\n",
       " u'disorder',\n",
       " u'A',\n",
       " u'condition',\n",
       " u'in',\n",
       " u'which',\n",
       " u'a',\n",
       " u'researcher',\n",
       " u'experiences',\n",
       " u'symptoms',\n",
       " u'of',\n",
       " u'trauma',\n",
       " u'as',\n",
       " u'they',\n",
       " u'learn',\n",
       " u'more',\n",
       " u'about',\n",
       " u'the',\n",
       " u'future',\n",
       " u'as',\n",
       " u'it',\n",
       " u'pertains',\n",
       " u'to',\n",
       " u'climate',\n",
       " u'change',\n",
       " u'and',\n",
       " u'watch',\n",
       " u'the',\n",
       " u'world',\n",
       " u'around',\n",
       " u'them',\n",
       " u'not',\n",
       " u'making',\n",
       " u'necessary',\n",
       " u'precautions',\n",
       " u'.',\n",
       " u'd\\xe9j\\xe0',\n",
       " u'Sisyph\\xe9',\n",
       " u'La',\n",
       " u'sensation',\n",
       " u'famili\\xe8re',\n",
       " u'et',\n",
       " u'r\\xe9currente',\n",
       " u'd',\n",
       " u'\\u2019',\n",
       " u'\\xe9puisement',\n",
       " u'et',\n",
       " u'de',\n",
       " u'la',\n",
       " u'frustration',\n",
       " u'qu',\n",
       " u'\\u2019',\n",
       " u'une',\n",
       " u'personne',\n",
       " u'\\xe9prouve',\n",
       " u'au',\n",
       " u'moment',\n",
       " u'o\\xf9',\n",
       " u'elle',\n",
       " u'se',\n",
       " u'rend',\n",
       " u'compte',\n",
       " u'qu',\n",
       " u'\\u2019',\n",
       " u'elle',\n",
       " u'devra',\n",
       " u'expliquer\\u2014\\xe0',\n",
       " u'nouveau\\u2014une',\n",
       " u'd\\xe9couverte',\n",
       " u'scientifique',\n",
       " u'importante',\n",
       " u',',\n",
       " u'accept\\xe9e',\n",
       " u'et',\n",
       " u'd\\xe9montr\\xe9e',\n",
       " u'\\xe0',\n",
       " u'son',\n",
       " u'interlocuteur',\n",
       " u'r\\xe9ticent',\n",
       " u'et',\n",
       " u'refusant',\n",
       " u'd',\n",
       " u'\\u2019',\n",
       " u'accepter',\n",
       " u'ce',\n",
       " u'fait',\n",
       " u'.',\n",
       " u'(',\n",
       " u'Le',\n",
       " u'plus',\n",
       " u'couramment',\n",
       " u'associ\\xe9',\n",
       " u'\\xe0',\n",
       " u'l',\n",
       " u'\\u2019',\n",
       " u'explication',\n",
       " u'du',\n",
       " u'fait',\n",
       " u'que',\n",
       " u'le',\n",
       " u'changement',\n",
       " u'climatique',\n",
       " u'a',\n",
       " u'\\xe9t\\xe9',\n",
       " u'g\\xe9n\\xe9r\\xe9',\n",
       " u'par',\n",
       " u'l',\n",
       " u'\\u2019',\n",
       " u'activit\\xe9',\n",
       " u'humaine',\n",
       " u')',\n",
       " u'A',\n",
       " u'recurring',\n",
       " u'sensation',\n",
       " u'of',\n",
       " u'exhaustion',\n",
       " u'and',\n",
       " u'frustration',\n",
       " u'one',\n",
       " u'experiences',\n",
       " u'during',\n",
       " u'a',\n",
       " u'conversation',\n",
       " u'in',\n",
       " u'the',\n",
       " u'moment',\n",
       " u'they',\n",
       " u'realize',\n",
       " u'they',\n",
       " u'will',\n",
       " u'need',\n",
       " u'to',\n",
       " u'explain',\n",
       " u'again\\u2014a',\n",
       " u'proven',\n",
       " u',',\n",
       " u'accepted',\n",
       " u'and',\n",
       " u'important',\n",
       " u'scientific',\n",
       " u'finding',\n",
       " u'to',\n",
       " u'the',\n",
       " u'person',\n",
       " u'with',\n",
       " u'whom',\n",
       " u'they',\n",
       " u'are',\n",
       " u'talking',\n",
       " u'.',\n",
       " u'(',\n",
       " u'Usually',\n",
       " u'associated',\n",
       " u'with',\n",
       " u'manmade',\n",
       " u'climate',\n",
       " u'change',\n",
       " u'.',\n",
       " u')',\n",
       " u'Some',\n",
       " u'of',\n",
       " u'the',\n",
       " u'words',\n",
       " u'describe',\n",
       " u'sensations',\n",
       " u'and',\n",
       " u'feelings',\n",
       " u'that',\n",
       " u'I',\n",
       " u'assume',\n",
       " u'are',\n",
       " u'experienced',\n",
       " u'only',\n",
       " u'by',\n",
       " u'those',\n",
       " u'in',\n",
       " u'a',\n",
       " u'narrow',\n",
       " u'segment',\n",
       " u'of',\n",
       " u'the',\n",
       " u'population',\n",
       " u',',\n",
       " u'while',\n",
       " u'others',\n",
       " u'describe',\n",
       " u'experiences',\n",
       " u'that',\n",
       " u'are',\n",
       " u'probably',\n",
       " u'more',\n",
       " u'widely',\n",
       " u'shared',\n",
       " u':',\n",
       " u'soltactiphoria',\n",
       " u'The',\n",
       " u'euphoria',\n",
       " u'a',\n",
       " u'farmer',\n",
       " u'experiences',\n",
       " u'when',\n",
       " u's/he',\n",
       " u'gathers',\n",
       " u'soil',\n",
       " u'from',\n",
       " u'the',\n",
       " u'ground',\n",
       " u'with',\n",
       " u'their',\n",
       " u'naked',\n",
       " u'hands',\n",
       " u',',\n",
       " u'assesses',\n",
       " u'the',\n",
       " u'soil',\n",
       " u'quality',\n",
       " u'with',\n",
       " u'the',\n",
       " u'highly',\n",
       " u'sensitive',\n",
       " u'skin',\n",
       " u'of',\n",
       " u'their',\n",
       " u'finger',\n",
       " u'tips',\n",
       " u',',\n",
       " u'breathes',\n",
       " u'in',\n",
       " u'the',\n",
       " u'aromas',\n",
       " u'of',\n",
       " u'the',\n",
       " u'soil',\n",
       " u'and',\n",
       " u'experiences',\n",
       " u'a',\n",
       " u'soil',\n",
       " u'\\u201c',\n",
       " u'high',\n",
       " u'\\u201d',\n",
       " u'when',\n",
       " u'the',\n",
       " u'commingling',\n",
       " u'of',\n",
       " u'all',\n",
       " u'of',\n",
       " u'these',\n",
       " u'senses',\n",
       " u'is',\n",
       " u'accentuated',\n",
       " u'by',\n",
       " u'the',\n",
       " u'ancient',\n",
       " u',',\n",
       " u'learned',\n",
       " u',',\n",
       " u'earned',\n",
       " u'knowledge',\n",
       " u'that',\n",
       " u'this',\n",
       " u'is',\n",
       " u'indeed',\n",
       " u'a',\n",
       " u'rich',\n",
       " u',',\n",
       " u'nourishing',\n",
       " u',',\n",
       " u'life',\n",
       " u'giving',\n",
       " u'soil',\n",
       " u'.',\n",
       " u'psychic',\n",
       " u'corpus',\n",
       " u'dissonance',\n",
       " u'A',\n",
       " u'term',\n",
       " u'to',\n",
       " u'express',\n",
       " u'the',\n",
       " u'conflict',\n",
       " u'between',\n",
       " u'mind',\n",
       " u'and',\n",
       " u'body',\n",
       " u'that',\n",
       " u'occurs',\n",
       " u'when',\n",
       " u'a',\n",
       " u'person',\n",
       " u'experiences',\n",
       " u'unusually',\n",
       " u'warm',\n",
       " u'weather',\n",
       " u'during',\n",
       " u'a',\n",
       " u'time',\n",
       " u'that',\n",
       " u'has',\n",
       " u'historically',\n",
       " u'been',\n",
       " u'considered',\n",
       " u'winter',\n",
       " u'.',\n",
       " u'In',\n",
       " u'this',\n",
       " u'state',\n",
       " u'the',\n",
       " u'body',\n",
       " u'experiences',\n",
       " u'ecstasy',\n",
       " u'to',\n",
       " u'be',\n",
       " u'in',\n",
       " u'unusually',\n",
       " u'warm',\n",
       " u'weather',\n",
       " u'while',\n",
       " u',',\n",
       " u'simultaneously',\n",
       " u',',\n",
       " u'the',\n",
       " u'mind',\n",
       " u'experiences',\n",
       " u'worry',\n",
       " u'and',\n",
       " u'concern',\n",
       " u'that',\n",
       " u'weather',\n",
       " u'patterns',\n",
       " u'are',\n",
       " u'deeply',\n",
       " u'amiss',\n",
       " u',',\n",
       " u'often',\n",
       " u'resulting',\n",
       " u'in',\n",
       " u'a',\n",
       " u'sensation',\n",
       " u'akin',\n",
       " u'to',\n",
       " u'guilt',\n",
       " u'or',\n",
       " u'guilty',\n",
       " u'pleasure',\n",
       " u'.',\n",
       " u'And',\n",
       " u'then',\n",
       " u'there',\n",
       " u'\\u2019',\n",
       " u's',\n",
       " u'this',\n",
       " u'one',\n",
       " u'(',\n",
       " u'which',\n",
       " u'I',\n",
       " u'think',\n",
       " u'comes',\n",
       " u'from',\n",
       " u'the',\n",
       " u'little-known',\n",
       " u'field',\n",
       " u'of',\n",
       " u'speculative',\n",
       " u'lexicography',\n",
       " u')',\n",
       " u',',\n",
       " u'in',\n",
       " u'which',\n",
       " u'the',\n",
       " u'word',\n",
       " u'\\u2019',\n",
       " u's',\n",
       " u'most',\n",
       " u'basic',\n",
       " u'sense',\n",
       " u'reflects',\n",
       " u'a',\n",
       " u'transformation',\n",
       " u'from',\n",
       " u'stench',\n",
       " u'to',\n",
       " u'sweetness',\n",
       " u',',\n",
       " u'and',\n",
       " u'the',\n",
       " u'relationships',\n",
       " u'between',\n",
       " u'the',\n",
       " u'word',\n",
       " u'\\u2019',\n",
       " u's',\n",
       " u'various',\n",
       " u'senses',\n",
       " u'display',\n",
       " u'a',\n",
       " u'continuum',\n",
       " u'of',\n",
       " u'increasing',\n",
       " u'abstraction',\n",
       " u':',\n",
       " u'Werr\\xedng',\n",
       " u'1',\n",
       " u'.',\n",
       " u'The',\n",
       " u'seemingly',\n",
       " u'miraculous',\n",
       " u'moment',\n",
       " u'of',\n",
       " u'transition',\n",
       " u'when',\n",
       " u'compost',\n",
       " u'turns',\n",
       " u'from',\n",
       " u'smelling',\n",
       " u'the',\n",
       " u'most',\n",
       " u'rank',\n",
       " u'to',\n",
       " u'smelling',\n",
       " u'sweet',\n",
       " u';',\n",
       " u'the',\n",
       " u'becoming',\n",
       " u'of',\n",
       " u'fertile',\n",
       " u'soil',\n",
       " u'full',\n",
       " u'of',\n",
       " u'life',\n",
       " u'.',\n",
       " u'This',\n",
       " u'involves',\n",
       " u'a',\n",
       " u'sort',\n",
       " u'of',\n",
       " u'tuning',\n",
       " u'where',\n",
       " u'the',\n",
       " u'frequency',\n",
       " u'of',\n",
       " u'the',\n",
       " u'matter',\n",
       " u'itself',\n",
       " u'changes',\n",
       " u',',\n",
       " u'it',\n",
       " u'is',\n",
       " u'the',\n",
       " u'edge',\n",
       " u'of',\n",
       " u'transition',\n",
       " u',',\n",
       " u'like',\n",
       " u'the',\n",
       " u'rim',\n",
       " u'of',\n",
       " u'a',\n",
       " u'glass',\n",
       " u'.',\n",
       " u'A',\n",
       " u'recognition',\n",
       " u'within',\n",
       " u'it',\n",
       " u'that',\n",
       " u'this',\n",
       " u'moment',\n",
       " u',',\n",
       " u'which',\n",
       " u'seems',\n",
       " u'like',\n",
       " u'magic',\n",
       " u',',\n",
       " u'is',\n",
       " u'the',\n",
       " u'alchemical',\n",
       " u'work',\n",
       " u'of',\n",
       " u'bacteria',\n",
       " u',',\n",
       " u'worms',\n",
       " u',',\n",
       " u'fungi',\n",
       " u'and',\n",
       " u'other',\n",
       " u'organisms',\n",
       " u'that',\n",
       " u'are',\n",
       " u'not',\n",
       " u'typically',\n",
       " u'associated',\n",
       " u'with',\n",
       " u'magic',\n",
       " u'.',\n",
       " u'An',\n",
       " u'acknowledgement',\n",
       " u'that',\n",
       " u'death',\n",
       " u'and',\n",
       " u'decay',\n",
       " u'are',\n",
       " u'the',\n",
       " u'necessary',\n",
       " u'fodder',\n",
       " u'for',\n",
       " u'life',\n",
       " u',',\n",
       " u'growth',\n",
       " u'and',\n",
       " u'beauty',\n",
       " u'.',\n",
       " u'2',\n",
       " u'.',\n",
       " u'A',\n",
       " u'collective',\n",
       " u'moment',\n",
       " u'of',\n",
       " u'transformation',\n",
       " u'when',\n",
       " u'what',\n",
       " u'has',\n",
       " u'seemed',\n",
       " u'mired',\n",
       " u',',\n",
       " u'foul',\n",
       " u'and',\n",
       " u'utterly',\n",
       " u'messed',\n",
       " u'up',\n",
       " u'in',\n",
       " u'a',\n",
       " u'society',\n",
       " u'turns',\n",
       " u'into',\n",
       " u'a',\n",
       " u'progressive',\n",
       " u'and',\n",
       " u'uniting',\n",
       " u'force',\n",
       " u'.',\n",
       " u'Where',\n",
       " u'rotting',\n",
       " u'structures',\n",
       " u'and',\n",
       " u'ideologies',\n",
       " u'are',\n",
       " u'turned',\n",
       " u'into',\n",
       " u'fertile',\n",
       " u'ground',\n",
       " u'for',\n",
       " u'new',\n",
       " u'growth',\n",
       " u'.',\n",
       " u'I.e',\n",
       " u'.',\n",
       " u'the',\n",
       " u'compost',\n",
       " u'empire',\n",
       " u'or',\n",
       " u'compost',\n",
       " u'capitalism',\n",
       " u'3',\n",
       " u'.',\n",
       " u'A',\n",
       " u'feature',\n",
       " u'of',\n",
       " u'the',\n",
       " u'collective',\n",
       " u'psychological',\n",
       " u'landscape',\n",
       " u'wherein',\n",
       " u'what',\n",
       " u'has',\n",
       " u'been',\n",
       " u'foul',\n",
       " u'transforms',\n",
       " u'into',\n",
       " u'that',\n",
       " u'which',\n",
       " u'is',\n",
       " u'divine',\n",
       " u'.',\n",
       " u'The',\n",
       " u'project',\n",
       " u'sees',\n",
       " u'itself',\n",
       " u'as',\n",
       " u'practicing',\n",
       " u'a',\n",
       " u'form',\n",
       " u'of',\n",
       " u'Whorfianism',\n",
       " u':',\n",
       " u'For',\n",
       " u'centuries',\n",
       " u'philosophers',\n",
       " u',',\n",
       " u'linguists',\n",
       " u',',\n",
       " u'psychologists',\n",
       " u'and',\n",
       " u'others',\n",
       " u'have',\n",
       " u'noted',\n",
       " u'the',\n",
       " u'power',\n",
       " u'of',\n",
       " u'words',\n",
       " u'to',\n",
       " u'influence',\n",
       " u'people',\n",
       " u'\\u2019',\n",
       " u's',\n",
       " u'thoughts',\n",
       " u'and',\n",
       " u'actions',\n",
       " u'and',\n",
       " u'vice',\n",
       " u'versa',\n",
       " u'.',\n",
       " u'A',\n",
       " u'principal',\n",
       " u'called',\n",
       " u'linguistic',\n",
       " u'relativity',\n",
       " u'(',\n",
       " u'also',\n",
       " u'known',\n",
       " u'as',\n",
       " u'the',\n",
       " u'Sapir-Whorf',\n",
       " u'hypothesis',\n",
       " u')',\n",
       " u',',\n",
       " u'holds',\n",
       " u'that',\n",
       " u'language',\n",
       " u'affects',\n",
       " u'the',\n",
       " u'very',\n",
       " u'ways',\n",
       " u'in',\n",
       " u'which',\n",
       " u'its',\n",
       " u'respective',\n",
       " u'speakers',\n",
       " u'conceptualize',\n",
       " u'their',\n",
       " u'entire',\n",
       " u'world',\n",
       " u',',\n",
       " u'in',\n",
       " u'short',\n",
       " u'their',\n",
       " u'cognitive',\n",
       " u'processes',\n",
       " u'which',\n",
       " u'often',\n",
       " u'inform',\n",
       " u'their',\n",
       " u'actions',\n",
       " u'.',\n",
       " u'It',\n",
       " u'is',\n",
       " u'from',\n",
       " u'the',\n",
       " u'term',\n",
       " u',',\n",
       " u'linguistic',\n",
       " u'relativity',\n",
       " u',',\n",
       " u'that',\n",
       " u'The',\n",
       " u'Bureau',\n",
       " u'of',\n",
       " u'Linguistical',\n",
       " u'Reality',\n",
       " u'takes',\n",
       " u'its',\n",
       " u'name',\n",
       " u'.',\n",
       " u'We',\n",
       " u'reference',\n",
       " u'this',\n",
       " u'term',\n",
       " u'playfully',\n",
       " u'but',\n",
       " u'believe',\n",
       " u'sincerely',\n",
       " u'that',\n",
       " u'until',\n",
       " u'we',\n",
       " u'have',\n",
       " u'the',\n",
       " ...]"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "raw = BeautifulSoup(content).get_text()\n",
    "word_tokenize(raw)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "f = open('document.txt')\n",
    "raw = f.read()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['.DS_Store',\n",
       " '.ipynb_checkpoints',\n",
       " 'DATA',\n",
       " 'document.txt',\n",
       " 'nltk_data',\n",
       " 'Pratik_Dhungel_Lab1.ipynb',\n",
       " 'Pratik_Dhungel_Lab2.ipynb',\n",
       " 'Pratik_Dhungel_Lab3.ipynb']"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import os\n",
    "os.listdir('.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'pip is a package management system used to install and manage software packages written in Python. Many packages can be found in the default source for packages and their dependencies \\xe2\\x80\\x94 Python Package Index.'"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "raw"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "pip is a package management system used to install and manage software packages written in Python. Many packages can be found in the default source for packages and their dependencies — Python Package Index.\n"
     ]
    }
   ],
   "source": [
    "f = open('document.txt', 'rU')\n",
    "for line in f:\n",
    "    print(line.strip())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "path = nltk.data.find('corpora/gutenberg/melville-moby_dick.txt')\n",
    "raw = open(path, 'rU').read()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter some text: \" On an exceptionally hot evening early in July\"\n"
     ]
    }
   ],
   "source": [
    "s = input(\"Enter some text: \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You typed 8 words.\n"
     ]
    }
   ],
   "source": [
    "print \"You typed\", len(word_tokenize(s)), \"words.\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "str"
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "raw = open('document.txt').read()\n",
    "type(raw)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "list"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tokens = word_tokenize(raw)\n",
    "type(tokens)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "list"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "words = [w.lower() for w in tokens]\n",
    "type(words)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "list"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "vocab = sorted(set(words))\n",
    "type(vocab)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "'str' object has no attribute 'append'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-74-b119f51d0980>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0mvocab\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'blog'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m \u001b[0mraw\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'blog'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mAttributeError\u001b[0m: 'str' object has no attribute 'append'"
     ]
    }
   ],
   "source": [
    "vocab.append('blog')\n",
    "raw.append('blog')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "cannot concatenate 'str' and 'list' objects",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-75-18d639fce0a0>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0mquery\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m'Who knows?'\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0mbeatles\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m[\u001b[0m\u001b[0;34m'john'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'paul'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'george'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'ringo'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 3\u001b[0;31m \u001b[0mquery\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0mbeatles\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m: cannot concatenate 'str' and 'list' objects"
     ]
    }
   ],
   "source": [
    "query = 'Who knows?'\n",
    "beatles = ['john', 'paul', 'george', 'ringo']\n",
    "query + beatles"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Monty Python'"
      ]
     },
     "execution_count": 77,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "monty = 'Monty Python'\n",
    "monty"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"Monty Python's Flying Circus\""
      ]
     },
     "execution_count": 79,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "circus = \"Monty Python's Flying Circus\"\n",
    "circus"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"Monty Python's Flying Circus\""
      ]
     },
     "execution_count": 80,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "circus = 'Monty Python\\'s Flying Circus' \n",
    "circus"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-82-d481af75953d>, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-82-d481af75953d>\"\u001b[0;36m, line \u001b[0;32m1\u001b[0m\n\u001b[0;31m    circus = 'Monty Python's Flying Circus'\u001b[0m\n\u001b[0m                           ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "circus = 'Monty Python's Flying Circus'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Shall I compare thee to a Summer's day?Thou are more lovely and more temperate:\n"
     ]
    }
   ],
   "source": [
    "couplet = \"Shall I compare thee to a Summer's day?\"\\\n",
    "           \"Thou are more lovely and more temperate:\"\n",
    "print(couplet)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Shall I compare thee to a Summer's day?Thou are more lovely and more temperate:\n"
     ]
    }
   ],
   "source": [
    "ouplet = (\"Rough winds do shake the darling buds of May,\"\n",
    "          \"And Summer's lease hath all too short a date:\")\n",
    "print(couplet)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Shall I compare thee to a Summer's day?\n",
      "Thou are more lovely and more temperate:\n"
     ]
    }
   ],
   "source": [
    "couplet = \"\"\"Shall I compare thee to a Summer's day?\n",
    "Thou are more lovely and more temperate:\"\"\"\n",
    "print(couplet)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Rough winds do shake the darling buds of May,\n",
      "And Summer's lease hath all too short a date:\n"
     ]
    }
   ],
   "source": [
    "couplet = '''Rough winds do shake the darling buds of May,\n",
    "And Summer's lease hath all too short a date:'''\n",
    "print(couplet)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'veryveryvery'"
      ]
     },
     "execution_count": 88,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'very' + 'very' + 'very'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'veryveryvery'"
      ]
     },
     "execution_count": 89,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'very' * 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "            very\n",
      "          veryvery\n",
      "        veryveryvery\n",
      "      veryveryveryvery\n",
      "    veryveryveryveryvery\n",
      "  veryveryveryveryveryvery\n",
      "veryveryveryveryveryveryvery\n",
      "  veryveryveryveryveryvery\n",
      "    veryveryveryveryvery\n",
      "      veryveryveryvery\n",
      "        veryveryvery\n",
      "          veryvery\n",
      "            very\n"
     ]
    }
   ],
   "source": [
    "a = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1]\n",
    "b = [' ' * 2 * (7 - i) + 'very' * i for i in a]\n",
    "for line in b:\n",
    "     print(line)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Monty Python\n"
     ]
    }
   ],
   "source": [
    " print(monty)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Monty PythonHoly Grail\n"
     ]
    }
   ],
   "source": [
    "grail = 'Holy Grail'\n",
    "print(monty + grail)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('Monty Python', 'Holy Grail')\n"
     ]
    }
   ],
   "source": [
    "print(monty, grail)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Monty Python and the Holy Grail\n"
     ]
    }
   ],
   "source": [
    "print monty, \"and the\", grail"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'M'"
      ]
     },
     "execution_count": 98,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "monty[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'t'"
      ]
     },
     "execution_count": 99,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "monty[3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "' '"
      ]
     },
     "execution_count": 100,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "monty[5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'n'"
      ]
     },
     "execution_count": 101,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "monty[-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "' '"
      ]
     },
     "execution_count": 102,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "monty[5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "' '"
      ]
     },
     "execution_count": 103,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "monty[-7]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "c o l o r l e s s   g r e e n   i d e a s   s l e e p   f u r i o u s l y\n"
     ]
    }
   ],
   "source": [
    "sent = 'colorless green ideas sleep furiously'\n",
    "for char in sent:\n",
    "    print char,"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[(u'e', 117092), (u't', 87996), (u'a', 77916), (u'o', 69326), (u'n', 65617)]"
      ]
     },
     "execution_count": 109,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from nltk.corpus import gutenberg\n",
    "raw = gutenberg.raw('melville-moby_dick.txt')\n",
    "fdist = nltk.FreqDist(ch.lower() for ch in raw if ch.isalpha())\n",
    "fdist.most_common(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[u'e',\n",
       " u't',\n",
       " u'a',\n",
       " u'o',\n",
       " u'n',\n",
       " u'i',\n",
       " u's',\n",
       " u'h',\n",
       " u'r',\n",
       " u'l',\n",
       " u'd',\n",
       " u'u',\n",
       " u'm',\n",
       " u'c',\n",
       " u'w',\n",
       " u'f',\n",
       " u'g',\n",
       " u'p',\n",
       " u'b',\n",
       " u'y',\n",
       " u'v',\n",
       " u'k',\n",
       " u'q',\n",
       " u'j',\n",
       " u'x',\n",
       " u'z']"
      ]
     },
     "execution_count": 110,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[char for (char, count) in fdist.most_common()]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Pyth'"
      ]
     },
     "execution_count": 111,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "monty[6:10]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Monty'"
      ]
     },
     "execution_count": 112,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "monty[-12:-7]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Monty'"
      ]
     },
     "execution_count": 113,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "monty[:5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Python'"
      ]
     },
     "execution_count": 114,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "monty[6:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "found \"thing\"\n"
     ]
    }
   ],
   "source": [
    "phrase = 'And now for something completely different'\n",
    "if 'thing' in phrase:\n",
    "     print 'found \"thing\"'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6"
      ]
     },
     "execution_count": 116,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "monty.find('Python')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 118,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'o'"
      ]
     },
     "execution_count": 118,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "query = 'Who knows?'\n",
    "beatles = ['John', 'Paul', 'George', 'Ringo']\n",
    "query[2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 119,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Wh'"
      ]
     },
     "execution_count": 119,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "query[:2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 120,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['John', 'Paul']"
      ]
     },
     "execution_count": 120,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "beatles[:2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"Who knows? I don't\""
      ]
     },
     "execution_count": 127,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "query +  \" I don't\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "can only concatenate list (not \"str\") to list",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-128-fa447bb3f680>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mbeatles\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0;34m'Brian'\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m: can only concatenate list (not \"str\") to list"
     ]
    }
   ],
   "source": [
    "beatles + 'Brian'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 130,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['John', 'Paul', 'George', 'Ringo', 'Pete']"
      ]
     },
     "execution_count": 130,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "beatles + ['Pete']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['John Lennon', 'Paul', 'George']"
      ]
     },
     "execution_count": 131,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "beatles[0] = \"John Lennon\"\n",
    "del beatles[-1]\n",
    "beatles"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Pruska Biblioteka Państwowa. Jej dawne zbiory znane pod nazwą\n",
      "\"Berlinka\" to skarb kultury i sztuki niemieckiej. Przewiezione przez\n",
      "Niemców pod koniec II wojny światowej na Dolny Śląsk, zostały\n",
      "odnalezione po 1945 r. na terytorium Polski. Trafiły do Biblioteki\n",
      "Jagiellońskiej w Krakowie, obejmują ponad 500 tys. zabytkowych\n",
      "archiwaliów, m.in. manuskrypty Goethego, Mozarta, Beethovena, Bacha.\n"
     ]
    }
   ],
   "source": [
    "import io\n",
    "path = nltk.data.find('corpora/unicode_samples/polish-lat2.txt')\n",
    "f = io.open(path, encoding = 'latin2')\n",
    "for line in f:\n",
    "    line = line.strip()\n",
    "    print(line)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Pruska Biblioteka Pa\\u0144stwowa. Jej dawne zbiory znane pod nazw\\u0105\n",
      "\"Berlinka\" to skarb kultury i sztuki niemieckiej. Przewiezione przez\n",
      "Niemc\\xf3w pod koniec II wojny \\u015bwiatowej na Dolny \\u015al\\u0105sk, zosta\\u0142y\n",
      "odnalezione po 1945 r. na terytorium Polski. Trafi\\u0142y do Biblioteki\n",
      "Jagiello\\u0144skiej w Krakowie, obejmuj\\u0105 ponad 500 tys. zabytkowych\n",
      "archiwali\\xf3w, m.in. manuskrypty Goethego, Mozarta, Beethovena, Bacha.\n"
     ]
    }
   ],
   "source": [
    "f = io.open(path, encoding='latin2')\n",
    "for line in f:\n",
    "     line = line.strip()\n",
    "     print(line.encode('unicode_escape'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "ord() expected a character, but string of length 2 found",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-19-d06069f4e4cf>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mord\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'ń'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m: ord() expected a character, but string of length 2 found"
     ]
    }
   ],
   "source": [
    "ord('ń')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'\\\\u0144'"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "nacute = '\\u0144'\n",
    "nacute "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'\\\\u0144'"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "nacute.encode('utf8')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Niemc\\xf3w pod koniec II wojny \\u015bwiatowej na Dolny \\u015al\\u0105sk, zosta\\u0142y\\n\n"
     ]
    }
   ],
   "source": [
    "import unicodedata\n",
    "lines = io.open(path, encoding='latin2').readlines()\n",
    "line = lines[2]\n",
    "print(line.encode('unicode_escape'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ó U+00f3 LATIN SMALL LETTER O WITH ACUTE\n",
      "ś U+015b LATIN SMALL LETTER S WITH ACUTE\n",
      "Ś U+015a LATIN CAPITAL LETTER S WITH ACUTE\n",
      "ą U+0105 LATIN SMALL LETTER A WITH OGONEK\n",
      "ł U+0142 LATIN SMALL LETTER L WITH STROKE\n"
     ]
    }
   ],
   "source": [
    "for c in line:\n",
    "     if ord(c) > 127:\n",
    "         print('{} U+{:04x} {}'.format(c.encode('utf8'), ord(c), unicodedata.name(c)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-1"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    " line.find('zosta\\u0142y')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "u'niemc\\xf3w pod koniec ii wojny \\u015bwiatowej na dolny \\u015bl\\u0105sk, zosta\\u0142y\\n'"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "line = line.lower()\n",
    "line"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'niemc\\\\xf3w pod koniec ii wojny \\\\u015bwiatowej na dolny \\\\u015bl\\\\u0105sk, zosta\\\\u0142y\\\\n'"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "line.encode('unicode_escape')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import re\n",
    "m = re.search('\\u015b\\w*', line)\n",
    "m"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[u'niemc\\xf3w',\n",
       " u'pod',\n",
       " u'koniec',\n",
       " u'ii',\n",
       " u'wojny',\n",
       " u'\\u015bwiatowej',\n",
       " u'na',\n",
       " u'dolny',\n",
       " u'\\u015bl\\u0105sk',\n",
       " u',',\n",
       " u'zosta\\u0142y']"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "word_tokenize(line)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import re\n",
    "wordlist = [w for w in nltk.corpus.words.words('en') if w.islower()]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[u'abaissed',\n",
       " u'abandoned',\n",
       " u'abased',\n",
       " u'abashed',\n",
       " u'abatised',\n",
       " u'abed',\n",
       " u'aborted',\n",
       " u'abridged',\n",
       " u'abscessed',\n",
       " u'absconded',\n",
       " u'absorbed',\n",
       " u'abstracted',\n",
       " u'abstricted',\n",
       " u'accelerated',\n",
       " u'accepted',\n",
       " u'accidented',\n",
       " u'accoladed',\n",
       " u'accolated',\n",
       " u'accomplished',\n",
       " u'accosted',\n",
       " u'accredited',\n",
       " u'accursed',\n",
       " u'accused',\n",
       " u'accustomed',\n",
       " u'acetated',\n",
       " u'acheweed',\n",
       " u'aciculated',\n",
       " u'aciliated',\n",
       " u'acknowledged',\n",
       " u'acorned',\n",
       " u'acquainted',\n",
       " u'acquired',\n",
       " u'acquisited',\n",
       " u'acred',\n",
       " u'aculeated',\n",
       " u'addebted',\n",
       " u'added',\n",
       " u'addicted',\n",
       " u'addlebrained',\n",
       " u'addleheaded',\n",
       " u'addlepated',\n",
       " u'addorsed',\n",
       " u'adempted',\n",
       " u'adfected',\n",
       " u'adjoined',\n",
       " u'admired',\n",
       " u'admitted',\n",
       " u'adnexed',\n",
       " u'adopted',\n",
       " u'adossed',\n",
       " u'adreamed',\n",
       " u'adscripted',\n",
       " u'aduncated',\n",
       " u'advanced',\n",
       " u'advised',\n",
       " u'aeried',\n",
       " u'aethered',\n",
       " u'afeared',\n",
       " u'affected',\n",
       " u'affectioned',\n",
       " u'affined',\n",
       " u'afflicted',\n",
       " u'affricated',\n",
       " u'affrighted',\n",
       " u'affronted',\n",
       " u'aforenamed',\n",
       " u'afterfeed',\n",
       " u'aftershafted',\n",
       " u'afterthoughted',\n",
       " u'afterwitted',\n",
       " u'agazed',\n",
       " u'aged',\n",
       " u'agglomerated',\n",
       " u'aggrieved',\n",
       " u'agminated',\n",
       " u'agnamed',\n",
       " u'agonied',\n",
       " u'agreed',\n",
       " u'agueweed',\n",
       " u'ahungered',\n",
       " u'aiguilletted',\n",
       " u'ailweed',\n",
       " u'airbrained',\n",
       " u'airified',\n",
       " u'aiseweed',\n",
       " u'aisled',\n",
       " u'alarmed',\n",
       " u'alated',\n",
       " u'alimonied',\n",
       " u'aliped',\n",
       " u'alleyed',\n",
       " u'allied',\n",
       " u'alligatored',\n",
       " u'allseed',\n",
       " u'almsdeed',\n",
       " u'aloed',\n",
       " u'altared',\n",
       " u'alveolated',\n",
       " u'amazed',\n",
       " u'ameed',\n",
       " u'amiced',\n",
       " u'amphitheatered',\n",
       " u'ampullated',\n",
       " u'amused',\n",
       " u'anchored',\n",
       " u'angled',\n",
       " u'anguiped',\n",
       " u'anguished',\n",
       " u'angulated',\n",
       " u'angulinerved',\n",
       " u'anhungered',\n",
       " u'animated',\n",
       " u'aniseed',\n",
       " u'annodated',\n",
       " u'annulated',\n",
       " u'anomaliped',\n",
       " u'anserated',\n",
       " u'anteflected',\n",
       " u'anteflexed',\n",
       " u'antimoniated',\n",
       " u'antimoniureted',\n",
       " u'antimoniuretted',\n",
       " u'antiquated',\n",
       " u'antired',\n",
       " u'antiweed',\n",
       " u'antlered',\n",
       " u'apertured',\n",
       " u'apexed',\n",
       " u'apicifixed',\n",
       " u'apiculated',\n",
       " u'apocopated',\n",
       " u'apostrophied',\n",
       " u'appearanced',\n",
       " u'appellatived',\n",
       " u'appendaged',\n",
       " u'appendiculated',\n",
       " u'applied',\n",
       " u'appressed',\n",
       " u'aralkylated',\n",
       " u'arbored',\n",
       " u'arched',\n",
       " u'architraved',\n",
       " u'arcked',\n",
       " u'arcuated',\n",
       " u'ared',\n",
       " u'areolated',\n",
       " u'ariled',\n",
       " u'arillated',\n",
       " u'armchaired',\n",
       " u'armed',\n",
       " u'armied',\n",
       " u'armillated',\n",
       " u'armored',\n",
       " u'armoried',\n",
       " u'arpeggiated',\n",
       " u'arpeggioed',\n",
       " u'arrased',\n",
       " u'arrowed',\n",
       " u'arrowheaded',\n",
       " u'arrowweed',\n",
       " u'arseneted',\n",
       " u'arsenetted',\n",
       " u'arseniureted',\n",
       " u'articled',\n",
       " u'articulated',\n",
       " u'ashamed',\n",
       " u'ashlared',\n",
       " u'ashweed',\n",
       " u'aspersed',\n",
       " u'asphyxied',\n",
       " u'assented',\n",
       " u'assessed',\n",
       " u'assigned',\n",
       " u'assistanted',\n",
       " u'associated',\n",
       " u'assonanced',\n",
       " u'assorted',\n",
       " u'assumed',\n",
       " u'assured',\n",
       " u'asteriated',\n",
       " u'astonied',\n",
       " u'aswooned',\n",
       " u'atrophiated',\n",
       " u'atrophied',\n",
       " u'attached',\n",
       " u'attired',\n",
       " u'attrited',\n",
       " u'augmented',\n",
       " u'aurated',\n",
       " u'auricled',\n",
       " u'auriculated',\n",
       " u'authorized',\n",
       " u'autoinhibited',\n",
       " u'autosensitized',\n",
       " u'autosled',\n",
       " u'averted',\n",
       " u'avowed',\n",
       " u'awearied',\n",
       " u'awned',\n",
       " u'awninged',\n",
       " u'axed',\n",
       " u'axhammered',\n",
       " u'axised',\n",
       " u'axled',\n",
       " u'axseed',\n",
       " u'axweed',\n",
       " u'azoted',\n",
       " u'azured',\n",
       " u'babied',\n",
       " u'babished',\n",
       " u'babyfied',\n",
       " u'baccated',\n",
       " u'backboned',\n",
       " u'backed',\n",
       " u'backhanded',\n",
       " u'backwatered',\n",
       " u'baconweed',\n",
       " u'badgerweed',\n",
       " u'bagged',\n",
       " u'bagwigged',\n",
       " u'baked',\n",
       " u'balanced',\n",
       " u'balconied',\n",
       " u'baldachined',\n",
       " u'baldricked',\n",
       " u'balled',\n",
       " u'ballweed',\n",
       " u'balsamweed',\n",
       " u'balustered',\n",
       " u'balustraded',\n",
       " u'bandannaed',\n",
       " u'banded',\n",
       " u'bandoleered',\n",
       " u'bangled',\n",
       " u'banked',\n",
       " u'bankweed',\n",
       " u'bannered',\n",
       " u'barbated',\n",
       " u'barbed',\n",
       " u'barebacked',\n",
       " u'bareboned',\n",
       " u'barefaced',\n",
       " u'barefooted',\n",
       " u'barehanded',\n",
       " u'bareheaded',\n",
       " u'barelegged',\n",
       " u'barenecked',\n",
       " u'barmybrained',\n",
       " u'barred',\n",
       " u'barreled',\n",
       " u'bartizaned',\n",
       " u'basebred',\n",
       " u'based',\n",
       " u'basehearted',\n",
       " u'basifixed',\n",
       " u'basilweed',\n",
       " u'basined',\n",
       " u'basinerved',\n",
       " u'basqued',\n",
       " u'bastioned',\n",
       " u'bated',\n",
       " u'bathroomed',\n",
       " u'battered',\n",
       " u'batteried',\n",
       " u'battled',\n",
       " u'battlemented',\n",
       " u'bayed',\n",
       " u'bayoneted',\n",
       " u'beached',\n",
       " u'beaded',\n",
       " u'beaked',\n",
       " u'bealtared',\n",
       " u'beamed',\n",
       " u'beanweed',\n",
       " u'beaproned',\n",
       " u'bearded',\n",
       " u'beautied',\n",
       " u'beavered',\n",
       " u'beballed',\n",
       " u'bebannered',\n",
       " u'bebed',\n",
       " u'bebelted',\n",
       " u'bebled',\n",
       " u'bebothered',\n",
       " u'bebouldered',\n",
       " u'bebuttoned',\n",
       " u'becassocked',\n",
       " u'bechained',\n",
       " u'bechignoned',\n",
       " u'becircled',\n",
       " u'becoiffed',\n",
       " u'becombed',\n",
       " u'becousined',\n",
       " u'becrinolined',\n",
       " u'becuffed',\n",
       " u'becurtained',\n",
       " u'becushioned',\n",
       " u'bed',\n",
       " u'bedaggered',\n",
       " u'bedangled',\n",
       " u'bedded',\n",
       " u'bediademed',\n",
       " u'bediamonded',\n",
       " u'beedged',\n",
       " u'beefheaded',\n",
       " u'beeheaded',\n",
       " u'beeswinged',\n",
       " u'beetled',\n",
       " u'beetleheaded',\n",
       " u'beetleweed',\n",
       " u'beeweed',\n",
       " u'befamilied',\n",
       " u'befanned',\n",
       " u'befathered',\n",
       " u'beferned',\n",
       " u'befetished',\n",
       " u'befezzed',\n",
       " u'befilleted',\n",
       " u'befilmed',\n",
       " u'beforested',\n",
       " u'befountained',\n",
       " u'befrocked',\n",
       " u'befrogged',\n",
       " u'befurbelowed',\n",
       " u'befurred',\n",
       " u'begabled',\n",
       " u'begarlanded',\n",
       " u'begartered',\n",
       " u'beggarweed',\n",
       " u'beglobed',\n",
       " u'begoggled',\n",
       " u'begowned',\n",
       " u'behatted',\n",
       " u'behaviored',\n",
       " u'beheadlined',\n",
       " u'behooped',\n",
       " u'beinked',\n",
       " u'bekilted',\n",
       " u'beknived',\n",
       " u'beknotted',\n",
       " u'belaced',\n",
       " u'belated',\n",
       " u'belatticed',\n",
       " u'belavendered',\n",
       " u'beledgered',\n",
       " u'belfried',\n",
       " u'beliked',\n",
       " u'belimousined',\n",
       " u'belled',\n",
       " u'bellied',\n",
       " u'bellmouthed',\n",
       " u'bellweed',\n",
       " u'beloved',\n",
       " u'belozenged',\n",
       " u'belted',\n",
       " u'bemazed',\n",
       " u'bemedaled',\n",
       " u'bemedalled',\n",
       " u'bemitered',\n",
       " u'bemitred',\n",
       " u'bemused',\n",
       " u'bemuslined',\n",
       " u'bended',\n",
       " u'beneaped',\n",
       " u'beneficed',\n",
       " u'beneighbored',\n",
       " u'benempted',\n",
       " u'benighted',\n",
       " u'bennetweed',\n",
       " u'benumbed',\n",
       " u'benweed',\n",
       " u'benzoated',\n",
       " u'benzoinated',\n",
       " u'bepastured',\n",
       " u'bepatched',\n",
       " u'beperiwigged',\n",
       " u'bepewed',\n",
       " u'bepillared',\n",
       " u'bepistoled',\n",
       " u'beplaided',\n",
       " u'beplumed',\n",
       " u'beribanded',\n",
       " u'beribboned',\n",
       " u'beringed',\n",
       " u'beringleted',\n",
       " u'berobed',\n",
       " u'berouged',\n",
       " u'berried',\n",
       " u'berthed',\n",
       " u'beruffed',\n",
       " u'beruffled',\n",
       " u'beshawled',\n",
       " u'besieged',\n",
       " u'beslushed',\n",
       " u'besotted',\n",
       " u'bespecked',\n",
       " u'bespectacled',\n",
       " u'besped',\n",
       " u'bespeed',\n",
       " u'bespelled',\n",
       " u'bespurred',\n",
       " u'bestatued',\n",
       " u'bestayed',\n",
       " u'bestrapped',\n",
       " u'bestubbled',\n",
       " u'besweatered',\n",
       " u'betattered',\n",
       " u'betaxed',\n",
       " u'betowered',\n",
       " u'betrothed',\n",
       " u'betrousered',\n",
       " u'betted',\n",
       " u'betuckered',\n",
       " u'beturbaned',\n",
       " u'betusked',\n",
       " u'betutored',\n",
       " u'betwattled',\n",
       " u'beuniformed',\n",
       " u'beveled',\n",
       " u'bevelled',\n",
       " u'bevesseled',\n",
       " u'bevesselled',\n",
       " u'bevined',\n",
       " u'bevoiled',\n",
       " u'bewaitered',\n",
       " u'bewhiskered',\n",
       " u'bewigged',\n",
       " u'bewildered',\n",
       " u'bewinged',\n",
       " u'bewired',\n",
       " u'bewrathed',\n",
       " u'biangulated',\n",
       " u'biarcuated',\n",
       " u'biarticulated',\n",
       " u'bicarbureted',\n",
       " u'biciliated',\n",
       " u'bicolored',\n",
       " u'bicorned',\n",
       " u'bidented',\n",
       " u'bifanged',\n",
       " u'bifidated',\n",
       " u'biflected',\n",
       " u'biforked',\n",
       " u'biformed',\n",
       " u'bifronted',\n",
       " u'bifurcated',\n",
       " u'bigeminated',\n",
       " u'bighearted',\n",
       " u'bigmouthed',\n",
       " u'bigoted',\n",
       " u'bigwigged',\n",
       " u'bilamellated',\n",
       " u'bilaminated',\n",
       " u'billed',\n",
       " u'bilobated',\n",
       " u'bilobed',\n",
       " u'bilsted',\n",
       " u'bimaculated',\n",
       " u'bimotored',\n",
       " u'bindweed',\n",
       " u'bineweed',\n",
       " u'binominated',\n",
       " u'binucleated',\n",
       " u'biparted',\n",
       " u'bipectinated',\n",
       " u'biped',\n",
       " u'bipennated',\n",
       " u'bipinnated',\n",
       " u'bipinnatiparted',\n",
       " u'bipinnatisected',\n",
       " u'biradiated',\n",
       " u'birdmouthed',\n",
       " u'birdseed',\n",
       " u'birdweed',\n",
       " u'birostrated',\n",
       " u'birthbed',\n",
       " u'bisexed',\n",
       " u'bishopweed',\n",
       " u'bistered',\n",
       " u'bistipuled',\n",
       " u'bisubstituted',\n",
       " u'bitted',\n",
       " u'bitterhearted',\n",
       " u'bitterweed',\n",
       " u'bituberculated',\n",
       " u'bitumed',\n",
       " u'bivalved',\n",
       " u'bivaulted',\n",
       " u'bivocalized',\n",
       " u'blackhearted',\n",
       " u'blackseed',\n",
       " u'blackshirted',\n",
       " u'bladderseed',\n",
       " u'bladderweed',\n",
       " u'bladed',\n",
       " u'blakeberyed',\n",
       " u'blamed',\n",
       " u'blanked',\n",
       " u'blanketed',\n",
       " u'blanketweed',\n",
       " u'blasted',\n",
       " u'bleached',\n",
       " u'bleared',\n",
       " u'bleed',\n",
       " u'blended',\n",
       " u'blessed',\n",
       " u'blighted',\n",
       " u'blinded',\n",
       " u'blindfolded',\n",
       " u'blindweed',\n",
       " u'blinked',\n",
       " u'blinkered',\n",
       " u'blistered',\n",
       " u'blisterweed',\n",
       " u'blithehearted',\n",
       " u'bloated',\n",
       " u'blobbed',\n",
       " u'blocked',\n",
       " u'blockheaded',\n",
       " u'blooded',\n",
       " u'bloodied',\n",
       " u'bloodshed',\n",
       " u'bloodstained',\n",
       " u'bloodweed',\n",
       " u'blossomed',\n",
       " u'blotched',\n",
       " u'bloused',\n",
       " u'blowzed',\n",
       " u'bludgeoned',\n",
       " u'bluebelled',\n",
       " u'bluehearted',\n",
       " u'blueweed',\n",
       " u'blunderheaded',\n",
       " u'blunthearted',\n",
       " u'blurred',\n",
       " u'bobbed',\n",
       " u'bobsled',\n",
       " u'bobtailed',\n",
       " u'bodiced',\n",
       " u'bodied',\n",
       " u'boiled',\n",
       " u'boldhearted',\n",
       " u'bolectioned',\n",
       " u'boled',\n",
       " u'boleweed',\n",
       " u'bolled',\n",
       " u'bombed',\n",
       " u'bonded',\n",
       " u'boned',\n",
       " u'boneheaded',\n",
       " u'bonneted',\n",
       " u'booked',\n",
       " u'booted',\n",
       " u'bootied',\n",
       " u'boozed',\n",
       " u'bordered',\n",
       " u'bordured',\n",
       " u'bosomed',\n",
       " u'bossed',\n",
       " u'bosselated',\n",
       " u'botched',\n",
       " u'botherheaded',\n",
       " u'bothsided',\n",
       " u'bottled',\n",
       " u'bottomed',\n",
       " u'boughed',\n",
       " u'bounded',\n",
       " u'bountied',\n",
       " u'bowed',\n",
       " u'boweled',\n",
       " u'bowlegged',\n",
       " u'bowstringed',\n",
       " u'braced',\n",
       " u'braceleted',\n",
       " u'brackened',\n",
       " u'bracted',\n",
       " u'braided',\n",
       " u'brambled',\n",
       " u'branched',\n",
       " u'branded',\n",
       " u'brandied',\n",
       " u'brangled',\n",
       " u'bravehearted',\n",
       " u'brawned',\n",
       " u'brazenfaced',\n",
       " u'breasted',\n",
       " u'breastweed',\n",
       " u'breathed',\n",
       " u'brecciated',\n",
       " u'bred',\n",
       " u'breeched',\n",
       " u'breed',\n",
       " u'breviped',\n",
       " u'bridebed',\n",
       " u'brideweed',\n",
       " u'bridged',\n",
       " u'bridled',\n",
       " u'briered',\n",
       " u'brimmed',\n",
       " u'bristled',\n",
       " u'broadhearted',\n",
       " u'brocaded',\n",
       " u'brocked',\n",
       " u'brokenhearted',\n",
       " u'bromoiodized',\n",
       " u'bronzed',\n",
       " u'brooked',\n",
       " u'brookweed',\n",
       " u'broomweed',\n",
       " u'broozled',\n",
       " u'browed',\n",
       " u'brownweed',\n",
       " u'bruckled',\n",
       " u'brushed',\n",
       " u'buboed',\n",
       " u'bucked',\n",
       " u'buckled',\n",
       " u'buckskinned',\n",
       " u'buffed',\n",
       " u'bugled',\n",
       " u'bugleweed',\n",
       " u'bugseed',\n",
       " u'bugweed',\n",
       " u'bulbed',\n",
       " u'bulked',\n",
       " u'bulkheaded',\n",
       " u'bullated',\n",
       " u'bulldogged',\n",
       " u'bulleted',\n",
       " u'bulletheaded',\n",
       " u'bullheaded',\n",
       " u'bullweed',\n",
       " u'bummed',\n",
       " u'bundlerooted',\n",
       " u'bundweed',\n",
       " u'bunted',\n",
       " u'buried',\n",
       " u'burled',\n",
       " u'burned',\n",
       " u'burnoosed',\n",
       " u'burntweed',\n",
       " u'burred',\n",
       " u'burroweed',\n",
       " u'burseed',\n",
       " u'burweed',\n",
       " u'bushed',\n",
       " u'busied',\n",
       " u'busked',\n",
       " u'buskined',\n",
       " u'busted',\n",
       " u'bustled',\n",
       " u'busybodied',\n",
       " u'buttered',\n",
       " u'butterfingered',\n",
       " u'butterweed',\n",
       " u'butteryfingered',\n",
       " u'buttocked',\n",
       " u'buttoned',\n",
       " u'buttonweed',\n",
       " u'cabled',\n",
       " u'caboshed',\n",
       " u'caddiced',\n",
       " u'caddised',\n",
       " u'cadenced',\n",
       " u'cadweed',\n",
       " u'caftaned',\n",
       " u'caged',\n",
       " u'cairned',\n",
       " u'caissoned',\n",
       " u'calced',\n",
       " u'calcified',\n",
       " u'calcined',\n",
       " u'calculated',\n",
       " u'calibered',\n",
       " u'calicoed',\n",
       " u'caligated',\n",
       " u'calpacked',\n",
       " u'calved',\n",
       " u'calycled',\n",
       " u'calyculated',\n",
       " u'camailed',\n",
       " u'camerated',\n",
       " u'cammed',\n",
       " u'campanulated',\n",
       " u'campshed',\n",
       " u'camused',\n",
       " u'canaliculated',\n",
       " u'cancellated',\n",
       " u'cancered',\n",
       " u'cancerweed',\n",
       " u'candied',\n",
       " u'candlelighted',\n",
       " u'candlesticked',\n",
       " u'candyweed',\n",
       " u'canioned',\n",
       " u'cankered',\n",
       " u'cankerweed',\n",
       " u'canned',\n",
       " u'cannelated',\n",
       " u'cannelured',\n",
       " u'cannoned',\n",
       " u'cannulated',\n",
       " u'canted',\n",
       " u'cantilevered',\n",
       " u'cantoned',\n",
       " u'cantred',\n",
       " u'caped',\n",
       " u'capernoited',\n",
       " u'capeweed',\n",
       " u'capitaled',\n",
       " u'capitated',\n",
       " u'capped',\n",
       " u'capriped',\n",
       " u'capsulated',\n",
       " u'capuched',\n",
       " u'carapaced',\n",
       " u'carbolated',\n",
       " u'carboyed',\n",
       " u'carbuncled',\n",
       " u'carcaneted',\n",
       " u'carded',\n",
       " u'carinated',\n",
       " u'carkled',\n",
       " u'carnaged',\n",
       " u'carnationed',\n",
       " u'carpetweed',\n",
       " u'carried',\n",
       " u'carrotweed',\n",
       " u'carucated',\n",
       " u'carunculated',\n",
       " u'cased',\n",
       " u'casemated',\n",
       " u'casemented',\n",
       " u'caseweed',\n",
       " u'casqued',\n",
       " u'castellated',\n",
       " u'castled',\n",
       " u'castorized',\n",
       " u'catamited',\n",
       " u'cataracted',\n",
       " u'catarrhed',\n",
       " u'catchweed',\n",
       " u'catenated',\n",
       " u'caterpillared',\n",
       " u'catfaced',\n",
       " u'catfooted',\n",
       " u'cathedraled',\n",
       " u'caudated',\n",
       " u'caverned',\n",
       " u'cavitied',\n",
       " u'cayenned',\n",
       " u'cedared',\n",
       " u'ceilinged',\n",
       " u'celebrated',\n",
       " u'cellated',\n",
       " u'celled',\n",
       " u'cellulated',\n",
       " u'celluloided',\n",
       " u'centered',\n",
       " u'centriffed',\n",
       " u'centuried',\n",
       " u'cerated',\n",
       " u'cered',\n",
       " u'certified',\n",
       " u'chafeweed',\n",
       " u'chaffseed',\n",
       " u'chaffweed',\n",
       " u'chafted',\n",
       " u'chained',\n",
       " u'chaliced',\n",
       " u'chambered',\n",
       " u'chamberleted',\n",
       " u'chamberletted',\n",
       " u'chanceled',\n",
       " u'channeled',\n",
       " u'channelled',\n",
       " u'chaped',\n",
       " u'chapleted',\n",
       " u'chapournetted',\n",
       " u'chapped',\n",
       " u'charioted',\n",
       " u'charqued',\n",
       " u'chartered',\n",
       " u'chasmed',\n",
       " u'chasteweed',\n",
       " u'chasubled',\n",
       " u'checked',\n",
       " u'checkered',\n",
       " u'checkrowed',\n",
       " u'cheered',\n",
       " u'cheliped',\n",
       " u'cherried',\n",
       " u'chickenbreasted',\n",
       " u'chickenhearted',\n",
       " u'chickenweed',\n",
       " u'chickweed',\n",
       " u'chicqued',\n",
       " u'chiggerweed',\n",
       " u'chignoned',\n",
       " u'childbed',\n",
       " u'childed',\n",
       " u'chilled',\n",
       " u'chined',\n",
       " u'chinned',\n",
       " u'chipped',\n",
       " u'chiseled',\n",
       " u'chitinized',\n",
       " u'chokered',\n",
       " u'chokeweed',\n",
       " u'cholterheaded',\n",
       " u'chopped',\n",
       " u'choppered',\n",
       " u'chorded',\n",
       " u'chowderheaded',\n",
       " u'christened',\n",
       " u'chubbed',\n",
       " u'chuckleheaded',\n",
       " u'churchified',\n",
       " u'churled',\n",
       " u'ciliated',\n",
       " u'cingulated',\n",
       " u'cinnamoned',\n",
       " u'cinquefoiled',\n",
       " u'circled',\n",
       " u'circumscribed',\n",
       " u'circumstanced',\n",
       " u'cirrated',\n",
       " u'cirrhosed',\n",
       " u'cirriped',\n",
       " u'cisted',\n",
       " u'citied',\n",
       " u'citified',\n",
       " u'citrated',\n",
       " u'civilized',\n",
       " u'clammed',\n",
       " u'clammyweed',\n",
       " u'clanned',\n",
       " u'clapped',\n",
       " u'classed',\n",
       " u'classified',\n",
       " u'clavated',\n",
       " u'clavellated',\n",
       " u'clawed',\n",
       " u'claybrained',\n",
       " u'clayweed',\n",
       " u'cleaded',\n",
       " u'cleanhanded',\n",
       " u'cleanhearted',\n",
       " u'clearheaded',\n",
       " u'clearhearted',\n",
       " u'clearweed',\n",
       " u'cled',\n",
       " u'cleeked',\n",
       " u'clefted',\n",
       " u'clerestoried',\n",
       " u'cliented',\n",
       " u'cliffed',\n",
       " u'cliffweed',\n",
       " u'clipped',\n",
       " u'cloaked',\n",
       " u'clocked',\n",
       " u'clodpated',\n",
       " u'cloistered',\n",
       " u'closed',\n",
       " u'closefisted',\n",
       " u'closehanded',\n",
       " u'closehearted',\n",
       " u'closemouthed',\n",
       " u'clotweed',\n",
       " u'clouded',\n",
       " u'clouted',\n",
       " u'clovered',\n",
       " u'clubbed',\n",
       " u'clubfisted',\n",
       " u'clubfooted',\n",
       " u'clubweed',\n",
       " u'clustered',\n",
       " u'coaged',\n",
       " u'coaggregated',\n",
       " u'coated',\n",
       " u'coattailed',\n",
       " u'cobbed',\n",
       " u'cocashweed',\n",
       " u'cochleated',\n",
       " u'cockaded',\n",
       " u'cocked',\n",
       " u'cockeyed',\n",
       " u'cockled',\n",
       " u'cockneybred',\n",
       " u'cockscombed',\n",
       " u'cockweed',\n",
       " u'codheaded',\n",
       " u'coed',\n",
       " u'coelongated',\n",
       " u'coembedded',\n",
       " u'coequated',\n",
       " u'coexpanded',\n",
       " u'coffeeweed',\n",
       " u'cogged',\n",
       " u'coifed',\n",
       " u'coiled',\n",
       " u'coldhearted',\n",
       " u'coleseed',\n",
       " u'colicweed',\n",
       " u'collared',\n",
       " u'collected',\n",
       " u'collied',\n",
       " u'colloped',\n",
       " u'colonnaded',\n",
       " u'colored',\n",
       " u'columnated',\n",
       " u'columned',\n",
       " u'combed',\n",
       " u'combined',\n",
       " u'compacted',\n",
       " u'complected',\n",
       " u'complexioned',\n",
       " u'complicated',\n",
       " u'componed',\n",
       " u'componented',\n",
       " u'composed',\n",
       " u'compressed',\n",
       " u'comprised',\n",
       " u'compulsed',\n",
       " u'conamed',\n",
       " u'concamerated',\n",
       " u'concealed',\n",
       " u'conceded',\n",
       " u'conceited',\n",
       " u'concentrated',\n",
       " u'concerned',\n",
       " u'concerted',\n",
       " u'conched',\n",
       " u'conchyliated',\n",
       " u'condemned',\n",
       " u'condensed',\n",
       " u'conditioned',\n",
       " u'conduplicated',\n",
       " u'coned',\n",
       " u'confated',\n",
       " u'conferted',\n",
       " u'confined',\n",
       " u'confirmed',\n",
       " u'conflated',\n",
       " u'confounded',\n",
       " u'confused',\n",
       " u'congested',\n",
       " u'conjoined',\n",
       " u'conjugated',\n",
       " u'connected',\n",
       " u'conred',\n",
       " u'consecrated',\n",
       " u'considered',\n",
       " u'consolidated',\n",
       " u'constrained',\n",
       " u'constricted',\n",
       " u'consumpted',\n",
       " u'contagioned',\n",
       " u'contented',\n",
       " u'contextured',\n",
       " u'continued',\n",
       " u'contorted',\n",
       " u'contortioned',\n",
       " u'contracted',\n",
       " u'contractured',\n",
       " u'contusioned',\n",
       " u'converted',\n",
       " u'convexed',\n",
       " u'convinced',\n",
       " u'convoluted',\n",
       " u'coolheaded',\n",
       " u'coolweed',\n",
       " u'copied',\n",
       " u'copleased',\n",
       " u'copped',\n",
       " u'coppernosed',\n",
       " u'copperytailed',\n",
       " u'coppiced',\n",
       " u'coppled',\n",
       " u'copsewooded',\n",
       " u'copygraphed',\n",
       " u'coraled',\n",
       " u'corded',\n",
       " u'corduroyed',\n",
       " u'cored',\n",
       " u'coreflexed',\n",
       " u'corked',\n",
       " u'cornered',\n",
       " u'cornified',\n",
       " u'cornuated',\n",
       " u'cornuted',\n",
       " u'corollated',\n",
       " u'coronaled',\n",
       " u'coronated',\n",
       " u'coroneted',\n",
       " u'coronetted',\n",
       " u'corpusculated',\n",
       " u'corrected',\n",
       " u'correlated',\n",
       " u'corridored',\n",
       " ...]"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[w for w in wordlist if re.search('ed$', w)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[u'abjectly',\n",
       " u'adjuster',\n",
       " u'dejected',\n",
       " u'dejectly',\n",
       " u'injector',\n",
       " u'majestic',\n",
       " u'objectee',\n",
       " u'objector',\n",
       " u'rejecter',\n",
       " u'rejector',\n",
       " u'unjilted',\n",
       " u'unjolted',\n",
       " u'unjustly']"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[w for w in wordlist if re.search('^..j..t..$', w)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[u'gold', u'golf', u'hold', u'hole']"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[w for w in wordlist if re.search('^[ghi][mno][jlk][def]$', w)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[u'miiiiiiiiiiiiinnnnnnnnnnneeeeeeeeee',\n",
       " u'miiiiiinnnnnnnnnneeeeeeee',\n",
       " u'mine',\n",
       " u'mmmmmmmmiiiiiiiiinnnnnnnnneeeeeeee']"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "chat_words = sorted(set(w for w in nltk.corpus.nps_chat.words()))\n",
    "[w for w in chat_words if re.search('^m+i+n+e+$', w)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[u'a',\n",
       " u'aaaaaaaaaaaaaaaaa',\n",
       " u'aaahhhh',\n",
       " u'ah',\n",
       " u'ahah',\n",
       " u'ahahah',\n",
       " u'ahh',\n",
       " u'ahhahahaha',\n",
       " u'ahhh',\n",
       " u'ahhhh',\n",
       " u'ahhhhhh',\n",
       " u'ahhhhhhhhhhhhhh',\n",
       " u'h',\n",
       " u'ha',\n",
       " u'haaa',\n",
       " u'hah',\n",
       " u'haha',\n",
       " u'hahaaa',\n",
       " u'hahah',\n",
       " u'hahaha',\n",
       " u'hahahaa',\n",
       " u'hahahah',\n",
       " u'hahahaha',\n",
       " u'hahahahaaa',\n",
       " u'hahahahahaha',\n",
       " u'hahahahahahaha',\n",
       " u'hahahahahahahahahahahahahahahaha',\n",
       " u'hahahhahah',\n",
       " u'hahhahahaha']"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[w for w in chat_words if re.search('^[ha]+$', w)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[u'0.0085',\n",
       " u'0.05',\n",
       " u'0.1',\n",
       " u'0.16',\n",
       " u'0.2',\n",
       " u'0.25',\n",
       " u'0.28',\n",
       " u'0.3',\n",
       " u'0.4',\n",
       " u'0.5',\n",
       " u'0.50',\n",
       " u'0.54',\n",
       " u'0.56',\n",
       " u'0.60',\n",
       " u'0.7',\n",
       " u'0.82',\n",
       " u'0.84',\n",
       " u'0.9',\n",
       " u'0.95',\n",
       " u'0.99',\n",
       " u'1.01',\n",
       " u'1.1',\n",
       " u'1.125',\n",
       " u'1.14',\n",
       " u'1.1650',\n",
       " u'1.17',\n",
       " u'1.18',\n",
       " u'1.19',\n",
       " u'1.2',\n",
       " u'1.20',\n",
       " u'1.24',\n",
       " u'1.25',\n",
       " u'1.26',\n",
       " u'1.28',\n",
       " u'1.35',\n",
       " u'1.39',\n",
       " u'1.4',\n",
       " u'1.457',\n",
       " u'1.46',\n",
       " u'1.49',\n",
       " u'1.5',\n",
       " u'1.50',\n",
       " u'1.55',\n",
       " u'1.56',\n",
       " u'1.5755',\n",
       " u'1.5805',\n",
       " u'1.6',\n",
       " u'1.61',\n",
       " u'1.637',\n",
       " u'1.64',\n",
       " u'1.65',\n",
       " u'1.7',\n",
       " u'1.75',\n",
       " u'1.76',\n",
       " u'1.8',\n",
       " u'1.82',\n",
       " u'1.8415',\n",
       " u'1.85',\n",
       " u'1.8500',\n",
       " u'1.9',\n",
       " u'1.916',\n",
       " u'1.92',\n",
       " u'10.19',\n",
       " u'10.2',\n",
       " u'10.5',\n",
       " u'107.03',\n",
       " u'107.9',\n",
       " u'109.73',\n",
       " u'11.10',\n",
       " u'11.5',\n",
       " u'11.57',\n",
       " u'11.6',\n",
       " u'11.72',\n",
       " u'11.95',\n",
       " u'112.9',\n",
       " u'113.2',\n",
       " u'116.3',\n",
       " u'116.4',\n",
       " u'116.7',\n",
       " u'116.9',\n",
       " u'118.6',\n",
       " u'12.09',\n",
       " u'12.5',\n",
       " u'12.52',\n",
       " u'12.68',\n",
       " u'12.7',\n",
       " u'12.82',\n",
       " u'12.97',\n",
       " u'120.7',\n",
       " u'1206.26',\n",
       " u'121.6',\n",
       " u'126.1',\n",
       " u'126.15',\n",
       " u'127.03',\n",
       " u'129.91',\n",
       " u'13.1',\n",
       " u'13.15',\n",
       " u'13.5',\n",
       " u'13.50',\n",
       " u'13.625',\n",
       " u'13.65',\n",
       " u'13.73',\n",
       " u'13.8',\n",
       " u'13.90',\n",
       " u'130.6',\n",
       " u'130.7',\n",
       " u'131.01',\n",
       " u'132.9',\n",
       " u'133.7',\n",
       " u'133.8',\n",
       " u'14.00',\n",
       " u'14.13',\n",
       " u'14.26',\n",
       " u'14.28',\n",
       " u'14.43',\n",
       " u'14.5',\n",
       " u'14.53',\n",
       " u'14.54',\n",
       " u'14.6',\n",
       " u'14.75',\n",
       " u'14.99',\n",
       " u'141.9',\n",
       " u'142.84',\n",
       " u'142.85',\n",
       " u'143.08',\n",
       " u'143.80',\n",
       " u'143.93',\n",
       " u'148.9',\n",
       " u'149.9',\n",
       " u'15.5',\n",
       " u'150.00',\n",
       " u'153.3',\n",
       " u'154.2',\n",
       " u'16.05',\n",
       " u'16.09',\n",
       " u'16.125',\n",
       " u'16.2',\n",
       " u'16.5',\n",
       " u'16.68',\n",
       " u'16.7',\n",
       " u'16.9',\n",
       " u'169.9',\n",
       " u'17.3',\n",
       " u'17.4',\n",
       " u'17.5',\n",
       " u'17.95',\n",
       " u'1738.1',\n",
       " u'176.1',\n",
       " u'18.3',\n",
       " u'18.6',\n",
       " u'18.95',\n",
       " u'185.9',\n",
       " u'188.84',\n",
       " u'19.3',\n",
       " u'19.50',\n",
       " u'19.6',\n",
       " u'19.94',\n",
       " u'19.95',\n",
       " u'191.9',\n",
       " u'2.07',\n",
       " u'2.1',\n",
       " u'2.15',\n",
       " u'2.19',\n",
       " u'2.2',\n",
       " u'2.25',\n",
       " u'2.29',\n",
       " u'2.3',\n",
       " u'2.30',\n",
       " u'2.35',\n",
       " u'2.375',\n",
       " u'2.4',\n",
       " u'2.42',\n",
       " u'2.44',\n",
       " u'2.46',\n",
       " u'2.47',\n",
       " u'2.5',\n",
       " u'2.50',\n",
       " u'2.6',\n",
       " u'2.62',\n",
       " u'2.65',\n",
       " u'2.7',\n",
       " u'2.75',\n",
       " u'2.8',\n",
       " u'2.80',\n",
       " u'2.87',\n",
       " u'2.875',\n",
       " u'2.9',\n",
       " u'2.95',\n",
       " u'20.07',\n",
       " u'20.5',\n",
       " u'21.1',\n",
       " u'21.9',\n",
       " u'2141.7',\n",
       " u'2160.1',\n",
       " u'2163.2',\n",
       " u'22.75',\n",
       " u'220.45',\n",
       " u'221.4',\n",
       " u'225.6',\n",
       " u'23.25',\n",
       " u'23.4',\n",
       " u'23.5',\n",
       " u'23.72',\n",
       " u'234.4',\n",
       " u'236.74',\n",
       " u'236.79',\n",
       " u'24.95',\n",
       " u'25.50',\n",
       " u'25.6',\n",
       " u'251.2',\n",
       " u'26.2',\n",
       " u'26.5',\n",
       " u'26.8',\n",
       " u'263.07',\n",
       " u'2645.90',\n",
       " u'2691.19',\n",
       " u'27.1',\n",
       " u'27.4',\n",
       " u'273.5',\n",
       " u'278.7',\n",
       " u'28.25',\n",
       " u'28.36',\n",
       " u'28.4',\n",
       " u'28.5',\n",
       " u'28.53',\n",
       " u'28.6',\n",
       " u'29.3',\n",
       " u'29.4',\n",
       " u'29.9',\n",
       " u'292.32',\n",
       " u'3.01',\n",
       " u'3.04',\n",
       " u'3.1',\n",
       " u'3.16',\n",
       " u'3.18',\n",
       " u'3.19',\n",
       " u'3.2',\n",
       " u'3.20',\n",
       " u'3.23',\n",
       " u'3.253',\n",
       " u'3.28',\n",
       " u'3.3',\n",
       " u'3.35',\n",
       " u'3.375',\n",
       " u'3.4',\n",
       " u'3.42',\n",
       " u'3.43',\n",
       " u'3.5',\n",
       " u'3.55',\n",
       " u'3.6',\n",
       " u'3.61',\n",
       " u'3.625',\n",
       " u'3.7',\n",
       " u'3.75',\n",
       " u'3.8',\n",
       " u'3.80',\n",
       " u'3.9',\n",
       " u'30.6',\n",
       " u'30.9',\n",
       " u'319.75',\n",
       " u'32.8',\n",
       " u'334.5',\n",
       " u'34.625',\n",
       " u'341.20',\n",
       " u'3436.58',\n",
       " u'35.2',\n",
       " u'35.7',\n",
       " u'352.7',\n",
       " u'352.9',\n",
       " u'35500.64',\n",
       " u'35564.43',\n",
       " u'36.9',\n",
       " u'361.8',\n",
       " u'3648.82',\n",
       " u'37.3',\n",
       " u'37.5',\n",
       " u'372.14',\n",
       " u'372.9',\n",
       " u'374.19',\n",
       " u'374.20',\n",
       " u'377.60',\n",
       " u'38.3',\n",
       " u'38.375',\n",
       " u'38.5',\n",
       " u'38.875',\n",
       " u'387.8',\n",
       " u'4.1',\n",
       " u'4.10',\n",
       " u'4.2',\n",
       " u'4.25',\n",
       " u'4.3',\n",
       " u'4.4',\n",
       " u'4.5',\n",
       " u'4.55',\n",
       " u'4.6',\n",
       " u'4.7',\n",
       " u'4.75',\n",
       " u'4.8',\n",
       " u'4.875',\n",
       " u'4.898',\n",
       " u'4.9',\n",
       " u'40.21',\n",
       " u'41.60',\n",
       " u'415.6',\n",
       " u'415.8',\n",
       " u'42.1',\n",
       " u'42.5',\n",
       " u'422.5',\n",
       " u'43.875',\n",
       " u'434.4',\n",
       " u'436.01',\n",
       " u'446.62',\n",
       " u'449.04',\n",
       " u'45.2',\n",
       " u'45.3',\n",
       " u'45.75',\n",
       " u'456.64',\n",
       " u'46.1',\n",
       " u'47.1',\n",
       " u'47.125',\n",
       " u'47.5',\n",
       " u'47.6',\n",
       " u'49.9',\n",
       " u'494.50',\n",
       " u'497.34',\n",
       " u'5.1',\n",
       " u'5.2180',\n",
       " u'5.276',\n",
       " u'5.29',\n",
       " u'5.3',\n",
       " u'5.39',\n",
       " u'5.4',\n",
       " u'5.435',\n",
       " u'5.5',\n",
       " u'5.57',\n",
       " u'5.6',\n",
       " u'5.63',\n",
       " u'5.7',\n",
       " u'5.70',\n",
       " u'5.8',\n",
       " u'5.82',\n",
       " u'5.9',\n",
       " u'5.92',\n",
       " u'50.1',\n",
       " u'50.38',\n",
       " u'50.45',\n",
       " u'51.25',\n",
       " u'51.6',\n",
       " u'55.1',\n",
       " u'566.54',\n",
       " u'57.50',\n",
       " u'57.6',\n",
       " u'57.7',\n",
       " u'58.64',\n",
       " u'59.6',\n",
       " u'59.9',\n",
       " u'6.03',\n",
       " u'6.1',\n",
       " u'6.20',\n",
       " u'6.21',\n",
       " u'6.25',\n",
       " u'6.4',\n",
       " u'6.40',\n",
       " u'6.44',\n",
       " u'6.5',\n",
       " u'6.50',\n",
       " u'6.53',\n",
       " u'6.6',\n",
       " u'6.7',\n",
       " u'6.70',\n",
       " u'6.79',\n",
       " u'6.84',\n",
       " u'6.9',\n",
       " u'60.36',\n",
       " u'618.1',\n",
       " u'62.1',\n",
       " u'62.5',\n",
       " u'62.625',\n",
       " u'63.79',\n",
       " u'630.9',\n",
       " u'64.5',\n",
       " u'66.5',\n",
       " u'7.15',\n",
       " u'7.2',\n",
       " u'7.20',\n",
       " u'7.272',\n",
       " u'7.3',\n",
       " u'7.4',\n",
       " u'7.40',\n",
       " u'7.422',\n",
       " u'7.45',\n",
       " u'7.458',\n",
       " u'7.5',\n",
       " u'7.50',\n",
       " u'7.52',\n",
       " u'7.55',\n",
       " u'7.60',\n",
       " u'7.62',\n",
       " u'7.63',\n",
       " u'7.65',\n",
       " u'7.74',\n",
       " u'7.78',\n",
       " u'7.79',\n",
       " u'7.8',\n",
       " u'7.80',\n",
       " u'7.84',\n",
       " u'7.88',\n",
       " u'7.90',\n",
       " u'7.95',\n",
       " u'70.2',\n",
       " u'70.7',\n",
       " u'705.6',\n",
       " u'72.7',\n",
       " u'734.9',\n",
       " u'737.5',\n",
       " u'77.56',\n",
       " u'77.6',\n",
       " u'77.70',\n",
       " u'8.04',\n",
       " u'8.06',\n",
       " u'8.07',\n",
       " u'8.1',\n",
       " u'8.12',\n",
       " u'8.14',\n",
       " u'8.15',\n",
       " u'8.19',\n",
       " u'8.2',\n",
       " u'8.22',\n",
       " u'8.25',\n",
       " u'8.30',\n",
       " u'8.35',\n",
       " u'8.45',\n",
       " u'8.467',\n",
       " u'8.47',\n",
       " u'8.48',\n",
       " u'8.5',\n",
       " u'8.50',\n",
       " u'8.53',\n",
       " u'8.55',\n",
       " u'8.56',\n",
       " u'8.575',\n",
       " u'8.60',\n",
       " u'8.64',\n",
       " u'8.65',\n",
       " u'8.70',\n",
       " u'8.75',\n",
       " u'8.9',\n",
       " u'80.50',\n",
       " u'80.8',\n",
       " u'81.8',\n",
       " u'811.9',\n",
       " u'83.4',\n",
       " u'84.29',\n",
       " u'84.9',\n",
       " u'85.1',\n",
       " u'85.7',\n",
       " u'86.12',\n",
       " u'87.5',\n",
       " u'88.32',\n",
       " u'89.7',\n",
       " u'89.9',\n",
       " u'9.3',\n",
       " u'9.32',\n",
       " u'9.37',\n",
       " u'9.45',\n",
       " u'9.5',\n",
       " u'9.625',\n",
       " u'9.75',\n",
       " u'9.8',\n",
       " u'9.82',\n",
       " u'9.9',\n",
       " u'92.9',\n",
       " u'93.3',\n",
       " u'93.9',\n",
       " u'94.2',\n",
       " u'94.8',\n",
       " u'95.09',\n",
       " u'96.4',\n",
       " u'98.3',\n",
       " u'99.1',\n",
       " u'99.3']"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "wsj = sorted(set(nltk.corpus.treebank.words()))\n",
    "[w for w in wsj if re.search('^[0-9]+\\.[0-9]+$', w)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[u'C$', u'US$']"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[w for w in wsj if re.search('^[A-Z]+\\$$', w)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[u'1614',\n",
       " u'1637',\n",
       " u'1787',\n",
       " u'1901',\n",
       " u'1903',\n",
       " u'1917',\n",
       " u'1925',\n",
       " u'1929',\n",
       " u'1933',\n",
       " u'1934',\n",
       " u'1948',\n",
       " u'1953',\n",
       " u'1955',\n",
       " u'1956',\n",
       " u'1961',\n",
       " u'1965',\n",
       " u'1966',\n",
       " u'1967',\n",
       " u'1968',\n",
       " u'1969',\n",
       " u'1970',\n",
       " u'1971',\n",
       " u'1972',\n",
       " u'1973',\n",
       " u'1975',\n",
       " u'1976',\n",
       " u'1977',\n",
       " u'1979',\n",
       " u'1980',\n",
       " u'1981',\n",
       " u'1982',\n",
       " u'1983',\n",
       " u'1984',\n",
       " u'1985',\n",
       " u'1986',\n",
       " u'1987',\n",
       " u'1988',\n",
       " u'1989',\n",
       " u'1990',\n",
       " u'1991',\n",
       " u'1992',\n",
       " u'1993',\n",
       " u'1994',\n",
       " u'1995',\n",
       " u'1996',\n",
       " u'1997',\n",
       " u'1998',\n",
       " u'1999',\n",
       " u'2000',\n",
       " u'2005',\n",
       " u'2009',\n",
       " u'2017',\n",
       " u'2019',\n",
       " u'2029',\n",
       " u'3057',\n",
       " u'8300']"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[w for w in wsj if re.search('^[0-9]{4}$', w)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[u'10-day',\n",
       " u'10-lap',\n",
       " u'10-year',\n",
       " u'100-share',\n",
       " u'12-point',\n",
       " u'12-year',\n",
       " u'14-hour',\n",
       " u'15-day',\n",
       " u'150-point',\n",
       " u'190-point',\n",
       " u'20-point',\n",
       " u'20-stock',\n",
       " u'21-month',\n",
       " u'237-seat',\n",
       " u'240-page',\n",
       " u'27-year',\n",
       " u'30-day',\n",
       " u'30-point',\n",
       " u'30-share',\n",
       " u'30-year',\n",
       " u'300-day',\n",
       " u'36-day',\n",
       " u'36-store',\n",
       " u'42-year',\n",
       " u'50-state',\n",
       " u'500-stock',\n",
       " u'52-week',\n",
       " u'69-point',\n",
       " u'84-month',\n",
       " u'87-store',\n",
       " u'90-day']"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[w for w in wsj if re.search('^[0-9]+-[a-z]{3,5}$', w)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[u'black-and-white',\n",
       " u'bread-and-butter',\n",
       " u'father-in-law',\n",
       " u'machine-gun-toting',\n",
       " u'savings-and-loan']"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[w for w in wsj if re.search('^[a-z]{5,}-[a-z]{2,3}-[a-z]{,6}$', w)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[u'62%-owned',\n",
       " u'Absorbed',\n",
       " u'According',\n",
       " u'Adopting',\n",
       " u'Advanced',\n",
       " u'Advancing',\n",
       " u'Alfred',\n",
       " u'Allied',\n",
       " u'Annualized',\n",
       " u'Anything',\n",
       " u'Arbitrage-related',\n",
       " u'Arbitraging',\n",
       " u'Asked',\n",
       " u'Assuming',\n",
       " u'Atlanta-based',\n",
       " u'Baking',\n",
       " u'Banking',\n",
       " u'Beginning',\n",
       " u'Beijing',\n",
       " u'Being',\n",
       " u'Bermuda-based',\n",
       " u'Betting',\n",
       " u'Boeing',\n",
       " u'Broadcasting',\n",
       " u'Bucking',\n",
       " u'Buying',\n",
       " u'Calif.-based',\n",
       " u'Change-ringing',\n",
       " u'Citing',\n",
       " u'Concerned',\n",
       " u'Confronted',\n",
       " u'Conn.based',\n",
       " u'Consolidated',\n",
       " u'Continued',\n",
       " u'Continuing',\n",
       " u'Declining',\n",
       " u'Defending',\n",
       " u'Depending',\n",
       " u'Designated',\n",
       " u'Determining',\n",
       " u'Developed',\n",
       " u'Died',\n",
       " u'During',\n",
       " u'Encouraged',\n",
       " u'Encouraging',\n",
       " u'English-speaking',\n",
       " u'Estimated',\n",
       " u'Everything',\n",
       " u'Excluding',\n",
       " u'Exxon-owned',\n",
       " u'Faulding',\n",
       " u'Fed',\n",
       " u'Feeding',\n",
       " u'Filling',\n",
       " u'Filmed',\n",
       " u'Financing',\n",
       " u'Following',\n",
       " u'Founded',\n",
       " u'Fracturing',\n",
       " u'Francisco-based',\n",
       " u'Fred',\n",
       " u'Funded',\n",
       " u'Funding',\n",
       " u'Generalized',\n",
       " u'Germany-based',\n",
       " u'Getting',\n",
       " u'Guaranteed',\n",
       " u'Having',\n",
       " u'Heating',\n",
       " u'Heightened',\n",
       " u'Holding',\n",
       " u'Housing',\n",
       " u'Illuminating',\n",
       " u'Indeed',\n",
       " u'Indexing',\n",
       " u'Irving',\n",
       " u'Jersey-based',\n",
       " u'Judging',\n",
       " u'Knowing',\n",
       " u'Learning',\n",
       " u'Legislating',\n",
       " u'Leming',\n",
       " u'Limited',\n",
       " u'London-based',\n",
       " u'Manfred',\n",
       " u'Manufacturing',\n",
       " u'Melamed',\n",
       " u'Miami-based',\n",
       " u'Mich.-based',\n",
       " u'Mining',\n",
       " u'Minneapolis-based',\n",
       " u'Mo.-based',\n",
       " u'Mortgage-Backed',\n",
       " u'Moving',\n",
       " u'Muzzling',\n",
       " u'N.J.-based',\n",
       " u'NBC-owned',\n",
       " u'NIH-appointed',\n",
       " u'Named',\n",
       " u'No-Smoking',\n",
       " u'Observing',\n",
       " u'Offering',\n",
       " u'Ohio-based',\n",
       " u'Orleans-based',\n",
       " u'Packaging',\n",
       " u'Performing',\n",
       " u'Philadelphia-based',\n",
       " u'Posted',\n",
       " u'Provided',\n",
       " u'Publishing',\n",
       " u'Purchasing',\n",
       " u'Rated',\n",
       " u'Reached',\n",
       " u'Red',\n",
       " u'Red-blooded',\n",
       " u'Reducing',\n",
       " u'Reed',\n",
       " u'Regarded',\n",
       " u'Rekindled',\n",
       " u'Related',\n",
       " u'Ringing',\n",
       " u'Rolling',\n",
       " u'Sacramento-based',\n",
       " u'Scoring',\n",
       " u'Seattle-based',\n",
       " u'Seed',\n",
       " u'Skilled',\n",
       " u'Smelting',\n",
       " u'Something',\n",
       " u'Spending',\n",
       " u'Standardized',\n",
       " u'Standing',\n",
       " u'Starting',\n",
       " u'Sterling',\n",
       " u'Taking',\n",
       " u'Texas-based',\n",
       " u'Toronto-based',\n",
       " u'Traded',\n",
       " u'Trading',\n",
       " u'Troubled',\n",
       " u'U.N.-supervised',\n",
       " u'U.S.-backed',\n",
       " u'United',\n",
       " u'Used',\n",
       " u'Varying',\n",
       " u'Washington-based',\n",
       " u'Whiting',\n",
       " u'Wilfred',\n",
       " u'Winning',\n",
       " u'Xiaoping',\n",
       " u'York-based',\n",
       " u'Zayed',\n",
       " u'abandoned',\n",
       " u'abating',\n",
       " u'abolishing',\n",
       " u'abortion-related',\n",
       " u'abounding',\n",
       " u'abridging',\n",
       " u'absorbed',\n",
       " u'acceded',\n",
       " u'accelerated',\n",
       " u'accepted',\n",
       " u'accepting',\n",
       " u'according',\n",
       " u'accounted',\n",
       " u'accounting',\n",
       " u'accrued',\n",
       " u'accumulated',\n",
       " u'accused',\n",
       " u'accusing',\n",
       " u'achieved',\n",
       " u'achieving',\n",
       " u'acknowledging',\n",
       " u'acquired',\n",
       " u'acquiring',\n",
       " u'acquisition-minded',\n",
       " u'acted',\n",
       " u'acting',\n",
       " u'adapted',\n",
       " u'adapting',\n",
       " u'added',\n",
       " u'adding',\n",
       " u'addressing',\n",
       " u'adjusted',\n",
       " u'adjusting',\n",
       " u'admitted',\n",
       " u'admitting',\n",
       " u'adopted',\n",
       " u'advanced',\n",
       " u'advancing',\n",
       " u'advertised',\n",
       " u'advertising',\n",
       " u'advised',\n",
       " u'advocated',\n",
       " u'advocating',\n",
       " u'affecting',\n",
       " u'afflicted',\n",
       " u'aggravated',\n",
       " u'agreed',\n",
       " u'agreeing',\n",
       " u'ailing',\n",
       " u'aimed',\n",
       " u'aiming',\n",
       " u'aired',\n",
       " u'airline-related',\n",
       " u'alarmed',\n",
       " u'alienated',\n",
       " u'alleged',\n",
       " u'alleging',\n",
       " u'allocated',\n",
       " u'allowed',\n",
       " u'altered',\n",
       " u'altering',\n",
       " u'amended',\n",
       " u'amending',\n",
       " u'amounted',\n",
       " u'amusing',\n",
       " u'angered',\n",
       " u'announced',\n",
       " u'annoyed',\n",
       " u'annualized',\n",
       " u'answered',\n",
       " u'anti-dumping',\n",
       " u'anticipated',\n",
       " u'anticipating',\n",
       " u'anything',\n",
       " u'apologizing',\n",
       " u'appealing',\n",
       " u'appeared',\n",
       " u'appearing',\n",
       " u'applied',\n",
       " u'appointed',\n",
       " u'approached',\n",
       " u'appropriated',\n",
       " u'approved',\n",
       " u'arched',\n",
       " u'argued',\n",
       " u'arguing',\n",
       " u'arising',\n",
       " u'armed',\n",
       " u'arranged',\n",
       " u'arrested',\n",
       " u'arrived',\n",
       " u'asbestos-related',\n",
       " u'asked',\n",
       " u'asking',\n",
       " u'assassinated',\n",
       " u'assembled',\n",
       " u'asserted',\n",
       " u'asserting',\n",
       " u'assessed',\n",
       " u'assigned',\n",
       " u'assisted',\n",
       " u'associated',\n",
       " u'assumed',\n",
       " u'assuming',\n",
       " u'assured',\n",
       " u'attached',\n",
       " u'attacking',\n",
       " u'attempted',\n",
       " u'attempting',\n",
       " u'attended',\n",
       " u'attending',\n",
       " u'attracted',\n",
       " u'attracting',\n",
       " u'attributed',\n",
       " u'auctioned',\n",
       " u'authorized',\n",
       " u'authorizing',\n",
       " u'automated',\n",
       " u'automotive-lighting',\n",
       " u'averaged',\n",
       " u'averted',\n",
       " u'avoiding',\n",
       " u'awarded',\n",
       " u'awarding',\n",
       " u'backed',\n",
       " u'backing',\n",
       " u'balanced',\n",
       " u'bald-faced',\n",
       " u'balkanized',\n",
       " u'balked',\n",
       " u'balloting',\n",
       " u'bank-backed',\n",
       " u'banking',\n",
       " u'banned',\n",
       " u'banning',\n",
       " u'barking',\n",
       " u'barred',\n",
       " u'based',\n",
       " u'battered',\n",
       " u'battery-operated',\n",
       " u'batting',\n",
       " u'bearing',\n",
       " u'becoming',\n",
       " u'bedding',\n",
       " u'befuddled',\n",
       " u'beginning',\n",
       " u'behaving',\n",
       " u'beheading',\n",
       " u'being',\n",
       " u'beleaguered',\n",
       " u'believed',\n",
       " u'bell-ringing',\n",
       " u'belonging',\n",
       " u'benefited',\n",
       " u'best-selling',\n",
       " u'betting',\n",
       " u'bickering',\n",
       " u'bidding',\n",
       " u'billed',\n",
       " u'billing',\n",
       " u'blamed',\n",
       " u'bled',\n",
       " u'blessing',\n",
       " u'blighted',\n",
       " u'blocked',\n",
       " u'blurred',\n",
       " u'boarding',\n",
       " u'bolstered',\n",
       " u'bombarding',\n",
       " u'booked',\n",
       " u'booming',\n",
       " u'boosted',\n",
       " u'boosting',\n",
       " u'borrowed',\n",
       " u'borrowing',\n",
       " u'botched',\n",
       " u'bothered',\n",
       " u'bounced',\n",
       " u'bowed',\n",
       " u'breaking',\n",
       " u'breathed',\n",
       " u'breathtaking',\n",
       " u'breed',\n",
       " u'bribed',\n",
       " u'bribing',\n",
       " u'briefing',\n",
       " u'brightened',\n",
       " u'bring',\n",
       " u'bringing',\n",
       " u'broad-based',\n",
       " u'broadcasting',\n",
       " u'broadened',\n",
       " u'brokering',\n",
       " u'brushed',\n",
       " u'budding',\n",
       " u'building',\n",
       " u'bundling',\n",
       " u'buoyed',\n",
       " u'burned',\n",
       " u'buying',\n",
       " u'calculated',\n",
       " u'called',\n",
       " u'calling',\n",
       " u'campaigning',\n",
       " u'cancer-causing',\n",
       " u'capitalized',\n",
       " u'capped',\n",
       " u'captivating',\n",
       " u'cared',\n",
       " u'carried',\n",
       " u'carrying',\n",
       " u'cascading',\n",
       " u'casting',\n",
       " u'caused',\n",
       " u'causing',\n",
       " u'cautioned',\n",
       " u'ceiling',\n",
       " u'centralized',\n",
       " u'certified',\n",
       " u'chaired',\n",
       " u'challenging',\n",
       " u'championing',\n",
       " u'change-ringing',\n",
       " u'changed',\n",
       " u'changing',\n",
       " u'characterized',\n",
       " u'characterizing',\n",
       " u'charged',\n",
       " u'charging',\n",
       " u'chastised',\n",
       " u'cheating',\n",
       " u'checking',\n",
       " u'cheerleading',\n",
       " u'chilled',\n",
       " u'choosing',\n",
       " u'chopped',\n",
       " u'circulated',\n",
       " u'cited',\n",
       " u'citing',\n",
       " u'citizen-sparked',\n",
       " u'city-owned',\n",
       " u'claimed',\n",
       " u'claiming',\n",
       " u'clamped',\n",
       " u'clarified',\n",
       " u'clashed',\n",
       " u'classed',\n",
       " u'classified',\n",
       " u'cleaned',\n",
       " u'cleaner-burning',\n",
       " u'cleared',\n",
       " u'clearing',\n",
       " u'clicked',\n",
       " u'climbed',\n",
       " u'climbing',\n",
       " u'clipped',\n",
       " u'clobbered',\n",
       " u'closed',\n",
       " u'closing',\n",
       " u'clothing',\n",
       " u'clouding',\n",
       " u'cluttered',\n",
       " u'co-founded',\n",
       " u'coaching',\n",
       " u'coal-fired',\n",
       " u'coated',\n",
       " u'codified',\n",
       " u'collaborated',\n",
       " u'collapsed',\n",
       " u'collected',\n",
       " u'collecting',\n",
       " u'collective-bargaining',\n",
       " u'colored',\n",
       " u'combined',\n",
       " u'coming',\n",
       " u'commanded',\n",
       " u'commenting',\n",
       " u'committed',\n",
       " u'committing',\n",
       " u'compared',\n",
       " u'compelling',\n",
       " u'competed',\n",
       " u'competing',\n",
       " u'compiled',\n",
       " u'complained',\n",
       " u'complaining',\n",
       " u'completed',\n",
       " u'completing',\n",
       " u'complicated',\n",
       " u'composed',\n",
       " u'composting',\n",
       " u'compressed',\n",
       " u'computer-aided',\n",
       " u'computer-assisted',\n",
       " u'computer-generated',\n",
       " u'computerized',\n",
       " u'computing',\n",
       " u'conceding',\n",
       " u'concentrated',\n",
       " u'concentrating',\n",
       " u'concerned',\n",
       " u'concluded',\n",
       " u'condemned',\n",
       " u'condemning',\n",
       " u'conducted',\n",
       " u'conducting',\n",
       " u'confined',\n",
       " u'confirmed',\n",
       " u'confused',\n",
       " u'connected',\n",
       " u'consented',\n",
       " u'considered',\n",
       " u'considering',\n",
       " u'consisting',\n",
       " u'construed',\n",
       " u'consulting',\n",
       " u'contacted',\n",
       " u'contained',\n",
       " u'containing',\n",
       " u'contesting',\n",
       " u'continued',\n",
       " u'continuing',\n",
       " u'contracted',\n",
       " u'contributed',\n",
       " u'contributing',\n",
       " u'controlled',\n",
       " u'controlling',\n",
       " u'converted',\n",
       " u'converting',\n",
       " u'convicted',\n",
       " u'convinced',\n",
       " u'cooled',\n",
       " u'cooperating',\n",
       " u'copied',\n",
       " u'copying',\n",
       " u'corn-buying',\n",
       " u'corrected',\n",
       " u'correcting',\n",
       " u'cost-cutting',\n",
       " u'cost-sharing',\n",
       " u'counseling',\n",
       " u'counting',\n",
       " u'coupled',\n",
       " u'court-ordered',\n",
       " u'covered',\n",
       " u'covering',\n",
       " u'cranked',\n",
       " u'crashing',\n",
       " u'created',\n",
       " u'creating',\n",
       " u'credit-rating',\n",
       " u'crippled',\n",
       " u'criticized',\n",
       " u'crossed',\n",
       " u'crossing',\n",
       " u'crowded',\n",
       " u'cruising',\n",
       " u'crushed',\n",
       " u'crying',\n",
       " u'cultivated',\n",
       " u'curbed',\n",
       " u'curbing',\n",
       " u'curled',\n",
       " u'current-carrying',\n",
       " u'curtailed',\n",
       " u'cushioned',\n",
       " u'customized',\n",
       " u'cutting',\n",
       " u'damaged',\n",
       " u'damaging',\n",
       " u'dancing',\n",
       " u'darned',\n",
       " u'dashed',\n",
       " u'dating',\n",
       " u'dead-eyed',\n",
       " u'dealing',\n",
       " u'decided',\n",
       " u'declared',\n",
       " u'declaring',\n",
       " u'declined',\n",
       " u'declining',\n",
       " u'decorated',\n",
       " u'decried',\n",
       " u'deducting',\n",
       " u'deemed',\n",
       " u'defeated',\n",
       " u'defended',\n",
       " u'defined',\n",
       " u'defying',\n",
       " u'delayed',\n",
       " u'deliberating',\n",
       " u'delisted',\n",
       " u'delivered',\n",
       " u'delivering',\n",
       " u'demanding',\n",
       " u'demonstrating',\n",
       " u'denied',\n",
       " u'denouncing',\n",
       " u'denying',\n",
       " u'depended',\n",
       " u'depending',\n",
       " u'depleted',\n",
       " u'depressed',\n",
       " u'deprived',\n",
       " u'derived',\n",
       " u'descending',\n",
       " u'described',\n",
       " u'deserving',\n",
       " u'designated',\n",
       " u'designed',\n",
       " u'designing',\n",
       " u'desired',\n",
       " u'despised',\n",
       " u'detailed',\n",
       " u'deteriorated',\n",
       " u'deteriorating',\n",
       " u'determined',\n",
       " u'deterring',\n",
       " u'devastating',\n",
       " u'developed',\n",
       " u'developing',\n",
       " u'devised',\n",
       " u'devoted',\n",
       " u'devouring',\n",
       " u'diagnosed',\n",
       " u'died',\n",
       " u'diluted',\n",
       " u'diming',\n",
       " u'diminished',\n",
       " u'directed',\n",
       " u'directing',\n",
       " u'disaffected',\n",
       " u'disagreed',\n",
       " u'disappointed',\n",
       " u'disappointing',\n",
       " u'disapproved',\n",
       " u'discarded',\n",
       " u'disciplined',\n",
       " u'disclosed',\n",
       " u'disclosing',\n",
       " u'discontinued',\n",
       " u'discontinuing',\n",
       " u'discouraging',\n",
       " u'discovered',\n",
       " u'discussed',\n",
       " u'discussing',\n",
       " u'disembodied',\n",
       " u'dismayed',\n",
       " u'dismissed',\n",
       " u'disposed',\n",
       " u'disputed',\n",
       " u'disseminating',\n",
       " u'distinguished',\n",
       " u'distorted',\n",
       " u'distributed',\n",
       " u'disturbing',\n",
       " u'diversified',\n",
       " u'diversifying',\n",
       " u'divided',\n",
       " u'dividing',\n",
       " u'documented',\n",
       " u'doing',\n",
       " u'doling',\n",
       " u'dollar-denominated',\n",
       " u'dominated',\n",
       " u'dominating',\n",
       " u'doubled',\n",
       " u'doubted',\n",
       " u'downgraded',\n",
       " u'downgrading',\n",
       " u'drafted',\n",
       " u'drawing',\n",
       " u'dreamed',\n",
       " u'dressed',\n",
       " u'drifted',\n",
       " u'drinking',\n",
       " u'driving',\n",
       " u'drooled',\n",
       " u'dropped',\n",
       " u'dubbed',\n",
       " u'duckling',\n",
       " u'dumbfounded',\n",
       " u'dumped',\n",
       " u'during',\n",
       " u'dwindling',\n",
       " u'earned',\n",
       " u'earning',\n",
       " u'eased',\n",
       " u'easing',\n",
       " u'eating',\n",
       " u'echoed',\n",
       " u'edged',\n",
       " u'editing',\n",
       " u'educated',\n",
       " u'elected',\n",
       " u'eliminated',\n",
       " u'eliminating',\n",
       " u'embarrassing',\n",
       " u'embroiled',\n",
       " u'emerged',\n",
       " u'emerging',\n",
       " u'emphasized',\n",
       " u'employed',\n",
       " u'empowered',\n",
       " u'enabled',\n",
       " u'enabling',\n",
       " u'enacted',\n",
       " u'encircling',\n",
       " u'enclosed',\n",
       " u'encouraging',\n",
       " u'encroaching',\n",
       " u'ended',\n",
       " u'ending',\n",
       " u'endorsed',\n",
       " u'engaged',\n",
       " u'engaging',\n",
       " u'engineered',\n",
       " u'engineering',\n",
       " u'enhanced',\n",
       " u'enjoyed',\n",
       " u'enjoying',\n",
       " u'enlarged',\n",
       " u'enraged',\n",
       " u'ensnarled',\n",
       " u'entangled',\n",
       " u'entered',\n",
       " u'entering',\n",
       " u'entertaining',\n",
       " u'enticed',\n",
       " u'entitled',\n",
       " u'entrenched',\n",
       " u'entrusted',\n",
       " u'equaling',\n",
       " u'equipped',\n",
       " u'escalated',\n",
       " u'escaped',\n",
       " u'established',\n",
       " u'establishing',\n",
       " u'estimated',\n",
       " u'evaluated',\n",
       " u'evaluating',\n",
       " u'evaporated',\n",
       " u'evening',\n",
       " u'everything',\n",
       " u'evoking',\n",
       " u'evolved',\n",
       " u'exacerbated',\n",
       " u'examined',\n",
       " u'exceed',\n",
       " u'exceeded',\n",
       " u'exceeding',\n",
       " u'exchanging',\n",
       " u'excited',\n",
       " u'exciting',\n",
       " u'executed',\n",
       " u'executing',\n",
       " u'exercised',\n",
       " u'exerting',\n",
       " u'exhausted',\n",
       " u'exhibited',\n",
       " u'existed',\n",
       " u'existing',\n",
       " u'expanded',\n",
       " u'expanding',\n",
       " u'expected',\n",
       " u'expecting',\n",
       " u'expedited',\n",
       " u'expelled',\n",
       " u'experienced',\n",
       " u'experiencing',\n",
       " u'expired',\n",
       " u'explained',\n",
       " u'explaining',\n",
       " u'exploded',\n",
       " u'export-oriented',\n",
       " u'exposed',\n",
       " u'expressed',\n",
       " u'expressing',\n",
       " u'expunged',\n",
       " u'extended',\n",
       " u'extending',\n",
       " u'exuded',\n",
       " u'eyeing',\n",
       " u'fabled',\n",
       " u'faced',\n",
       " u'facing',\n",
       " u'factoring',\n",
       " u'faded',\n",
       " u'failed',\n",
       " u'failing',\n",
       " u'fainting',\n",
       " u'falling',\n",
       " u'faltered',\n",
       " u'famed',\n",
       " u'family-planning',\n",
       " u'fared',\n",
       " u'fashioned',\n",
       " u'fast-growing',\n",
       " u'fastest-growing',\n",
       " u'fattened',\n",
       " u'favored',\n",
       " u'fawning',\n",
       " u'feared',\n",
       " u'featured',\n",
       " u'featuring',\n",
       " u'fed',\n",
       " u'feed',\n",
       " u'feeling',\n",
       " u'fetching',\n",
       " u'fielded',\n",
       " u'fighting',\n",
       " u'filed',\n",
       " u'filing',\n",
       " u'filled',\n",
       " u'filling',\n",
       " u'finalized',\n",
       " u'financed',\n",
       " u'financing',\n",
       " u'finding',\n",
       " u'fined',\n",
       " u'finished',\n",
       " u'fired',\n",
       " u'firmed',\n",
       " u'fixed',\n",
       " u'fizzled',\n",
       " u'fled',\n",
       " u'fledgling',\n",
       " u'fleeting',\n",
       " u'flirted',\n",
       " u'floated',\n",
       " u'flooded',\n",
       " u'focused',\n",
       " u'focusing',\n",
       " u'folded',\n",
       " u'followed',\n",
       " u'following',\n",
       " u'forced',\n",
       " u'forcing',\n",
       " u'forecasting',\n",
       " u'foreign-led',\n",
       " u'formed',\n",
       " u'forthcoming',\n",
       " u'founded',\n",
       " u'foundering',\n",
       " u'fretted',\n",
       " u'frightened',\n",
       " u'frustrating',\n",
       " u'fueled',\n",
       " u'fueling',\n",
       " u'full-fledged',\n",
       " u'fuming',\n",
       " u'functioning',\n",
       " u'funded',\n",
       " u'funding',\n",
       " u'fundraising',\n",
       " u'futures-related',\n",
       " u'gained',\n",
       " u'gaining',\n",
       " u'galling',\n",
       " u'galvanized',\n",
       " u'gambling',\n",
       " u'gauging',\n",
       " u'generated',\n",
       " u'getting',\n",
       " u'giving',\n",
       " u'going',\n",
       " u'good-hearted',\n",
       " u'good-natured',\n",
       " u'gored',\n",
       " u'government-certified',\n",
       " u'government-funded',\n",
       " u'government-owned',\n",
       " u'graduated',\n",
       " u'granted',\n",
       " u'granting',\n",
       " u'greed',\n",
       " u'gripping',\n",
       " u'growing',\n",
       " u'guaranteed',\n",
       " u'guarding',\n",
       " u'guided',\n",
       " u'gut-wrenching',\n",
       " u'hailed',\n",
       " u'hailing',\n",
       " u'halted',\n",
       " u'hampered',\n",
       " u'handed',\n",
       " u'handled',\n",
       " u'handling',\n",
       " u'happened',\n",
       " u'happening',\n",
       " u'hard-charging',\n",
       " u'hard-drinking',\n",
       " u'hard-hitting',\n",
       " u'harmed',\n",
       " u'harped',\n",
       " u'harvested',\n",
       " u'hauled',\n",
       " u'hauling',\n",
       " u'having',\n",
       " u'headed',\n",
       " u'heading',\n",
       " u'headlined',\n",
       " u'healing',\n",
       " u'hearing',\n",
       " u'heated',\n",
       " u'heating',\n",
       " u'hedging',\n",
       " u'heightened',\n",
       " u'helped',\n",
       " u'helping',\n",
       " u'high-flying',\n",
       " u'high-minded',\n",
       " u'high-polluting',\n",
       " u'high-priced',\n",
       " u'high-rolling',\n",
       " u'high-speed',\n",
       " u'higher-salaried',\n",
       " u'highest-pitched',\n",
       " u'hired',\n",
       " u'hitting',\n",
       " u'holding',\n",
       " u'hoped',\n",
       " u'hosted',\n",
       " u'housing',\n",
       " u'hugging',\n",
       " u'hundred',\n",
       " u'hunted',\n",
       " u'hurting',\n",
       " u'identified',\n",
       " u'ignored',\n",
       " u'ignoring',\n",
       " u'impaired',\n",
       " u'impeding',\n",
       " u'impending',\n",
       " u'implemented',\n",
       " u'implied',\n",
       " u'imported',\n",
       " u'imposed',\n",
       " u'imposing',\n",
       " u'impressed',\n",
       " u'improved',\n",
       " u'improving',\n",
       " u'incentive-backed',\n",
       " u'inched',\n",
       " u'inching',\n",
       " u'included',\n",
       " u'including',\n",
       " u'incorporated',\n",
       " u'increased',\n",
       " u'increasing',\n",
       " u'incurred',\n",
       " u'indeed',\n",
       " u'index-related',\n",
       " u'indicated',\n",
       " u'indicating',\n",
       " u'indulging',\n",
       " u'industrialized',\n",
       " u'industry-supported',\n",
       " u'inflated',\n",
       " u'influenced',\n",
       " u'influencing',\n",
       " u'infringed',\n",
       " u'inherited',\n",
       " u'initialing',\n",
       " u'initiated',\n",
       " u'initiating',\n",
       " u'injecting',\n",
       " u'injuring',\n",
       " u'inkling',\n",
       " u'inquiring',\n",
       " u'inserted',\n",
       " u'insider-trading',\n",
       " u'insinuating',\n",
       " u'insisted',\n",
       " u'inspired',\n",
       " u'installed',\n",
       " u'installing',\n",
       " u'instituted',\n",
       " u'instructed',\n",
       " u'insured',\n",
       " u'integrated',\n",
       " u'intended',\n",
       " u'intentioned',\n",
       " u'interest-bearing',\n",
       " u'interested',\n",
       " u'interesting',\n",
       " u'interrogated',\n",
       " u'interviewed',\n",
       " u'intriguing',\n",
       " u'introduced',\n",
       " u'introducing',\n",
       " u'invented',\n",
       " u'inverted',\n",
       " u'invested',\n",
       " u'investigating',\n",
       " u'investing',\n",
       " u'inviting',\n",
       " u'involved',\n",
       " u'involving',\n",
       " u'issued',\n",
       " u'issuing',\n",
       " u'jeopardizing',\n",
       " u'joined',\n",
       " u'joining',\n",
       " u'judged',\n",
       " u'jumped',\n",
       " u'jumping',\n",
       " u'justified',\n",
       " u'justifying',\n",
       " u'keeping',\n",
       " u'kicked',\n",
       " u'kidnapping',\n",
       " u'killed',\n",
       " u'killing',\n",
       " u'knitted',\n",
       " u'knocked',\n",
       " u'labeled',\n",
       " u'labeling',\n",
       " u'labor-backed',\n",
       " u'lacked',\n",
       " u'lagging',\n",
       " u'land-idling',\n",
       " u'landing',\n",
       " u'lasted',\n",
       " u'lasting',\n",
       " u'lauded',\n",
       " u'laughing',\n",
       " u'launched',\n",
       " u'lawmaking',\n",
       " u'laying',\n",
       " u'leading',\n",
       " u'learned',\n",
       " u'learning',\n",
       " u'leasing',\n",
       " u'leaving',\n",
       " u'led',\n",
       " u'lending',\n",
       " u'lengthened',\n",
       " u'lessening',\n",
       " u'letter-writing',\n",
       " u'letting',\n",
       " u'leveling',\n",
       " u'leveraged',\n",
       " u'leveraging',\n",
       " u'licensed',\n",
       " u'licensing',\n",
       " u'lifted',\n",
       " ...]"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[w for w in wsj if re.search('(ed|ing)$', w)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['u',\n",
       " 'e',\n",
       " 'a',\n",
       " 'i',\n",
       " 'a',\n",
       " 'i',\n",
       " 'i',\n",
       " 'i',\n",
       " 'e',\n",
       " 'i',\n",
       " 'a',\n",
       " 'i',\n",
       " 'o',\n",
       " 'i',\n",
       " 'o',\n",
       " 'u']"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "word = 'supercalifragilisticexpialidocious'\n",
    "re.findall(r'[aeiou]', word)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "16"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(re.findall(r'[aeiou]', word))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[(u'io', 549),\n",
       " (u'ea', 476),\n",
       " (u'ie', 331),\n",
       " (u'ou', 329),\n",
       " (u'ai', 261),\n",
       " (u'ia', 253),\n",
       " (u'ee', 217),\n",
       " (u'oo', 174),\n",
       " (u'ua', 109),\n",
       " (u'au', 106),\n",
       " (u'ue', 105),\n",
       " (u'ui', 95)]"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "wsj = sorted(set(nltk.corpus.treebank.words()))\n",
    "fd = nltk.FreqDist(vs for word in wsj\n",
    "                       for vs in re.findall(r'[aeiou]{2,}', word))\n",
    "fd.most_common(12)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Unvrsl Dclrtn of Hmn Rghts Prmble Whrs rcgntn of the inhrnt dgnty and\n",
      "of the eql and inlnble rghts of all mmbrs of the hmn fmly is the fndtn\n",
      "of frdm , jstce and pce in the wrld , Whrs dsrgrd and cntmpt fr hmn\n",
      "rghts hve rsltd in brbrs acts whch hve outrgd the cnscnce of mnknd ,\n",
      "and the advnt of a wrld in whch hmn bngs shll enjy frdm of spch and\n"
     ]
    }
   ],
   "source": [
    "regexp = r'^[AEIOUaeiou]+|[AEIOUaeiou]+$|[^AEIOUaeiou]'\n",
    "def compress(word):\n",
    "     pieces = re.findall(regexp, word)\n",
    "     return ''.join(pieces)\n",
    "\n",
    "english_udhr = nltk.corpus.udhr.words('English-Latin1')\n",
    "print(nltk.tokenwrap(compress(w) for w in english_udhr[:75]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    a   e   i   o   u \n",
      "k 418 148  94 420 173 \n",
      "p  83  31 105  34  51 \n",
      "r 187  63  84  89  79 \n",
      "s   0   0 100   2   1 \n",
      "t  47   8   0 148  37 \n",
      "v  93  27 105  48  49 \n"
     ]
    }
   ],
   "source": [
    "rotokas_words = nltk.corpus.toolbox.words('rotokas.dic')\n",
    "cvs = [cv for w in rotokas_words for cv in re.findall(r'[ptksvr][aeiou]', w)]\n",
    "cfd = nltk.ConditionalFreqDist(cvs)\n",
    "cfd.tabulate()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[u'kasuari']"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cv_word_pairs = [(cv, w) for w in rotokas_words\n",
    "                          for cv in re.findall(r'[ptksvr][aeiou]', w)]\n",
    "cv_index = nltk.Index(cv_word_pairs)\n",
    "cv_index['su']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[u'kaapo',\n",
       " u'kaapopato',\n",
       " u'kaipori',\n",
       " u'kaiporipie',\n",
       " u'kaiporivira',\n",
       " u'kapo',\n",
       " u'kapoa',\n",
       " u'kapokao',\n",
       " u'kapokapo',\n",
       " u'kapokapo',\n",
       " u'kapokapoa',\n",
       " u'kapokapoa',\n",
       " u'kapokapora',\n",
       " u'kapokapora',\n",
       " u'kapokaporo',\n",
       " u'kapokaporo',\n",
       " u'kapokari',\n",
       " u'kapokarito',\n",
       " u'kapokoa',\n",
       " u'kapoo',\n",
       " u'kapooto',\n",
       " u'kapoovira',\n",
       " u'kapopaa',\n",
       " u'kaporo',\n",
       " u'kaporo',\n",
       " u'kaporopa',\n",
       " u'kaporoto',\n",
       " u'kapoto',\n",
       " u'karokaropo',\n",
       " u'karopo',\n",
       " u'kepo',\n",
       " u'kepoi',\n",
       " u'keposi',\n",
       " u'kepoto']"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cv_index['po']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def stem(word):\n",
    "     for suffix in ['ing', 'ly', 'ed', 'ious', 'ies', 'ive', 'es', 's', 'ment']:\n",
    "         if word.endswith(suffix):\n",
    "             return word[:-len(suffix)]\n",
    "     return word"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['ing']"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "re.findall(r'^.*(ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processing')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['processing']"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "re.findall(r'^.*(?:ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processing')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('process', 'ing')]"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "re.findall(r'^(.*)(ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processing')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('processe', 's')]"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "re.findall(r'^(.*)(ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processes')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('process', 'es')]"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "re.findall(r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processes')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('language', '')]"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "re.findall(r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)?$', 'language')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def stem(word):\n",
    "     regexp = r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)?$'\n",
    "     stem, suffix = re.findall(regexp, word)[0]\n",
    "     return stem"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "raw = \"\"\"DENNIS: Listen, strange women lying in ponds distributing swords\n",
    "... is no basis for a system of government.  Supreme executive power derives from\n",
    "... a mandate from the masses, not from some farcical aquatic ceremony.\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['DENNIS',\n",
       " ':',\n",
       " 'Listen',\n",
       " ',',\n",
       " 'strange',\n",
       " 'women',\n",
       " 'ly',\n",
       " 'in',\n",
       " 'pond',\n",
       " 'distribut',\n",
       " 'sword',\n",
       " 'i',\n",
       " 'no',\n",
       " 'basi',\n",
       " 'for',\n",
       " 'a',\n",
       " 'system',\n",
       " 'of',\n",
       " 'govern',\n",
       " '.',\n",
       " 'Supreme',\n",
       " 'execut',\n",
       " 'power',\n",
       " 'deriv',\n",
       " 'from',\n",
       " 'a',\n",
       " 'mandate',\n",
       " 'from',\n",
       " 'the',\n",
       " 'mass',\n",
       " ',',\n",
       " 'not',\n",
       " 'from',\n",
       " 'some',\n",
       " 'farcical',\n",
       " 'aquatic',\n",
       " 'ceremony',\n",
       " '.']"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tokens = word_tokenize(raw)\n",
    "[stem(t) for t in tokens]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "monied; nervous; dangerous; white; white; white; pious; queer; good;\n",
      "mature; white; Cape; great; wise; wise; butterless; white; fiendish;\n",
      "pale; furious; better; certain; complete; dismasted; younger; brave;\n",
      "brave; brave; brave\n"
     ]
    }
   ],
   "source": [
    "from nltk.corpus import gutenberg, nps_chat\n",
    "moby = nltk.Text(gutenberg.words('melville-moby_dick.txt'))\n",
    "moby.findall(r\"<a> (<.*>) <man>\") "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "you rule bro; telling you bro; u twizted bro\n"
     ]
    }
   ],
   "source": [
    "chat = nltk.Text(nps_chat.words())\n",
    "chat.findall(r\"<.*> <.*> <bro>\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "lol lol lol; lmao lol lol; lol lol lol; la la la la la; la la la; la\n",
      "la la; lovely lol lol love; lol lol lol.; la la la; la la la\n"
     ]
    }
   ],
   "source": [
    "chat.findall(r\"<l.*>{3,}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "speed and other activities; water and other liquids; tomb and other\n",
      "landmarks; Statues and other monuments; pearls and other jewels;\n",
      "charts and other items; roads and other features; figures and other\n",
      "objects; military and other areas; demands and other factors;\n",
      "abstracts and other compilations; iron and other metals\n"
     ]
    }
   ],
   "source": [
    "from nltk.corpus import brown\n",
    "hobbies_learned = nltk.Text(brown.words(categories=['hobbies', 'learned']))\n",
    "hobbies_learned.findall(r\"<\\w*> <and> <other> <\\w*s>\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "raw = \"\"\"DENNIS: Listen, strange women lying in ponds distributing swords\n",
    " is no basis for a system of government.  Supreme executive power derives from\n",
    " a mandate from the masses, not from some farcical aquatic ceremony.\"\"\"\n",
    "tokens = word_tokenize(raw)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'tokens' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-4-1906f9872c2e>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0mporter\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mnltk\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mPorterStemmer\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0mlancaster\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mnltk\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mLancasterStemmer\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 3\u001b[0;31m \u001b[0;34m[\u001b[0m\u001b[0mporter\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstem\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mt\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0mt\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mtokens\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m: name 'tokens' is not defined"
     ]
    }
   ],
   "source": [
    "porter = nltk.PorterStemmer()\n",
    "lancaster = nltk.LancasterStemmer()\n",
    "[porter.stem(t) for t in tokens]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'tokens' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-5-8e6157da5250>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;34m[\u001b[0m\u001b[0mlancaster\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstem\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mt\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0mt\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mtokens\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m: name 'tokens' is not defined"
     ]
    }
   ],
   "source": [
    "[lancaster.stem(t) for t in tokens]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "class IndexedText(object):\n",
    "\n",
    "    def __init__(self, stemmer, text):\n",
    "        self._text = text\n",
    "        self._stemmer = stemmer\n",
    "        self._index = nltk.Index((self._stem(word), i)\n",
    "                                 for (i, word) in enumerate(text))\n",
    "\n",
    "    def concordance(self, word, width=40):\n",
    "        key = self._stem(word)\n",
    "        wc = int(width/4)                # words of context\n",
    "        for i in self._index[key]:\n",
    "            lcontext = ' '.join(self._text[i-wc:i])\n",
    "            rcontext = ' '.join(self._text[i:i+wc])\n",
    "            ldisplay = '{:>{width}}'.format(lcontext[-width:], width=width)\n",
    "            rdisplay = '{:{width}}'.format(rcontext[:width], width=width)\n",
    "            print(ldisplay, rdisplay)\n",
    "\n",
    "    def _stem(self, word):\n",
    "        return self._stemmer.stem(word).lower()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('r king ! DENNIS : Listen , strange women', 'lying in ponds distributing swords is no')\n",
      "(' beat a very brave retreat . ROBIN : All', 'lies ! MINSTREL : [ singing ] Bravest of')\n",
      "('       Nay . Nay . Come . Come . You may', 'lie here . Oh , but you are wounded !   ')\n",
      "('doctors immediately ! No , no , please !', 'Lie down . [ clap clap ] PIGLET : Well  ')\n",
      "('ere is much danger , for beyond the cave', 'lies the Gorge of Eternal Peril , which ')\n",
      "('   you . Oh ... TIM : To the north there', 'lies a cave -- the cave of Caerbannog --')\n",
      "('h it and lived ! Bones of full fifty men', 'lie strewn about its lair . So , brave k')\n",
      "(\"not stop our fight ' til each one of you\", 'lies dead , and the Holy Grail returns t')\n"
     ]
    }
   ],
   "source": [
    "porter = nltk.PorterStemmer()\n",
    "grail = nltk.corpus.webtext.words('grail.txt')\n",
    "text = IndexedText(porter, grail)\n",
    "text.concordance('lie')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['DENNIS',\n",
       " ':',\n",
       " 'Listen',\n",
       " ',',\n",
       " 'strange',\n",
       " u'woman',\n",
       " 'lying',\n",
       " 'in',\n",
       " u'pond',\n",
       " 'distributing',\n",
       " u'sword',\n",
       " 'is',\n",
       " 'no',\n",
       " 'basis',\n",
       " 'for',\n",
       " 'a',\n",
       " 'system',\n",
       " 'of',\n",
       " 'government',\n",
       " '.',\n",
       " 'Supreme',\n",
       " 'executive',\n",
       " 'power',\n",
       " 'derives',\n",
       " 'from',\n",
       " 'a',\n",
       " 'mandate',\n",
       " 'from',\n",
       " 'the',\n",
       " u'mass',\n",
       " ',',\n",
       " 'not',\n",
       " 'from',\n",
       " 'some',\n",
       " 'farcical',\n",
       " 'aquatic',\n",
       " 'ceremony',\n",
       " '.']"
      ]
     },
     "execution_count": 79,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "wnl = nltk.WordNetLemmatizer()\n",
    "[wnl.lemmatize(t) for t in tokens]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    " raw = \"\"\"'When I'M a Duchess,' she said to herself, (not in a very hopeful tone\n",
    "though), 'I won't have any pepper in my kitchen AT ALL. Soup does very\n",
    "well without--Maybe it's always pepper that makes people hot-tempered,'...\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[\"'When\",\n",
       " \"I'M\",\n",
       " 'a',\n",
       " \"Duchess,'\",\n",
       " 'she',\n",
       " 'said',\n",
       " 'to',\n",
       " 'herself,',\n",
       " '(not',\n",
       " 'in',\n",
       " 'a',\n",
       " 'very',\n",
       " 'hopeful',\n",
       " 'tone\\nthough),',\n",
       " \"'I\",\n",
       " \"won't\",\n",
       " 'have',\n",
       " 'any',\n",
       " 'pepper',\n",
       " 'in',\n",
       " 'my',\n",
       " 'kitchen',\n",
       " 'AT',\n",
       " 'ALL.',\n",
       " 'Soup',\n",
       " 'does',\n",
       " 'very\\nwell',\n",
       " 'without--Maybe',\n",
       " \"it's\",\n",
       " 'always',\n",
       " 'pepper',\n",
       " 'that',\n",
       " 'makes',\n",
       " 'people',\n",
       " \"hot-tempered,'...\"]"
      ]
     },
     "execution_count": 81,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "re.split(r' ', raw)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[\"'When\",\n",
       " \"I'M\",\n",
       " 'a',\n",
       " \"Duchess,'\",\n",
       " 'she',\n",
       " 'said',\n",
       " 'to',\n",
       " 'herself,',\n",
       " '(not',\n",
       " 'in',\n",
       " 'a',\n",
       " 'very',\n",
       " 'hopeful',\n",
       " 'tone',\n",
       " 'though),',\n",
       " \"'I\",\n",
       " \"won't\",\n",
       " 'have',\n",
       " 'any',\n",
       " 'pepper',\n",
       " 'in',\n",
       " 'my',\n",
       " 'kitchen',\n",
       " 'AT',\n",
       " 'ALL.',\n",
       " 'Soup',\n",
       " 'does',\n",
       " 'very',\n",
       " 'well',\n",
       " 'without--Maybe',\n",
       " \"it's\",\n",
       " 'always',\n",
       " 'pepper',\n",
       " 'that',\n",
       " 'makes',\n",
       " 'people',\n",
       " \"hot-tempered,'...\"]"
      ]
     },
     "execution_count": 82,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "re.split(r'[ \\t\\n]+', raw)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['',\n",
       " 'When',\n",
       " 'I',\n",
       " 'M',\n",
       " 'a',\n",
       " 'Duchess',\n",
       " 'she',\n",
       " 'said',\n",
       " 'to',\n",
       " 'herself',\n",
       " 'not',\n",
       " 'in',\n",
       " 'a',\n",
       " 'very',\n",
       " 'hopeful',\n",
       " 'tone',\n",
       " 'though',\n",
       " 'I',\n",
       " 'won',\n",
       " 't',\n",
       " 'have',\n",
       " 'any',\n",
       " 'pepper',\n",
       " 'in',\n",
       " 'my',\n",
       " 'kitchen',\n",
       " 'AT',\n",
       " 'ALL',\n",
       " 'Soup',\n",
       " 'does',\n",
       " 'very',\n",
       " 'well',\n",
       " 'without',\n",
       " 'Maybe',\n",
       " 'it',\n",
       " 's',\n",
       " 'always',\n",
       " 'pepper',\n",
       " 'that',\n",
       " 'makes',\n",
       " 'people',\n",
       " 'hot',\n",
       " 'tempered',\n",
       " '']"
      ]
     },
     "execution_count": 83,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "re.split(r'\\W+', raw)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[\"'When\",\n",
       " 'I',\n",
       " \"'M\",\n",
       " 'a',\n",
       " 'Duchess',\n",
       " ',',\n",
       " \"'\",\n",
       " 'she',\n",
       " 'said',\n",
       " 'to',\n",
       " 'herself',\n",
       " ',',\n",
       " '(not',\n",
       " 'in',\n",
       " 'a',\n",
       " 'very',\n",
       " 'hopeful',\n",
       " 'tone',\n",
       " 'though',\n",
       " ')',\n",
       " ',',\n",
       " \"'I\",\n",
       " 'won',\n",
       " \"'t\",\n",
       " 'have',\n",
       " 'any',\n",
       " 'pepper',\n",
       " 'in',\n",
       " 'my',\n",
       " 'kitchen',\n",
       " 'AT',\n",
       " 'ALL',\n",
       " '.',\n",
       " 'Soup',\n",
       " 'does',\n",
       " 'very',\n",
       " 'well',\n",
       " 'without',\n",
       " '-',\n",
       " '-Maybe',\n",
       " 'it',\n",
       " \"'s\",\n",
       " 'always',\n",
       " 'pepper',\n",
       " 'that',\n",
       " 'makes',\n",
       " 'people',\n",
       " 'hot',\n",
       " '-tempered',\n",
       " ',',\n",
       " \"'\",\n",
       " '.',\n",
       " '.',\n",
       " '.']"
      ]
     },
     "execution_count": 84,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "re.findall(r'\\w+|\\S\\w*', raw)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[\"'\", 'When', \"I'M\", 'a', 'Duchess', ',', \"'\", 'she', 'said', 'to', 'herself', ',', '(', 'not', 'in', 'a', 'very', 'hopeful', 'tone', 'though', ')', ',', \"'\", 'I', \"won't\", 'have', 'any', 'pepper', 'in', 'my', 'kitchen', 'AT', 'ALL', '.', 'Soup', 'does', 'very', 'well', 'without', '--', 'Maybe', \"it's\", 'always', 'pepper', 'that', 'makes', 'people', 'hot-tempered', ',', \"'\", '...']\n"
     ]
    }
   ],
   "source": [
    "print(re.findall(r\"\\w+(?:[-']\\w+)*|'|[-.(]+|\\S\\w*\", raw))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('', '', ''),\n",
       " ('A.', '', ''),\n",
       " ('', '-print', ''),\n",
       " ('', '', ''),\n",
       " ('', '', '.40'),\n",
       " ('', '', '')]"
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "text = 'That U.S.A. poster-print costs $12.40...'\n",
    "pattern = r'''(?x)    # set flag to allow verbose regexps\n",
    "     ([A-Z]\\.)+        # abbreviations, e.g. U.S.A.\n",
    "   | \\w+(-\\w+)*        # words with optional internal hyphens\n",
    "   | \\$?\\d+(\\.\\d+)?%?  # currency and percentages, e.g. $12.40, 82%\n",
    "   | \\.\\.\\.            # ellipsis\n",
    "   | [][.,;\"'?():-_`]  # these are separate tokens; includes ], [\n",
    " '''\n",
    "nltk.regexp_tokenize(text, pattern)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "20.250994070456922"
      ]
     },
     "execution_count": 87,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(nltk.corpus.brown.words()) / len(nltk.corpus.brown.sents())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[u'\"Nonsense!\"',\n",
      " u'said Gregory, who was very rational when anyone else\\nattempted paradox.',\n",
      " u'\"Why do all the clerks and navvies in the\\nrailway trains look so sad and tired, so very sad and tired?',\n",
      " u'I will\\ntell you.',\n",
      " u'It is because they know that the train is going right.',\n",
      " u'It\\nis because they know that whatever place they have taken a ticket\\nfor that place they will reach.',\n",
      " u'It is because after they have\\npassed Sloane Square they know that the next station must be\\nVictoria, and nothing but Victoria.',\n",
      " u'Oh, their wild rapture!',\n",
      " u'oh,\\ntheir eyes like stars and their souls again in Eden, if the next\\nstation were unaccountably Baker Street!\"',\n",
      " u'\"It is you who are unpoetical,\" replied the poet Syme.']\n"
     ]
    }
   ],
   "source": [
    "text = nltk.corpus.gutenberg.raw('chesterton-thursday.txt')\n",
    "sents = nltk.sent_tokenize(text)\n",
    "pprint.pprint(sents[79:89])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "text = \"doyouseethekittyseethedoggydoyoulikethekittylikethedoggy\"\n",
    "seg1 = \"0000000000000001000000000010000000000000000100000000000\"\n",
    "seg2 = \"0100100100100001001001000010100100010010000100010010000\"\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def segment(text, segs):\n",
    "    words = []\n",
    "    last = 0\n",
    "    for i in range(len(segs)):\n",
    "        if segs[i] == '1':\n",
    "            words.append(text[last:i+1])\n",
    "            last = i+1\n",
    "    words.append(text[last:])\n",
    "    return words"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['doyouseethekitty', 'seethedoggy', 'doyoulikethekitty', 'likethedoggy']"
      ]
     },
     "execution_count": 91,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "text = \"doyouseethekittyseethedoggydoyoulikethekittylikethedoggy\"\n",
    "seg1 = \"0000000000000001000000000010000000000000000100000000000\"\n",
    "seg2 = \"0100100100100001001001000010100100010010000100010010000\"\n",
    "segment(text, seg1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['do',\n",
       " 'you',\n",
       " 'see',\n",
       " 'the',\n",
       " 'kitty',\n",
       " 'see',\n",
       " 'the',\n",
       " 'doggy',\n",
       " 'do',\n",
       " 'you',\n",
       " 'like',\n",
       " 'the',\n",
       " 'kitty',\n",
       " 'like',\n",
       " 'the',\n",
       " 'doggy']"
      ]
     },
     "execution_count": 92,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "segment(text, seg2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def evaluate(text, segs):\n",
    "    words = segment(text, segs)\n",
    "    text_size = len(words)\n",
    "    lexicon_size = sum(len(word) + 1 for word in set(words))\n",
    "    return text_size + lexicon_size"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['doyou',\n",
       " 'see',\n",
       " 'thekitt',\n",
       " 'y',\n",
       " 'see',\n",
       " 'thedogg',\n",
       " 'y',\n",
       " 'doyou',\n",
       " 'like',\n",
       " 'thekitt',\n",
       " 'y',\n",
       " 'like',\n",
       " 'thedogg',\n",
       " 'y']"
      ]
     },
     "execution_count": 94,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "text = \"doyouseethekittyseethedoggydoyoulikethekittylikethedoggy\"\n",
    "seg1 = \"0000000000000001000000000010000000000000000100000000000\"\n",
    "seg2 = \"0100100100100001001001000010100100010010000100010010000\"\n",
    "seg3 = \"0000100100000011001000000110000100010000001100010000001\"\n",
    "segment(text, seg3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "47"
      ]
     },
     "execution_count": 95,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "evaluate(text, seg3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "48"
      ]
     },
     "execution_count": 99,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "evaluate(text, seg2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "64"
      ]
     },
     "execution_count": 98,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "evaluate(text, seg1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "from random import randint\n",
    "\n",
    "def flip(segs, pos):\n",
    "    return segs[:pos] + str(1-int(segs[pos])) + segs[pos+1:]\n",
    "\n",
    "def flip_n(segs, n):\n",
    "    for i in range(n):\n",
    "        segs = flip(segs, randint(0, len(segs)-1))\n",
    "    return segs\n",
    "\n",
    "def anneal(text, segs, iterations, cooling_rate):\n",
    "    temperature = float(len(segs))\n",
    "    while temperature > 0.5:\n",
    "        best_segs, best = segs, evaluate(text, segs)\n",
    "        for i in range(iterations):\n",
    "            guess = flip_n(segs, int(temperature))\n",
    "            score = evaluate(text, guess)\n",
    "            if score < best:\n",
    "                best, best_segs = score, guess\n",
    "        score, segs = best, best_segs\n",
    "        temperature = temperature / cooling_rate\n",
    "        print(evaluate(text, segs), segment(text, segs))\n",
    "    print()\n",
    "    return segs"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(64, ['doyouseethekitty', 'seethedoggy', 'doyoulikethekitty', 'likethedoggy'])\n",
      "(64, ['doyouseethekitty', 'seethedoggy', 'doyoulikethekitty', 'likethedoggy'])\n",
      "(64, ['doyouseethekitty', 'seethedoggy', 'doyoulikethekitty', 'likethedoggy'])\n",
      "(64, ['doyouseethekitty', 'seethedoggy', 'doyoulikethekitty', 'likethedoggy'])\n",
      "(64, ['doyouseethekitty', 'seethedoggy', 'doyoulikethekitty', 'likethedoggy'])\n",
      "(64, ['doyouseethekitty', 'seethedoggy', 'doyoulikethekitty', 'likethedoggy'])\n",
      "(64, ['doyouseethekitty', 'seethedoggy', 'doyoulikethekitty', 'likethedoggy'])\n",
      "(60, ['doyou', 'seethekittyseet', 'hedoggy', 'doyou', 'li', 'ket', 'hekittylike', 't', 'hedoggy'])\n",
      "(60, ['doyou', 'seethekittyseet', 'hedoggy', 'doyou', 'li', 'ket', 'hekittylike', 't', 'hedoggy'])\n",
      "(60, ['doyou', 'seethekittyseet', 'hedoggy', 'doyou', 'li', 'ket', 'hekittylike', 't', 'hedoggy'])\n",
      "(60, ['doyou', 'seethekittyseet', 'hedoggy', 'doyou', 'li', 'ket', 'hekittylike', 't', 'hedoggy'])\n",
      "(60, ['doyou', 'seethekittyseet', 'hedoggy', 'doyou', 'li', 'ket', 'hekittylike', 't', 'hedoggy'])\n",
      "(58, ['doyou', 'see', 'theki', 'ttyseet', 'hedoggy', 'doyou', 'liket', 'he', 'kitty', 'liket', 'hedoggy'])\n",
      "(56, ['doyou', 'seethekitty', 'seet', 'hedoggy', 'doyou', 'liket', 'he', 'kitty', 'liket', 'hedoggy'])\n",
      "(46, ['doyou', 'seet', 'he', 'kitty', 'seet', 'hedoggy', 'doyou', 'liket', 'he', 'kitty', 'liket', 'hedoggy'])\n",
      "(46, ['doyou', 'seet', 'he', 'kitty', 'seet', 'hedoggy', 'doyou', 'liket', 'he', 'kitty', 'liket', 'hedoggy'])\n",
      "(43, ['doyou', 'seet', 'hekitty', 'seet', 'hedoggy', 'doyou', 'liket', 'hekitty', 'liket', 'hedoggy'])\n",
      "(43, ['doyou', 'seet', 'hekitty', 'seet', 'hedoggy', 'doyou', 'liket', 'hekitty', 'liket', 'hedoggy'])\n",
      "(43, ['doyou', 'seet', 'hekitty', 'seet', 'hedoggy', 'doyou', 'liket', 'hekitty', 'liket', 'hedoggy'])\n",
      "(43, ['doyou', 'seet', 'hekitty', 'seet', 'hedoggy', 'doyou', 'liket', 'hekitty', 'liket', 'hedoggy'])\n",
      "(43, ['doyou', 'seet', 'hekitty', 'seet', 'hedoggy', 'doyou', 'liket', 'hekitty', 'liket', 'hedoggy'])\n",
      "(43, ['doyou', 'seet', 'hekitty', 'seet', 'hedoggy', 'doyou', 'liket', 'hekitty', 'liket', 'hedoggy'])\n",
      "(43, ['doyou', 'seet', 'hekitty', 'seet', 'hedoggy', 'doyou', 'liket', 'hekitty', 'liket', 'hedoggy'])\n",
      "(43, ['doyou', 'seet', 'hekitty', 'seet', 'hedoggy', 'doyou', 'liket', 'hekitty', 'liket', 'hedoggy'])\n",
      "(43, ['doyou', 'seet', 'hekitty', 'seet', 'hedoggy', 'doyou', 'liket', 'hekitty', 'liket', 'hedoggy'])\n",
      "(43, ['doyou', 'seet', 'hekitty', 'seet', 'hedoggy', 'doyou', 'liket', 'hekitty', 'liket', 'hedoggy'])\n",
      "()\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'0000100010000001000100000010000100001000000100001000000'"
      ]
     },
     "execution_count": 107,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "text = \"doyouseethekittyseethedoggydoyoulikethekittylikethedoggy\"\n",
    "seg1 = \"0000000000000001000000000010000000000000000100000000000\"\n",
    "anneal(text, seg1, 5000, 1.2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'We called him Tortoise because he taught us .'"
      ]
     },
     "execution_count": 108,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "silly = ['We', 'called', 'him', 'Tortoise', 'because', 'he', 'taught', 'us', '.']\n",
    "' '.join(silly)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'We;called;him;Tortoise;because;he;taught;us;.'"
      ]
     },
     "execution_count": 109,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "';'.join(silly)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'WecalledhimTortoisebecausehetaughtus.'"
      ]
     },
     "execution_count": 110,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "''.join(silly)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "word = 'cat'\n",
    "sentence = \"\"\"hello\n",
    "world\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "cat\n"
     ]
    }
   ],
   "source": [
    "print(word)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello\n",
      "world\n"
     ]
    }
   ],
   "source": [
    "print(sentence)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'cat'"
      ]
     },
     "execution_count": 116,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "word"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'hello\\nworld'"
      ]
     },
     "execution_count": 117,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sentence"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 123,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "cat -> 3 ;  dog -> 4 ;  snake -> 1 ; \n"
     ]
    }
   ],
   "source": [
    "fdist = nltk.FreqDist(['dog', 'cat', 'dog', 'cat', 'dog', 'snake', 'dog', 'cat'])\n",
    "for word in sorted(fdist):\n",
    "     print word, '->', fdist[word], '; ',"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 124,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "cat->3;   dog->4;   snake->1;  \n"
     ]
    }
   ],
   "source": [
    "for word in sorted(fdist):\n",
    "    print '{}->{};'.format(word, fdist[word]), ' ',"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 125,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'cat->3;'"
      ]
     },
     "execution_count": 125,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'{}->{};'.format ('cat', 3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 126,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'cat->'"
      ]
     },
     "execution_count": 126,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'{}->'.format('cat')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'3'"
      ]
     },
     "execution_count": 127,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'{}'.format(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'I want a coffee right now'"
      ]
     },
     "execution_count": 128,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'I want a {} right now'.format('coffee')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Lee wants a sandwich for lunch'"
      ]
     },
     "execution_count": 129,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    " '{} wants a {} {}'.format ('Lee', 'sandwich', 'for lunch')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Lee wants a sandwich'"
      ]
     },
     "execution_count": 131,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'{} wants a {}'.format ('Lee', 'sandwich', 'for lunch')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 132,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'from B to A'"
      ]
     },
     "execution_count": 132,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'from {1} to {0}'.format('A', 'B')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 134,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Lee wants a sandwich right now\n",
      "Lee wants a spam fritter right now\n",
      "Lee wants a pancake right now\n"
     ]
    }
   ],
   "source": [
    "template = 'Lee wants a {} right now'\n",
    "menu = ['sandwich', 'spam fritter', 'pancake']\n",
    "for snack in menu:\n",
    "     print(template.format(snack))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 135,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'    41'"
      ]
     },
     "execution_count": 135,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'{:6}'.format(41)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 136,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'41    '"
      ]
     },
     "execution_count": 136,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'{:<6}' .format(41)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 137,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'dog   '"
      ]
     },
     "execution_count": 137,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'{:6}'.format('dog')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 140,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'   dog'"
      ]
     },
     "execution_count": 140,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'{:>6}'.format('dog')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 139,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'3.1416'"
      ]
     },
     "execution_count": 139,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import math\n",
    "'{:.4f}'.format(math.pi)\n",
    "'3.1416'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 141,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'accuracy for 9375 words: 34.1867%'"
      ]
     },
     "execution_count": 141,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "count, total = 3205, 9375\n",
    "\"accuracy for {} words: {:.4%}\".format(total, count / total)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 153,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Category            can  could    may  might   must   will\n",
      "news                 93     86     66     38     50    389\n",
      "religion             82     59     78     12     54     71\n",
      "hobbies             268     58    131     22     83    264\n",
      "science_fiction      16     49      4     12      8     16\n",
      "romance              74    193     11     51     45     43\n",
      "humor                16     30      8      8      9     13\n"
     ]
    }
   ],
   "source": [
    "def tabulate(cfdist, words, categories):\n",
    "    print '{:16}'.format('Category'),                    # column headings\n",
    "    for word in words:\n",
    "        print'{:>6}'.format(word),\n",
    "    print\n",
    "    for category in categories:\n",
    "        print '{:16}'.format(category),                  # row heading\n",
    "        for word in words:                                        # for each word\n",
    "            print '{:6}'.format(cfdist[category][word]), # print table cell\n",
    "        print                                                   # end the row\n",
    "\n",
    "from nltk.corpus import brown\n",
    "cfd = nltk.ConditionalFreqDist(\n",
    "           (genre, word)\n",
    "           for genre in brown.categories()\n",
    "           for word in brown.words(categories=genre))\n",
    "genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']\n",
    "modals = ['can', 'could', 'may', 'might', 'must', 'will']\n",
    "tabulate(cfd, modals, genres)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 157,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "After (5),  \n",
      "all (3),  \n",
      "is (2),  \n",
      "said (4),  \n",
      "and (3),  \n",
      "done (4),  \n",
      ", (1),  \n",
      "more (4),  \n",
      "is (2),  \n",
      "said (4),  \n",
      "than (4),  \n",
      "done (4),  \n",
      ". (1),  \n"
     ]
    }
   ],
   "source": [
    "saying = ['After', 'all', 'is', 'said', 'and', 'done', ',',\n",
    "           'more', 'is', 'said', 'than', 'done', '.']\n",
    "for word in saying:\n",
    "     print word, '(' + str(len(word)) + '),', ' '"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 158,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "After (5), all (3), is (2), said (4), and (3), done (4), , (1), more\n",
      "(4), is (2), said (4), than (4), done (4), . (1),\n"
     ]
    }
   ],
   "source": [
    "from textwrap import fill\n",
    "format = '%s (%d),'\n",
    "pieces = [format % (word, len(word)) for word in saying]\n",
    "output = ' '.join(pieces)\n",
    "wrapped = fill(output)\n",
    "print(wrapped)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 159,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('The', 3),\n",
       " ('dog', 3),\n",
       " ('gave', 4),\n",
       " ('John', 4),\n",
       " ('the', 3),\n",
       " ('newspaper', 9)]"
      ]
     },
     "execution_count": 159,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sent = ['The', 'dog', 'gave', 'John', 'the', 'newspaper']\n",
    "result = []\n",
    "for word in sent:\n",
    "     word_len = (word, len(word))\n",
    "     result.append(word_len)\n",
    "result"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 2",
   "language": "python",
   "name": "python2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
