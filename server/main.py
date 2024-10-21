
from test import get_active_matches, look_up_results


#every 5 minutes
ongoing_games = []
ongoing_games.clear()
finished_matches = get_active_matches(ongoing_games)
look_up_results(finished_matches)

