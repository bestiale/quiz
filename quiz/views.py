# encoding: utf-8
import json, calendar
from django.http import HttpResponse
from django.db.models import Max
from .models import Category, Question
from calendar import timegm


def get_json(request):

	data = Question.objects.all()

	languages = {
		'de': [],
		'en': [],
		'fr': [],
		'it': []
	}

	for question in data:
		languages['de'].append({
			'id': question.pk, 
			'question': question.question_de,
			'answer1': question.answer1_de,
			'answer2': question.answer2_de,
			'answer3': question.answer3_de,
			'tags': [tag.tag for tag in question.tags.all()],
			'failcount':0,
		})
		languages['fr'].append({
			'id': question.pk, 
			'question': question.question_fr,
			'answer1': question.answer1_fr,
			'answer2': question.answer2_fr,
			'answer3': question.answer3_fr,
			'tags': [tag.tag for tag in question.tags.all()],
			'failcount':0
		})
		languages['it'].append({
			'id': question.pk, 
			'question': question.question_it,
			'answer1': question.answer1_it,
			'answer2': question.answer2_it,
			'answer3': question.answer3_it,
			'tags': [tag.tag for tag in question.tags.all()],
			'failcount':0
		})
		languages['en'].append({
			'id': question.pk, 
			'question': question.question_en,
			'answer1': question.answer1_en,
			'answer2': question.answer2_en,
			'answer3': question.answer3_en,
			'tags': [tag.tag for tag in question.tags.all()],
			'failcount':0
		})

	json_list = json.dumps(languages, 
		indent=4,
		encoding="utf-8"
	)
	
	return HttpResponse(json_list, content_type="application/json")


def get_timestamp(request):

	newest = Question.objects.aggregate(Max('timestamp')).values()
	timestamp = timegm(newest[0].utctimetuple())
	json_time = {'last timestamp': timestamp}

	json_timestamp = json.dumps(json_time,
		indent=4,
		encoding="utf-8"
	)

	return HttpResponse(json_timestamp, content_type="application/json")