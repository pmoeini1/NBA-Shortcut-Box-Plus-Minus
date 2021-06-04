## NBA Shortcut-Box-Plus-Minus

Linear regression model to estimate the offensive impact an NBA player has for his team, given (pace-adjusted) points, assists, (estimated) scoring turnovers, points per true shooting attempt, and lineup context stats from bball-index.com as features, and offensive on/off as y-value.

### Source Code
For source code (.py, .ipynb, .csv files) see: https://github.com/pmoeini1/NBA-Shortcut-Box-Plus-Minus

### Statistical Decisions
Box score stats were adjusted for pace in order to combat the difference in speed teams play at, and the differences in minutes played between star players.
Scoring turnovers were estimated as total turnovers multiplied by 1 - ((2.2 x assists) / ((2.2 x assists) + true shooting attempts)).
Playmaking turnovers were not included as to not penalize playmakers who try risky passes in order to create very easy shots for teammates, but also to not reward poor passing.
Lineup context stats from bball-index.com were used in order to adjust player box-plus-minus scores based on teammate spacing, playmaking, rim finishing, scoring gravity, and penetration (players with bad teammates get a boost, players with good teammates get a deduction as their "production" is likely a result of being surrounded by good passers and shooters).

### Weaknesses
Model assumes each star player's team's lineups when they are off the floor are of equal ability to contextual lineups.
Lack of data severely limits accuracy.
Model seems to be biased towards perimeter players, however that is likely a result of perimeter players tending to be more skilled offensive players.

Note: This model does not account for defensive impact in any way.

### Top 10 Box-Plus-Minus Scores
1. Stephen Curry: 15.24
2. Bradley Beal: 15.01
3. Damian Lillard: 13.27
4. Kawhi Leonard: 12.34
5. Luka Doncic: 12.08
6. Kyrie Irving: 11.57
7. LeBron James: 11.54
8. Trae Young: 10.71
9. Giannis Antetokounmpo: 10.12
10. Donovan Mitchell: 9.88
