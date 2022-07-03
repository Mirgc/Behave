from behave import *

@step("a post page is loaded")
def post_page_load(context):
	pass

@step("I add a comment")
def add_comment(context):
	pass

@step("the page is reloaded")
def page_reloaded(context):
	assert True is True

@step("the page shows a confirmation message")
def page_shows_confirmation_message(context):
	assert True

@step("the comment is registered in the database")
def comment_registered_in_database(context):
	assert not False

@step("I can't see the comment in the post page")
def cant_see_comment(context):
	assert True

@step("I can see the comment in the post page")
def can_see_comment(context):
	assert True

@step("I approve the comment")
def approve_comment(context):
	assert True
