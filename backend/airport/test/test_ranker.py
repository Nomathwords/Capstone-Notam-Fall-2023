import unittest
from backend.airport import ranker

# Run unit tests by running this from the root of the repo:
# python3 -m unittest backend/airport/test/test_ranker.py

class TestRanker( unittest.TestCase ):

	def test_high_category( self ):
		notams = []
		notam = {
			"text": "!DYR 10/018 DYR RWY 16/34 CLSD 1910301309-PERM"
			}
		notams.append( notam )
		results = ranker.determine_rank( notams )
		self.assertEqual( "high", results[0]["CS4273_Rank"].lower(), "Expected NOTAM to be a high category" )

	def test_moderate_category( self ):
		notams = []
		notam = {
			"text": "!ROA 03/027 ROA OBST CRANE (ASN UNKNOWN) 371500N0795635W (4.20NM SSE APCH END RWY 34) 949FT (265FT AGL) FLAGGED AND LGTD 2203091958-PERM"
			}
		notams.append( notam )
		results = ranker.determine_rank( notams )
		self.assertEquals( "moderate", results[0]["CS4273_Rank"].lower(), "Expected NOTAM to be a moderate category" )

	def test_low_category( self ):
		notams = []
		notam = {
			"text": "!MLC 04/200 1F4 AD AP WILDLIFE HAZARD DEER 2204141404-PERM"
			}
		notams.append( notam )
		results = ranker.determine_rank( notams )
		self.assertEquals( "low", results[0]["CS4273_Rank"].lower(), "Expected NOTAM to be a low category" )
