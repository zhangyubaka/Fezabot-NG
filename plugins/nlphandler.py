#!/usr/bin/env python3

from snownlp import SnowNLP

async def nlpHandler(msg):
	_,*text = msg['text'].split()
	text = ''.join(text)
	s=SnowNLP(text)
	return s.summary()