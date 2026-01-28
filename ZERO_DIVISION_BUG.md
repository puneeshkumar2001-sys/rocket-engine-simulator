# PROBLEM: App Crashes When Entering Zero

## What Happens
When users type 0 in any input box, the app crashes.

## Why It Happens
The code tries to divide by zero in calculations.

## Simple Fixes Needed
1. Stop users from entering 0
2. Make the code check for 0 before dividing

## Files to Fix
- rocket_engine_ultimate.py
- streamlit_app.py

## Status
Waiting to be fixed
