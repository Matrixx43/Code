repeat_exp = 10000;

v = -log(rand(1, repeat_exp));

x = 0:0.01:10;

hist(v, 100);
hold;
plot(x, 900*exp(-x))
