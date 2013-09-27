
/*
Here is the tool
Given a list of adgroups as above and a csv file containing search phrases search_term  (and optionally a few other columns)
the tool would filter the rows above and produce the portion of the csv that matches the adgroups together with some additional columns, that include the # of tokens matched a
ad the ad copy that would be shown for that match.

the matching logic is approximately as follows:
 - negatives are matched first - if you match a negative the whole adgroup is out non-negatives are matched then  (
 - if multiple keywords match the search term - then you can pick the own with the maximum # of words matcged
      if multiple of those pick the first in order provided
 - phrase match means substring match with the extra complexity that it can only match at word delimiters. E.g. free dooes not match freelance
 - for broad match - you can assume that all words have the +, which you should strip and assume that the meaning of the match type is
   that the search term includes at least each on of the words in the keyword. 
 - Allow for a global option (broad_match_variants) that controls whether in the broad case the word by word match is 
   exact or a stemming is first performed to allow matching close variants (e.g. translator => translat*)
 - Assume that phrase and exact do not do any close variant matching
 - If multiple adgroups match resolve based a) highest CPC first b) order of appearence
 - For every matching search term you will find in the end the matching adgroup and within that the particular matching keyword  that matched
   in addition to repeating all the fields of the original csv add the following columns
     Keyword
     Criterion Type
     Matched Words  # just the number of matched words
     Max CPC
     Headline  # by default do not include the ad information - do so only if a command line option explicitely asks for it
     Description Line 1
     Description Line 2
     Display
     Destination URL
*/

