# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 06:05:32 2016

@author: bkunneke
"""

# Great write up on how to do everything in JIRA here:
# https://pythonhosted.org/jira/
from jira import JIRA

jira = JIRA(server='https://te2web.atlassian.net', basic_auth=('user', 'pwd'))    # a username/password tuple
projects = jira.projects() # Gets a list of all projects

# Create an issue
new_issue = jira.create_issue(project='PROJ_key_or_id', summary='New issue from jira-python',
                              description='Look into this one', issuetype={'name': 'Bug'})

# Find a specific issue
issues = jira.search_issues("key = 'HIL-163'")

