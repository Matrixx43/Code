repeat = 1000;

pass_time = zeros(1,repeat);

% Get random passing times
pass_time = -30 * log(rand(1,repeat));

% Show a historgram
hist(pass_time, 30);
% Plot function
hold;
x = 0:0.1:200;
plot(x, 10000*(1/30) * exp(-(1/30)*x));