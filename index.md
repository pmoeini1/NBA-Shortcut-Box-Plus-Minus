## NBA Shortcut-Box-Plus-Minus

Linear regression model to estimate the offensive impact an NBA player has for his team, given (pace-adjusted) points, assists, (estimated) scoring turnovers, points per true shooting attempt, and lineup context stats from bball-index.com as features, and offensive on/off as y-value.

### Source Code
For source code (.py, .ipynb, .csv files) see: https://github.com/pmoeini1/NBA-Shortcut-Box-Plus-Minus

### Statistical Decisions
Box score stats were adjusted for pace in order to combat the difference in speed teams play at, and the differences in minutes played between star players.
Scoring turnovers were estimated as total turnovers multiplied by 1 - ((2.2 x assists) / ((2.2 x assists) + true shooting attempts)).
Playmaking turnovers were not included as to not penalize playmakers who try risky passes in order to create very easy shots for teammates, but also to not reward poor passing.
Lineup context stats from bball-index.com were used in order to adjust player box-plus-minus scores based on teammate spacing, playmaking, rim finishing, scoring gravity, and penetration.

### Weaknesses
Model assumes each star player's team's lineups when they are off the floor are average NBA players.
Lack of data severely limits accuracy.
Model heavily favours good and willing passers, so much so as poor scorers (ex. Draymond Green) can have a higher score than elite scorers (ex. Joel Embiid).
With current data, model likely has more value as a measure of playmaking ability than global offense. Model seems to be biased towards perimeter players, however that is likely a result of preimeter players tending to be more skilled offensive players.

Note: This model does not account for defensive impact in any way.

### Top 10 Box-Plus-Minus Scores
1. Trae Young: 13.48
2. James Harden: 13.40
3. Luka Doncic: 13.38
4. Damian Lillard: 13.13
5. Stephen Curry: 12.97
6. LeBron James: 12.83
7. Chris Paul: 12.23
8. Nikola Jokic: 12.05
9. Bradley Beal: 11.68
10. Kawhi Leonard: 11.35
