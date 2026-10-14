# Bug Bounty Report - XSS Vulnerability

**Target:** http://localhost:8000/hack_test.html
**Found By:** Sufiyan Ansari (sufiyan_ansari_00786)
**Date:** 14 Oct 2026
**Severity:** High

## 1. Vulnerability Type: Stored XSS / Reflected XSS

## 2. Steps to Reproduce:
1. Go to http://localhost:8000/hack_test.html
2. In input box, enter payload: <img src=x onerror=alert('Hacked')>
3. Click Check
4. Alert box pops up = Site hacked!

## 3. Proof of Concept (Screenshot):
[ Yaha tumhara wala 404 -> 200 wala screenshot lagega ]

## 4. Impact:
Attacker can steal user cookies, redirect to phishing site, hack Instagram login.

## 5. Fix (Maine khud kiya):
Use innerText instead of innerHTML
`document.getElementById('out').innerText = ...`

## 6. Status: FIXED by me
