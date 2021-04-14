% Assuming stocks behave randomly, buy a stock and wait until it goes up one dollar, then sell and walk away

% Max number of days to play
days = 100;
days++;
% Initial stock value is 100
initial_price = 100;
prices = initial_price * ones(1, days);
% Vector to record price only when playing
your_play = initial_price;
% Bool playing
playing = 1;
% Record price when you stopped playing
price_stop_play = 0;

for i = 2:days
  % Randomly update stock
  if rand < .5
    prices(i) = prices(i - 1) + 1;
  else
    prices(i) = prices(i - 1) - 1;
  endif
  % Record results if still playing
  if playing == 1
    % Check if there is a win and stop playing
    if prices(i) > initial_price
      playing = 0;
      price_stop_play = prices(i);
      your_play = [your_play, price_stop_play];
    else
      your_play = [your_play, prices(i)];
    endif
  else
    your_play = [your_play, price_stop_play];
  endif
endfor


% Show results
plot(prices);
hold;
plot(your_play);
plot(initial_price * ones(1, days));


  
  
  
  
  
  