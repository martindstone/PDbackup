#!/usr/bin/env python

import pd
import json
import os
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("pd_api_key", help="PagerDuty API key")
parser.add_argument("output_file", help="Filename to write the backup to")
args = parser.parse_args()

if os.path.isfile(args.output_file):
	overwrite = input(f"File '{args.output_file}' exists; overwrite? (y/N) ")
	if overwrite.lower() != "y":
		print("Aborted.")
		sys.exit(0)


r = {}

print("Getting users...", end=" ", flush=True)
users = pd.fetch_users(api_key=args.pd_api_key, params={"include[]": ["contact_methods","notification_rules","teams"]})
print(f"Got {len(users)}.")

print("Getting teams... ", end="", flush=True)
teams = pd.fetch_teams(api_key=args.pd_api_key)
print(f"Got {len(teams)}.")

print("Getting services... ", end="", flush=True)
services = pd.fetch_services(api_key=args.pd_api_key)
print(f"Got {len(services)}.")

print("Getting schedules... ", end="", flush=True)
schedules = pd.fetch_schedules(api_key=args.pd_api_key)
print(f"Got {len(schedules)}.")

print("Getting escalation policies... ", end="", flush=True)
escalation_policies = pd.fetch_escalation_policies(api_key=args.pd_api_key)
print(f"Got {len(escalation_policies)}.")


r['users'] = users
r['teams'] = teams
r['services'] = services
r['schedules'] = schedules
r['escalation_policies'] = escalation_policies

f = open(args.output_file, "w")
json.dump(r, f, indent=4)