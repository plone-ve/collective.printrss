# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s collective.printrss -t test_rss_feed.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src collective.printrss.testing.COLLECTIVE_PRINTRSS_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_rss_feed.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a rss_feed
  Given a logged-in site administrator
    and an add rss_feed form
   When I type 'My rss_feed' into the title field
    and I submit the form
   Then a rss_feed with the title 'My rss_feed' has been created

Scenario: As a site administrator I can view a rss_feed
  Given a logged-in site administrator
    and a rss_feed 'My rss_feed'
   When I go to the rss_feed view
   Then I can see the rss_feed title 'My rss_feed'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add rss_feed form
  Go To  ${PLONE_URL}/++add++rss_feed

a rss_feed 'My rss_feed'
  Create content  type=rss_feed  id=my-rss_feed  title=My rss_feed


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.title  ${title}

I submit the form
  Click Button  Save

I go to the rss_feed view
  Go To  ${PLONE_URL}/my-rss_feed
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a rss_feed with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the rss_feed title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
