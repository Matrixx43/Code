% We will do 500 plays of roulette.

% PART A: We bet always on red

resultsA = zeros(500, 1);
resultsB = zeros(500, 1);
C = zeros(500,1);
balance = 0;

for i = 1:500
  rolled = randi(38);
  % Look for red: 18 of the 38 outcomes
  if rolled <= 18
    balance++;
  else
    balance--;
  endif
  resultsA(i) = balance;
endfor

% PART B: We bet always on number 17

balance = 0;
for i = 1:500
  rolled = randi(38);
  % Look for n 17
  if rolled == 17
    % If correct, we win 35 dollars and dont lose anything
    balance += 35;
  else
    % Otherwise we lose 1
    balance--;
  endif
  resultsB(i) = balance;
endfor


% PART C: Plot

plot(resultsA);
hold;
plot(resultsB);
plot(C);
xlabel("Times played");
ylabel("Balance")
