repeat = 10000;

results = zeros(1,repeat);

for i = 1:repeat
  sum = 2;
  a = 0;
  while sum > 1
    a = rand;
    sum = a + rand;
  endwhile
  results(i) = a;
endfor

hist(results,10);
hold;
x = 0:0.01:1;
plot(x,2000-2000*x);
