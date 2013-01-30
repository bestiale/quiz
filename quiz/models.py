# encoding: utf-8
from django.db import models
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
	title = models.CharField(max_length="60")
	tag = models.CharField(max_length="50")

	class Meta:
		verbose_name = _('Category')
		verbose_name_plural = _('Categories')

	def __unicode__(self):
		return self.title


class Question(models.Model):

	question_de = models.CharField(_('Question'), max_length="190")
	answer1_de = models.CharField(_('Answer 1'), max_length="50",
		help_text=_('correct answer'))
	answer2_de = models.CharField(_('Answer 2'), max_length="50")
	answer3_de = models.CharField(_('Answer 3'), max_length="50")
	question_fr = models.CharField(_('Question'), max_length="190")
	answer1_fr = models.CharField(_('Answer 1'), max_length="50",
		help_text=_('correct answer'))
	answer2_fr = models.CharField(_('Answer 2'), max_length="50")
	answer3_fr = models.CharField(_('Answer 3'), max_length="50")
	question_it = models.CharField(_('Question'), max_length="190")
	answer1_it = models.CharField(_('Answer 1'), max_length="50",
		help_text=_('correct answer'))
	answer2_it = models.CharField(_('Answer 2'), max_length="50")
	answer3_it = models.CharField(_('Answer 3'), max_length="50")
	question_en = models.CharField(_('Question'), max_length="190")
	answer1_en = models.CharField(_('Answer 1'), max_length="50",
		help_text=_('correct answer'))
	answer2_en = models.CharField(_('Answer 2'), max_length="50")
	answer3_en = models.CharField(_('Answer 3'), max_length="50")
	timestamp = models.DateTimeField(_('Updated'), auto_now=True)
	created = models.DateTimeField(_('Added'), auto_now_add=True)
	tags = models.ManyToManyField(Category, related_name="tags")

	class Meta:
		verbose_name = _('Question')
		verbose_name_plural = _('Questions')

	def __unicode__(self):
		return self.question_de

	def get_tags(self):
		return ', '.join([a.title for a in self.tags.all()])

	get_tags.short_description = 'Tags'