SELECT
	COUNT(*)
FROM
	"notes-00000"
WHERE
	classification = "MISINFORMED_OR_POTENTIALLY_MISLEADING"
	AND believable <> '';


SELECT t1.noteId, t2.tweetId, t2.believable FROM scoredNotes AS t1 JOIN "notes-00000" AS t2 on t1.noteId = t2.noteId WHERE t1.ratingStatus = 'CURRENTLY_RATED_HELPFUL' AND t1.classification = "MISINFORMED_OR_POTENTIALLY_MISLEADING" AND t2.believable <> '';

SELECT COUNT(*) FROM scoredNotes WHERE noteIntercept >= 0.4;

SELECT COUNT(*) FROM "notes-00000" WHERE classification = "MISINFORMED_OR_POTENTIALLY_MISLEADING" AND believable <> '' GROUP BY tweetId HAVING COUNT(noteId) >= 5;


-- this is saved as "tweets_with_3_notes"
SELECT t.noteId, t.tweetId, t.believable FROM "notes-00000" AS t WHERE t.classification = "MISINFORMED_OR_POTENTIALLY_MISLEADING" AND t.believable <> '' AND (SELECT COUNT(*) FROM "notes-00000" AS t1 WHERE t1.tweetId = t.tweetId AND t1.classification = "MISINFORMED_OR_POTENTIALLY_MISLEADING" AND t1.believable <> '') >= 3;


SELECT COUNT(DISTINCT tweetId) FROM tweets_with_3_notes;

SELECT * FROM (SELECT t1.noteId, t2.tweetId, t2.believable FROM scoredNotes AS t1 JOIN "notes-00000" AS t2 on t1.noteId = t2.noteId WHERE t1.ratingStatus = 'CURRENTLY_RATED_HELPFUL' AND t1.classification = "MISINFORMED_OR_POTENTIALLY_MISLEADING" AND t2.believable <> '') AS t1 FULL JOIN tweets_with_3_notes AS t2 ON t1.noteId = t2.noteId;

SELECT COUNT(DISTINCT tweetId) FROM (SELECT t1.noteId, t2.tweetId, t2.believable FROM scoredNotes AS t1 JOIN "notes-00000" AS t2 on t1.noteId = t2.noteId WHERE t1.ratingStatus = 'CURRENTLY_RATED_HELPFUL' AND t1.classification = "MISINFORMED_OR_POTENTIALLY_MISLEADING" AND t2.believable <> '' UNION SELECT * FROM tweets_with_3_notes) WHERE believable = "BELIEVABLE_BY_MANY";