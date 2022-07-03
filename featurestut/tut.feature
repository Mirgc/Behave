Feature: comments

Scenario: add a comment in blog post
	Given a post page is loaded
	When I add a comment
	Then the page is reloaded
	And the page shows a confirmation message
	And the comment is registered in the database

Scenario: approve comment
	Given the comment is registered in the database
	And I can't see the comment in the post page
	When I approve the comment
	Then I can see the comment in the post page
